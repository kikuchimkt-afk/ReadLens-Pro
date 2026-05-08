import json
import re

with open('data/kyotsu/2024/honshiken/data.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for s in d.get('sections', []):
    for i, q in enumerate(s.get('questions', [])):
        if 'question_id' in q:
            # Replace 1 with 問1, etc.
            q['question_id'] = re.sub(r'[?]', '問', q['question_id'])
            # If it's something like '問問1', fix it
            q['question_id'] = re.sub(r'問+', '問', q['question_id'])
            
            # For 6B, it might be 問1, but let's just make it '問' + str(i+1) just in case
            # Wait, no, sometimes the question_id is '問1' or '問2'.
            # It's better to just set it to '問' + str(i+1) for all questions!
            q['question_id'] = f"問{i+1}"

with open('data/kyotsu/2024/honshiken/data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print("Fixed question_ids!")
