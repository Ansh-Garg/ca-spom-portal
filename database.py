"""
Database layer for CA Final SPOM Intelligence-Driven Portal
Features:
- Safe, non-destructive schema migrations
- Exam Intelligence Centre & Topic Priority Scoring (0-100)
- Master Question Bank with verification & provenance tracking
- My Mistakes Book with spaced revision status
- Research Records & Ingestion Logging
- Syllabus & Amendment Control
- Important Topics & Quick Revision Handbook
"""
import sqlite3
import json
import os
import shutil
from datetime import datetime

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spom_portal.db")
BACKUP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "backups")

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def backup_database():
    """Create timestamped backup before migrations"""
    if os.path.exists(DB_FILE):
        os.makedirs(BACKUP_DIR, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(BACKUP_DIR, f"spom_portal_backup_{ts}.db")
        shutil.copy2(DB_FILE, backup_path)
        return backup_path
    return None

def init_db():
    """Initialize or upgrade database schema safely without data loss"""
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Chapters table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chapters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        set_name TEXT NOT NULL,
        code TEXT NOT NULL UNIQUE,
        name TEXT NOT NULL,
        section_group TEXT NOT NULL,
        weightage TEXT NOT NULL,
        description TEXT,
        youtube_review_tips TEXT,
        icai_resource_link TEXT,
        order_seq INTEGER DEFAULT 0
    )
    """)

    # 2. MCQs table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mcqs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        set_name TEXT NOT NULL,
        section_group TEXT NOT NULL,
        chapter_code TEXT NOT NULL,
        topic TEXT NOT NULL,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_option TEXT NOT NULL,
        marks INTEGER DEFAULT 2,
        explanation TEXT NOT NULL,
        section_ref TEXT,
        exam_tip TEXT,
        source_tag TEXT DEFAULT 'ICAI BoS Module',
        difficulty TEXT DEFAULT 'Moderate',
        is_case_study INTEGER DEFAULT 0,
        case_scenario TEXT,
        is_user_uploaded INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Check and add new columns to mcqs safely
    cursor.execute("PRAGMA table_info(mcqs)")
    existing_mcq_cols = {row['name'] for row in cursor.fetchall()}
    
    new_mcq_cols = {
        'subtopic': "TEXT DEFAULT ''",
        'why_incorrect_a': "TEXT DEFAULT ''",
        'why_incorrect_b': "TEXT DEFAULT ''",
        'why_incorrect_c': "TEXT DEFAULT ''",
        'why_incorrect_d': "TEXT DEFAULT ''",
        'source_url_or_ref': "TEXT DEFAULT ''",
        'source_date': "TEXT DEFAULT ''",
        'verification_status': "TEXT DEFAULT 'Verified'",
        'is_outdated_law': "INTEGER DEFAULT 0",
        'amendment_notes': "TEXT DEFAULT ''",
        'topic_id': "INTEGER DEFAULT NULL"
    }

    for col, col_def in new_mcq_cols.items():
        if col not in existing_mcq_cols:
            cursor.execute(f"ALTER TABLE mcqs ADD COLUMN {col} {col_def}")

    # 3. Attempts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        set_name TEXT NOT NULL,
        mode TEXT NOT NULL,
        chapter_code TEXT,
        total_questions INTEGER NOT NULL,
        attempted INTEGER NOT NULL,
        correct INTEGER NOT NULL,
        incorrect INTEGER NOT NULL,
        score REAL NOT NULL,
        max_marks REAL NOT NULL,
        percentage REAL NOT NULL,
        passed INTEGER NOT NULL,
        time_taken_seconds INTEGER NOT NULL,
        attempted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        breakdown_json TEXT,
        responses_json TEXT
    )
    """)

    # 4. Bookmarks table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookmarks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mcq_id INTEGER NOT NULL UNIQUE,
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (mcq_id) REFERENCES mcqs (id) ON DELETE CASCADE
    )
    """)

    # 5. Topics & Priority Scoring table (Intelligence Engine)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS topics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        set_name TEXT NOT NULL,
        chapter_code TEXT NOT NULL,
        name TEXT NOT NULL,
        subtopic TEXT DEFAULT '',
        description TEXT,
        icai_score REAL DEFAULT 0,           -- 25% weight: ICAI study material / TYK relevance
        student_recall_score REAL DEFAULT 0, -- 25% weight: Actual exam recall frequency (Reddit/Quora)
        faculty_score REAL DEFAULT 0,        -- 20% weight: Faculty masterclass recommendations
        case_score REAL DEFAULT 0,           -- 15% weight: ICAI case scenarios & MTPs
        trap_score REAL DEFAULT 0,           -- 15% weight: Conceptual difficulty & traps
        priority_score REAL DEFAULT 0,       -- Sum of weights (0 to 100)
        priority_level TEXT DEFAULT 'Moderate Priority', -- Very High, High, Moderate, Standard
        student_reports_count INTEGER DEFAULT 0,
        faculty_recs_count INTEGER DEFAULT 0,
        icai_question_count INTEGER DEFAULT 0,
        key_provisions TEXT,
        common_traps TEXT,
        is_revised INTEGER DEFAULT 0,
        last_revised_at TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(set_name, chapter_code, name)
    )
    """)

    # 6. My Mistakes Book table (Performance Tracking & Spaced Revision)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mistakes_book (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mcq_id INTEGER NOT NULL UNIQUE,
        set_name TEXT NOT NULL,
        chapter_code TEXT NOT NULL,
        incorrect_count INTEGER DEFAULT 1,
        last_selected_option TEXT,
        last_attempted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        revision_status TEXT DEFAULT 'Unrevised', -- 'Unrevised', 'Reviewed', 'Mastered'
        notes TEXT DEFAULT '',
        FOREIGN KEY (mcq_id) REFERENCES mcqs (id) ON DELETE CASCADE
    )
    """)

    # 7. Research Records table (Research Ingestion & Audit Log)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS research_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        set_name TEXT NOT NULL,
        source_type TEXT NOT NULL, -- 'ICAI Official', 'Reddit / Student Recall', 'YouTube / Faculty', 'Educational Forum'
        source_author TEXT,
        title TEXT NOT NULL,
        source_url TEXT,
        summary TEXT NOT NULL,
        extracted_topics TEXT,
        reliability_rating TEXT DEFAULT 'High', -- 'Official / Highest', 'High', 'Moderate'
        verification_status TEXT DEFAULT 'Verified', -- 'Verified', 'Under Review', 'Draft'
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 8. Syllabus & Amendment Versions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS syllabus_versions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        set_name TEXT NOT NULL,
        scheme_name TEXT NOT NULL,
        applicable_attempt TEXT NOT NULL,
        amendment_cutoff_date TEXT NOT NULL,
        law_applicable_notes TEXT,
        is_active INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 9. Important Topics & Revision Handbook Content
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS handbook_content (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        set_name TEXT NOT NULL,
        chapter_code TEXT NOT NULL,
        category TEXT NOT NULL, -- 'summary', 'quick_sheet', 'formulas_limits', 'confused_concepts', 'exam_traps'
        title TEXT NOT NULL,
        content_json TEXT NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(set_name, chapter_code, category)
    )
    """)

    conn.commit()
    conn.close()

# =========================================================================
# CHAPTERS & TOPICS INTELLIGENCE CRUD
# =========================================================================

def get_chapters(set_name=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if set_name:
        cursor.execute("""
            SELECT c.*, COUNT(m.id) as mcq_count 
            FROM chapters c
            LEFT JOIN mcqs m ON c.code = m.chapter_code AND c.set_name = m.set_name
            WHERE c.set_name = ?
            GROUP BY c.id
            ORDER BY c.order_seq ASC
        """, (set_name.upper(),))
    else:
        cursor.execute("""
            SELECT c.*, COUNT(m.id) as mcq_count 
            FROM chapters c
            LEFT JOIN mcqs m ON c.code = m.chapter_code AND c.set_name = m.set_name
            GROUP BY c.id
            ORDER BY c.set_name ASC, c.order_seq ASC
        """)
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def get_topics(set_name=None, chapter_code=None, priority_level=None, search=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM topics WHERE 1=1"
    params = []

    if set_name:
        query += " AND set_name = ?"
        params.append(set_name.upper())
    if chapter_code and chapter_code != 'all':
        query += " AND chapter_code = ?"
        params.append(chapter_code)
    if priority_level and priority_level != 'all':
        query += " AND priority_level = ?"
        params.append(priority_level)
    if search:
        query += " AND (name LIKE ? OR key_provisions LIKE ? OR description LIKE ?)"
        term = f"%{search}%"
        params.extend([term, term, term])

    query += " ORDER BY priority_score DESC, student_reports_count DESC"
    cursor.execute(query, params)
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def calculate_priority_score(icai_score, recall_score, faculty_score, case_score, trap_score):
    """
    Explainable Priority Formula:
    ICAI (25%) + Recall (25%) + Faculty (20%) + Case Study (15%) + Trap/Difficulty (15%)
    Total = 0 to 100
    """
    total = round(icai_score + recall_score + faculty_score + case_score + trap_score, 1)
    total = min(100.0, max(0.0, total))
    
    if total >= 85.0:
        level = "Very High Priority"
    elif total >= 70.0:
        level = "High Priority"
    elif total >= 50.0:
        level = "Moderate Priority"
    else:
        level = "Standard Coverage"

    return total, level

def upsert_topic(topic_data):
    conn = get_db_connection()
    cursor = conn.cursor()

    icai = float(topic_data.get('icai_score', 0))
    recall = float(topic_data.get('student_recall_score', 0))
    faculty = float(topic_data.get('faculty_score', 0))
    case = float(topic_data.get('case_score', 0))
    trap = float(topic_data.get('trap_score', 0))

    total, level = calculate_priority_score(icai, recall, faculty, case, trap)

    cursor.execute("""
    INSERT INTO topics (
        set_name, chapter_code, name, subtopic, description,
        icai_score, student_recall_score, faculty_score, case_score, trap_score,
        priority_score, priority_level, student_reports_count, faculty_recs_count,
        icai_question_count, key_provisions, common_traps
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(set_name, chapter_code, name) DO UPDATE SET
        subtopic=excluded.subtopic,
        description=excluded.description,
        icai_score=excluded.icai_score,
        student_recall_score=excluded.student_recall_score,
        faculty_score=excluded.faculty_score,
        case_score=excluded.case_score,
        trap_score=excluded.trap_score,
        priority_score=excluded.priority_score,
        priority_level=excluded.priority_level,
        student_reports_count=excluded.student_reports_count,
        faculty_recs_count=excluded.faculty_recs_count,
        icai_question_count=excluded.icai_question_count,
        key_provisions=excluded.key_provisions,
        common_traps=excluded.common_traps
    """, (
        topic_data.get('set_name', 'A').upper(),
        topic_data.get('chapter_code', ''),
        topic_data.get('name', '').strip(),
        topic_data.get('subtopic', ''),
        topic_data.get('description', ''),
        icai, recall, faculty, case, trap,
        total, level,
        int(topic_data.get('student_reports_count', 0)),
        int(topic_data.get('faculty_recs_count', 0)),
        int(topic_data.get('icai_question_count', 0)),
        topic_data.get('key_provisions', ''),
        topic_data.get('common_traps', '')
    ))
    conn.commit()
    conn.close()

def mark_topic_revised(topic_id, is_revised=1):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE topics 
    SET is_revised = ?, last_revised_at = CURRENT_TIMESTAMP
    WHERE id = ?
    """, (is_revised, topic_id))
    conn.commit()
    conn.close()

def get_study_today_recommendations(set_name='A', limit=5):
    """
    Intelligent Study Recommendation Algorithm:
    Selects top unrevised topics weighted by priority score,
    plus chapters where the student has recorded mistakes in My Mistakes Book.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Unrevised High & Very High Priority Topics
    cursor.execute("""
    SELECT t.*, c.name as chapter_name, c.weightage as chapter_weightage
    FROM topics t
    JOIN chapters c ON t.chapter_code = c.code AND t.set_name = c.set_name
    WHERE t.set_name = ? AND t.is_revised = 0
    ORDER BY t.priority_score DESC
    LIMIT ?
    """, (set_name.upper(), limit))
    recs = [dict(r) for r in cursor.fetchall()]

    # 2. Check weak chapters from mistakes
    cursor.execute("""
    SELECT chapter_code, COUNT(*) as mistake_count
    FROM mistakes_book
    WHERE set_name = ? AND revision_status != 'Mastered'
    GROUP BY chapter_code
    ORDER BY mistake_count DESC
    LIMIT 3
    """, (set_name.upper(),))
    weak_chapters = [dict(r) for r in cursor.fetchall()]

    conn.close()
    return {
        "recommended_topics": recs,
        "weak_chapters": weak_chapters
    }

# =========================================================================
# MASTER QUESTION BANK CRUD & QUALITY CONTROL
# =========================================================================

def get_mcqs(set_name=None, chapter_code=None, source_tag=None, section_group=None, 
             difficulty=None, verification_status=None, limit=None, random_order=False):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        SELECT m.*, 
               CASE WHEN b.id IS NOT NULL THEN 1 ELSE 0 END as is_bookmarked,
               CASE WHEN mb.id IS NOT NULL THEN mb.incorrect_count ELSE 0 END as mistake_count,
               mb.revision_status as mistake_status
        FROM mcqs m
        LEFT JOIN bookmarks b ON m.id = b.mcq_id
        LEFT JOIN mistakes_book mb ON m.id = mb.mcq_id
        WHERE 1=1
    """
    params = []
    
    if set_name:
        query += " AND m.set_name = ?"
        params.append(set_name.upper())
    if chapter_code and chapter_code != 'all':
        if isinstance(chapter_code, (list, tuple)):
            codes = [c.strip() for c in chapter_code if c.strip() and c.strip().lower() != 'all']
        elif isinstance(chapter_code, str) and ',' in chapter_code:
            codes = [c.strip() for c in chapter_code.split(',') if c.strip() and c.strip().lower() != 'all']
        else:
            codes = [chapter_code.strip()] if str(chapter_code).strip().lower() != 'all' else []
        
        if len(codes) == 1:
            query += " AND m.chapter_code = ?"
            params.append(codes[0])
        elif len(codes) > 1:
            placeholders = ','.join(['?'] * len(codes))
            query += f" AND m.chapter_code IN ({placeholders})"
            params.extend(codes)
    if source_tag and source_tag != 'all':
        query += " AND m.source_tag = ?"
        params.append(source_tag)
    if section_group and section_group != 'all':
        if section_group.strip() in ['Part I', 'Part II']:
            query += " AND m.section_group LIKE ?"
            params.append(f"{section_group.strip()}:%")
        else:
            query += " AND m.section_group LIKE ?"
            params.append(f"%{section_group}%")
    if difficulty and difficulty != 'all':
        query += " AND m.difficulty = ?"
        params.append(difficulty)
    if verification_status and verification_status != 'all':
        query += " AND m.verification_status = ?"
        params.append(verification_status)
        
    if random_order:
        query += " ORDER BY RANDOM()"
    else:
        query += " ORDER BY m.id ASC"
        
    if limit:
        query += f" LIMIT {int(limit)}"
        
    cursor.execute(query, params)
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def get_mcq_by_id(mcq_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.*, 
               CASE WHEN b.id IS NOT NULL THEN 1 ELSE 0 END as is_bookmarked,
               CASE WHEN mb.id IS NOT NULL THEN mb.incorrect_count ELSE 0 END as mistake_count,
               mb.revision_status as mistake_status
        FROM mcqs m
        LEFT JOIN bookmarks b ON m.id = b.mcq_id
        LEFT JOIN mistakes_book mb ON m.id = mb.mcq_id
        WHERE m.id = ?
    """, (mcq_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def add_mcq(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    set_name = data.get('set_name', 'A').upper()
    chapter_code = data.get('chapter_code', 'A_DIR')
    
    section_group = data.get('section_group', '')
    if not section_group:
        if set_name == 'A':
            section_group = 'Part II: Economic Laws (30 Marks)' if chapter_code in ['A_FEMA', 'A_IBC', 'A_PMLA_FCRA', 'A_ARB'] else 'Part I: Corporate Laws (70 Marks)'
        else:
            section_group = 'Part II: Strategic Performance Management (50 Marks)' if chapter_code in ['B_PERF', 'B_EVA_DIV', 'B_TP', 'B_STD'] else 'Part I: Strategic Cost Management (50 Marks)'

    cursor.execute("""
        INSERT INTO mcqs (
            set_name, section_group, chapter_code, topic, subtopic, question, 
            option_a, option_b, option_c, option_d, 
            correct_option, marks, explanation, section_ref, 
            exam_tip, source_tag, difficulty, is_case_study, case_scenario,
            why_incorrect_a, why_incorrect_b, why_incorrect_c, why_incorrect_d,
            source_url_or_ref, source_date, verification_status, is_outdated_law, amendment_notes,
            is_user_uploaded
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        set_name,
        section_group,
        chapter_code,
        data.get('topic', 'General').strip(),
        data.get('subtopic', '').strip(),
        data.get('question', '').strip(),
        data.get('option_a', '').strip(),
        data.get('option_b', '').strip(),
        data.get('option_c', '').strip(),
        data.get('option_d', '').strip(),
        data.get('correct_option', 'A').upper().strip(),
        int(data.get('marks', 2)),
        data.get('explanation', '').strip(),
        data.get('section_ref', '').strip(),
        data.get('exam_tip', '').strip(),
        data.get('source_tag', 'ICAI BoS Module'),
        data.get('difficulty', 'Moderate'),
        1 if data.get('is_case_study') else 0,
        data.get('case_scenario', '').strip(),
        data.get('why_incorrect_a', '').strip(),
        data.get('why_incorrect_b', '').strip(),
        data.get('why_incorrect_c', '').strip(),
        data.get('why_incorrect_d', '').strip(),
        data.get('source_url_or_ref', '').strip(),
        data.get('source_date', '').strip(),
        data.get('verification_status', 'Verified'),
        1 if data.get('is_outdated_law') else 0,
        data.get('amendment_notes', '').strip(),
        1 if data.get('is_user_uploaded', True) else 0
    ))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return new_id

def delete_mcq(mcq_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mcqs WHERE id = ?", (mcq_id,))
    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return deleted

# =========================================================================
# BOOKMARKS & MY MISTAKES BOOK
# =========================================================================

def toggle_bookmark(mcq_id, notes=""):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM bookmarks WHERE mcq_id = ?", (mcq_id,))
    existing = cursor.fetchone()
    if existing:
        cursor.execute("DELETE FROM bookmarks WHERE mcq_id = ?", (mcq_id,))
        is_bookmarked = False
    else:
        cursor.execute("INSERT INTO bookmarks (mcq_id, notes) VALUES (?, ?)", (mcq_id, notes))
        is_bookmarked = True
    conn.commit()
    conn.close()
    return is_bookmarked

def get_bookmarked_mcqs():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.*, 1 as is_bookmarked, b.created_at as bookmarked_at, b.notes as bookmark_notes
        FROM bookmarks b
        JOIN mcqs m ON b.mcq_id = m.id
        ORDER BY b.created_at DESC
    """)
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def record_mistake(mcq_id, selected_option):
    """Called automatically upon test evaluation when answer is wrong"""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get question info
    cursor.execute("SELECT set_name, chapter_code FROM mcqs WHERE id = ?", (mcq_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return

    set_name = row['set_name']
    chapter_code = row['chapter_code']

    cursor.execute("""
    INSERT INTO mistakes_book (mcq_id, set_name, chapter_code, incorrect_count, last_selected_option, last_attempted_at, revision_status)
    VALUES (?, ?, ?, 1, ?, CURRENT_TIMESTAMP, 'Unrevised')
    ON CONFLICT(mcq_id) DO UPDATE SET
        incorrect_count = incorrect_count + 1,
        last_selected_option = excluded.last_selected_option,
        last_attempted_at = CURRENT_TIMESTAMP,
        revision_status = CASE WHEN revision_status = 'Mastered' THEN 'Reviewed' ELSE revision_status END
    """, (mcq_id, set_name, chapter_code, selected_option))

    conn.commit()
    conn.close()

def record_correct_attempt(mcq_id):
    """If user previously failed and now gets it right, upgrade status"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT revision_status FROM mistakes_book WHERE mcq_id = ?", (mcq_id,))
    row = cursor.fetchone()
    if row:
        new_status = 'Mastered' if row['revision_status'] == 'Reviewed' else 'Reviewed'
        cursor.execute("UPDATE mistakes_book SET revision_status = ?, last_attempted_at = CURRENT_TIMESTAMP WHERE mcq_id = ?", (new_status, mcq_id))
        conn.commit()
    conn.close()

def get_mistakes_book(set_name=None, status=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        SELECT mb.*, m.question, m.option_a, m.option_b, m.option_c, m.option_d,
               m.correct_option, m.explanation, m.section_ref, m.exam_tip, m.topic,
               m.source_tag, m.difficulty, c.name as chapter_name
        FROM mistakes_book mb
        JOIN mcqs m ON mb.mcq_id = m.id
        LEFT JOIN chapters c ON mb.chapter_code = c.code AND mb.set_name = c.set_name
        WHERE 1=1
    """
    params = []
    if set_name and set_name != 'all':
        query += " AND mb.set_name = ?"
        params.append(set_name.upper())
    if status and status != 'all':
        query += " AND mb.revision_status = ?"
        params.append(status)

    query += " ORDER BY mb.incorrect_count DESC, mb.last_attempted_at DESC"
    cursor.execute(query, params)
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def update_mistake_status(mistake_id, status, notes=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if notes is not None:
        cursor.execute("UPDATE mistakes_book SET revision_status = ?, notes = ? WHERE id = ?", (status, notes, mistake_id))
    else:
        cursor.execute("UPDATE mistakes_book SET revision_status = ? WHERE id = ?", (status, mistake_id))
    conn.commit()
    conn.close()

# =========================================================================
# REVISION HANDBOOK & CONTENT
# =========================================================================

def get_handbook_content(set_name, chapter_code=None, category=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM handbook_content WHERE set_name = ?"
    params = [set_name.upper()]

    if chapter_code and chapter_code != 'all':
        query += " AND chapter_code = ?"
        params.append(chapter_code)
    if category and category != 'all':
        query += " AND category = ?"
        params.append(category)

    cursor.execute(query, params)
    rows = []
    for r in cursor.fetchall():
        d = dict(r)
        d['content'] = json.loads(d['content_json']) if d['content_json'] else {}
        rows.append(d)
    conn.close()
    return rows

def upsert_handbook_content(set_name, chapter_code, category, title, content_data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO handbook_content (set_name, chapter_code, category, title, content_json, updated_at)
    VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    ON CONFLICT(set_name, chapter_code, category) DO UPDATE SET
        title = excluded.title,
        content_json = excluded.content_json,
        updated_at = CURRENT_TIMESTAMP
    """, (set_name.upper(), chapter_code, category, title, json.dumps(content_data)))
    conn.commit()
    conn.close()

# =========================================================================
# RESEARCH RECORDS & INGESTION
# =========================================================================

def get_research_records(set_name=None, source_type=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM research_records WHERE 1=1"
    params = []
    if set_name and set_name != 'all':
        query += " AND set_name = ?"
        params.append(set_name.upper())
    if source_type and source_type != 'all':
        query += " AND source_type = ?"
        params.append(source_type)
    query += " ORDER BY created_at DESC"
    cursor.execute(query, params)
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def add_research_record(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO research_records (
        set_name, source_type, source_author, title, source_url, 
        summary, extracted_topics, reliability_rating, verification_status
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get('set_name', 'A').upper(),
        data.get('source_type', 'Student Recall'),
        data.get('source_author', 'Community'),
        data.get('title', '').strip(),
        data.get('source_url', '').strip(),
        data.get('summary', '').strip(),
        data.get('extracted_topics', '').strip(),
        data.get('reliability_rating', 'High'),
        data.get('verification_status', 'Verified')
    ))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return new_id

# =========================================================================
# ATTEMPTS & ANALYTICS
# =========================================================================

def save_attempt(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    total_q = int(data.get('total_questions', 0))
    attempted = int(data.get('attempted', 0))
    correct = int(data.get('correct', 0))
    incorrect = int(data.get('incorrect', 0))
    score = float(data.get('score', 0.0))
    max_marks = float(data.get('max_marks', 100.0))
    percentage = (score / max_marks * 100) if max_marks > 0 else 0.0
    passed = 1 if percentage >= 50.0 else 0
    
    cursor.execute("""
        INSERT INTO attempts (
            set_name, mode, chapter_code, total_questions, attempted,
            correct, incorrect, score, max_marks, percentage, passed,
            time_taken_seconds, breakdown_json, responses_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get('set_name', 'A').upper(),
        data.get('mode', 'full_mock_50'),
        data.get('chapter_code', None),
        total_q,
        attempted,
        correct,
        incorrect,
        score,
        max_marks,
        percentage,
        passed,
        int(data.get('time_taken_seconds', 0)),
        json.dumps(data.get('breakdown', {})),
        json.dumps(data.get('responses', []))
    ))
    attempt_id = cursor.lastrowid
    conn.commit()
    conn.close()

    # Feed into My Mistakes Book for every incorrect answer
    for resp in data.get('responses', []):
        q_id = resp.get('id')
        if not q_id:
            continue
        if resp.get('is_attempted') and not resp.get('is_correct'):
            record_mistake(q_id, resp.get('selected_option'))
        elif resp.get('is_correct'):
            record_correct_attempt(q_id)

    return {
        "id": attempt_id,
        "score": score,
        "max_marks": max_marks,
        "percentage": round(percentage, 2),
        "passed": bool(passed),
        "attempted": attempted,
        "correct": correct,
        "incorrect": incorrect
    }

def get_attempts(limit=25):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attempts ORDER BY attempted_at DESC LIMIT ?", (limit,))
    rows = []
    for r in cursor.fetchall():
        d = dict(r)
        d['breakdown'] = json.loads(d['breakdown_json']) if d['breakdown_json'] else {}
        d['responses'] = json.loads(d['responses_json']) if d['responses_json'] else []
        rows.append(d)
    conn.close()
    return rows

def get_stats():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM mcqs WHERE set_name = 'A'")
    count_a = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM mcqs WHERE set_name = 'B'")
    count_b = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM mcqs WHERE source_tag = 'Offline SPOM Recall'")
    count_recall = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM mcqs WHERE source_tag = 'ICAI BoS Module'")
    count_icai = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM bookmarks")
    count_bookmarks = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM mistakes_book WHERE revision_status != 'Mastered'")
    count_active_mistakes = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM topics WHERE priority_level IN ('Very High Priority', 'High Priority')")
    count_high_priority_topics = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM attempts")
    total_attempts = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM attempts WHERE passed = 1")
    passed_attempts = cursor.fetchone()[0]
    
    cursor.execute("SELECT AVG(percentage) FROM attempts")
    avg_score_row = cursor.fetchone()[0]
    avg_score = round(avg_score_row, 1) if avg_score_row else 0.0
    
    conn.close()
    return {
        "count_set_a": count_a,
        "count_set_b": count_b,
        "total_mcqs": count_a + count_b,
        "offline_recalls": count_recall,
        "icai_official": count_icai,
        "bookmarks_count": count_bookmarks,
        "active_mistakes_count": count_active_mistakes,
        "high_priority_topics": count_high_priority_topics,
        "total_attempts": total_attempts,
        "passed_attempts": passed_attempts,
        "pass_rate": round((passed_attempts / total_attempts * 100), 1) if total_attempts > 0 else 0.0,
        "avg_score": avg_score
    }

def get_syllabus_versions(set_name=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if set_name:
        cursor.execute("SELECT * FROM syllabus_versions WHERE set_name = ? ORDER BY id DESC", (set_name.upper(),))
    else:
        cursor.execute("SELECT * FROM syllabus_versions ORDER BY set_name ASC, id DESC")
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def get_topic_stats(set_name='A'):
    conn = get_db_connection()
    cursor = conn.cursor()
    set_name = set_name.upper()
    
    cursor.execute("SELECT COUNT(*) FROM topics WHERE set_name = ?", (set_name,))
    total_topics = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM topics WHERE set_name = ? AND priority_level = 'Very High Priority'", (set_name,))
    very_high = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM topics WHERE set_name = ? AND priority_level = 'High Priority'", (set_name,))
    high = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM topics WHERE set_name = ? AND priority_level = 'Moderate Priority'", (set_name,))
    moderate = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM topics WHERE set_name = ? AND is_revised = 1", (set_name,))
    revised = cursor.fetchone()[0]

    conn.close()
    return {
        "total_topics": total_topics,
        "very_high_count": very_high,
        "high_count": high,
        "moderate_count": moderate,
        "revised_count": revised,
        "revision_percentage": round((revised / total_topics * 100), 1) if total_topics > 0 else 0.0
    }

def get_practice_questions(set_name='A', mode='mixed', chapter_code=None, count=10):
    """
    Supports 10 Exam Practice Modes:
    1. important: Questions from top high-priority topics
    2. icai: Official ICAI BoS Module, TYK, and Case Booklet
    3. student_recall: Offline SPOM Exam Recalls
    4. faculty_picked: Faculty recommended
    5. chapter: Single chapter selection
    6. mixed: Multi-chapter random
    7. weak_area: Questions from chapters where user has mistakes
    8. rapid_blitz: Fast-paced review
    9. case_scenarios: Case study questions
    10. adaptive: Blended review based on difficulty & mistake history
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    set_name = set_name.upper()
    count = int(count)

    base_query = """
        SELECT m.*,
               CASE WHEN b.id IS NOT NULL THEN 1 ELSE 0 END as is_bookmarked,
               CASE WHEN mb.id IS NOT NULL THEN mb.incorrect_count ELSE 0 END as mistake_count,
               mb.revision_status as mistake_status
        FROM mcqs m
        LEFT JOIN bookmarks b ON m.id = b.mcq_id
        LEFT JOIN mistakes_book mb ON m.id = mb.mcq_id
        WHERE m.set_name = ?
    """
    params = [set_name]

    if mode == 'important':
        # Match questions tagged with high priority topics or hard difficulty
        base_query += " AND (m.difficulty IN ('Hard', 'Moderate') OR m.source_tag IN ('Offline SPOM Recall', 'ICAI BoS Module'))"
        base_query += " ORDER BY RANDOM() LIMIT ?"
        params.append(count)

    elif mode == 'icai':
        base_query += " AND m.source_tag IN ('ICAI BoS Module', 'ICAI Test Your Knowledge', 'ICAI Case Scenario')"
        base_query += " ORDER BY RANDOM() LIMIT ?"
        params.append(count)

    elif mode == 'student_recall':
        base_query += " AND m.source_tag = 'Offline SPOM Recall'"
        base_query += " ORDER BY RANDOM() LIMIT ?"
        params.append(count)

    elif mode == 'faculty_picked':
        base_query += " AND m.source_tag = 'Faculty Recommended'"
        base_query += " ORDER BY RANDOM() LIMIT ?"
        params.append(count)

    elif mode in ('chapter', 'chapters', 'combination'):
        if chapter_code and chapter_code != 'all':
            if isinstance(chapter_code, (list, tuple)):
                codes = [c.strip() for c in chapter_code if c.strip() and c.strip().lower() != 'all']
            elif isinstance(chapter_code, str):
                codes = [c.strip() for c in chapter_code.split(',') if c.strip() and c.strip().lower() != 'all']
            else:
                codes = []

            if len(codes) == 1:
                base_query += " AND m.chapter_code = ?"
                params.append(codes[0])
            elif len(codes) > 1:
                placeholders = ','.join(['?'] * len(codes))
                base_query += f" AND m.chapter_code IN ({placeholders})"
                params.extend(codes)

        if count and count > 0:
            base_query += " ORDER BY RANDOM() LIMIT ?"
            params.append(count)
        else:
            base_query += " ORDER BY RANDOM()"

    elif mode == 'weak_area':
        # Join with mistakes book
        cursor.execute("SELECT DISTINCT chapter_code FROM mistakes_book WHERE set_name = ? AND revision_status != 'Mastered'", (set_name,))
        weak_chaps = [r[0] for r in cursor.fetchall()]
        if weak_chaps:
            placeholders = ','.join(['?'] * len(weak_chaps))
            base_query += f" AND m.chapter_code IN ({placeholders})"
            params.extend(weak_chaps)
        base_query += " ORDER BY RANDOM() LIMIT ?"
        params.append(count)

    elif mode == 'case_scenarios':
        base_query += " AND m.is_case_study = 1"
        base_query += " ORDER BY RANDOM() LIMIT ?"
        params.append(count)

    elif mode == 'adaptive':
        # Mix of mistakes book questions + unattempted
        base_query += " ORDER BY mistake_count DESC, RANDOM() LIMIT ?"
        params.append(count)

    else: # mixed or rapid_blitz
        base_query += " ORDER BY RANDOM() LIMIT ?"
        params.append(count)

    cursor.execute(base_query, params)
    rows = [dict(r) for r in cursor.fetchall()]

    # Fallback if specific filter yielded fewer questions than requested
    if len(rows) < count:
        fallback_query = """
            SELECT m.*,
                   CASE WHEN b.id IS NOT NULL THEN 1 ELSE 0 END as is_bookmarked,
                   CASE WHEN mb.id IS NOT NULL THEN mb.incorrect_count ELSE 0 END as mistake_count,
                   mb.revision_status as mistake_status
            FROM mcqs m
            LEFT JOIN bookmarks b ON m.id = b.mcq_id
            LEFT JOIN mistakes_book mb ON m.id = mb.mcq_id
            WHERE m.set_name = ?
            ORDER BY RANDOM() LIMIT ?
        """
        cursor.execute(fallback_query, (set_name, count))
        rows = [dict(r) for r in cursor.fetchall()]

    conn.close()
    return rows

