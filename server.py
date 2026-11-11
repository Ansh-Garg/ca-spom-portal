"""
CA Final SPOM Testing Platform - Enhanced Backend Server
Features:
- Strict ICAI Section-wise Weightage Allocation
- Option Shuffling & Randomization for Real Conceptual Rigor
- Offline SPOM Recall & ICAI BoS Provenance Badges
- Question Bookmarking & Sectional Breakdown
"""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import json
import urllib.parse
import os
import sys
import csv
import io
import random
from datetime import datetime

import database
import seed_data
import seed_intelligence

PORT = int(os.environ.get('PORT', 8080))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLIC_DIR = os.path.join(BASE_DIR, "public")

class SPOMRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PUBLIC_DIR, **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def send_json(self, data, status_code=200):
        response_bytes = json.dumps(data, indent=2, ensure_ascii=False).encode('utf-8')
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(response_bytes)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(response_bytes)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query = urllib.parse.parse_qs(parsed_url.query)

        # 1. Platform Statistics
        if path == "/api/stats":
            stats = database.get_stats()
            self.send_json({"success": True, "data": stats})
            return

        # 2. Chapters Metadata
        elif path == "/api/chapters":
            set_name = query.get('set', [None])[0]
            chapters = database.get_chapters(set_name)
            self.send_json({"success": True, "data": chapters})
            return

        # 3. Question Bank with Rich Filters
        elif path == "/api/mcqs":
            set_name = query.get('set', [None])[0]
            chapter_code = query.get('chapter', [None])[0]
            source_tag = query.get('source', [None])[0]
            section_group = query.get('section', [None])[0]
            limit = query.get('limit', [None])[0]
            random_order = query.get('random', ['false'])[0].lower() == 'true'
            
            mcqs = database.get_mcqs(
                set_name=set_name, 
                chapter_code=chapter_code, 
                source_tag=source_tag,
                section_group=section_group,
                limit=limit, 
                random_order=random_order
            )
            self.send_json({"success": True, "count": len(mcqs), "data": mcqs})
            return

        # 4. Bookmarked MCQs
        elif path == "/api/bookmarks":
            bookmarks = database.get_bookmarked_mcqs()
            self.send_json({"success": True, "count": len(bookmarks), "data": bookmarks})
            return

        # 4b. Question Bank Coverage & Cohort Metrics
        elif path == "/api/question-bank-coverage":
            set_name = query.get('set', ['A'])[0].upper()
            cov = database.get_bank_coverage(set_name)
            self.send_json({"success": True, "data": cov})
            return

        # 5. Authentic 100 Marks Mock Generation (Section Weightage + Shuffling)
        elif path == "/api/mock-test":
            set_name = query.get('set', ['A'])[0].upper()
            mode = query.get('mode', ['full_mock_50'])[0] # 'full_mock_50', 'full_mock_70', 'quick_blitz', 'custom_chapters', 'cohort'
            shuffle_options = query.get('shuffle_options', ['true'])[0].lower() == 'true'
            chapters_arg = query.get('chapters', [None])[0] or query.get('chapter', [None])[0]
            cohort_arg = query.get('cohort', [None])[0]

            if cohort_arg:
                # Cohort specific mock test (Never Attempted, Wrong Many Times, Correct Many Times, Attempted)
                pool = database.get_cohort_mcqs(set_name=set_name, cohort=cohort_arg, chapter_codes=chapters_arg, random_order=True)
                if not pool:
                    self.send_json({"success": False, "error": f"No questions found in cohort '{cohort_arg}' for Set {set_name}"}, status_code=404)
                    return
                req_count = int(query.get('count', [20])[0])
                if req_count <= 0 or req_count >= len(pool):
                    chosen = list(pool)
                    random.shuffle(chosen)
                else:
                    chosen = random.sample(pool, req_count)

                cohort_label_map = {
                    'never_attempted': 'Never Attempted (Unseen)',
                    'wrong_many_times': 'Wrong Many Times (Needs Practice)',
                    'correct_many_times': 'Correct Many Times (Mastered)',
                    'attempted': 'All Attempted Questions'
                }
                c_lbl = cohort_label_map.get(cohort_arg, cohort_arg.replace('_', ' ').title())
                combined = []
                for q in chosen:
                    q_copy = dict(q)
                    sec_g = q_copy.get('section_group', '')
                    q_copy['section_title'] = sec_g if sec_g else f"Cohort Test · {c_lbl}"
                    combined.append(q_copy)

            elif chapters_arg:
                # Custom single chapter or combination of chapters test
                pool = database.get_mcqs(set_name=set_name, chapter_code=chapters_arg, random_order=True)
                if not pool:
                    self.send_json({"success": False, "error": f"No questions found for selected chapters in Set {set_name}"}, status_code=404)
                    return
                req_count = int(query.get('count', [20])[0])
                if req_count <= 0 or req_count >= len(pool):
                    chosen = list(pool)
                    random.shuffle(chosen)
                else:
                    chosen = random.sample(pool, req_count)

                combined = []
                for q in chosen:
                    q_copy = dict(q)
                    sec_g = q_copy.get('section_group', '')
                    q_copy['section_title'] = sec_g if sec_g else f"Chapter Test · {q_copy.get('chapter_code', '')}"
                    combined.append(q_copy)
            else:
                # Define section requirements
                if set_name == 'A':
                    # Part I: Corporate Laws (70 Marks), Part II: Economic Laws (30 Marks)
                    part1_group = "Part I"
                    part2_group = "Part II"
                    if mode == 'quick_blitz':
                        target_p1 = 17 # ~34 marks
                        target_p2 = 8  # ~16 marks
                    elif mode == 'full_mock_70':
                        target_p1 = 49 # 70 marks mix
                        target_p2 = 21 # 30 marks mix
                    else: # Default 50 questions x 2 marks = 100 marks
                        target_p1 = 35 # 35 x 2 = 70 Marks
                        target_p2 = 15 # 15 x 2 = 30 Marks
                else:
                    # Set B: Part I: Cost Management (50M), Part II: Performance Management (50M)
                    part1_group = "Part I"
                    part2_group = "Part II"
                    if mode == 'quick_blitz':
                        target_p1 = 13
                        target_p2 = 12
                    else:
                        target_p1 = 25 # 25 x 2 = 50 Marks
                        target_p2 = 25 # 25 x 2 = 50 Marks

                all_p1 = database.get_mcqs(set_name=set_name, section_group=part1_group, random_order=True)
                all_p2 = database.get_mcqs(set_name=set_name, section_group=part2_group, random_order=True)

                if not all_p1 and not all_p2:
                    self.send_json({"success": False, "error": f"No questions found for Set {set_name}"}, status_code=404)
                    return

                def pick_weighted(pool, count):
                    if not pool:
                        return []
                    chosen = []
                    pool_copy = list(pool)
                    random.shuffle(pool_copy)
                    while len(chosen) < count:
                        for item in pool_copy:
                            if len(chosen) >= count:
                                break
                            chosen.append(item)
                    return chosen

                selected_p1 = pick_weighted(all_p1, target_p1)
                selected_p2 = pick_weighted(all_p2, target_p2)

                # Combine and assign section badges
                combined = []
                for q in selected_p1:
                    q_copy = dict(q)
                    q_copy['section_title'] = "Part I: Corporate Laws (70 Marks)" if set_name == 'A' else "Part I: Strategic Cost Management (50 Marks)"
                    combined.append(q_copy)

                for q in selected_p2:
                    q_copy = dict(q)
                    q_copy['section_title'] = "Part II: Economic Laws (30 Marks)" if set_name == 'A' else "Part II: Strategic Performance Management (50 Marks)"
                    combined.append(q_copy)

            # Build safe question payload with option shuffling
            final_questions = []
            for idx, q in enumerate(combined):
                opts = [
                    {"original_key": "A", "text": q['option_a']},
                    {"original_key": "B", "text": q['option_b']},
                    {"original_key": "C", "text": q['option_c']},
                    {"original_key": "D", "text": q['option_d']}
                ]

                # Shuffle options if requested to prevent position memorization
                if shuffle_options:
                    random.shuffle(opts)

                # Re-map to A, B, C, D
                shuffled_opts = {
                    "option_a": opts[0]["text"],
                    "option_b": opts[1]["text"],
                    "option_c": opts[2]["text"],
                    "option_d": opts[3]["text"]
                }
                # Track which shuffled key corresponds to the true correct answer
                correct_orig = q['correct_option'].strip().upper()
                shuffled_correct_key = "A"
                for letter, opt_obj in zip(["A", "B", "C", "D"], opts):
                    if opt_obj["original_key"] == correct_orig:
                        shuffled_correct_key = letter
                        break

                q_safe = {
                    "id": q['id'],
                    "q_index": idx + 1,
                    "set_name": q['set_name'],
                    "section_group": q['section_group'],
                    "section_title": q['section_title'],
                    "chapter_code": q['chapter_code'],
                    "topic": q['topic'],
                    "question": q['question'],
                    "option_a": shuffled_opts["option_a"],
                    "option_b": shuffled_opts["option_b"],
                    "option_c": shuffled_opts["option_c"],
                    "option_d": shuffled_opts["option_d"],
                    "shuffled_correct_key": shuffled_correct_key, # Verified server-side on submit
                    "marks": q.get('marks', 2),
                    "difficulty": q['difficulty'],
                    "source_tag": q.get('source_tag', 'ICAI BoS Module'),
                    "is_case_study": q['is_case_study'],
                    "case_scenario": q['case_scenario'],
                    "is_bookmarked": q.get('is_bookmarked', 0)
                }
                final_questions.append(q_safe)

            duration = 180 if mode != 'quick_blitz' else 45
            total_marks = sum(q['marks'] for q in final_questions)

            self.send_json({
                "success": True,
                "set_name": set_name,
                "mode": mode,
                "total_questions": len(final_questions),
                "total_marks": total_marks,
                "duration_minutes": duration,
                "passing_percentage": 50,
                "passing_marks": total_marks * 0.5,
                "questions": final_questions
            })
            return

        # 6. Test Attempts History
        elif path == "/api/attempts":
            attempts = database.get_attempts()
            self.send_json({"success": True, "data": attempts})
            return

        # 7. Sample CSV / JSON Templates
        elif path == "/api/template/csv":
            csv_content = (
                "set_name,section_group,chapter_code,topic,question,option_a,option_b,option_c,option_d,correct_option,marks,explanation,section_ref,exam_tip,source_tag,difficulty\n"
                'A,"Part I: Corporate Laws",A_DIR,Independent Directors,"What is the maximum tenure of an Independent Director under Section 149(10)?","3 consecutive years","Up to 5 consecutive years","Up to 2 consecutive terms of up to 5 years each","Indefinite period until removed",C,2,"Section 149(10) allows up to two consecutive terms of up to 5 years each subject to special resolution.","Section 149(10)","Cooling period of 3 years required before re-appointment.","ICAI BoS Module",Moderate\n'
                'B,"Part I: Strategic Cost Management",B_MBE,Target Costing,"What is the fundamental formula of Target Costing?","Target Cost = Cost Plus Desired Margin","Target Cost = Target Selling Price - Desired Profit Margin","Target Cost = Standard Cost - Variances","Target Cost = Marginal Cost + Opportunity Cost",B,2,"Target Costing starts from market driven price and backs out target profit.","Target Costing Concept","Driven by customer willingness to pay and competitive market price.","Offline SPOM Recall",Easy\n'
            )
            csv_bytes = csv_content.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/csv; charset=utf-8')
            self.send_header('Content-Disposition', 'attachment; filename="spom_mcq_upload_template.csv"')
            self.send_header('Content-Length', str(len(csv_bytes)))
            self.end_headers()
            self.wfile.write(csv_bytes)
            return

        elif path == "/api/template/json":
            sample_json = [
                {
                    "set_name": "A",
                    "section_group": "Part I: Corporate Laws",
                    "chapter_code": "A_DIR",
                    "topic": "Independent Director Eligibility",
                    "question": "Can a person who was a Key Managerial Personnel in the holding company 2 years ago be appointed as an Independent Director in the subsidiary?",
                    "option_a": "Yes, cooling period is only 1 year",
                    "option_b": "No, cooling period is 3 financial years under Section 149(6)",
                    "option_c": "Yes, with approval of 90% shareholders",
                    "option_d": "Yes, if Central Government permits",
                    "correct_option": "B",
                    "marks": 2,
                    "explanation": "Section 149(6)(e)(i) bars any person who was a KMP or employee in the company or its holding/subsidiary during any of the 3 immediately preceding financial years.",
                    "section_ref": "Section 149(6)(e)(i)",
                    "exam_tip": "3-year lookback period is strictly applied for KMP and employees!",
                    "source_tag": "ICAI BoS Module",
                    "difficulty": "Moderate"
                }
            ]
            json_bytes = json.dumps(sample_json, indent=2).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Disposition', 'attachment; filename="spom_mcq_upload_template.json"')
            self.send_header('Content-Length', str(len(json_bytes)))
            self.end_headers()
            self.wfile.write(json_bytes)
            return

        # 8. Resources & Study Material Hub
        elif path == "/api/resources":
            resources = {
                "study_materials": [
                    {
                        "set": "A",
                        "title": "ICAI BoS Knowledge Portal - SPOM Set A (Corporate & Economic Laws)",
                        "url": "https://www.icai.org/post/bos-knowledge-portal-spom-set-a",
                        "description": "Complete Modules: Part I Corporate Laws (70 Marks) and Part II Economic Laws (30 Marks), MTPs, Case Digest."
                    },
                    {
                        "set": "B",
                        "title": "ICAI BoS Knowledge Portal - SPOM Set B (Strategic Cost & Performance Management)",
                        "url": "https://www.icai.org/post/bos-knowledge-portal-spom-set-b",
                        "description": "Part I Strategic Cost Management (50 Marks) and Part II Performance Evaluation (50 Marks), Formula Compendium."
                    }
                ],
                "youtube_faculty": [
                    {
                        "name": "CA Harsh Gupta",
                        "subject": "Set A - Law & IBC",
                        "highlights": "Comprehensive Bare Act section marathon, penalty codes, and IBC CIRP timelines."
                    },
                    {
                        "name": "CA Shubham Singhal",
                        "subject": "Set A - Fast Track Summary",
                        "highlights": "Summary charts, tricky MCQ traps breakdown, and FEMA Schedule III limits."
                    },
                    {
                        "name": "CA Sankalp Kanstiya",
                        "subject": "Set B - SCMPE & SCPM",
                        "highlights": "Formula revisions, Throughput Accounting, Transfer Pricing case scenarios, and Fitzgerald & Moon Building Block model."
                    },
                    {
                        "name": "CA Hemant Somani",
                        "subject": "Set A & Set B - SPOM Exam Experience & Hacks",
                        "highlights": "Real TCS iON test center experience, actual question traps, and time management."
                    }
                ],
                "high_yield_traps": [
                    {
                        "set": "A",
                        "topic": "Director Disqualification (Sec 164(2))",
                        "rule": "Vacates office in ALL companies EXCEPT the defaulting company (Proviso to Sec 167(1)(a))."
                    },
                    {
                        "set": "A",
                        "topic": "Woman Director Vacancy (Sec 149(1))",
                        "rule": "Intermittent vacancy to be filled by the Board at the earliest, but not later than immediate next Board Meeting OR 3 months from vacancy date, whichever is LATER."
                    },
                    {
                        "set": "A",
                        "topic": "IBC CIRP Extension & Withdrawal",
                        "rule": "Requires 66% CoC voting share for 90-day extension (outer cap 330 days). Withdrawal under Sec 12A requires 90% voting share."
                    },
                    {
                        "set": "A",
                        "topic": "SEBI LODR Material Related Party Transaction",
                        "rule": "Exceeding Rs 1,000 Crore OR 10% of annual consolidated turnover, WHICHEVER IS LOWER."
                    },
                    {
                        "set": "A",
                        "topic": "FCRA 2010 Crucial Amendments",
                        "rule": "Mandatory account exclusively at SBI New Delhi Main Branch; Administrative expense cap strictly 20% (reduced from 50%)."
                    },
                    {
                        "set": "B",
                        "topic": "Throughput Accounting (Goldratt)",
                        "rule": "Throughput = Sales - Direct Material. Labour and overheads are FIXED factory costs, NOT deducted from Throughput! TA Ratio = Return per bottleneck min / Factory cost per bottleneck min."
                    },
                    {
                        "set": "B",
                        "topic": "Transfer Pricing Golden Rule",
                        "rule": "Min TP = Marginal Cost + Opportunity Cost. If spare capacity -> Opportunity Cost = 0 -> Min TP = Marginal Cost. If full capacity -> Opportunity Cost = Lost Contribution -> Min TP = Market Price."
                    },
                    {
                        "set": "B",
                        "topic": "Fitzgerald & Moon Building Block",
                        "rule": "Standards = Ownership, Achievability, Equity (OAE). Rewards = Clarity, Motivation, Controllability (CMC)."
                    },
                    {
                        "set": "B",
                        "topic": "Economic Value Added (EVA)",
                        "rule": "EVA = NOPAT - (Capital Employed x WACC). Non-cash investments like Brand Building & R&D are capitalized, added back to both NOPAT and Capital Employed."
                    }
                ]
            }
            self.send_json({"success": True, "data": resources})
            return

        # 9. Exam Intelligence Dashboard & Recommendations
        elif path == "/api/intelligence/dashboard":
            set_name = query.get('set', ['A'])[0].upper()
            stats = database.get_topic_stats(set_name)
            study_today = database.get_study_today_recommendations(set_name, limit=5)
            syllabus = database.get_syllabus_versions(set_name)
            self.send_json({
                "success": True,
                "set_name": set_name,
                "stats": stats,
                "study_today": study_today,
                "syllabus": syllabus[0] if syllabus else None
            })
            return

        # 10. Exam Intelligence Topics (with explainable 0-100 priority scores)
        elif path == "/api/intelligence/topics":
            set_name = query.get('set', [None])[0]
            chapter_code = query.get('chapter', [None])[0]
            priority_level = query.get('priority', [None])[0]
            search = query.get('search', [None])[0]
            topics = database.get_topics(set_name, chapter_code, priority_level, search)
            self.send_json({"success": True, "count": len(topics), "data": topics})
            return

        # 11. Important Topics & Revision Handbook Content
        elif path == "/api/handbook":
            set_name = query.get('set', ['A'])[0].upper()
            chapter_code = query.get('chapter', [None])[0]
            category = query.get('category', [None])[0]
            content = database.get_handbook_content(set_name, chapter_code, category)
            self.send_json({"success": True, "count": len(content), "data": content})
            return

        # 12. My Mistakes Book
        elif path == "/api/mistakes":
            set_name = query.get('set', [None])[0]
            status = query.get('status', [None])[0]
            mistakes = database.get_mistakes_book(set_name, status)
            self.send_json({"success": True, "count": len(mistakes), "data": mistakes})
            return

        # 13. Intelligent Practice Engine (10 Modes + Immediate Feedback)
        elif path == "/api/practice/questions":
            set_name = query.get('set', ['A'])[0].upper()
            mode = query.get('mode', ['mixed'])[0]
            chapter_code = query.get('chapter', [None])[0] or query.get('chapters', [None])[0]
            count = int(query.get('count', [10])[0])
            cohort = query.get('cohort', [None])[0]
            shuffle_options = query.get('shuffle_options', ['true'])[0].lower() == 'true'

            questions = database.get_practice_questions(set_name, mode, chapter_code, count, cohort=cohort)
            final_qs = []
            for idx, q in enumerate(questions):
                opts = [
                    {"original_key": "A", "text": q['option_a']},
                    {"original_key": "B", "text": q['option_b']},
                    {"original_key": "C", "text": q['option_c']},
                    {"original_key": "D", "text": q['option_d']}
                ]
                if shuffle_options:
                    random.shuffle(opts)

                shuffled_opts = {
                    "option_a": opts[0]["text"],
                    "option_b": opts[1]["text"],
                    "option_c": opts[2]["text"],
                    "option_d": opts[3]["text"]
                }
                correct_orig = q['correct_option'].strip().upper()
                shuffled_correct_key = "A"
                for letter, opt_obj in zip(["A", "B", "C", "D"], opts):
                    if opt_obj["original_key"] == correct_orig:
                        shuffled_correct_key = letter
                        break

                # Map why_incorrect rationale to match shuffled option positions
                why_incorrect_mapped = {}
                for letter, opt_obj in zip(["A", "B", "C", "D"], opts):
                    orig_k = opt_obj["original_key"].lower()
                    why_incorrect_mapped[f"why_incorrect_{letter.lower()}"] = q.get(f"why_incorrect_{orig_k}", "")

                q_safe = {
                    "id": q['id'],
                    "q_index": idx + 1,
                    "set_name": q['set_name'],
                    "section_group": q['section_group'],
                    "chapter_code": q['chapter_code'],
                    "topic": q['topic'],
                    "subtopic": q.get('subtopic', ''),
                    "question": q['question'],
                    "option_a": shuffled_opts["option_a"],
                    "option_b": shuffled_opts["option_b"],
                    "option_c": shuffled_opts["option_c"],
                    "option_d": shuffled_opts["option_d"],
                    "correct_option": shuffled_correct_key,
                    "marks": q.get('marks', 2),
                    "explanation": q.get('explanation', ''),
                    "why_incorrect_a": why_incorrect_mapped["why_incorrect_a"],
                    "why_incorrect_b": why_incorrect_mapped["why_incorrect_b"],
                    "why_incorrect_c": why_incorrect_mapped["why_incorrect_c"],
                    "why_incorrect_d": why_incorrect_mapped["why_incorrect_d"],
                    "section_ref": q.get('section_ref', ''),
                    "exam_tip": q.get('exam_tip', ''),
                    "source_tag": q.get('source_tag', 'ICAI BoS Module'),
                    "difficulty": q.get('difficulty', 'Moderate'),
                    "is_case_study": q.get('is_case_study', 0),
                    "case_scenario": q.get('case_scenario', ''),
                    "is_bookmarked": q.get('is_bookmarked', 0),
                    "mistake_count": q.get('mistake_count', 0),
                    "mistake_status": q.get('mistake_status', '')
                }
                final_qs.append(q_safe)

            self.send_json({
                "success": True,
                "set_name": set_name,
                "mode": mode,
                "count": len(final_qs),
                "questions": final_qs
            })
            return

        # 14. Research Records & Audit Log
        elif path == "/api/research/logs":
            set_name = query.get('set', [None])[0]
            source_type = query.get('source_type', [None])[0]
            records = database.get_research_records(set_name, source_type)
            self.send_json({"success": True, "count": len(records), "data": records})
            return

        # 15. Syllabus & Amendment Status
        elif path == "/api/syllabus/status":
            set_name = query.get('set', [None])[0]
            versions = database.get_syllabus_versions(set_name)
            self.send_json({"success": True, "data": versions})
            return

        # Serve static file from PUBLIC_DIR
        return super().do_GET()

    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        content_length = int(self.headers.get('Content-Length', 0))
        body_bytes = self.rfile.read(content_length)
        content_type = self.headers.get('Content-Type', '')

        # 1. Bookmark Toggle Endpoint
        if path == "/api/bookmark/toggle":
            try:
                data = json.loads(body_bytes.decode('utf-8'))
                mcq_id = int(data.get('mcq_id'))
                notes = data.get('notes', '')
                is_bm = database.toggle_bookmark(mcq_id, notes)
                self.send_json({"success": True, "is_bookmarked": is_bm, "mcq_id": mcq_id})
            except Exception as e:
                self.send_json({"success": False, "error": str(e)}, status_code=400)
            return

        # 2. Submit Mock Test & Score Calculation
        # 2. Submit Mock Test & Score Calculation (Strictly Evaluated Across ALL Test Questions)
        elif path == "/api/submit-test":
            try:
                data = json.loads(body_bytes.decode('utf-8'))
            except Exception as e:
                self.send_json({"success": False, "error": f"Invalid JSON payload: {str(e)}"}, status_code=400)
                return

            set_name = data.get('set_name', 'A').upper()
            mode = data.get('mode', 'full_mock_50')
            time_taken_seconds = int(data.get('time_taken_seconds', 0))

            submitted_questions = data.get('questions', [])
            user_responses = data.get('responses', {})
            correct_keys_map = data.get('correct_keys', {})

            evaluated_items = []
            total_score = 0.0
            max_marks = 0.0
            correct_count = 0
            incorrect_count = 0
            unattempted_count = 0

            part1_score = 0.0
            part1_max = 0.0
            part2_score = 0.0
            part2_max = 0.0
            chapter_breakdown = {}

            if submitted_questions:
                total_questions = len(submitted_questions)
                for idx, q_item in enumerate(submitted_questions):
                    q_id = q_item.get('id')
                    mcq_db = database.get_mcq_by_id(q_id) if q_id else None

                    marks = float(q_item.get('marks') or (mcq_db.get('marks', 2) if mcq_db else 2))
                    max_marks += marks

                    ch_code = q_item.get('chapter_code') or (mcq_db.get('chapter_code', 'GEN') if mcq_db else 'GEN')
                    sec_group = q_item.get('section_group') or (mcq_db.get('section_group', '') if mcq_db else '')
                    is_part1 = "Part I" in sec_group

                    if is_part1:
                        part1_max += marks
                    else:
                        part2_max += marks

                    if ch_code not in chapter_breakdown:
                        chapter_breakdown[ch_code] = {
                            "name": ch_code,
                            "section_group": sec_group,
                            "total": 0, "correct": 0, "incorrect": 0, "unattempted": 0, "score": 0.0, "max_marks": 0.0
                        }
                    chapter_breakdown[ch_code]["total"] += 1
                    chapter_breakdown[ch_code]["max_marks"] += marks

                    # Exact options presented to candidate during exam (PRESERVED 100% WITHOUT RESHUFFLE)
                    opt_a = q_item.get('option_a') or (mcq_db.get('option_a', '') if mcq_db else '')
                    opt_b = q_item.get('option_b') or (mcq_db.get('option_b', '') if mcq_db else '')
                    opt_c = q_item.get('option_c') or (mcq_db.get('option_c', '') if mcq_db else '')
                    opt_d = q_item.get('option_d') or (mcq_db.get('option_d', '') if mcq_db else '')

                    opts_dict = {'A': opt_a, 'B': opt_b, 'C': opt_c, 'D': opt_d}

                    # Determine selected answer and correct answer for this presentation
                    user_sel = (q_item.get('user_selected_key') or user_responses.get(str(q_id), '') or '').strip().upper()
                    correct_key = (q_item.get('shuffled_correct_key') or correct_keys_map.get(str(q_id)) or (mcq_db.get('correct_option', 'A') if mcq_db else 'A')).strip().upper()

                    is_attempted = bool(user_sel and user_sel in ['A', 'B', 'C', 'D'])
                    is_correct = bool(is_attempted and user_sel == correct_key)

                    selected_text = opts_dict.get(user_sel, '') if is_attempted else None
                    correct_text = opts_dict.get(correct_key, '')

                    # Map selected option back to database canonical key for Mistakes Book
                    orig_sel_key = user_sel if is_attempted else None
                    if is_attempted and mcq_db and selected_text:
                        for db_k in ['A', 'B', 'C', 'D']:
                            if mcq_db.get(f'option_{db_k.lower()}') == selected_text:
                                orig_sel_key = db_k
                                break

                    if is_attempted:
                        if is_correct:
                            total_score += marks
                            correct_count += 1
                            chapter_breakdown[ch_code]["correct"] += 1
                            chapter_breakdown[ch_code]["score"] += marks
                            if is_part1:
                                part1_score += marks
                            else:
                                part2_score += marks
                        else:
                            incorrect_count += 1
                            chapter_breakdown[ch_code]["incorrect"] += 1
                    else:
                        unattempted_count += 1
                        chapter_breakdown[ch_code]["unattempted"] += 1

                    evaluated_items.append({
                        "id": q_id,
                        "q_index": idx + 1,
                        "question": q_item.get('question') or (mcq_db.get('question', '') if mcq_db else ''),
                        "section_group": sec_group,
                        "chapter_code": ch_code,
                        "topic": q_item.get('topic') or (mcq_db.get('topic', '') if mcq_db else ''),
                        "option_a": opt_a,
                        "option_b": opt_b,
                        "option_c": opt_c,
                        "option_d": opt_d,
                        "selected_option": user_sel if is_attempted else None,
                        "selected_text": selected_text,
                        "correct_option": correct_key,
                        "correct_text": correct_text,
                        "canonical_selected_option": orig_sel_key,
                        "is_correct": is_correct,
                        "is_attempted": is_attempted,
                        "marks_awarded": marks if is_correct else 0.0,
                        "max_marks": marks,
                        "explanation": mcq_db.get('explanation', '') if mcq_db else '',
                        "section_ref": mcq_db.get('section_ref', '') if mcq_db else '',
                        "exam_tip": mcq_db.get('exam_tip', '') if mcq_db else '',
                        "source_tag": q_item.get('source_tag') or (mcq_db.get('source_tag', 'ICAI BoS Module') if mcq_db else 'ICAI BoS Module'),
                        "is_bookmarked": mcq_db.get('is_bookmarked', 0) if mcq_db else 0
                    })
            else:
                # Fallback if client sent only user_responses map
                question_ids = list(user_responses.keys())
                total_questions = len(question_ids)
                for idx, q_id_str in enumerate(question_ids):
                    try:
                        q_id = int(q_id_str)
                    except ValueError:
                        continue
                    mcq = database.get_mcq_by_id(q_id)
                    if not mcq:
                        continue

                    marks = mcq.get('marks', 2)
                    max_marks += marks
                    ch_code = mcq.get('chapter_code', 'GEN')
                    sec_group = mcq.get('section_group', '')
                    is_part1 = "Part I" in sec_group

                    if is_part1:
                        part1_max += marks
                    else:
                        part2_max += marks

                    if ch_code not in chapter_breakdown:
                        chapter_breakdown[ch_code] = {
                            "name": ch_code, "section_group": sec_group,
                            "total": 0, "correct": 0, "incorrect": 0, "unattempted": 0, "score": 0.0, "max_marks": 0.0
                        }
                    chapter_breakdown[ch_code]["total"] += 1
                    chapter_breakdown[ch_code]["max_marks"] += marks

                    user_ans = (user_responses.get(q_id_str) or '').strip().upper()
                    correct_clean = correct_keys_map.get(q_id_str, mcq.get('correct_option', 'A')).strip().upper()
                    is_attempted = bool(user_ans and user_ans in ['A', 'B', 'C', 'D'])
                    is_correct = bool(is_attempted and user_ans == correct_clean)

                    if is_attempted:
                        if is_correct:
                            total_score += marks
                            correct_count += 1
                            chapter_breakdown[ch_code]["correct"] += 1
                            chapter_breakdown[ch_code]["score"] += marks
                            if is_part1: part1_score += marks
                            else: part2_score += marks
                        else:
                            incorrect_count += 1
                            chapter_breakdown[ch_code]["incorrect"] += 1
                    else:
                        unattempted_count += 1
                        chapter_breakdown[ch_code]["unattempted"] += 1

                    evaluated_items.append({
                        "id": mcq['id'],
                        "q_index": idx + 1,
                        "question": mcq['question'],
                        "section_group": sec_group,
                        "chapter_code": ch_code,
                        "topic": mcq['topic'],
                        "option_a": mcq['option_a'],
                        "option_b": mcq['option_b'],
                        "option_c": mcq['option_c'],
                        "option_d": mcq['option_d'],
                        "selected_option": user_ans if is_attempted else None,
                        "selected_text": mcq.get(f"option_{user_ans.lower()}") if is_attempted else None,
                        "correct_option": correct_clean,
                        "correct_text": mcq.get(f"option_{correct_clean.lower()}"),
                        "canonical_selected_option": user_ans if is_attempted else None,
                        "is_correct": is_correct,
                        "is_attempted": is_attempted,
                        "marks_awarded": marks if is_correct else 0.0,
                        "max_marks": marks,
                        "explanation": mcq['explanation'],
                        "section_ref": mcq['section_ref'],
                        "exam_tip": mcq['exam_tip'],
                        "source_tag": mcq.get('source_tag', 'ICAI BoS Module'),
                        "is_bookmarked": mcq.get('is_bookmarked', 0)
                    })

            # Percentage computed strictly on total possible exam marks (e.g. 100 Marks)
            percentage = round((total_score / max_marks * 100), 2) if max_marks > 0 else 0.0
            passed = bool(total_score >= (max_marks * 0.50)) # Mandatory 50% passing threshold

            # Result record prepared for database and client
            result_record = {
                "set_name": set_name,
                "mode": mode,
                "total_questions": total_questions,
                "attempted": correct_count + incorrect_count,
                "unattempted": unattempted_count,
                "correct": correct_count,
                "incorrect": incorrect_count,
                "score": round(total_score, 1),
                "max_marks": round(max_marks, 1),
                "percentage": percentage,
                "passed": passed,
                "time_taken_seconds": time_taken_seconds,
                "breakdown": {
                    "part1": {"score": round(part1_score, 1), "max_marks": round(part1_max, 1), "percentage": round((part1_score/part1_max*100) if part1_max>0 else 0, 1)},
                    "part2": {"score": round(part2_score, 1), "max_marks": round(part2_max, 1), "percentage": round((part2_score/part2_max*100) if part2_max>0 else 0, 1)},
                    "chapters": chapter_breakdown
                },
                "responses": [
                    {
                        "id": it["id"],
                        "is_attempted": it["is_attempted"],
                        "is_correct": it["is_correct"],
                        "selected_option": it.get("canonical_selected_option") or it.get("selected_option")
                    } for it in evaluated_items
                ]
            }

            saved_attempt = database.save_attempt(result_record)

            self.send_json({
                "success": True,
                "attempt_id": saved_attempt['id'],
                "result": {
                    "set_name": set_name,
                    "mode": mode,
                    "total_questions": total_questions,
                    "attempted": correct_count + incorrect_count,
                    "unattempted": unattempted_count,
                    "correct": correct_count,
                    "incorrect": incorrect_count,
                    "score": round(total_score, 1),
                    "max_marks": round(max_marks, 1),
                    "percentage": percentage,
                    "passed": passed,
                    "time_taken_seconds": time_taken_seconds,
                    "sectional_breakdown": {
                        "part1": {"score": round(part1_score, 1), "max_marks": round(part1_max, 1), "percentage": round((part1_score/part1_max*100) if part1_max>0 else 0, 1)},
                        "part2": {"score": round(part2_score, 1), "max_marks": round(part2_max, 1), "percentage": round((part2_score/part2_max*100) if part2_max>0 else 0, 1)}
                    },
                    "chapter_breakdown": chapter_breakdown,
                    "questions": evaluated_items,
                    "responses": evaluated_items
                }
            })
            return

        # Record immediate practice drill question attempt
        elif path == "/api/record-practice-attempt":
            try:
                data = json.loads(body_bytes.decode('utf-8'))
                q_id = int(data.get('mcq_id'))
                is_correct = bool(data.get('is_correct'))
                selected_text = data.get('selected_text', '')

                mcq = database.get_mcq_by_id(q_id)
                if mcq:
                    if is_correct:
                        database.record_correct_attempt(q_id)
                    else:
                        orig_sel_key = 'A'
                        for db_k in ['A', 'B', 'C', 'D']:
                            if mcq.get(f'option_{db_k.lower()}') == selected_text:
                                orig_sel_key = db_k
                                break
                        database.record_mistake(q_id, orig_sel_key)
                    database.record_question_progress(q_id, is_correct)
                self.send_json({"success": True})
            except Exception as e:
                self.send_json({"success": False, "error": str(e)}, status_code=400)
            return

        # 3. Add Single MCQ
        elif path == "/api/mcq":
            try:
                data = json.loads(body_bytes.decode('utf-8'))
            except Exception as e:
                self.send_json({"success": False, "error": f"Invalid JSON payload: {str(e)}"}, status_code=400)
                return

            required = ['set_name', 'question', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option']
            missing = [r for r in required if not data.get(r)]
            if missing:
                self.send_json({"success": False, "error": f"Missing required fields: {', '.join(missing)}"}, status_code=400)
                return

            new_id = database.add_mcq(data)
            self.send_json({"success": True, "message": "MCQ added successfully", "mcq_id": new_id})
            return

        # 4. Delete Single MCQ
        elif path == "/api/mcq/delete":
            try:
                data = json.loads(body_bytes.decode('utf-8'))
                mcq_id = data.get('id')
            except Exception:
                mcq_id = None

            if not mcq_id:
                self.send_json({"success": False, "error": "MCQ id is required"}, status_code=400)
                return

            deleted = database.delete_mcq(mcq_id)
            if deleted:
                self.send_json({"success": True, "message": f"MCQ #{mcq_id} deleted successfully"})
            else:
                self.send_json({"success": False, "error": "MCQ not found"}, status_code=404)
            return

        # 5. Bulk Upload (CSV / JSON)
        elif path == "/api/mcqs/bulk-upload":
            content_str = body_bytes.decode('utf-8', errors='ignore')
            items_to_insert = []
            
            if "application/json" in content_type or content_str.strip().startswith("[") or content_str.strip().startswith("{"):
                try:
                    parsed = json.loads(content_str)
                    items_to_insert = parsed.get("mcqs", parsed) if isinstance(parsed, dict) else parsed
                except Exception as e:
                    self.send_json({"success": False, "error": f"Failed to parse JSON: {str(e)}"}, status_code=400)
                    return
            else:
                try:
                    f = io.StringIO(content_str)
                    reader = csv.DictReader(f)
                    for row in reader:
                        cleaned_row = {k.strip(): v.strip() for k, v in row.items() if k}
                        if cleaned_row.get('question'):
                            items_to_insert.append(cleaned_row)
                except Exception as e:
                    self.send_json({"success": False, "error": f"Failed to parse CSV: {str(e)}"}, status_code=400)
                    return

            if not items_to_insert:
                self.send_json({"success": False, "error": "No valid MCQs found in payload."}, status_code=400)
                return

            added_count = 0
            errors = []
            for idx, item in enumerate(items_to_insert):
                try:
                    set_name = item.get('set_name', 'A').strip().upper()
                    if set_name not in ['A', 'B']:
                        set_name = 'A'
                    
                    correct_opt = item.get('correct_option', 'A').strip().upper()
                    if correct_opt not in ['A', 'B', 'C', 'D']:
                        correct_opt = 'A'

                    mcq_payload = {
                        "set_name": set_name,
                        "section_group": item.get('section_group', ''),
                        "chapter_code": item.get('chapter_code', f"{set_name}_DIR" if set_name=='A' else f"{set_name}_SCM"),
                        "topic": item.get('topic', 'General'),
                        "question": item.get('question', ''),
                        "option_a": item.get('option_a', ''),
                        "option_b": item.get('option_b', ''),
                        "option_c": item.get('option_c', ''),
                        "option_d": item.get('option_d', ''),
                        "correct_option": correct_opt,
                        "marks": int(item.get('marks', 2)),
                        "explanation": item.get('explanation', ''),
                        "section_ref": item.get('section_ref', ''),
                        "exam_tip": item.get('exam_tip', ''),
                        "source_tag": item.get('source_tag', 'ICAI BoS Module'),
                        "difficulty": item.get('difficulty', 'Moderate'),
                        "is_case_study": 1 if item.get('is_case_study') in [1, True, '1', 'true', 'True'] else 0,
                        "case_scenario": item.get('case_scenario', ''),
                        "is_user_uploaded": True
                    }

                    if mcq_payload['question'] and mcq_payload['option_a'] and mcq_payload['option_b']:
                        database.add_mcq(mcq_payload)
                        added_count += 1
                    else:
                        errors.append(f"Row #{idx + 1}: Missing question or options.")
                except Exception as ex:
                    errors.append(f"Row #{idx + 1}: {str(ex)}")

            self.send_json({
                "success": True,
                "message": f"Successfully uploaded {added_count} MCQs into the database.",
                "added_count": added_count,
                "total_rows": len(items_to_insert),
                "errors": errors
            })
            return

        # 6. Mark Topic Revised / Unrevised
        elif path == "/api/intelligence/topic/revise":
            try:
                data = json.loads(body_bytes.decode('utf-8'))
                topic_id = int(data.get('topic_id'))
                is_revised = int(data.get('is_revised', 1))
                database.mark_topic_revised(topic_id, is_revised)
                self.send_json({"success": True, "topic_id": topic_id, "is_revised": is_revised})
            except Exception as e:
                self.send_json({"success": False, "error": str(e)}, status_code=400)
            return

        # 7. Update Mistakes Book Status & Notes
        elif path == "/api/mistakes/status":
            try:
                data = json.loads(body_bytes.decode('utf-8'))
                mistake_id = int(data.get('mistake_id'))
                status = data.get('status', 'Reviewed')
                notes = data.get('notes', None)
                database.update_mistake_status(mistake_id, status, notes)
                self.send_json({"success": True, "mistake_id": mistake_id, "status": status})
            except Exception as e:
                self.send_json({"success": False, "error": str(e)}, status_code=400)
            return

        # 8. Research Ingestion Record
        elif path == "/api/research/ingest":
            try:
                data = json.loads(body_bytes.decode('utf-8'))
                new_id = database.add_research_record(data)
                self.send_json({"success": True, "id": new_id, "message": "Research record ingested successfully."})
            except Exception as e:
                self.send_json({"success": False, "error": str(e)}, status_code=400)
            return

        self.send_json({"success": False, "error": f"Endpoint not found: {path}"}, status_code=404)

def run_server(port=PORT):
    database.init_db()
    seed_data.seed_database()
    seed_intelligence.seed_intelligence()

    server_address = ('', port)
    httpd = ThreadingHTTPServer(server_address, SPOMRequestHandler)
    print(f"============================================================")
    print(f" CA FINAL SPOM HIGH-STAKES EXAM PORTAL")
    print(f" Port: {port} | Root: {PUBLIC_DIR}")
    print(f" Set A: Part I Corporate Laws (70M) + Part II Economic Laws (30M)")
    print(f" Set B: Part I Strategic Cost (50M) + Part II Performance (50M)")
    print(f" Dynamic Shuffling & Provenance Tracking Active")
    print(f"============================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server gracefully...")
        httpd.server_close()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    run_server(port)
