# -*- coding: utf-8 -*-
"""
2025 共通テスト追試験 大問3（主な語句・表現）を
data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json に登録する。

区分: 3M1=第1段落, 3M2=第2段落
既存の section 3／3M1／3M2 かつ語彙シード系、および過去の追試大問3公式を取り除いてから差し替える。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION3_OFFICIAL_SOURCE = "kyotsu2025_tsuishiken_section3_official"
SECTION3_NUMBERS = frozenset({3, "3", "3M1", "3M2", "3m1", "3m2"})


def strip_section3_vocab_only(entries):
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        filtered = [
            o
            for o in occs
            if not (
                o.get("section_number") in SECTION3_NUMBERS
                and o.get("source") in VOCAB_ONLY_SOURCES
            )
        ]
        if not filtered:
            continue
        ne = dict(e)
        ne["occurrences"] = filtered
        out.append(ne)
    return out


def drop_previous_section3_official(entries):
    return [
        e
        for e in entries
        if not any(
            o.get("source") == SECTION3_OFFICIAL_SOURCE
            for o in (e.get("occurrences") or [])
        )
    ]


OFFICIAL = [
    # 3M1 第1段落
    ("3M1", "gaze", "〈動〉見つめる"),
    ("3M1", "cabin", "〈名〉船室"),
    ("3M1", "a dream come true", "〈表現〉実現した夢；夢がかなうこと"),
    ("3M1", "planet", "〈名〉惑星"),
    ("3M1", "innovator", "〈名〉革新者"),
    ("3M1", "tune", "〈名〉曲；メロディー"),
    ("3M1", "interrupt", "〈動〉…をさえぎる"),
    ("3M1", "thought", "〈名〉思考"),
    ("3M1", "approach", "〈動〉…に近づく"),
    ("3M1", "departure", "〈名〉出発"),
    ("3M1", "in person", "〈表現〉直接自分で"),
    (
        "3M1",
        "first things first",
        "〈表現〉最も大事なことを最初に（しよう）；何はともあれ",
    ),
    ("3M1", "make sure that ...", "〈表現〉…を確かめる［確実にする］"),
    ("3M1", "charge", "〈動〉…を充電する"),
    ("3M1", "remind oneself", "〈表現〉自分に言い聞かせる"),
    ("3M1", "double-check", "〈動〉…を再確認する"),
    ("3M1", "excellent", "〈形〉非常に優れた"),
    ("3M1", "upgrade", "〈動〉…を改良する"),
    ("3M1", "latest", "〈形〉最新の"),
    ("3M1", "explorer", "〈名〉探検家"),
    ("3M1", "Upon hearing ...", "〈表現〉…を聞くと（すぐに）"),
    ("3M1", "gladly", "〈副〉喜んで；進んで"),
    ("3M1", "present A with B", "〈表現〉AにBを贈呈する"),
    ("3M1", "gear", "〈名〉道具；装備（≒ equipment）"),
    # 3M2 第2段落
    ("3M2", "one by one", "〈表現〉１人ずつ"),
    ("3M2", "ladder", "〈名〉ハシゴ"),
    ("3M2", "surface", "〈名〉表面"),
    ("3M2", "take in", "〈表現〉見てとる；じっくり見る"),
    ("3M2", "amazing", "〈形〉すばらしい"),
    ("3M2", "tap", "〈名〉軽くたたくこと"),
    ("3M2", "brilliant", "〈形〉とても鮮やかな"),
]


def build_official_entries():
    entries = []
    for i, (sec, term_en, term_ja) in enumerate(OFFICIAL):
        ex_en = f"I will use {term_en} in class."
        ex_ja = f"授業で「{term_en}（{term_ja}）」を使います。"
        entries.append(
            {
                "term_en": term_en,
                "term_ja": term_ja,
                "example_en": ex_en,
                "example_ja": ex_ja,
                "flashcard_order": i,
                "occurrences": [
                    {
                        "section_number": sec,
                        "question_id": "vocabulary",
                        "answer_number": None,
                        "source": SECTION3_OFFICIAL_SOURCE,
                    }
                ],
            }
        )
    return entries


def main():
    data = json.loads(VOCAB_FILE.read_text(encoding="utf-8"))
    old = data.get("entries") or []
    stripped = strip_section3_vocab_only(old)
    stripped = drop_previous_section3_official(stripped)
    official = build_official_entries()

    meta = data.get("meta") or {}
    meta["section3_official"] = {
        "label": "2025追試験 大問3（主な語句・表現・画像準拠）",
        "parts": {
            "3M1": "第1段落",
            "3M2": "第2段落",
        },
        "count": len(OFFICIAL),
    }

    data["entries"] = stripped + official
    data.pop("by_section", None)

    VOCAB_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {VOCAB_FILE}")
    print(f"  Section-3 official cards: {len(official)}.")


if __name__ == "__main__":
    main()
