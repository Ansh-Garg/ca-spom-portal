with open(r"C:\Users\Ansh\Desktop\Coding\ca-spom-portal\public\app.js", "r", encoding="utf-8") as f:
    code = f.read()

stack = []
in_squote = False
in_dquote = False
in_btick = False
in_line_comment = False
in_block_comment = False
escaped = False

errors = []
for i, ch in enumerate(code):
    if escaped:
        escaped = False
        continue
    if ch == '\\':
        escaped = True
        continue
    
    # Comments
    if in_line_comment:
        if ch == '\n':
            in_line_comment = False
        continue
    if in_block_comment:
        if ch == '/' and i > 0 and code[i-1] == '*':
            in_block_comment = False
        continue
    
    # Strings
    if in_squote:
        if ch == "'":
            in_squote = False
        continue
    if in_dquote:
        if ch == '"':
            in_dquote = False
        continue
    if in_btick:
        if ch == '`':
            in_btick = False
        continue

    # Start comments
    if ch == '/' and i+1 < len(code):
        nxt = code[i+1]
        if nxt == '/':
            in_line_comment = True
            continue
        elif nxt == '*':
            in_block_comment = True
            continue

    # Start strings
    if ch == "'":
        in_squote = True
        continue
    if ch == '"':
        in_dquote = True
        continue
    if ch == '`':
        in_btick = True
        continue

    # Brackets
    if ch in '({[':
        stack.append((ch, i))
    elif ch in ')}]':
        if not stack:
            line_num = code[:i].count('\n') + 1
            errors.append(f"Unmatched closing '{ch}' at line {line_num}")
        else:
            top, pos = stack.pop()
            matches = {')': '(', '}': '{', ']': '['}
            if matches[ch] != top:
                line_num = code[:i].count('\n') + 1
                open_line = code[:pos].count('\n') + 1
                errors.append(f"Mismatched closing '{ch}' at line {line_num}, expected match for '{top}' opened at line {open_line}")

print(f"Done checking app.js. Stack length: {len(stack)}, Errors: {len(errors)}")
if errors:
    for e in errors[:10]:
        print("  ", e)
if stack:
    print("Unclosed brackets:")
    for b in stack[-5:]:
        line_num = code[:b[1]].count('\n') + 1
        print(f"  '{b[0]}' opened at line {line_num}")
