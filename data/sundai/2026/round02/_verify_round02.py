import json, re
from pathlib import Path

ALLOWED_EXPL_KEYS = {"quoted_ja", "quoted_source", "evidence_sentences", "instructor_note"}
data = json.loads(Path(r"c:\Users\makoto\Documents\GitHub\ReadLens-Pro\data\sundai\2026\round02\data.json").read_text(encoding="utf-8"))

all_ids = set()
for sec in data["sections"]:
    for p in sec.get("passages", []):
        for s in p.get("sentences", []) or []:
            all_ids.add(s["id"])
        for para in p.get("paragraphs", []) or []:
            for s in para:
                all_ids.add(s["id"])

bad = []
for sec in data["sections"]:
    for q in sec.get("questions", []):
        ex = q.get("explanation") or {}
        tag = "sec{} {}".format(sec["section_number"], q["question_id"])
        extra = set(ex.keys()) - ALLOWED_EXPL_KEYS
        if extra:
            bad.append("{}: extra fields {}".format(tag, extra))
        note = ex.get("instructor_note")
        if not isinstance(note, dict):
            bad.append("{}: instructor_note is not dict".format(tag))
            continue
        if len(note.get("ja", "")) < 10:
            bad.append("{}: instructor_note.ja too short".format(tag))
        if len(note.get("points", [])) < 3:
            bad.append("{}: instructor_note.points < 3".format(tag))
        # Accept multiple sentence ID formats:
        #   p1_s1, hd_title, b6_s4 (round02 sec6), auth_b_s7 (round02 sec8 著者),
        #   sa_s5/sb_s2 (Source A/B), eo_in1 (essay outline), sv_m6 (survey member),
        #   ve_s4 (round01 sec4), shin_s1 (round01 sec8 speaker), etc.
        sid_re = re.compile(
            r"\b[a-z]{1,6}\d?(?:_[a-z]{1,4}\d?)?_[a-z]\d+\b"  # auth_a_s5, b6_s4, sv_m6, sa_s5
            r"|\bp\d+_s\d+\b"                                  # p1_s1
            r"|\b[a-z]{1,4}_(?:title|h|s\d+|in\d+|b\d+|c\d+|m\d+)\b"  # hd_title, eo_b1
        )
        for i, p in enumerate(note.get("points", [])):
            if not sid_re.search(p):
                bad.append("{}: points[{}] no sentence ID: {}...".format(tag, i, p[:50]))
        evid_bad = [e for e in ex.get("evidence_sentences", []) if e not in all_ids]
        if evid_bad:
            bad.append("{}: bad evidence IDs {}".format(tag, evid_bad))
        ans = q.get("answer")
        correct = [c["label"] for c in q.get("choices", []) if c.get("is_correct")]
        if correct and isinstance(ans, str) and correct[0] != ans:
            bad.append("{}: answer mismatch {} vs {}".format(tag, ans, correct))
        elif correct and isinstance(ans, dict):
            # ordering/multi-slot question: verify all slot values are correct labels
            slot_vals = list(ans.values())
            correct_set = set(correct)
            wrong = [v for v in slot_vals if v not in correct_set]
            if wrong:
                bad.append("{}: multi-slot answer has wrong values {} (correct={})".format(tag, wrong, correct))

if bad:
    print("NG:")
    for b in bad:
        print(" -", b)
else:
    print("OK: all questions pass validation")

for sec in data["sections"]:
    for q in sec.get("questions", []):
        ex = q.get("explanation", {})
        note = ex.get("instructor_note", {})
        evid_ok = all(e in all_ids for e in ex.get("evidence_sentences", []))
        print("sec{} {}: ans={} note_ja={}chars points={} evidence_ok={}".format(
            sec["section_number"], q["question_id"], q.get("answer"),
            len(note.get("ja", "")), len(note.get("points", [])), evid_ok))
