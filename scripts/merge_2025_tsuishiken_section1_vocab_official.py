# -*- coding: utf-8 -*-
"""
2025 共通テスト追試験 大問1（主な語句・表現）を
data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json に登録する。

既存の section 1 かつ語彙シード系の occurrence、および過去の追試大問1公式を取り除いてから差し替える。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION1_OFFICIAL_SOURCE = "kyotsu2025_tsuishiken_section1_official"


def strip_section1_vocab_only(entries):
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        filtered = [
            o
            for o in occs
            if not (
                o.get("section_number") in (1, "1")
                and o.get("source") in VOCAB_ONLY_SOURCES
            )
        ]
        if not filtered:
            continue
        ne = dict(e)
        ne["occurrences"] = filtered
        out.append(ne)
    return out


def drop_previous_section1_official(entries):
    return [
        e
        for e in entries
        if not any(
            o.get("source") == SECTION1_OFFICIAL_SOURCE
            for o in (e.get("occurrences") or [])
        )
    ]


OFFICIAL = [
    ("stationery", "〈名〉文房具"),
    ("celebrate", "〈動〉…を祝う"),
    ("supplies", "〈名〉用品"),
    ("flyer", "〈名〉チラシ；びら"),
    ("purchase", "〈名・動〉（…を）購入（する）；購入品"),
    ("memo pad", "〈名〉メモ帳"),
    ("limited to ...", "〈表現〉…に限られた"),
    ("monthly", "〈形〉1ヵ月間の"),
    ("special", "〈名〉特売品"),
    ("discount", "〈名・動〉（…を）割引（する）"),
    ("available", "〈形〉利用できる；入手できる"),
    ("delightful", "〈形〉楽しい；愉快な"),
    ("desktop", "〈形〉卓上の"),
    ("tray", "〈名〉トレイ；整理箱"),
    ("planner", "〈名〉スケジュール帳；手帳"),
    (
        "come in ...",
        "〈表現〉大きさ・色・種類などで手に入る［売られる］",
    ),
    ("a range of ...", "〈表現〉さまざまな…"),
    ("effectively", "〈副〉効果的に"),
    ("durable", "〈形〉耐久性のある；丈夫な"),
    ("erase / erasable", "〈動〉…を消す／〈形〉消すことのできる"),
    ("excellent", "〈形〉非常に優れた"),
    ("decorate", "〈動〉…を飾る"),
    ("seasonal theme", "〈名〉季節のテーマ；季題"),
]


def build_official_entries():
    entries = []
    for i, (term_en, term_ja) in enumerate(OFFICIAL):
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
                        "section_number": 1,
                        "question_id": "vocabulary",
                        "answer_number": None,
                        "source": SECTION1_OFFICIAL_SOURCE,
                    }
                ],
            }
        )
    return entries


def main():
    data = json.loads(VOCAB_FILE.read_text(encoding="utf-8"))
    old = data.get("entries") or []
    stripped = strip_section1_vocab_only(old)
    stripped = drop_previous_section1_official(stripped)
    official = build_official_entries()

    meta = data.get("meta") or {}
    meta["section1_official"] = {
        "label": "2025追試験 大問1（主な語句・表現・画像準拠）",
        "count": len(OFFICIAL),
    }

    data["entries"] = stripped + official
    data.pop("by_section", None)

    VOCAB_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {VOCAB_FILE}")
    print(f"  Section-1 official cards: {len(official)}.")


if __name__ == "__main__":
    main()
