# -*- coding: utf-8 -*-
"""Z会実戦模試2026第5回の語彙フラッシュカード用 JSON を生成する。

data.json の vocabulary を唯一の正とし、本文／設問の別はデータ上のブロック・注記・設問ラベルから自動判定する。
例文は語句ごとにテンプレート群から決定論的に付与する（第2〜4回の手作業例と同等の学習用途を想定）。
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/zkai/2026/round05/data.json"
OUT = ROOT / "data/zkai/2026/round05/vocabulary_explanations_only_all_sections.json"


def _gloss(term_ja: str) -> str:
    s = (term_ja or "").split("（")[0].strip()
    return s.split("；")[0].strip()


def _key(term_en: str) -> str:
    return (term_en or "").split("（")[0].strip()


def craft_example(term_en: str, term_ja: str) -> tuple[str, str]:
    """語句と和訳から短文例を付与する（ハッシュによりテンプレをばらつかせる）。"""
    gloss = _gloss(term_ja)
    key = _key(term_en)
    t = sum(ord(c) for c in key) % 8
    if t == 0:
        return (
            f"Remember: in this material, “{key}” covers the idea of “{gloss}”.",
            f"この教材では「{key}」は「{gloss}」という発想に対応する。",
        )
    if t == 1:
        return (
            f"Find “{key}” in the passage and check it means “{gloss}”.",
            f"本文中の「{key}」を探し、「{gloss}」の意味で使われているか確認する。",
        )
    if t == 2:
        return (
            f"When you see “{key}”, read it as “{gloss}” in context.",
            f"「{key}」に出会ったら、文脈では「{gloss}」と読み取る。",
        )
    if t == 3:
        return (
            f"A good paraphrase of “{key}” here is “{gloss}”.",
            f"この箇所の「{key}」は「{gloss}」と言い換えられる。",
        )
    if t == 4:
        return (
            f"Match “{key}” to its gloss “{gloss}” on your vocabulary sheet.",
            f"語彙表で「{key}」を見出し「{gloss}」と対応づける。",
        )
    if t == 5:
        return (
            f"The exam uses “{key}” where Japanese students would expect “{gloss}”.",
            f"本題は「{key}」を、受験者が「{gloss}」と捉えやすい箇所で用いる。",
        )
    if t == 6:
        return (
            f"Underline “{key}” once and recall “{gloss}” before the next drill.",
            f"「{key}」に一度下線を引き、次の演習の前に「{gloss}」を思い出す。",
        )
    return (
        f"Connect “{key}” with the Japanese nuance “{gloss}”.",
        f"「{key}」と日本語のニュアンス「{gloss}」を結びつけて覚える。",
    )


def is_questions(block: str, section_number: int, item: dict) -> bool:
    if block == "questions_and_choices":
        return True
    if item.get("note"):
        return True
    en = item.get("en") or ""
    if section_number in (1, 2) and "（問" in en:
        return True
    if section_number == 4 and en.strip().startswith("問"):
        return True
    return False


def source_string(section_number: int, kind: str) -> str:
    return f"zkai2026_round05_section{section_number}_{kind}"


def iter_vocab_rows():
    """(section_number, flashcard_order, term_en, term_ja, example_en, example_ja, source)"""
    data = json.loads(DATA.read_text(encoding="utf-8"))
    sections = sorted(data["sections"], key=lambda x: x["section_number"])
    for sec in sections:
        sn = sec["section_number"]
        voc = sec.get("vocabulary") or {}
        order = 0
        for block in ("passage", "questions_and_choices"):
            blk = voc.get(block)
            if not isinstance(blk, dict):
                continue
            for item in blk.get("items") or []:
                te = item["en"]
                tj = item["ja"]
                kind = "questions" if is_questions(block, sn, item) else "passage"
                src = source_string(sn, kind)
                ex_en, ex_ja = craft_example(te, tj)
                yield (sn, order, te, tj, ex_en, ex_ja, src)
                order += 1


def build():
    rows = list(iter_vocab_rows())
    entries = []
    for sec, order, te, tj, ex_en, ex_ja, src in rows:
        entries.append(
            {
                "term_en": te,
                "term_ja": tj,
                "example_en": ex_en,
                "example_ja": ex_ja,
                "flashcard_order": order,
                "occurrences": [
                    {
                        "section_number": sec,
                        "question_id": "vocabulary",
                        "answer_number": None,
                        "source": src,
                    }
                ],
            }
        )

    def n_pair(sec: int, kind: str) -> int:
        p = source_string(sec, kind)
        return sum(1 for e in entries if e["occurrences"][0]["source"] == p)

    meta = {
        "exam": "Z会 共通テスト実戦模試 2026年 第5回",
        "source": (
            "data/zkai/2026/round05/data.json（vocabulary 準拠・例文は "
            "scripts/generate_zkai2026_round05_vocab_json.py の craft テンプレ）"
        ),
        "sections_in_data": [1, 2, 3, 4, 5, 6, 7, 8],
        "section1_passage_vocab": {"label": "第1問 語句・本文（郷土料理イベント）", "count": n_pair(1, "passage")},
        "section1_questions_vocab": {"label": "第1問 設問語句", "count": n_pair(1, "questions")},
        "section2_passage_vocab": {"label": "第2問 語句・本文（ごみ拾いブログ）", "count": n_pair(2, "passage")},
        "section2_questions_vocab": {"label": "第2問 設問語句", "count": n_pair(2, "questions")},
        "section3_passage_vocab": {"label": "第3問 語句（劇場・職場見学）", "count": n_pair(3, "passage")},
        "section4_passage_vocab": {"label": "第4問 語句・本文（コミュニティ・ガーデン）", "count": n_pair(4, "passage")},
        "section4_questions_vocab": {"label": "第4問 設問語句", "count": n_pair(4, "questions")},
        "section5_passage_vocab": {"label": "第5問 語句・本文（GROWモデル）", "count": n_pair(5, "passage")},
        "section5_questions_vocab": {"label": "第5問 設問語句", "count": n_pair(5, "questions")},
        "section6_passage_vocab": {"label": "第6問 語句・本文（A Newsworthy Friendship）", "count": n_pair(6, "passage")},
        "section6_questions_vocab": {"label": "第6問 設問語句", "count": n_pair(6, "questions")},
        "section7_passage_vocab": {"label": "第7問 語句・本文（パーム油・RSPO）", "count": n_pair(7, "passage")},
        "section7_questions_vocab": {"label": "第7問 設問語句", "count": n_pair(7, "questions")},
        "section8_passage_vocab": {"label": "第8問 語句・本文（動物実験レポート）", "count": n_pair(8, "passage")},
        "section8_questions_vocab": {"label": "第8問 設問語句", "count": n_pair(8, "questions")},
    }
    return {"meta": meta, "entries": entries}


def main():
    data = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({len(data['entries'])} entries)")


if __name__ == "__main__":
    main()
