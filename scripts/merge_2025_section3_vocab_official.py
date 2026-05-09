# -*- coding: utf-8 -*-
"""2025 共通テスト本試験 大問3（主な語句・表現）を vocabulary_explanations_only_all_sections.json に登録する。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/honshiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION3_OFFICIAL_SOURCE = "kyotsu2025_section3_official"


def strip_section3_vocab_only(entries):
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        filtered = [
            o
            for o in occs
            if not (
                o.get("section_number") in (3, "3")
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
    ("capable", "〈形〉有能な"),
    ("classically-trained", "〈形〉古典的な［クラシックの］訓練を受けた"),
    ("perform", "〈動〉…を演奏する"),
    ("bassist", "〈名〉ベース奏者"),
    ("follower", "〈名〉（SNSなどの）フォロワー"),
    ("kind of", "〈表現〉いくぶん；かなり"),
    ("figure ... out", "〈表現〉…を理解する"),
    ("additional", "〈形〉追加の"),
    (
        "play tricks on 〈人〉",
        "〈表現〉（〈人〉の目や耳などが）錯誤を起こす；機能がおかしくなる",
    ),
    ("instrument", "〈名〉楽器"),
    ("get it", "〈表現〉わかる；理解する"),
    ("What's the matter?", "〈表現〉どうしたのだろう？"),
    ("show off", "〈表現〉〈能力などを〉ひけらかす"),
    ("from that day on", "〈表現〉その日以来（ずっと）"),
    ("take a step forward", "〈表現〉一歩踏み出す"),
    ("like the saying goes", "〈表現〉ことわざにもあるように"),
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
                        "section_number": 3,
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
        "label": "2025本試験 大問3（主な語句・表現・画像準拠）",
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
