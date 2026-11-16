import re

with open('deploy/homepage.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'<[a-z0-9]+[^>]*id="([^"]+)"[^>]*>', text):
    tag_id = m.group(1)
    if any(k in tag_id.lower() for k in ['audio', 'music', 'player', 'eq', 'sound', 'deck']):
        print("Tag:", m.group(0)[:120])
