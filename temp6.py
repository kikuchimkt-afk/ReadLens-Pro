import json
with open('data/kyotsu/2024/honshiken/data.json', encoding='utf-8') as f:
    d = json.load(f)
s4 = next(s for s in d['sections'] if s['section_number']==4)
print(json.dumps(s4['questions'], ensure_ascii=False, indent=2))
