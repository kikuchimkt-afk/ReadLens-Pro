# -*- coding: utf-8 -*-
"""
2025 共通テスト追試験 大問6（主な語句・表現）を
data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json に登録する。

区分: 6N1=物語, 6N2=ワークシート, 6N3=設問文・選択肢
（本試験の 6M1–4=§ とは別。追試験 JSON 内のみ）
既存の section 6／6N1／6N2／6N3 かつ語彙シード系、および過去の追試大問6公式を取り除いてから差し替える。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION6_OFFICIAL_SOURCE = "kyotsu2025_tsuishiken_section6_official"
SECTION6_NUMBERS = frozenset(
    {6, "6", "6N1", "6N2", "6N3", "6n1", "6n2", "6n3"}
)


def strip_section6_vocab_only(entries):
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        filtered = [
            o
            for o in occs
            if not (
                o.get("section_number") in SECTION6_NUMBERS
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
    # 6N1 物語
    ("6N1", "adventure", "〈名〉冒険"),
    ("6N1", "by oneself", "〈表現〉自分１人で"),
    ("6N1", "nervous", "〈形〉不安で；緊張して"),
    ("6N1", "favorite", "〈形〉お気に入りの"),
    ("6N1", "cookie", "〈名〉クッキー"),
    ("6N1", "accompany", "〈動〉…に付き添う"),
    ("6N1", "make sure (that) ...", "〈表現〉…を確かめる"),
    ("6N1", "stranger", "〈名〉見知らぬ人"),
    ("6N1", "flash by", "〈表現〉さっと過ぎる"),
    ("6N1", "suburban", "〈形〉郊外の"),
    ("6N1", "rice field", "〈名〉水田；稲田"),
    ("6N1", "take over", "〈表現〉引き継ぐ；優勢になる"),
    ("6N1", "passenger", "〈名〉乗客"),
    ("6N1", "middle-aged", "〈形〉中年の"),
    ("6N1", "aisle seat", "〈名〉通路側の座席"),
    ("6N1", "occupy", "〈動〉…を使う；占める"),
    ("6N1", "retreat", "〈動〉撤退する"),
    ("6N1", "armrest", "〈名〉肘掛け"),
    ("6N1", "shift", "〈動〉…を移動させる"),
    ("6N1", "nod", "〈動〉うなずく"),
    ("6N1", "in reply", "〈表現〉返事として"),
    ("6N1", "respond", "〈動〉返答する"),
    ("6N1", "be cautious of ...", "〈表現〉…に用心する"),
    ("6N1", "widen", "〈動〉大きく開く"),
    ("6N1", "dig around", "〈表現〉手を入れて探す"),
    ("6N1", "fancy", "〈形〉高級な"),
    (
        "6N1",
        "tempt O to -",
        "〈表現〉Oを（誘惑して）-する気にさせる",
    ),
    ("6N1", "go against ...", "〈表現〉…に従わない"),
    ("6N1", "refuse", "〈動〉断る"),
    (
        "6N1",
        "ma'am",
        "〈名〉奥様〈年上の女性へのていねいな呼びかけ語〉",
    ),
    ("6N1", "shy", "〈形〉恥ずかしがりの"),
    ("6N1", "help oneself", "〈表現〉遠慮なく取る"),
    ("6N1", "breathe in", "〈表現〉息を吸い込む"),
    ("6N1", "thank you for asking", "〈表現〉お気遣いありがとう"),
    ("6N1", "silence", "〈名〉沈黙"),
    ("6N1", "tap", "〈動〉軽くたたく"),
    ("6N1", "tension", "〈名〉緊張状態"),
    ("6N1", "ease", "〈動〉和らぐ"),
    ("6N1", "announcement", "〈名〉案内；アナウンス"),
    ("6N1", "pull into the station", "〈表現〉駅に着く"),
    ("6N1", "How about that!", "〈表現〉驚いた！"),
    ("6N1", "hurriedly", "〈副〉大急ぎで"),
    ("6N1", "for a little bit", "〈表現〉少しの時間"),
    ("6N1", "interfere with ...", "〈表現〉…を妨害する"),
    ("6N1", "reunion", "〈名〉再会"),
    ("6N1", "rush", "〈動〉急いで行く"),
    ("6N1", "pleasure", "〈名〉喜び；楽しさ"),
    ("6N1", "impressed", "〈形〉感動して"),
    # 6N2 ワークシート
    ("6N2", "sentiment", "〈名〉感情"),
    ("6N2", "emerge", "〈動〉現れる"),
    ("6N2", "characteristic", "〈名〉特徴"),
    # 6N3 設問文・選択肢
    ("6N3", "reject", "〈動〉…を拒絶する"),
    ("6N3", "connection", "〈名〉つながり"),
    ("6N3", "frustration", "〈名〉失望；欲求不満"),
    ("6N3", "interest", "〈名〉興味；関心"),
    ("6N3", "awkward", "〈形〉落ち着かない；気まずい"),
    ("6N3", "thoughtfulness", "〈名〉思いやり"),
    ("6N3", "generous", "〈形〉気前のよい"),
    ("6N3", "harm", "〈名〉害"),
    ("6N3", "carelessly", "〈副〉不注意に"),
    ("6N3", "aggressive", "〈形〉攻撃的な"),
    ("6N3", "intelligent", "〈形〉知的な；聡明な"),
    ("6N3", "behave", "〈動〉振る舞う"),
    ("6N3", "maturely", "〈副〉大人のように"),
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
        "label": "2025追試験 大問6（主な語句・表現・画像準拠）",
        "parts": {
            "6N1": "物語",
            "6N2": "ワークシート",
            "6N3": "設問文・選択肢",
        },
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
