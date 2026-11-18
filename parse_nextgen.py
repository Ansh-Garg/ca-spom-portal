import json, re

with open(r"C:\Users\Ansh\Desktop\Coding\nextgen_set_b_raw.html", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Let's see what scripts contain questions
scripts = re.findall(r'<script[^>]*>(.*?)</script>', text, re.DOTALL)
print("Scripts count:", len(scripts))
found_data = None
for s in scripts:
    if 'question' in s and 'options' in s:
        # try to find json array
        match = re.search(r'(\[\s*\{.*"question".*\}\s*\])', s, re.DOTALL)
        if match:
            try:
                found_data = json.loads(match.group(1))
                print("Successfully parsed JSON! Count:", len(found_data))
                break
            except Exception as e:
                print("Regex matched but json load error:", e)

if found_data:
    print("Sample Q:", found_data[0]['question'][:100])
    print("Sample options:", found_data[0].get('options'))
    print("Sample answer:", found_data[0].get('answer') or found_data[0].get('correctAnswer'))
