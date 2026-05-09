# -*- coding: utf-8 -*-
"""
2025 共通テスト追試験 大問2（主な語句・表現）を
data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json に登録する。

既存の section 2 かつ語彙シード系の occurrence、および過去の追試大問2公式を取り除いてから差し替える。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION2_OFFICIAL_SOURCE = "kyotsu2025_tsuishiken_section2_official"


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
    (
        "host",
        "〈名〉〈自宅に留学生を迎え入れる〉ホスト；主人役",
    ),
    ("resident", "〈名〉住民"),
    ("respondent", "〈名〉回答者"),
    ("in general", "〈表現〉概して"),
    ("majority", "〈名〉大部分"),
    ("household chores", "〈名〉家事"),
    ("child raising", "〈名〉育児；子育て"),
    ("furthermore", "〈副〉さらに；加えて"),
    ("responsibility", "〈名〉責任"),
    ("working hours", "〈名〉労働［勤務］時間"),
    ("favour", "〈動〉賛成［支持］する"),
    ("awareness", "〈名〉意識"),
    ("perceive", "〈動〉…を知覚［認識］する"),
    ("angle", "〈名〉角度；観点"),
    ("current situation", "〈名〉現状"),
    ("satisfactory", "〈形〉満足のゆく"),
    ("encouraging", "〈形〉励みになる"),
    ("improve", "〈動〉…を改善する"),
    ("promising", "〈形〉有望な"),
    ("describe", "〈動〉…を説明［描写］する"),
    ("tasty", "〈形〉おいしい"),
    ("the following", "〈名〉次に述べること"),
    ("participant / participate", "〈名・動〉参加者／参加する"),
    ("preference", "〈名〉好み"),
    ("definitely", "〈副〉絶対に"),
    ("moderately", "〈副〉適度に；ほどほどに"),
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
        "label": "2025追試験 大問2（主な語句・表現・画像準拠）",
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
