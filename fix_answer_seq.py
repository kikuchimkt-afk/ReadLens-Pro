import json

with open('data/kyotsu/2024/honshiken/data.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for s in d.get('sections', []):
    for q in s.get('questions', []):
        if q.get('question_type') == 'ordering' and 'answer_sequence' in q:
            # If answer_sequence contains integers
            if all(isinstance(x, int) for x in q['answer_sequence']):
                new_seq = []
                for idx in q['answer_sequence']:
                    # choices are 1-indexed in answer_sequence
                    # wait, let's verify if index 4 means the 4th choice!
                    # "C" is 4th choice, "D" is 5th choice, "@" is 1st choice, "A" is 2nd choice
                    # 4 -> C, 5 -> D, 1 -> @, 2 -> A. Yes!
                    if 1 <= idx <= len(q.get('choices', [])):
                        new_seq.append(q['choices'][idx-1]['label'])
                    else:
                        new_seq.append(str(idx)) # Fallback
                q['answer_sequence'] = new_seq

with open('data/kyotsu/2024/honshiken/data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Fixed answer_sequence!")
