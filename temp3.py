import json
with open('data/kyotsu/2024/honshiken/data.json', encoding='utf-8') as f:
    d = json.load(f)
s4 = next((s for s in d['sections'] if s['section_number']==4), None)

print("--- QUESTIONNAIRE ---")
q = next(p for p in s4['passages'] if p['id'] == 'questionnaire_4')
for s in q.get('sentences', []):
    print(f"{s['id']}: {s['en'][:60]}...")

print("\n--- HANDOUT ---")
h = next(p for p in s4['passages'] if p['id'] == 'handout_4')
for s in h.get('sentences', []):
    print(f"{s['id']}: {s['en'][:60]}...")
