import json
d=json.load(open('data/kyotsu/2025/tsuishiken/data.json','r',encoding='utf-8'))
for s in d['sections']:
    for q in s.get('questions',[]):
        has = 'YES' if q.get('explanation',{}).get('instructor_note') else 'NO'
        print(f"S{s['section_number']}: {q['question_id']} -> {has}")
