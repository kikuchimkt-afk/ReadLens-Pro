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

    # 既存の手動語彙（term_ja付き）が同フォルダにある場合は優先利用
    term_ja_lookup = {}
    manual_entries = []
    manual_keys = set()
    manual_vocab = src.parent / "vocabulary_from_explanations.json"
    if manual_vocab.exists():
        try:
            mv = json.loads(manual_vocab.read_text(encoding="utf-8"))
            manual_entries = mv.get("entries", []) if isinstance(mv.get("entries", []), list) else []
            for e in manual_entries:
                ten = str(e.get("term_en", "")).strip().lower()
                tja = str(e.get("term_ja", "")).strip()
                if ten and tja:
                    term_ja_lookup[ten] = tja
                    manual_keys.add(ten)
        except Exception:
            pass

    # 追加シード語彙（PDFの語句欄を手入力した補助データ）
    seed_entries = []
    seed_mode_only = False
    seed_keys = set()
    seed_sections_by_key = {}
    seed_vocab = src.parent / "vocabulary_seed.json"
    if seed_vocab.exists():
        try:
            sv = json.loads(seed_vocab.read_text(encoding="utf-8"))
            seed_entries = sv.get("entries", []) if isinstance(sv.get("entries", []), list) else []
            for e in seed_entries:
                ten = str(e.get("term_en", "")).strip().lower()
                tja = str(e.get("term_ja", "")).strip()
                if ten and tja:
                    term_ja_lookup[ten] = tja
                    seed_keys.add(ten)
                    sec = e.get("section_number")
                    if sec is not None:
                        seed_sections_by_key.setdefault(ten, set()).add(str(sec))
            # シードがある年度は、過去の抽出語彙を混ぜずシードのみを採用する
            if seed_entries:
                seed_mode_only = True
        except Exception:
            pass

    # en -> ja の対訳候補（data.json中の bilingual ペアから構築）
    bilingual_map = {}
    english_corpus_chunks = []

    def add_bilingual_pair(en_text, ja_text):
        en = str(en_text or "").strip()
        ja = str(ja_text or "").strip()
        if not en or not ja:
            return
        if len(en) > 120:
            return
        key = en.lower()
        bilingual_map.setdefault(key, ja)
        english_corpus_chunks.append(key)

    def walk_bilingual(node):
        if isinstance(node, list):
            for x in node:
                walk_bilingual(x)
            return
        if isinstance(node, dict):
            if ("en" in node) and ("ja" in node):
                add_bilingual_pair(node.get("en", ""), node.get("ja", ""))
            for v in node.values():
                walk_bilingual(v)

    walk_bilingual(data)
    english_corpus = "\n".join(english_corpus_chunks)

    def normalize_term_for_match(term: str) -> str:
        x = str(term or "").lower().strip()
        x = x.replace("~", " ")
        x = re.sub(r"\s+", " ", x)
        x = x.replace("attemptto", "attempt to")
        return x.strip()

    def term_exists_in_corpus(term: str) -> bool:
        t = normalize_term_for_match(term)
        if not t:
            return False
        # 1語は単語境界、複数語は部分一致
        if " " not in t:
            return re.search(rf"\b{re.escape(t)}\b", english_corpus) is not None
        return t in english_corpus

    # sentence id -> {en, ja}
    sentence_map = {}

    def add_sentence(obj):
        if not isinstance(obj, dict):
            return
        sid = obj.get("id")
        if sid and (obj.get("en") or obj.get("ja")):
            sentence_map[sid] = {"en": obj.get("en", ""), "ja": obj.get("ja", "")}

    def walk_para(node):
        if isinstance(node, list):
            for x in node:
                walk_para(x)
            return
        if isinstance(node, dict):
            add_sentence(node)
            if isinstance(node.get("items"), list):
                for it in node["items"]:
                    walk_para(it)

    for sec in data.get("sections", []):
        passages = []
        if sec.get("subsections"):
            for sub in sec["subsections"]:
                passages.extend(sub.get("passages", []))
        else:
            passages.extend(sec.get("passages", []))
        for p in passages:
            if isinstance(p.get("sentences"), list):
                for s in p["sentences"]:
                    add_sentence(s)
            if isinstance(p.get("paragraphs"), list):
                for para in p["paragraphs"]:
                    walk_para(para)
            if isinstance(p.get("floating_aside"), dict) and isinstance(p["floating_aside"].get("sentences"), list):
                for s in p["floating_aside"]["sentences"]:
                    add_sentence(s)

    # 解説文の和文中に出る英語語句（1語/複数語）だけ抽出
    word_re = re.compile(r"[A-Za-z][A-Za-z'\-]+")
    phrase_re = re.compile(r"[A-Za-z][A-Za-z'\-]+(?:\s+[A-Za-z][A-Za-z'\-]+)+")
    entries: dict[str, dict] = {}
    stop_words = {
        "about", "after", "before", "below", "above", "across", "around", "because",
        "could", "should", "would", "there", "their", "while", "where", "which", "these",
        "those", "being", "every", "other", "another", "through", "without", "between",
    }
    strict_require_translation = False

    def resolve_term_ja(key: str, default_empty: bool = False) -> str:
        if key in term_ja_lookup:
            return term_ja_lookup[key]
        if key in bilingual_map:
            return bilingual_map[key]
        return "" if default_empty else "（未登録）"

    def pick_best_example(term_key: str, evidence_sentences):
        if not evidence_sentences:
            return "", ""
        # 1) 語句一致する根拠文を優先
        for sid in evidence_sentences:
            if sid in sentence_map:
                en = sentence_map[sid].get("en", "") or ""
                ja = sentence_map[sid].get("ja", "") or ""
                if term_key and term_key in en.lower():
                    return shorten_example(en, ja, term_key)
        # 2) 一致しない場合は先頭
        for sid in evidence_sentences:
            if sid in sentence_map:
                en = sentence_map[sid].get("en", "") or ""
                ja = sentence_map[sid].get("ja", "") or ""
                return shorten_example(en, ja, term_key)
        return "", ""

    def is_bad_phrase(term: str) -> bool:
        t = term.strip().lower()
        if len(t) < 4:
            return True
        for p in ("and ", "or ", "but ", "to ", "of ", "in ", "on ", "at ", "for ", "with "):
            if t.startswith(p):
                return True
        return False

    def shorten_text(s: str, max_len: int) -> str:
        x = str(s or "").strip()
        x = re.sub(r"<[^>]*>", " ", x)
        x = re.sub(r"\s+", " ", x).strip()
        if len(x) <= max_len:
            return x
        return x[: max_len - 1].rstrip() + "…"

    def pick_short_clause(text: str, term_key: str) -> str:
        x = str(text or "").strip()
        if not x:
            return ""
        chunks = [c.strip() for c in re.split(r"[.;:!?]", x) if c.strip()]
        if not chunks:
            return x
        if term_key:
            matched = [c for c in chunks if term_key in c.lower()]
            if matched:
                return min(matched, key=len)
        return min(chunks, key=len)

    def shorten_example(en: str, ja: str, term_key: str):
        en0 = shorten_text(en, 180)
        ja0 = shorten_text(ja, 120)
        en1 = pick_short_clause(en0, term_key)
        ja1 = pick_short_clause(ja0, "")
        return shorten_text(en1 or en0, 95), shorten_text(ja1 or ja0, 58)

    def build_generated_example(term_en: str, term_ja: str):
        t = str(term_en or "").strip()
        j = str(term_ja or "").strip()
        en = f"I will use {t} in class."
        ja = f"授業で「{t}（{j or 'この語句'}）」を使います。"
        return en, ja

    def add_term(term: str, sec: int, qid: str, ans, evidence_sentences):
        t = (term or "").strip()
        if not t:
            return
        key = t.lower()
        ex_en, ex_ja = pick_best_example(key, evidence_sentences)
        resolved_ja = resolve_term_ja(key, default_empty=strict_require_translation)
        # 厳格モード時のみ、訳が取れない語を除外
        if strict_require_translation and (not resolved_ja):
            return
        rec = entries.setdefault(
            key,
            {
                "term_en": t,
                "term_ja": resolved_ja,
                "example_en": ex_en,
                "example_ja": ex_ja,
                "occurrences": [],
            },
        )
        # 先に空なら例文を補完
        if (not rec.get("example_en")) and ex_en:
            rec["example_en"] = ex_en
        if (not rec.get("example_ja")) and ex_ja:
            rec["example_ja"] = ex_ja
        if (not rec.get("term_ja")) and resolved_ja:
            rec["term_ja"] = resolved_ja
        occ = {
            "section_number": sec,
            "question_id": qid,
            "answer_number": ans,
            "source": "explanation_ja",
        }
        if evidence_sentences:
            occ["evidence_sentences"] = sorted(set(evidence_sentences))
        rec["occurrences"].append(occ)

    # manual語彙がある場合はそれを優先（訳欠け/断片語の混入を防ぐ）
    if manual_entries:
        for e in manual_entries:
            term = str(e.get("term_en", "")).strip()
            if not term:
                continue
            key = term.lower()
            term_ja = str(e.get("term_ja", "")).strip() or resolve_term_ja(key, default_empty=True)
            if not term_ja:
                continue
            occs = e.get("occurrences", []) if isinstance(e.get("occurrences", []), list) else []
            best_en = ""
            best_ja = ""
            normalized_occs = []
            for occ in occs:
                if not isinstance(occ, dict):
                    continue
                sec_num = occ.get("section_number")
                qid = occ.get("question_id")
                ans = occ.get("answer_number")
                ev = occ.get("evidence_sentences", []) if isinstance(occ.get("evidence_sentences", []), list) else []
                ex_en, ex_ja = pick_best_example(key, ev)
                if (not best_en) and ex_en:
                    best_en = ex_en
                    best_ja = ex_ja
                o = {
                    "section_number": sec_num,
                    "question_id": qid,
                    "answer_number": ans,
                    "source": "manual_explanations_vocab",
                }
                if ev:
                    o["evidence_sentences"] = sorted(set(ev))
                normalized_occs.append(o)
            entries[key] = {
                "term_en": term,
                "term_ja": term_ja,
                "example_en": best_en,
                "example_ja": best_ja,
                "occurrences": normalized_occs,
            }
    else:
        strict_require_translation = False
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
                    if len(ph) <= 120 and (not is_bad_phrase(ph)):
                        add_term(ph, sec_num, qid, ans, ev)

                # 単語（一般語ノイズを避ける）
                for w in word_re.findall(exja):
                    wl = w.lower()
                    if len(wl) >= 4 and wl not in stop_words:
                        add_term(wl, sec_num, qid, ans, ev)

    # explanation.ja から抽出できない年度向けフォールバック:
    # section.vocabulary.*.items[{en,ja}] を語彙源として利用
    if not entries:
        def collect_vocab_items(node):
            if isinstance(node, dict):
                items = node.get("items")
                if isinstance(items, list):
                    for it in items:
                        if isinstance(it, dict):
                            en = (it.get("en") or "").strip()
                            ja = (it.get("ja") or "").strip()
                            if en:
                                yield en, ja
                for v in node.values():
                    yield from collect_vocab_items(v)
            elif isinstance(node, list):
                for x in node:
                    yield from collect_vocab_items(x)

        for sec in data.get("sections", []):
            sec_num = sec.get("section_number")
            vocab = sec.get("vocabulary")
            if not vocab:
                continue
            for en, ja in collect_vocab_items(vocab):
                key = en.lower()
                rec = entries.setdefault(
                    key,
                    {
                        "term_en": en,
                        "term_ja": ja or resolve_term_ja(key),
                        "example_en": "",
                        "example_ja": "",
                        "occurrences": [],
                    },
                )
                if (not rec.get("term_ja")) and ja:
                    rec["term_ja"] = ja
                rec["occurrences"].append(
                    {
                        "section_number": sec_num,
                        "question_id": "vocabulary",
                        "answer_number": None,
                        "source": "section_vocabulary",
                    }
                )

    # シード語彙を最終マージ（PDF語句欄からの補完）
    for e in seed_entries:
        term = str(e.get("term_en", "")).strip()
        term_ja = str(e.get("term_ja", "")).strip()
        if not term or not term_ja:
            continue
        key = term.lower()
        rec = entries.setdefault(
            key,
            {
                "term_en": term,
                "term_ja": term_ja,
                "example_en": "",
                "example_ja": "",
                "occurrences": [],
            },
        )
        rec["term_ja"] = rec.get("term_ja") or term_ja
        sec = e.get("section_number")
        qid = e.get("question_id", "vocabulary")
        ans = e.get("answer_number")
        occ = {
            "section_number": sec,
            "question_id": qid,
            "answer_number": ans,
            "source": "vocabulary_seed",
        }
        if occ not in rec["occurrences"]:
            rec["occurrences"].append(occ)

    if seed_mode_only:
        # ユーザー提供画像の語句（seed）のみに厳密限定
        entries = {k: v for k, v in entries.items() if k in seed_keys}
        # 出現情報も seed 指定大問のみに限定
        for k, v in list(entries.items()):
            allowed_secs = seed_sections_by_key.get(k, set())
            occs = v.get("occurrences", []) if isinstance(v.get("occurrences", []), list) else []
            if allowed_secs:
                occs = [o for o in occs if str(o.get("section_number")) in allowed_secs]
            if not occs:
                # 念のため最低1件をseed情報から補完
                seed_hit = next((s for s in seed_entries if str(s.get("term_en", "")).strip().lower() == k), None)
                if seed_hit:
                    occs = [
                        {
                            "section_number": seed_hit.get("section_number"),
                            "question_id": seed_hit.get("question_id", "vocabulary"),
                            "answer_number": seed_hit.get("answer_number"),
                            "source": "vocabulary_seed",
                        }
                    ]
            v["occurrences"] = occs

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
        if not v.get("example_en") or not v.get("example_ja"):
            ge, gj = build_generated_example(v.get("term_en", ""), v.get("term_ja", ""))
            if not v.get("example_en"):
                v["example_en"] = ge
            if not v.get("example_ja"):
                v["example_ja"] = gj
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
                    "term_ja": e.get("term_ja", "（未登録）"),
                    "example_en": e.get("example_en", ""),
                    "example_ja": e.get("example_ja", ""),
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
