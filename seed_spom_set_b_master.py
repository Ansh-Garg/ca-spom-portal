"""
Database Seeder for CA Final SPOM Set B Master Questions
Merges Part 1 (54 MCQs) and Part 2 (62 MCQs) into spom_portal.db
Total: 116 Master MCQs
"""

import sqlite3
import shutil
import os
import datetime
import sys

# Ensure ca-spom-portal directory is on path
BASE_DIR = r"C:\Users\Ansh\Desktop\Coding\ca-spom-portal"
sys.path.insert(0, BASE_DIR)

from seed_spom_set_b_part1 import SET_B_PART1_MCQS
from seed_spom_set_b_part2 import SET_B_PART2_MCQS

DB_PATH = os.path.join(BASE_DIR, "spom_portal.db")
BACKUP_DIR = os.path.join(BASE_DIR, "backups")
os.makedirs(BACKUP_DIR, exist_ok=True)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_path = os.path.join(BACKUP_DIR, f"spom_portal_pre_set_b_master_{timestamp}.db")

print(f"Creating backup of database at: {backup_path}")
shutil.copy2(DB_PATH, backup_path)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Get existing Set B questions to prevent duplicate insertion
cursor.execute("SELECT question FROM mcqs WHERE set_name = 'B'")
existing_questions = set(row[0].strip().lower() for row in cursor.fetchall())
print(f"Existing Set B questions in database: {len(existing_questions)}")

all_master_mcqs = SET_B_PART1_MCQS + SET_B_PART2_MCQS
print(f"Total Master MCQs to process: {len(all_master_mcqs)}")

inserted_count = 0
skipped_count = 0

for mcq in all_master_mcqs:
    q_text = mcq["question"].strip()
    if q_text.lower() in existing_questions:
        print(f"Skipping duplicate: {mcq['topic'][:50]}")
        skipped_count += 1
        continue

    # Prepare fields
    cursor.execute("""
        INSERT INTO mcqs (
            set_name, section_group, chapter_code, topic, subtopic, question,
            option_a, option_b, option_c, option_d, correct_option, marks,
            explanation, why_incorrect_a, why_incorrect_b, why_incorrect_c, why_incorrect_d,
            section_ref, exam_tip, source_tag, difficulty, is_case_study,
            case_scenario, is_user_uploaded, created_at, verification_status
        ) VALUES (
            ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?,
            ?, ?, datetime('now'), ?
        )
    """, (
        mcq["set_name"],
        mcq.get("section_group", ""),
        mcq["chapter_code"],
        mcq["topic"],
        mcq.get("subtopic", ""),
        q_text,
        mcq["option_a"],
        mcq["option_b"],
        mcq["option_c"],
        mcq["option_d"],
        mcq["correct_option"],
        mcq.get("marks", 2),
        mcq["explanation"],
        mcq.get("why_incorrect_a", ""),
        mcq.get("why_incorrect_b", ""),
        mcq.get("why_incorrect_c", ""),
        mcq.get("why_incorrect_d", ""),
        mcq.get("section_ref", ""),
        mcq.get("exam_tip", ""),
        mcq.get("source_tag", "ICAI BoS / Exam Recalls"),
        mcq.get("difficulty", "Moderate"),
        mcq.get("is_case_study", 1 if "case" in mcq.get("topic", "").lower() or len(q_text) > 250 else 0),
        mcq.get("case_scenario", ""),
        0, # is_user_uploaded
        "Verified ICAI Standard"
    ))
    existing_questions.add(q_text.lower())
    inserted_count += 1

conn.commit()

# Print statistics
cursor.execute("SELECT chapter_code, count(id) FROM mcqs WHERE set_name = 'B' GROUP BY chapter_code ORDER BY chapter_code")
breakdown = cursor.fetchall()
cursor.execute("SELECT count(id) FROM mcqs WHERE set_name = 'A'")
set_a_total = cursor.fetchone()[0]
cursor.execute("SELECT count(id) FROM mcqs WHERE set_name = 'B'")
set_b_total = cursor.fetchone()[0]

conn.close()

print("\n" + "=" * 60)
print(f"SET B MASTER SEEDING COMPLETED SUCCESSFULLY!")
print(f"Inserted: {inserted_count} new Master MCQs")
print(f"Skipped duplicates: {skipped_count}")
print(f"Total Set A Questions: {set_a_total}")
print(f"Total Set B Questions: {set_b_total}")
print("\nSet B Chapter Breakdown in Database:")
for ch, cnt in breakdown:
    print(f"  - {ch}: {cnt} MCQs")
print("=" * 60)
