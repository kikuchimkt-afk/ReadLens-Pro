import json
import pathlib
import re
import sys


def main() -> None:
    # Usage:
    #   python scripts/generate_2023_vocab_explanations_only.py [input_json] [output_json]
    # Defaults keep backward compatibility for 2023 honshiken.
    in_arg = sys.argv[1] if len(sys.argv) >= 2 else "data/kyotsu/2023/honshiken/data.json"
    out_arg = (
        sys.argv[2]
        if len(sys.argv) >= 3
        else "data/kyotsu/2023/honshiken/vocabulary_explanations_only_all_sections.json"
    )
    src = pathlib.Path(in_arg)
    data = json.loads(src.read_text(encoding="utf-8"))

    # 解説文の和文中に出る英語語句（1語/複数語）だけ抽出
    word_re = re.compile(r"[A-Za-z][A-Za-z'\-]+")
    phrase_re = re.compile(r"[A-Za-z][A-Za-z'\-]+(?:\s+[A-Za-z][A-Za-z'\-]+)+")
    entries: dict[str, dict] = {}

    def add_term(term: str, sec: int, qid: str, ans, evidence_sentences):
        t = (term or "").strip()
        if not t:
            return
        key = t.lower()
        rec = entries.setdefault(key, {"term_en": t, "occurrences": []})
        occ = {
            "section_number": sec,
            "question_id": qid,
            "answer_number": ans,
            "source": "explanation_ja",
        }
        if evidence_sentences:
            occ["evidence_sentences"] = sorted(set(evidence_sentences))
        rec["occurrences"].append(occ)

    for sec in data.get("sections", []):
        sec_num = sec.get("section_number")
        qgroups = []
        if sec.get("subsections"):
            for sub in sec["subsections"]:
                for q in sub.get("questions", []):
                    qgroups.append((q, sub.get("label")))
        else:
            for q in sec.get("questions", []):
                qgroups.append((q, None))

        for q, sub in qgroups:
            qid = q.get("question_id")
            if sub:
                qid = f"{sub}_{qid}"
            ans = q.get("answer_number")
            exp = q.get("explanation") or {}
            exja = exp.get("ja", "")
            ev = exp.get("evidence_sentences", [])

            # 複数語句
            for ph in phrase_re.findall(exja):
                ph = " ".join(ph.split())
                if len(ph) <= 120:
                    add_term(ph, sec_num, qid, ans, ev)

            # 単語
            for w in word_re.findall(exja):
                if len(w) >= 4:
                    add_term(w.lower(), sec_num, qid, ans, ev)

    out_entries = []
    for _, v in entries.items():
        seen = set()
        occs = []
        for o in v["occurrences"]:
            sig = (
                o["section_number"],
                o["question_id"],
                o["answer_number"],
                tuple(o.get("evidence_sentences", [])),
            )
            if sig in seen:
                continue
            seen.add(sig)
            occs.append(o)
        v["occurrences"] = sorted(
            occs,
            key=lambda o: (
                str(o["section_number"]),
                str(o["question_id"]),
                str(o["answer_number"]),
            ),
        )
        out_entries.append(v)

    out_entries.sort(key=lambda x: x["term_en"].lower())

    # sectionごとに語彙を引けるインデックス（大問ソート用）
    by_section = {}
    for e in out_entries:
        for occ in e["occurrences"]:
            sec = str(occ["section_number"])
            by_section.setdefault(sec, []).append(
                {
                    "term_en": e["term_en"],
                    "question_id": occ["question_id"],
                    "answer_number": occ["answer_number"],
                    "evidence_sentences": occ.get("evidence_sentences", []),
                }
            )
    for sec in by_section:
        by_section[sec].sort(
            key=lambda x: (
                x["term_en"].lower(),
                str(x["question_id"]),
                str(x["answer_number"]),
            )
        )
    out = {
        "meta": {
            "exam": data.get("exam_info", {}).get("title", "unknown"),
            "source": str(src).replace("\\", "/"),
            "sections_in_data": [s.get("section_number") for s in data.get("sections", [])],
            "constraint": "解説文（explanation.ja）内の英語語句のみに限定",
            "sort_keys": {
                "entries": ["term_en"],
                "by_section": ["section_number", "term_en", "question_id", "answer_number"]
            }
        },
        "entries": out_entries,
        "by_section": by_section
    }

    outp = pathlib.Path(out_arg)
    outp.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"written {outp} entries={len(out_entries)}")


if __name__ == "__main__":
    main()
