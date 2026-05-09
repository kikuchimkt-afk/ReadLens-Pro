# -*- coding: utf-8 -*-
"""
2025 共通テスト追試験 大問8（主な語句・表現・8-1画像準拠）を
data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json に登録する。

区分: 8U1=冒頭, 8U2=ステップ1・Aya, 8U3=ステップ1・David, 8U4=Indira, 8U5=Kenyatta,
      8U6=Yo, 8U7=設問文・選択肢, 8U8=ステップ2
（本試験の 8M / 8N とは別。economically/economic, potential/potentially, leap/jumping, actively/active は1枚ずつ）
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION8_1_OFFICIAL_SOURCE = "kyotsu2025_tsuishiken_section8_1_official"
SECTION8_NUMBERS = frozenset(
    {8, "8"}
    | {f"8U{i}" for i in range(1, 9)}
    | {f"8u{i}" for i in range(1, 9)}
    | {f"8V{i}" for i in range(1, 5)}
    | {f"8v{i}" for i in range(1, 5)}
)


def strip_section8_vocab_only(entries):
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        filtered = [
            o
            for o in occs
            if not (
                o.get("section_number") in SECTION8_NUMBERS
                and o.get("source") in VOCAB_ONLY_SOURCES
            )
        ]
        if not filtered:
            continue
        ne = dict(e)
        ne["occurrences"] = filtered
        out.append(ne)
    return out


def drop_previous_section8_1_official(entries):
    return [
        e
        for e in entries
        if not any(
            o.get("source") == SECTION8_1_OFFICIAL_SOURCE
            for o in (e.get("occurrences") or [])
        )
    ]


OFFICIAL = [
    # 8U1 冒頭（画像2・継続）
    ("8U1", "pose", "〈動〉…を引き起こす"),
    ("8U1", "citizen", "〈名〉国民；市民"),
    ("8U1", "safety", "〈名〉安全"),
    # 8U2 ステップ1・Aya
    ("8U2", "advisor", "〈名〉顧問"),
    ("8U2", "in terms of ...", "〈表現〉…の点で"),
    ("8U2", "be unusual in that ...", "〈表現〉…という点で珍しい"),
    ("8U2", "in principle", "〈表現〉原則的に"),
    ("8U2", "apart from ...", "〈表現〉…は別にして"),
    ("8U2", "nevertheless", "〈副〉それにもかかわらず"),
    ("8U2", "boost", "〈動〉…を増大させる"),
    ("8U2", "purchase", "〈動〉…を購入する"),
    ("8U2", "employ", "〈動〉…を雇う"),
    ("8U2", "infrastructure", "〈名〉インフラ"),
    ("8U2", "medical", "〈形〉医療の"),
    ("8U2", "benefit", "〈名〉利益；恩恵"),
    ("8U2", "provide", "〈動〉…を提供する；もたらす"),
    ("8U2", "include", "〈動〉…を含む"),
    ("8U2", "collaborate with A on B", "〈表現〉BをAと共同で行う"),
    # 8U3 ステップ1・David
    ("8U3", "urban", "〈形〉都市の"),
    ("8U3", "planner", "〈名〉設計家"),
    ("8U3", "located", "〈形〉位置して；存在して"),
    ("8U3", "ensure (that) ...", "〈表現〉確実に…するようにする"),
    ("8U3", "economically / economic", "〈副・形〉経済的に／経済的な"),
    ("8U3", "viable", "〈形〉実行できる"),
    ("8U3", "man-eating", "〈形〉人喰いの"),
    ("8U3", "a sea of ...", "〈表現〉たくさんの…"),
    ("8U3", "huge", "〈形〉巨大な"),
    ("8U3", "risk", "〈名〉危険；リスク"),
    ("8U3", "bear", "〈名〉クマ"),
    ("8U3", "escape", "〈動〉逃げる"),
    ("8U3", "flooding", "〈名〉洪水"),
    # 8U4 Indira
    ("8U4", "prison", "〈名〉刑務所；監獄"),
    ("8U4", "imagine", "〈動〉…を想像する"),
    ("8U4", "cheetah", "〈名〉チータ"),
    ("8U4", "used to -ing", "〈表現〉-することに慣れている"),
    ("8U4", "distance", "〈名〉距離"),
    ("8U4", "lock up", "〈表現〉閉じ込める"),
    ("8U4", "for the rest of one's life", "〈表現〉その後死ぬまで"),
    ("8U4", "relatively", "〈副〉比較的"),
    ("8U4", "stimulation", "〈名〉刺激"),
    ("8U4", "noisy", "〈形〉騒がしい"),
    ("8U4", "expose A to B", "〈表現〉AをBにさらす"),
    ("8U4", "cruel", "〈形〉残酷な"),
    ("8U4", "treatment", "〈名〉扱い"),
    # 8U5 Kenyatta
    ("8U5", "perform", "〈動〉…を行う；果たす"),
    ("8U5", "relation", "〈名〉関係"),
    ("8U5", "politics", "〈名〉政治"),
    ("8U5", "whereby", "〈副〉それによって…"),
    ("8U5", "loan", "〈動〉…を貸し出す"),
    ("8U5", "deal", "〈名〉取引"),
    ("8U5", "be symbolic of ...", "〈表現〉…を象徴する"),
    ("8U5", "in demand", "〈表現〉需要がある"),
    ("8U5", "temporarily", "〈副〉一時的に"),
    ("8U5", "swap", "〈動〉交換する"),
    ("8U5", "treaty", "〈名〉条約；協定"),
    ("8U5", "painting", "〈名〉絵"),
    ("8U5", "promote", "〈動〉…を促進する"),
    ("8U5", "mutual", "〈形〉相互の"),
    ("8U5", "flow", "〈名〉流れ"),
    ("8U5", "zoological", "〈形〉動物学上の"),
    ("8U5", "improve", "〈動〉…を改善する"),
    ("8U5", "global", "〈形〉全世界の"),
    ("8U5", "connectivity", "〈名〉接続性"),
    # 8U6 Yo
    ("8U6", "pandemic", "〈名〉世界的な流行病；パンデミック"),
    ("8U6", "migration", "〈名〉移住；移動"),
    ("8U6", "virus", "〈名〉ウイルス"),
    ("8U6", "so-called", "〈形〉いわゆる"),
    ("8U6", "live", "〈形〉生きている"),
    ("8U6", "potential / potentially", "〈形・副〉潜在的な／潜在的に"),
    ("8U6", "source", "〈名〉源"),
    ("8U6", "given", "〈前〉…を考慮に入れると"),
    ("8U6", "disruption", "〈名〉混乱；中断"),
    ("8U6", "bring about ...", "〈表現〉…をもたらす"),
    ("8U6", "guarantee", "〈動〉…を保証する"),
    ("8U6", "proper", "〈形〉適切な"),
    ("8U6", "procedure", "〈名〉方法；手順"),
    ("8U6", "leap / jumping", "〈名〉跳躍；ジャンプ"),
    ("8U6", "species", "〈名〉（分類上の）種"),
    ("8U6", "occur", "〈動〉起こる"),
    # 8U7 設問文・選択肢
    ("8U7", "summarize", "〈動〉…を要約する"),
    ("8U7", "mistreatment", "〈名〉不当な扱い；虐待"),
    ("8U7", "observation", "〈名〉観察"),
    ("8U7", "suffering", "〈名〉苦しむこと"),
    ("8U7", "infectious", "〈形〉感染性の"),
    ("8U7", "harm", "〈名〉害"),
    ("8U7", "protect", "〈動〉…を保護する"),
    # 8U8 ステップ2
    ("8U8", "actively / active", "〈副・形〉積極的に／積極的な"),
    ("8U8", "maintain", "〈動〉…を維持する"),
    ("8U8", "welfare", "〈名〉幸福"),
    ("8U8", "priority", "〈名〉優先事項"),
    ("8U8", "knowledge", "〈名〉知識"),
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
                        "source": SECTION8_1_OFFICIAL_SOURCE,
                    }
                ],
            }
        )
    return entries


def main():
    data = json.loads(VOCAB_FILE.read_text(encoding="utf-8"))
    old = data.get("entries") or []
    stripped = strip_section8_vocab_only(old)
    stripped = drop_previous_section8_1_official(stripped)
    official = build_official_entries()

    meta = data.get("meta") or {}
    sis = list(meta.get("sections_in_data") or [])
    if 8 not in sis:
        meta["sections_in_data"] = sorted(set(sis) | {8})

    meta["section8_1_official"] = {
        "label": "2025追試験 大問8（主な語句・表現・8-1画像準拠）",
        "parts": {
            "8U1": "冒頭",
            "8U2": "ステップ1・Aya",
            "8U3": "ステップ1・David",
            "8U4": "Indira",
            "8U5": "Kenyatta",
            "8U6": "Yo",
            "8U7": "設問文・選択肢",
            "8U8": "ステップ2",
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
