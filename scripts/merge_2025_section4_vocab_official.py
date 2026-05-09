# -*- coding: utf-8 -*-
"""2025 共通テスト本試験 大問4（主な語句・表現）を vocabulary_explanations_only_all_sections.json に登録する。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/honshiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION4_OFFICIAL_SOURCE = "kyotsu2025_section4_official"


def strip_section4_vocab_only(entries):
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        filtered = [
            o
            for o in occs
            if not (
                o.get("section_number") in (4, "4")
                and o.get("source") in VOCAB_ONLY_SOURCES
            )
        ]
        if not filtered:
            continue
        ne = dict(e)
        ne["occurrences"] = filtered
        out.append(ne)
    return out


def drop_previous_section4_official(entries):
    return [
        e
        for e in entries
        if not any(
            o.get("source") == SECTION4_OFFICIAL_SOURCE
            for o in (e.get("occurrences") or [])
        )
    ]


OFFICIAL = [
    ("(be) related to ...", "〈表現〉…と関係がある"),
    ("draft", "〈名〉草稿"),
    ("(be) based on ...", "〈表現〉…に基づいている"),
    ("stressful", "〈形〉ストレスの多い"),
    ("meaningful", "〈形〉重要な；意味のある"),
    ("take one's time", "〈表現〉ゆっくりやる"),
    ("be focused on ...", "〈表現〉…に集中して［焦点を合わせて］いる"),
    ("quality", "〈名〉質"),
    ("describe", "〈動〉…の特徴を述べる；…を説明する"),
    ("own", "〈動〉…を所有する"),
    ("belongings", "〈名〉所有物（≒ possessions）"),
    ("concentrate on ...", "〈表現〉…に集中する"),
    ("consume", "〈動〉…を消費する"),
    ("latest", "〈形〉最新の"),
    ("recommend", "〈動〉…を勧める"),
    ("recommendation", "〈名〉勧告；助言"),
    ("face-to-face", "〈形〉対面の"),
    ("impolite", "〈形〉失礼な"),
    ("affect ... negatively", "〈表現〉…に悪い影響を及ぼす"),
    ("aspect", "〈名〉面；特徴"),
    ("reflect on ...", "〈表現〉…を熟考する"),
    ("recollect", "〈動〉…を思い出す"),
    ("mentally", "〈副〉精神的に；心の中で"),
    ("highlight", "〈動〉…を強調する"),
    ("fulfillment", "〈名〉充足［満足］感"),
    ("in summary", "〈表現〉要約すると"),
    ("non-essential", "〈形〉不必要な"),
    ("quality time", "〈名〉（親しい人と過ごす）上質な時間"),
    ("rewarding", "〈形〉価値のある；報われる"),
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
                        "section_number": 4,
                        "question_id": "vocabulary",
                        "answer_number": None,
                        "source": SECTION4_OFFICIAL_SOURCE,
                    }
                ],
            }
        )
    return entries


def main():
    data = json.loads(VOCAB_FILE.read_text(encoding="utf-8"))
    old = data.get("entries") or []
    stripped = strip_section4_vocab_only(old)
    stripped = drop_previous_section4_official(stripped)
    official = build_official_entries()

    meta = data.get("meta") or {}
    meta["section4_official"] = {
        "label": "2025本試験 大問4（主な語句・表現・画像準拠）",
        "count": len(OFFICIAL),
    }

    data["entries"] = stripped + official
    data.pop("by_section", None)

    VOCAB_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {VOCAB_FILE}")
    print(f"  Section-4 official cards: {len(official)}.")


if __name__ == "__main__":
    main()
