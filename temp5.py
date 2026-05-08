import json
with open('data/kyotsu/2024/honshiken/data.json', encoding='utf-8') as f:
    d = json.load(f)
s4 = next(s for s in d['sections'] if s['section_number']==4)
for q in s4.get('questions', []):
    print(f"Q{q.get('number')}: answer={q.get('answer')} points={q.get('points')}")
