import json
with open('data/kyotsu/2024/honshiken/data.json', encoding='utf-8') as f:
    d = json.load(f)
s4 = next((s for s in d['sections'] if s['section_number']==4), None)
for p in s4.get('passages', []):
    print(f"ID: {p['id']}")
    print(f"Title: {p.get('title',{}).get('en')}")
    print(f"Sentences: {len(p.get('sentences',[]))}")
    print(f"Slides: {len(p.get('slides',[]))}")
    print("---")
