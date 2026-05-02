"""第3回 data.json の自動検証スクリプト。

検証項目:
- explanation の許可フィールドのみが使われているか
- instructor_note が dict で、ja が十分長く、points が3個以上、各 point に sentence ID が含まれるか
- evidence_sentences が実在する ID か
- answer がスカラーの場合は choices.is_correct と整合、dict の場合は全 slot が正解ラベルに含まれるか
"""

import json
import re
from pathlib import Path

ALLOWED_EXPL_KEYS = {"quoted_ja", "quoted_source", "evidence_sentences", "instructor_note"}
data = json.loads(
    Path(r"c:\Users\makoto\Documents\GitHub\ReadLens-Pro\data\sundai\2026\round03\data.json").read_text(encoding="utf-8")
)

all_ids: set[str] = set()
for sec in data["sections"]:
    for p in sec.get("passages", []):
        for s in p.get("sentences", []) or []:
            all_ids.add(s["id"])
        for para in p.get("paragraphs", []) or []:
            for s in para:
                all_ids.add(s["id"])

bad: list[str] = []
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
        # Round02 と同等の sentence ID 正規表現
        sid_re = re.compile(
            r"\b[a-z]{1,6}\d?(?:_[a-z]{1,4}\d?)?_[a-z]\d+\b"
            r"|\bp\d+_s\d+\b"
            r"|\b[a-z]{1,4}_(?:title|h|s\d+|in\d+|b\d+|c\d+|m\d+)\b"
        )
        for i, p in enumerate(note.get("points", [])):
            if not sid_re.search(p):
                bad.append("{}: points[{}] no sentence ID: {}...".format(tag, i, p[:50]))
        evid_bad = [e for e in ex.get("evidence_sentences", []) if e not in all_ids]
        if evid_bad:
            bad.append("{}: bad evidence IDs {}".format(tag, evid_bad))
        ans = q.get("answer")
        if isinstance(ans, str):
            # スカラー解答: 単一の choices と整合性チェック
            correct = [c["label"] for c in q.get("choices", []) if c.get("is_correct")]
            if correct and correct[0] != ans:
                bad.append("{}: answer mismatch {} vs {}".format(tag, ans, correct))
        elif isinstance(ans, dict):
            # multi-slot 解答: slot ごとに choices_NN があればそれを優先、なければ q.choices で代用。
            # 順不同 slot は unordered_slots に列挙されている。順不同の場合は集合で比較。
            unordered = set(str(n) for n in q.get("unordered_slots", []))
            unordered_correct: set[str] = set()
            unordered_ans: set[str] = set()
            for slot_str, ans_label in ans.items():
                slot_choices = q.get("choices_{}".format(slot_str)) or q.get("choices", [])
                slot_correct = [c["label"] for c in slot_choices if c.get("is_correct")]
                if slot_str in unordered:
                    unordered_correct.update(slot_correct)
                    unordered_ans.add(ans_label)
                else:
                    if slot_correct and ans_label not in slot_correct:
                        bad.append("{}: slot {} answer={} not in correct {}".format(
                            tag, slot_str, ans_label, slot_correct))
            if unordered:
                # 順不同 slot 群: ans の集合が correct の集合に部分集合として含まれるか
                missing = unordered_ans - unordered_correct
                if missing:
                    bad.append("{}: unordered slots answer has wrong values {} (correct={})".format(
                        tag, sorted(missing), sorted(unordered_correct)))

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
