# -*- coding: utf-8 -*-
"""
2025 共通テスト本試験 大問8（語彙リスト8-1相当）を vocabulary_explanations_only_all_sections.json に登録する。

区分: 8M1=Apu, 8M2=Christine, 8M3=Meilin, 8M4=中盤（画像2・上段）, 8M5=Naomi, 8M6=Victor
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/honshiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION8_OFFICIAL_SOURCE = "kyotsu2025_section8_1_official"


def strip_section8_vocab_only(entries):
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        filtered = [
            o
            for o in occs
            if not (
                o.get("section_number") in (8, "8")
                and o.get("source") in VOCAB_ONLY_SOURCES
            )
        ]
        if not filtered:
            continue
        ne = dict(e)
        ne["occurrences"] = filtered
        out.append(ne)
    return out


def drop_previous_section8_official(entries):
    return [
        e
        for e in entries
        if not any(
            o.get("source") == SECTION8_OFFICIAL_SOURCE
            for o in (e.get("occurrences") or [])
        )
    ]


OFFICIAL = [
    # 8M1 Apu
    ("8M1", "exploration / explore", "〈名・動〉探検；…を探検する"),
    ("8M1", "require", "〈動〉…を必要とする"),
    ("8M1", "lead to ...", "〈表現〉…につながる；…をもたらす"),
    ("8M1", "invention", "〈名〉発明（品）"),
    ("8M1", "boost", "〈動〉…を高める；増やす"),
    ("8M1", "humanity", "〈名〉人類"),
    ("8M1", "surgery", "〈名〉外科手術"),
    ("8M1", "solar cell", "〈名〉太陽電池"),
    ("8M1", "come out of ...", "〈表現〉…から生じる"),
    # 8M2 Christine
    ("8M2", "CEO", "〈名〉最高経営責任者（chief executive officer）"),
    ("8M2", "rely on ...", "〈表現〉…に依存する"),
    ("8M2", "cooperation", "〈名〉協力"),
    ("8M2", "launch", "〈動・名〉（…を）打ち上げ（る）"),
    ("8M2", "costs involved", "〈名〉必要となる費用"),
    ("8M2", "prestige", "〈名〉威信"),
    ("8M2", "commercial", "〈形〉商業的な"),
    ("8M2", "corporation", "〈名〉法人；大企業"),
    ("8M2", "colonize / colonization", "〈動・名〉移民する；植民地を建設する／植民地化"),
    ("8M2", "Mars", "〈名〉火星"),
    ("8M2", "financial", "〈形〉財政的な"),
    ("8M2", "improper", "〈形〉不適切な"),
    ("8M2", "military", "〈形〉軍事的な"),
    ("8M2", "outer space", "〈名〉大気圏外空間"),
    # 8M3 Meilin
    ("8M3", "physicist", "〈名〉物理学者"),
    ("8M3", "broadcast", "〈動〉…を放送する"),
    # 8M4 中盤（画像2・冒頭〜aggressive）
    ("8M4", "existence", "〈名〉存在"),
    ("8M4", "intelligent", "〈形〉知能の高い"),
    ("8M4", "alien", "〈名・形〉異星人（の）"),
    ("8M4", "anything like ...", "〈表現〉いくらかでも…のような"),
    ("8M4", "conquer", "〈動〉…を征服する"),
    ("8M4", "threat", "〈名〉脅威"),
    ("8M4", "(be) associated with ...", "〈表現〉…と関連づけられる"),
    ("8M4", "likelihood", "〈名〉可能性"),
    ("8M4", "aggressive", "〈形〉攻撃的な"),
    # 8M5 Naomi
    ("8M5", "likely", "〈副〉たぶん"),
    ("8M5", "if not ...", "〈表現〉…ではないにしても"),
    ("8M5", "... or so", "〈表現〉…かそこら"),
    ("8M5", "oxygen", "〈名〉酸素"),
    ("8M5", "survival", "〈名〉生存"),
    ("8M5", "astronaut", "〈名〉宇宙飛行士"),
    ("8M5", "fatality rate", "〈名〉死亡率"),
    ("8M5", "tolerate", "〈動〉大目に見る；我慢する"),
    # 8M6 Victor
    ("8M6", "analyst", "〈名〉分析者；アナリスト"),
    ("8M6", "contribute (A) to B", "〈表現〉（Aの分だけ）Bに貢献する"),
    ("8M6", "provide A for B", "〈表現〉AをBに供給する"),
    ("8M6", "estimate", "〈動〉…を見積もる"),
    ("8M6", "billion", "〈名〉10億"),
    ("8M6", "ensure", "〈動〉…を確実にする；保証する"),
    ("8M6", "private firm", "〈名〉民間会社［企業］"),
    ("8M6", "mining", "〈名〉採鉱；鉱業"),
    ("8M6", "militarization", "〈名〉軍事化"),
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
                        "source": SECTION8_OFFICIAL_SOURCE,
                    }
                ],
            }
        )
    return entries


def main():
    data = json.loads(VOCAB_FILE.read_text(encoding="utf-8"))
    old = data.get("entries") or []
    stripped = strip_section8_vocab_only(old)
    stripped = drop_previous_section8_official(stripped)
    official = build_official_entries()

    meta = data.get("meta") or {}
    meta["section8_1_official"] = {
        "label": "2025本試験 大問8（主な語句・表現・8-1画像準拠）",
        "parts": {
            "8M1": "Apu",
            "8M2": "Christine",
            "8M3": "Meilin",
            "8M4": "中盤",
            "8M5": "Naomi",
            "8M6": "Victor",
        },
        "count": len(OFFICIAL),
    }

    data["entries"] = stripped + official
    data.pop("by_section", None)

    VOCAB_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {VOCAB_FILE}")
    print(f"  Section-8 (8-1) official cards: {len(official)}.")


if __name__ == "__main__":
    main()
