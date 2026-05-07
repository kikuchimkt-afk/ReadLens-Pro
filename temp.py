import json

with open('data/kyotsu/2024/honshiken/data.json', encoding='utf-8') as f:
    d = json.load(f)

p = [p for s in d['sections'] if s['section_number']==3 for sub in s['subsections'] for p in sub.get('passages',[]) if p['id']=='article_3b'][0]
for i, s in enumerate(p['sentences']):
    print(f"{i}: {s['id']}: {s['en'][:50]}...")
