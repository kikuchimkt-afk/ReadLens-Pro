import json

# Include the replacement character '\ufffd'
mapping = {
    "\ufffd@": "①",
    "\ufffdA": "②",
    "\ufffdB": "③",
    "\ufffdC": "④",
    "\ufffdD": "⑤",
    "\ufffdE": "⑥"
}

with open('data/kyotsu/2024/honshiken/data.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for s in d.get('sections', []):
    for q in s.get('questions', []):
        for c in q.get('choices', []):
            label = c.get('label')
            if label in mapping:
                c['label'] = mapping[label]
        
        if 'answer_sequence' in q and isinstance(q['answer_sequence'], list):
            new_seq = []
            for item in q['answer_sequence']:
                if isinstance(item, str) and item in mapping:
                    new_seq.append(mapping[item])
                else:
                    new_seq.append(item)
            q['answer_sequence'] = new_seq

with open('data/kyotsu/2024/honshiken/data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Fixed garbled choice labels and answer_sequences with \\ufffd!")
