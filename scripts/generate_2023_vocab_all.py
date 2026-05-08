import json
import pathlib
import re


def main() -> None:
    src = pathlib.Path("data/kyotsu/2023/honshiken/data.json")
    data = json.loads(src.read_text(encoding="utf-8"))

    stop = {
        "the", "a", "an", "and", "or", "to", "of", "in", "on", "at", "for", "with", "from", "by",
        "is", "are", "was", "were", "be", "been", "being", "this", "that", "these", "those",
        "it", "its", "as", "if", "then", "than", "not", "no", "do", "does", "did", "can", "could",
        "should", "would", "may", "might", "will", "shall", "you", "your", "we", "our", "they",
        "their", "he", "she", "his", "her", "them", "us", "i", "me", "my", "mine", "yours",
        "ours", "theirs",
    }
    word_re = re.compile(r"[A-Za-z][A-Za-z'\-]+")
    phrase_re = re.compile(r"[A-Za-z][A-Za-z'\-]+(?:\s+[A-Za-z][A-Za-z'\-]+)+")
    entries: dict[str, dict] = {}

    def add_term(term: str, sec: int, qid: str, ans, source: str, sent_ids=None) -> None:
        t = (term or "").strip()
        if not t:
            return
        key = t.lower()
        rec = entries.setdefault(key, {"term_en": t, "occurrences": []})
        occ = {
            "section_number": sec,
            "question_id": qid,
            "answer_number": ans,
            "source": source,
        }
        if sent_ids:
            occ["evidence_sentences"] = sorted(set(sent_ids))
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

            stem = (q.get("stem") or {}).get("en", "")
            for w in word_re.findall(stem):
                lw = w.lower()
                if len(lw) >= 4 and lw not in stop:
                    add_term(lw, sec_num, qid, ans, "stem")

            choice_keys = [k for k in q.keys() if k == "choices" or k.startswith("choices_")]
            for ck in choice_keys:
                for c in q.get(ck, []) or []:
                    cen = c.get("en", "")
                    if not cen:
                        continue
                    add_term(cen, sec_num, qid, ans, ck)
                    for w in word_re.findall(cen):
                        lw = w.lower()
                        if len(lw) >= 4 and lw not in stop:
                            add_term(lw, sec_num, qid, ans, ck)

            exp = q.get("explanation") or {}
            exja = exp.get("ja", "")
            for ph in phrase_re.findall(exja):
                ph = " ".join(ph.split())
                if len(ph) <= 120:
                    add_term(ph, sec_num, qid, ans, "explanation_ja", exp.get("evidence_sentences"))

    out_entries = []
    for _, v in entries.items():
        seen = set()
        occs = []
        for o in v["occurrences"]:
            sig = (
                o["section_number"],
                o["question_id"],
                o["answer_number"],
                o["source"],
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
                o["source"],
            ),
        )
        out_entries.append(v)

    out_entries.sort(key=lambda x: x["term_en"].lower())
    out = {
        "meta": {
            "exam": "共通テスト 2023年度 本試験",
            "source": str(src).replace("\\", "/"),
            "sections_in_data": [s.get("section_number") for s in data.get("sections", [])],
            "note": "data.json内の全大問（現在実装済み）から語彙・表現を抽出。",
        },
        "entries": out_entries,
    }

    outp = pathlib.Path("data/kyotsu/2023/honshiken/vocabulary_all_sections.json")
    outp.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"written {outp} entries={len(out_entries)}")


if __name__ == "__main__":
    main()
