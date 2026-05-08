import json
with open('data/kyotsu/2024/honshiken/data.json', encoding='utf-8') as f:
    d = json.load(f)
p = next(p for s in d['sections'] if s['section_number']==4 for p in s.get('passages',[]) if p['id'] == 'article_4')
for i, s in enumerate(p['sentences']):
    print(f"{i}: {s['id']}: {s['en'][:40]}...")
