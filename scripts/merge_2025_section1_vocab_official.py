# -*- coding: utf-8 -*-
"""
2025 共通テスト本試験 大問1（主な語句・表現）を vocabulary_explanations_only_all_sections.json に登録する。

既存の section 1 かつ語彙シード系の occurrence、および過去の公式エントリを取り除いてから差し替える。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/honshiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION1_OFFICIAL_SOURCE = "kyotsu2025_section1_official"


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
    ("decorate", "〈動〉…を飾る"),
    ("decoration", "〈名〉装飾（物）"),
    ("aquarium", "〈名〉水槽"),
    (
        "sand to cover themselves in",
        "〈名〉自分を覆い隠すことのできる砂",
    ),
    (
        "non-hiding fish",
        "〈名〉隠れない［退避行動をしない］魚",
    ),
    ("solid", "〈形〉硬い"),
    ("log", "〈名〉丸木；丸太"),
    ("shallow", "〈形〉浅い"),
    ("soft", "〈形〉柔らかい"),
    ("(be) intended for ...", "〈表現〉…のために意図されている"),
    (
        "make sure (that) ...",
        "〈表現〉…であることを確実にする［確かめる］",
    ),
    ("room", "〈名〉空間；場所"),
    ("edge", "〈名〉縁；端"),
    ("place", "〈動〉…を置く"),
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
        "label": "2025本試験 大問1（主な語句・表現・画像準拠）",
        "count": len(OFFICIAL),
    }

    data["entries"] = stripped + official
    data.pop("by_section", None)

    VOCAB_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {VOCAB_FILE}")
    print(f"  Section-1 official cards: {len(official)} (replaced previous).")


if __name__ == "__main__":
    main()
