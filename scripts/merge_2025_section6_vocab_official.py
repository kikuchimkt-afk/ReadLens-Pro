# -*- coding: utf-8 -*-
"""
2025 共通テスト本試験 大問6（主な語句・表現）を vocabulary_explanations_only_all_sections.json に登録する。

区分: 6M1=§1 … 6M4=§4（2024 の 6A/6B 段落コードと衝突しない）
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/honshiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION6_OFFICIAL_SOURCE = "kyotsu2025_section6_official"


def strip_section6_vocab_only(entries):
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        filtered = [
            o
            for o in occs
            if not (
                o.get("section_number") in (6, "6")
                and o.get("source") in VOCAB_ONLY_SOURCES
            )
        ]
        if not filtered:
            continue
        ne = dict(e)
        ne["occurrences"] = filtered
        out.append(ne)
    return out


def drop_previous_section6_official(entries):
    return [
        e
        for e in entries
        if not any(
            o.get("source") == SECTION6_OFFICIAL_SOURCE
            for o in (e.get("occurrences") or [])
        )
    ]


OFFICIAL = [
    # 6M1 §1
    ("6M1", "in name", "〈表現〉名前だけの"),
    ("6M1", "deserve one's title", "〈表現〉自分の肩書きに値する"),
    ("6M1", "serve as ...", "〈表現〉…として務める"),
    ("6M1", "incredibly", "〈副〉信じられないほど；とても"),
    ("6M1", "humanity", "〈名〉人類"),
    ("6M1", "star", "〈動〉主演する"),
    ("6M1", "(be) caught up in ...", "〈表現〉…に没頭［熱中］している"),
    ("6M1", "fame", "〈名〉名声"),
    ("6M1", "fake", "〈形〉にせの"),
    # 6M2 §2
    ("6M2", "reality show", "〈名〉実録番組"),
    ("6M2", "deed", "〈名〉行為"),
    ("6M2", "be supposed to -", "〈表現〉-することになっている"),
    ("6M2", "wander", "〈動〉歩き回る；迷う"),
    ("6M2", "drain", "〈名〉排水溝"),
    ("6M2", "underground", "〈形・副〉地下の；地下へ"),
    ("6M2", "throw open ...", "〈表現〉…を押し開ける"),
    ("6M2", "to one's surprise", "〈表現〉驚いたことに"),
    ("6M2", "out of nowhere", "〈表現〉どこからともなく；いきなり"),
    ("6M2", "identity", "〈名〉正体"),
    ("6M2", "in less than a second", "〈表現〉1秒未満で；またたく間に"),
    ("6M2", "convince O to -", "〈表現〉Oを説得して-させる"),
    ("6M2", "meow", "〈名〉ニャーと鳴く声"),
    ("6M2", "cheer", "〈動〉…に喝采を送る"),
    ("6M2", "onlooker", "〈名〉見物人"),
    ("6M2", "pose for ...", "〈表現〉…のためにポーズをとる"),
    ("6M2", "pop into one's head", "〈表現〉頭に浮かぶ"),
    ("6M2", "celebrity", "〈名〉有名人"),
    ("6M2", "vanish", "〈動〉消え去る"),
    # 6M3 §3
    ("6M3", "ranger", "〈名〉監視員；レンジャー"),
    ("6M3", "in trouble", "〈表現〉困っている"),
    ("6M3", "float", "〈動〉浮かぶ"),
    ("6M3", "flyer", "〈名〉飛行士；パイロット"),
    ("6M3", "extraordinary", "〈形〉驚くべき；並外れた"),
    ("6M3", "let O go", "〈表現〉Oを手離す"),
    ("6M3", "put O to use", "〈表現〉Oを利用する"),
    ("6M3", "locate", "〈動〉…を見つける"),
    ("6M3", "eventually", "〈副〉結局；ついに"),
    ("6M3", "recruit", "〈動〉…を採用する；入隊させる"),
    ("6M3", "upon -ing", "〈表現〉-するとすぐに"),
    # 6M4 §4
    ("6M4", "buzz", "〈動〉ブーンという音を立てる"),
    ("6M4", "notification", "〈名〉通知"),
    ("6M4", "briefly", "〈副〉少しの間"),
    (
        "6M4",
        "On my desk was a note.",
        "〈表現〉机の上には短い手紙があった（倒置：wasの主語は a note）",
    ),
    ("6M4", "proud", "〈形〉誇り高い"),
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
                        "source": SECTION6_OFFICIAL_SOURCE,
                    }
                ],
            }
        )
    return entries


def main():
    data = json.loads(VOCAB_FILE.read_text(encoding="utf-8"))
    old = data.get("entries") or []
    stripped = strip_section6_vocab_only(old)
    stripped = drop_previous_section6_official(stripped)
    official = build_official_entries()

    meta = data.get("meta") or {}
    meta["section6_official"] = {
        "label": "2025本試験 大問6（主な語句・表現・画像準拠）",
        "parts": {"6M1": "§1", "6M2": "§2", "6M3": "§3", "6M4": "§4"},
        "count": len(OFFICIAL),
    }

    data["entries"] = stripped + official
    data.pop("by_section", None)

    VOCAB_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {VOCAB_FILE}")
    print(f"  Section-6 official cards: {len(official)}.")


if __name__ == "__main__":
    main()
