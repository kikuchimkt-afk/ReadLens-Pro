"""第4回 data.json の自動検証スクリプト。

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
    Path(r"c:\Users\makoto\Documents\GitHub\ReadLens-Pro\data\sundai\2026\round04\data.json").read_text(encoding="utf-8")
)

def _collect_ids_from_paragraphs(paragraphs: list, into: set) -> None:
    for para in paragraphs or []:
        if isinstance(para, dict) and para.get("list_style") == "star" and isinstance(
            para.get("items"), list
        ):
            for it in para["items"]:
                into.add(it["id"])
        elif isinstance(para, list):
            for s in para:
                into.add(s["id"])
        elif isinstance(para, dict) and para.get("id"):
            into.add(para["id"])


def _collect_ids_from_hotel_sheet(hs: dict | None, into: set) -> None:
    if not hs or not isinstance(hs.get("sections"), list):
        return
    for hsec in hs["sections"]:
        k = hsec.get("kind")
        if k == "heading_paragraph" and hsec.get("paragraph"):
            para = hsec["paragraph"]
            if isinstance(para, list):
                for p in para:
                    into.add(p["id"])
            else:
                into.add(para["id"])
        elif k == "two_column_dashes":
            for item in (hsec.get("left") or []) + (hsec.get("right") or []):
                into.add(item["id"])
        elif k == "prices":
            for line in hsec.get("lines") or []:
                into.add(line["id"])
        elif k == "guest_review" and hsec.get("body"):
            body = hsec["body"]
            if isinstance(body, list):
                for b in body:
                    into.add(b["id"])
            else:
                into.add(body["id"])


def verify_section4(sec: dict) -> list[str]:
    """問題実装手引書 §3.4.1 E に基づく大問4専用チェック。"""
    bad_local: list[str] = []
    if sec.get("section_number") != 4:
        return bad_local
    if len(sec.get("passages", [])) != 1:
        bad_local.append("大問4: passages は 1 個のみであるべき（本文＋コメントは同一 passage 内）")
        return bad_local
    p = sec["passages"][0]

    mcs = p.get("margin_comments") or []
    if not mcs:
        bad_local.append("大問4: margin_comments が空")
    for i, mc in enumerate(mcs):
        extra_k = set(mc.keys()) - {"marker", "en", "ja"}
        if extra_k:
            bad_local.append("大問4: margin_comments[{}] に余計なキー {}".format(i, extra_k))
        for k in ("marker", "en", "ja"):
            if not mc.get(k):
                bad_local.append("大問4: margin_comments[{}].{} が空または欠落".format(i, k))

    cm_in_text: set[str] = set()
    for para in p.get("paragraphs", []):
        for s in para:
            if "comment_marker" in s:
                cm_in_text.add(s["comment_marker"])
                if s.get("marker_position") not in ("before", "after"):
                    bad_local.append(
                        "大問4: {} の marker_position が不正: {}".format(s["id"], s.get("marker_position"))
                    )
    mc_set = {mc["marker"] for mc in mcs}
    if cm_in_text != mc_set:
        bad_local.append(
            "大問4: comment_marker 集合と margin_comments.marker が一致しない: text={} margin={}".format(
                cm_in_text, mc_set
            )
        )

    for para in p.get("paragraphs", []):
        for s in para:
            if "underline_word" in s:
                uw = s["underline_word"]
                if uw not in s["en"]:
                    bad_local.append(
                        "大問4: {}.underline_word '{}' が en に無い: '{}'".format(s["id"], uw, s["en"])
                    )
                if uw.endswith("."):
                    bad_local.append("大問4: {}.underline_word の末尾にピリオド".format(s["id"]))

    tc = p.get("teacher_comment")
    if not (isinstance(tc, dict) and tc.get("en") and tc.get("ja")):
        bad_local.append("大問4: teacher_comment が欠落（passages[0] 直下に {en, ja} 必須）")

    return bad_local


all_ids: set[str] = set()
for sec in data["sections"]:
    sit = sec.get("situation")
    if sit and isinstance(sit.get("intro_sentences"), list):
        for s in sit["intro_sentences"]:
            all_ids.add(s["id"])
    for q in sec.get("questions", []):
        st = q.get("stem") or q.get("question_text")
        if isinstance(st, dict) and isinstance(st.get("sentences"), list):
            for s in st["sentences"]:
                all_ids.add(s["id"])
    for p in sec.get("passages", []):
        for s in p.get("sentences", []) or []:
            all_ids.add(s["id"])
        _collect_ids_from_paragraphs(p.get("paragraphs", []), all_ids)
        if p.get("hotel_sheet"):
            _collect_ids_from_hotel_sheet(p["hotel_sheet"], all_ids)
        if p.get("id") == "questionnaire" and p.get("comments"):
            for c in p["comments"]:
                if isinstance(c.get("sentences"), list):
                    for s in c["sentences"]:
                        all_ids.add(s["id"])
                elif c.get("id"):
                    all_ids.add(c["id"])

bad: list[str] = []
for sec in data["sections"]:
    bad.extend(verify_section4(sec))

bad_q: list[str] = []
for sec in data["sections"]:
    for q in sec.get("questions", []):
        ex = q.get("explanation") or {}
        tag = "sec{} {}".format(sec["section_number"], q["question_id"])
        extra = set(ex.keys()) - ALLOWED_EXPL_KEYS
        if extra:
            bad_q.append("{}: extra fields {}".format(tag, extra))
        note = ex.get("instructor_note")
        if not isinstance(note, dict):
            bad_q.append("{}: instructor_note is not dict".format(tag))
            continue
        if len(note.get("ja", "")) < 10:
            bad_q.append("{}: instructor_note.ja too short".format(tag))
        if len(note.get("points", [])) < 3:
            bad_q.append("{}: instructor_note.points < 3".format(tag))
        sid_re = re.compile(
            r"\b[a-z]{1,6}\d?(?:_[a-z]{1,4}\d?)?_[a-z]\d+\b"
            r"|\bp\d+_s\d+\b"
            r"|\b[a-z]{1,4}_(?:title|h|s\d+|in\d+|b\d+|c\d+|m\d+)\b"
        )
        for i, p in enumerate(note.get("points", [])):
            if not sid_re.search(p):
                bad_q.append("{}: points[{}] no sentence ID: {}...".format(tag, i, p[:50]))
        evid_bad = [e for e in ex.get("evidence_sentences", []) if e not in all_ids]
        if evid_bad:
            bad_q.append("{}: bad evidence IDs {}".format(tag, evid_bad))
        ans = q.get("answer")
        if isinstance(ans, str):
            correct = [c["label"] for c in q.get("choices", []) if c.get("is_correct")]
            if correct and correct[0] != ans:
                bad_q.append("{}: answer mismatch {} vs {}".format(tag, ans, correct))
        elif isinstance(ans, dict):
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
                        bad_q.append("{}: slot {} answer={} not in correct {}".format(
                            tag, slot_str, ans_label, slot_correct))
            if unordered:
                missing = unordered_ans - unordered_correct
                if missing:
                    bad_q.append("{}: unordered slots answer has wrong values {} (correct={})".format(
                        tag, sorted(missing), sorted(unordered_correct)))

bad_all = bad + bad_q
if bad_all:
    print("NG:")
    for b in bad_all:
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
