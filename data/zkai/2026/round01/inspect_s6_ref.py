"""Inspect existing section 6 structure from sundai round01 as reference."""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

d = json.load(open('../../../sundai/2026/round01/data.json', 'r', encoding='utf-8'))
s6 = [s for s in d['sections'] if s['section_number'] == 6][0]

# Top-level keys
print("=== Section 6 top-level ===")
for k in sorted(s6.keys()):
    if k not in ('passages', 'questions', 'vocabulary'):
        print(f"  {k}: {s6[k]}")

# Passages
print(f"\n=== Passages ({len(s6['passages'])}) ===")
for i, p in enumerate(s6['passages']):
    print(f"\n  passage[{i}]:")
    for k in sorted(p.keys()):
        if k == 'paragraphs':
            print(f"    paragraphs: {len(p['paragraphs'])} groups")
            for j, para in enumerate(p['paragraphs']):
                print(f"      para[{j}]: {len(para)} sentences, first_id={para[0].get('id','?')}")
        elif k == 'block_separators':
            print(f"    block_separators: {p[k]}")
        else:
            v = p[k]
            if isinstance(v, dict):
                print(f"    {k}: {json.dumps(v, ensure_ascii=False)[:120]}")
            else:
                print(f"    {k}: {v}")

# Questions
print(f"\n=== Questions ({len(s6['questions'])}) ===")
for q in s6['questions']:
    qid = q.get('question_id', '?')
    an = q.get('answer_number') or q.get('answer_numbers')
    ans = q.get('answer')
    slots = q.get('unordered_slots')
    nchoices = len(q.get('choices', []))
    # Check for choices_N pattern
    extra_choices = [k for k in q.keys() if k.startswith('choices_')]
    print(f"  {qid}: answer_number={an}, answer={ans}, choices={nchoices}, unordered_slots={slots}, extra={extra_choices}")
    # Show stem
    stem = q.get('stem', {})
    print(f"    stem_en: {stem.get('en','')[:80]}")
