import re
with open(r"C:\Users\Ansh\Desktop\Coding\ca-spom-portal\nextgen_set_b_raw.html", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# find questions
blocks = re.findall(r'<div class="wp-block-group.*?</div>\s*</div>', text, re.DOTALL)
print("Blocks:", len(blocks))

# Let's search by keywords in entire text
keywords = ["division aa", "oral ltd", "brazil", "olderhelp", "beautician", "mckinsey", "7s", "building block", "z-score", "argenti", "whale curve"]
for kw in keywords:
    pos = 0
    found = 0
    while True:
        idx = text.lower().find(kw, pos)
        if idx == -1:
            break
        found += 1
        snippet = text[max(0, idx-100):min(len(text), idx+200)]
        clean = re.sub(r'<[^>]+>', ' ', snippet).replace('\n', ' ')
        print(f"[{kw.upper()}] match {found}: {clean[:150]}...")
        pos = idx + len(kw) + 100
        if found >= 3:
            break
