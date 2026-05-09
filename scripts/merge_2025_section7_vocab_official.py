# -*- coding: utf-8 -*-
"""
2025 共通テスト本試験 大問7（主な語句・表現）を vocabulary_explanations_only_all_sections.json に登録する。

区分: 7M1=§1 … 7M7=§7, 7M8=最終段落
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/honshiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION7_OFFICIAL_SOURCE = "kyotsu2025_section7_official"


def strip_section7_vocab_only(entries):
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        filtered = [
            o
            for o in occs
            if not (
                o.get("section_number") in (7, "7")
                and o.get("source") in VOCAB_ONLY_SOURCES
            )
        ]
        if not filtered:
            continue
        ne = dict(e)
        ne["occurrences"] = filtered
        out.append(ne)
    return out


def drop_previous_section7_official(entries):
    return [
        e
        for e in entries
        if not any(
            o.get("source") == SECTION7_OFFICIAL_SOURCE
            for o in (e.get("occurrences") or [])
        )
    ]


OFFICIAL = [
    # 7M1 §1
    ("7M1", "during the day", "〈表現〉日中は；昼の間は"),
    ("7M1", "active", "〈形〉活動的な"),
    ("7M1", "on the other hand", "〈接続〉他方；それに対して"),
    ("7M1", "awake", "〈形〉目が覚めて"),
    # 7M2 §2
    ("7M2", "essential", "〈形〉必要不可欠な"),
    ("7M2", "function", "〈動〉働く；機能する"),
    ("7M2", "efficiently", "〈副〉効率的に"),
    ("7M2", "central nervous system", "〈名〉中枢神経系"),
    ("7M2", "define", "〈動〉…を定義する"),
    ("7M2", "altered state of consciousness", "〈名〉意識変容状態"),
    ("7M2", "characterize", "〈動〉…を特徴づける"),
    ("7M2", "specific", "〈形〉特定の"),
    ("7M2", "position", "〈名〉姿勢"),
    ("7M2", "response", "〈名〉反応"),
    ("7M2", "neuron", "〈名〉神経単位"),
    ("7M2", "energize", "〈動〉…を元気［活気］づける"),
    ("7M2", "differ from species to species", "〈表現〉種によって異なる"),
    # 7M3 §3
    ("7M3", "identify", "〈動〉…を確認する"),
    ("7M3", "monophasic", "〈形〉単相の"),
    ("7M3", "biphasic", "〈形〉2相の"),
    ("7M3", "polyphasic", "〈形〉多相の"),
    ("7M3", "extended period", "〈名〉長期間"),
    ("7M3", "mammal", "〈名〉哺乳動物"),
    ("7M3", "utilize", "〈動〉…を利用する"),
    ("7M3", "nap", "〈名〉うたた寝"),
    # 7M4 §4
    ("7M4", "variation", "〈名〉変化；変種"),
    ("7M4", "depending on ...", "〈表現〉…に応じて"),
    ("7M4", "diet", "〈名〉飲食物"),
    ("7M4", "squirrel", "〈名〉リス"),
    ("7M4", "use up", "〈表現〉使い果たす"),
    ("7M4", "result in ...", "〈表現〉…という結果になる"),
    ("7M4", "carnivorous", "〈形〉肉食性の"),
    ("7M4", "satisfy", "〈動〉…を満たす"),
    ("7M4", "hunger", "〈名〉飢え；空腹感"),
    ("7M4", "herbivore", "〈名〉草食動物"),
    ("7M4", "plant-based", "〈形〉植物ベースの"),
    ("7M4", "relatively", "〈副〉比較的"),
    # 7M5 §5
    ("7M5", "safety", "〈名〉安全"),
    ("7M5", "variable", "〈名〉変数；変化するもの"),
    ("7M5", "alert", "〈形〉警戒［用心］して"),
    ("7M5", "ape", "〈名〉類人猿；サル"),
    ("7M5", "platform", "〈名〉高台"),
    ("7M5", "floor", "〈名〉底；地面"),
    ("7M5", "keep A away from B", "〈表現〉AをBから遠ざけておく"),
    ("7M5", "shelter", "〈名〉避難所；住みか"),
    ("7M5", "predator", "〈名〉捕食動物"),
    ("7M5", "as a result", "〈接続〉その結果"),
    ("7M5", "in contrast", "〈接続〉対照的に"),
    ("7M5", "feel exposed to ...", "〈表現〉…にさらされていると感じる"),
    ("7M5", "contribute to ...", "〈表現〉…の一因となる"),
    # 7M6 §6
    ("7M6", "so far", "〈表現〉これまで"),
    ("7M6", "typical", "〈形〉典型的な"),
    ("7M6", "unihemispheric", "〈形〉単半球の"),
    ("7M6", "keep O open", "〈表現〉Oを開けたままでいる"),
    ("7M6", "surroundings", "〈名〉環境"),
    ("7M6", "revive", "〈動〉…を生き返らせる；回復させる"),
    ("7M6", "watch out for ...", "〈表現〉…を警戒する"),
    ("7M6", "threat", "〈名〉脅威；おびやかすもの"),
    ("7M6", "outer edge", "〈名〉外縁部"),
    ("7M6", "with both eyes closed", "〈表現〉両目を閉じたままで"),
    # 7M7 §7
    ("7M7", "besides", "〈前〉…に加えて"),
    ("7M7", "hibernation", "〈名〉冬眠"),
    ("7M7", "inactive", "〈形〉不活発な"),
    ("7M7", "scarce", "〈形〉乏しい"),
    ("7M7", "heart rate", "〈名〉心拍数"),
    ("7M7", "breathing", "〈名〉呼吸"),
    ("7M7", "jellyfish", "〈名〉クラゲ"),
    ("7M7", "relaxation", "〈名〉くつろぎ；弛緩"),
    ("7M7", "responsive", "〈形〉よく反応する；敏感な"),
    # 7M8 最終段落
    ("7M8", "as shown above", "〈表現〉上に示されたように"),
    ("7M8", "play an important role in ...", "〈表現〉…において重要な役割を果たす"),
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
                        "source": SECTION7_OFFICIAL_SOURCE,
                    }
                ],
            }
        )
    return entries


def main():
    data = json.loads(VOCAB_FILE.read_text(encoding="utf-8"))
    old = data.get("entries") or []
    stripped = strip_section7_vocab_only(old)
    stripped = drop_previous_section7_official(stripped)
    official = build_official_entries()

    meta = data.get("meta") or {}
    meta["section7_official"] = {
        "label": "2025本試験 大問7（主な語句・表現・画像準拠）",
        "parts": {
            "7M1": "§1",
            "7M2": "§2",
            "7M3": "§3",
            "7M4": "§4",
            "7M5": "§5",
            "7M6": "§6",
            "7M7": "§7",
            "7M8": "最終段落",
        },
        "count": len(OFFICIAL),
    }

    data["entries"] = stripped + official
    data.pop("by_section", None)

    VOCAB_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {VOCAB_FILE}")
    print(f"  Section-7 official cards: {len(official)}.")


if __name__ == "__main__":
    main()
