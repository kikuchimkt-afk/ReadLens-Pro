import json

d = json.load(open('data/kyotsu/2025/honshiken/data.json', 'r', encoding='utf-8'))
sec8 = [s for s in d['sections'] if s['section_number'] == 8][0]

print('Section 8 keys:', list(sec8.keys()))
print('Passages:')
for p in sec8['passages']:
    print(f"  {p['id']}: keys={list(p.keys())}")
print(f"Questions: {len(sec8['questions'])}")
for q in sec8['questions']:
    print(f"  {q['question_id']}: keys={list(q.keys())}")
