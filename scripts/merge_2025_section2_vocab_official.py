# -*- coding: utf-8 -*-
"""
2025 共通テスト本試験 大問2（主な語句・表現）を vocabulary_explanations_only_all_sections.json に登録する。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/honshiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION2_OFFICIAL_SOURCE = "kyotsu2025_section2_official"


def strip_section2_vocab_only(entries):
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        filtered = [
            o
            for o in occs
            if not (
                o.get("section_number") in (2, "2")
                and o.get("source") in VOCAB_ONLY_SOURCES
            )
        ]
        if not filtered:
            continue
        ne = dict(e)
        ne["occurrences"] = filtered
        out.append(ne)
    return out


def drop_previous_section2_official(entries):
    return [
        e
        for e in entries
        if not any(
            o.get("source") == SECTION2_OFFICIAL_SOURCE
            for o in (e.get("occurrences") or [])
        )
    ]


OFFICIAL = [
    ("transportation", "〈名〉交通機関"),
    ("vehicle", "〈名〉乗り物；車"),
    ("be electrically powered", "〈表現〉電気を動力源としている"),
    ("in general", "〈表現〉概して"),
    ("zero-emission", "〈形〉有害ガスを排出しない"),
    ("emergency services", "〈名〉救急（医療）サービス"),
    ("ambulance", "〈名〉救急車"),
    ("from a ... point of view", "〈表現〉…の観点からは"),
    ("operating costs", "〈名〉経営［運営；営業］費"),
    ("look forward to -ing", "〈表現〉－するのを楽しみに待つ"),
    ("prediction", "〈名〉予測"),
    ("turn out to be ...", "〈表現〉…であることがわかる"),
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
                        "section_number": 2,
                        "question_id": "vocabulary",
                        "answer_number": None,
                        "source": SECTION2_OFFICIAL_SOURCE,
                    }
                ],
            }
        )
    return entries


def main():
    data = json.loads(VOCAB_FILE.read_text(encoding="utf-8"))
    old = data.get("entries") or []
    stripped = strip_section2_vocab_only(old)
    stripped = drop_previous_section2_official(stripped)
    official = build_official_entries()

    meta = data.get("meta") or {}
    meta["section2_official"] = {
        "label": "2025本試験 大問2（主な語句・表現・画像準拠）",
        "count": len(OFFICIAL),
    }

    data["entries"] = stripped + official
    data.pop("by_section", None)

    VOCAB_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {VOCAB_FILE}")
    print(f"  Section-2 official cards: {len(official)}.")


if __name__ == "__main__":
    main()
