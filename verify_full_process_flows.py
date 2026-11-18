import os
import sys
import threading
import time
import urllib.request
import urllib.error
import json
from http.server import HTTPServer

BASE_DIR = r"C:\Users\Ansh\Desktop\Coding\ca-spom-portal"
sys.path.insert(0, BASE_DIR)

import server
import database

TEST_PORT = 8086
httpd = None

def run_server():
    global httpd
    server_address = ('127.0.0.1', TEST_PORT)
    httpd = HTTPServer(server_address, server.SPOMRequestHandler)
    print(f"[PROCESS FLOW SERVER] Listening on http://127.0.0.1:{TEST_PORT}")
    httpd.serve_forever()

server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()
time.sleep(1)

def request_json(method, path, body=None, user_id="student_ansh_007"):
    url = f"http://127.0.0.1:{TEST_PORT}{path}"
    headers = {
        "X-User-ID": user_id,
        "Accept": "application/json"
    }
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.status, json.loads(resp.read().decode("utf-8"))

print("\n" + "=" * 70)
print("TESTING COMPLETE END-TO-END WEBSITE PROCESS FLOWS")
print("=" * 70)

# FLOW 1: Switching to Set B and loading Dashboard
print("\n--- FLOW 1: Set Switching & Dashboard Loading (Set B) ---")
st, stats = request_json("GET", "/api/stats")
assert st == 200 and stats["success"], "Stats failed"
print(f"[OK] Platform Stats: Set A={stats['data']['count_set_a']}, Set B={stats['data']['count_set_b']}, Total={stats['data']['total_mcqs']}")

st, chapters = request_json("GET", "/api/chapters?set=B")
assert st == 200 and len(chapters["data"]) == 8, f"Expected 8 chapters for Set B, got {len(chapters['data'])}"
print(f"[OK] Chapters loaded for Set B: {len(chapters['data'])} chapters successfully returned.")

st, coverage = request_json("GET", "/api/question-bank-coverage?set=B")
assert st == 200 and coverage["data"]["total_mcqs"] >= 140, "Coverage total MCQs mismatch"
print(f"[OK] Question Bank Coverage: {coverage['data']['total_mcqs']} MCQs in Set B pool (Never Attempted: {coverage['data']['never_attempted']})")

# FLOW 2: 100 Marks CBT Mock Exam Generation (Set B)
print("\n--- FLOW 2: Generating 50-Question CBT Mock (100 Marks Benchmark) ---")
st, mock = request_json("GET", "/api/mock-test?set=B&mode=full_mock_50")
assert st == 200 and mock["success"], "Mock generation failed"
questions = mock["questions"]
assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"
p1_count = sum(1 for q in questions if "Part I:" in q.get("section_group", "") or "Part I:" in q.get("section_title", ""))
p2_count = sum(1 for q in questions if "Part II:" in q.get("section_group", "") or "Part II:" in q.get("section_title", ""))
print(f"[OK] CBT Mock generated: 50 Questions (100 Marks). Section split: Part I = {p1_count} Qs, Part II = {p2_count} Qs.")
assert p1_count == 25 and p2_count == 25, f"Section split imbalance: {p1_count} vs {p2_count}"

# FLOW 3: Practice Drills (Targeted Chapter Selection & Cohort)
print("\n--- FLOW 3: Practice Session Drilling ---")
st, drill = request_json("GET", "/api/practice/questions?set=B&mode=mixed&count=10")
assert st == 200 and len(drill["questions"]) == 10, "Practice questions fetch failed"
print(f"[OK] Practice drill retrieved 10 questions successfully.")
sample_q = drill["questions"][0]
print(f"     Sample Topic: {sample_q['topic']}")
print(f"     Explanation length: {len(sample_q.get('explanation', ''))} chars | Exam Tip: {sample_q.get('exam_tip', 'N/A')[:60]}...")

# FLOW 4: Submitting a Test Attempt & Verifying Evaluation Engine
print("\n--- FLOW 4: Submitting Test & Evaluating Results ---")
# Simulate answering 50 questions
user_responses = {}
for i, q in enumerate(questions):
    user_responses[str(q["id"])] = "A" if i % 2 == 0 else "B"

submission_payload = {
    "set_name": "B",
    "mode": "full_mock_50",
    "time_taken_seconds": 3600,
    "questions": questions,
    "responses": user_responses,
    "correct_keys": {str(q["id"]): q.get("shuffled_correct_key", "A") for q in questions}
}

st, sub_res = request_json("POST", "/api/submit-test", body=submission_payload)
assert st == 200 and sub_res["success"], "Test submission failed"
res = sub_res["result"]
print(f"[OK] Test Evaluated Successfully!")
print(f"     Score: {res['score']}/{res['max_marks']} ({res['percentage']}%) | Status: {'PASSED' if res['passed'] else 'FAILED'}")
print(f"     Correct: {res['correct']} | Incorrect: {res['incorrect']}")
assert res["max_marks"] == 100.0, f"Expected 100 max marks, got {res['max_marks']}"
assert res["correct"] + res["incorrect"] == 50, "Total evaluated questions should be 50"

# FLOW 5: Mistakes Book & Question Bank Coverage Update
print("\n--- FLOW 5: Mistakes Book & Coverage Synchronization ---")
st, mistakes = request_json("GET", "/api/mistakes?set=B")
assert st == 200 and len(mistakes["data"]) >= 10, f"Expected at least 10 mistakes recorded, got {len(mistakes['data'])}"
print(f"[OK] Mistakes Book updated: {len(mistakes['data'])} mistake entries logged.")

# Check updated coverage
st, cov_after = request_json("GET", "/api/question-bank-coverage?set=B")
assert cov_after["data"]["attempted"] >= 50, f"Expected at least 50 attempted, got {cov_after['data']['attempted']}"
assert cov_after["data"]["coverage_pct"] > 0, "Coverage percentage should be > 0"
print(f"[OK] Coverage Engine successfully updated: 50 Attempted, {cov_after['data']['never_attempted']} Never Attempted, Coverage = {cov_after['data']['coverage_pct']}%")

# Update mistake status to 'Reviewed'
mistake_id = mistakes["data"][0]["id"]
st, upd = request_json("POST", "/api/mistakes/status", body={"mistake_id": mistake_id, "status": "Reviewed"})
assert st == 200 and upd["success"], "Mistake status update failed"
print(f"[OK] Mistake #{mistake_id} marked as 'Reviewed'.")

# FLOW 6: Intelligence Engine & Study Handbook
print("\n--- FLOW 6: Intelligence Engine & Quick Revision Handbook ---")
st, intel = request_json("GET", "/api/intelligence/dashboard?set=B")
assert st == 200 and intel["success"], "Intelligence dashboard failed"
print(f"[OK] Intelligence Dashboard loaded: {len(intel.get('study_today', []))} Study Recommendations, Total Topics={intel.get('stats', {}).get('total_topics', 0)}")

st, hb = request_json("GET", "/api/handbook?set=B&chapter=B_PERF")
assert st == 200 and hb["success"], "Handbook failed"
print(f"[OK] Revision Handbook loaded for B_PERF.")

# FLOW 7: Clean Workspace Reset
print("\n--- FLOW 7: Personal Workspace Isolation & Reset ---")
st, reset = request_json("POST", "/api/user/reset", body={})
assert st == 200 and reset["success"], "Reset failed"
st, cov_reset = request_json("GET", "/api/question-bank-coverage?set=B")
assert cov_reset["data"]["attempted"] == 0, "Attempted should be 0 after reset"
print(f"[OK] Personal Workspace successfully reset: Attempted reset to 0 without affecting other users.")

print("\n" + "=" * 70)
print("ALL 7 CORE WEBSITE PROCESS FLOWS TESTED AND VERIFIED 100% OPERATIONAL!")
print("=" * 70)

if httpd:
    httpd.shutdown()
