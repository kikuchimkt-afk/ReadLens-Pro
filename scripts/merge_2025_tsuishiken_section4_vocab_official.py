# -*- coding: utf-8 -*-
"""
2025 共通テスト追試験 大問4（主な語句・表現）を
data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json に登録する。

既存の section 4 かつ語彙シード系の occurrence、および過去の追試大問4公式を取り除いてから差し替える。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION4_OFFICIAL_SOURCE = "kyotsu2025_tsuishiken_section4_official"


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
    ("revision", "〈名〉修正；変更"),
    ("based on ...", "〈表現〉…に基づいて"),
    ("school night", "〈名〉翌日学校がある夜"),
    ("assign / assignment", "〈動・名〉…を与える；課す／課題"),
    ("as a result", "〈表現〉その結果"),
    ("homework-free", "〈形〉宿題のない（≒ no-homework）"),
    ("benefit", "〈名・動〉恩恵（を得る）"),
    ("lesson materials", "〈名〉教材"),
    ("thoroughly", "〈副〉完全に"),
    ("upcoming", "〈形〉まもなくやって来る"),
    ("concentrate", "〈動〉集中する"),
    ("go over ...", "〈表現〉…を繰り返す［復習する］"),
    ("prefer to -", "〈表現〉-する方を好む"),
    ("refresh", "〈動〉…をさわやかにする；元気づける"),
    ("reset", "〈動〉…を再起動する；修復する"),
    ("motivate O to -", "〈表現〉Oを動機づけて-させる"),
    ("improve", "〈動〉…を改善する"),
    ("academic performance", "〈名〉学業成績"),
    ("in conclusion", "〈表現〉結論として；要するに"),
    ("review", "〈動〉…を復習する"),
    ("preview", "〈動〉…を下検分する；先立って見る"),
    ("content", "〈名〉内容"),
    ("vague", "〈形〉あいまいな；漠然とした"),
    ("connect", "〈動〉つながる"),
    ("summary sentence", "〈名〉要約文"),
    ("missing", "〈形〉欠けている"),
    ("propose", "〈動〉…を提案する"),
    ("preparation", "〈名〉準備"),
    ("expand", "〈動〉…を拡大する"),
    ("learning strategies", "〈名〉学習戦略"),
    ("reflect on ...", "〈表現〉…を熟考する"),
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
        "label": "2025追試験 大問4（主な語句・表現・画像準拠）",
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
