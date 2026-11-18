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

TEST_PORT = 8085
httpd = None

def run_server():
    global httpd
    server_address = ('127.0.0.1', TEST_PORT)
    httpd = HTTPServer(server_address, server.SPOMRequestHandler)
    print(f"[TEST SERVER] Listening on http://127.0.0.1:{TEST_PORT}")
    httpd.serve_forever()

server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()
time.sleep(1) # wait for server to start

test_endpoints = [
    # Static & Health
    ("GET", "/health", None, None),
    ("GET", "/healthz", None, None),
    ("GET", "/", None, None),
    ("GET", "/index.html", None, None),
    ("GET", "/app.js", None, None),
    ("GET", "/styles.css", None, None),

    # User & Progress
    ("GET", "/api/user/me", None, {"X-User-ID": "test_user_123"}),
    ("GET", "/api/stats", None, {"X-User-ID": "test_user_123"}),

    # Chapters & Content
    ("GET", "/api/chapters?set=A", None, None),
    ("GET", "/api/chapters?set=B", None, None),
    ("GET", "/api/mcqs?set=A&limit=5", None, None),
    ("GET", "/api/mcqs?set=B&limit=5", None, None),
    
    # Question Bank Coverage Engine
    ("GET", "/api/question-bank-coverage?set=A", None, {"X-User-ID": "test_user_123"}),
    ("GET", "/api/question-bank-coverage?set=B", None, {"X-User-ID": "test_user_123"}),
    ("GET", "/api/question-bank-cohort?set=B&cohort=never_attempted&limit=5", None, {"X-User-ID": "test_user_123"}),
    
    # Mock Test Generation (Set A and Set B)
    ("GET", "/api/mock-test?set=A&mode=full_mock_50", None, None),
    ("GET", "/api/mock-test?set=B&mode=full_mock_50", None, None),

    # Intelligence & Handbook
    ("GET", "/api/intelligence/dashboard?set=A", None, None),
    ("GET", "/api/intelligence/dashboard?set=B", None, None),
    ("GET", "/api/handbook?set=B&chapter=B_PERF", None, None),
    ("GET", "/api/syllabus/status?set=B", None, None),

    # Reset User Workspace
    ("POST", "/api/user/reset", {}, {"X-User-ID": "test_user_123", "Content-Type": "application/json"})
]

results = []
all_passed = True

print(f"\n{'='*70}\nSTARTING ENDPOINT VALIDATION SUITE\n{'='*70}")

for method, path, body, headers in test_endpoints:
    url = f"http://127.0.0.1:{TEST_PORT}{path}"
    req_headers = headers or {}
    data = None
    if body is not None:
        data = json.dumps(body).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, headers=req_headers, method=method)
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            elapsed_ms = (time.time() - t0) * 1000
            status = resp.status
            resp_body = resp.read()
            content_type = resp.headers.get('Content-Type', '')
            
            # Special check for /health
            if path in ["/health", "/healthz"]:
                is_ok = (status == 200 and resp_body == b"OK" and "text/plain" in content_type)
            else:
                is_ok = (status == 200)

            results.append((method, path, status, f"{elapsed_ms:.1f}ms", len(resp_body), is_ok, None))
            print(f"[{'PASS' if is_ok else 'FAIL'}] {method:4} {path:45} -> {status} ({elapsed_ms:.1f}ms, {len(resp_body)} bytes)")
    except Exception as e:
        elapsed_ms = (time.time() - t0) * 1000
        all_passed = False
        results.append((method, path, "ERR", f"{elapsed_ms:.1f}ms", 0, False, str(e)))
        print(f"[FAIL] {method:4} {path:45} -> ERROR: {e}")

print(f"\n{'='*70}\nENDPOINT VALIDATION SUMMARY\n{'='*70}")
pass_count = sum(1 for r in results if r[5])
print(f"Passed: {pass_count} / {len(results)}")

if not all_passed:
    print("\nFAILED ENDPOINTS:")
    for r in results:
        if not r[5]:
            print(f"  - {r[0]} {r[1]}: {r[6]}")
else:
    print("\nALL ENDPOINTS RESPONDED WITH HTTP 200 OK AND VALID PAYLOADS!")

if httpd:
    httpd.shutdown()
