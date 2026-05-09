# -*- coding: utf-8 -*-
"""
2025 共通テスト追試験 大問5（主な語句・表現）を
data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json に登録する。

区分: 5M1=記事, 5M2=調査結果（本試験の 5T1–3 とは別物。追試験 JSON 内のみ使用）
既存の section 5／5M1／5M2 かつ語彙シード系、および過去の追試大問5公式を取り除いてから差し替える。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION5_OFFICIAL_SOURCE = "kyotsu2025_tsuishiken_section5_official"
SECTION5_NUMBERS = frozenset({5, "5", "5M1", "5M2", "5m1", "5m2"})


def strip_section5_vocab_only(entries):
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        filtered = [
            o
            for o in occs
            if not (
                o.get("section_number") in SECTION5_NUMBERS
                and o.get("source") in VOCAB_ONLY_SOURCES
            )
        ]
        if not filtered:
            continue
        ne = dict(e)
        ne["occurrences"] = filtered
        out.append(ne)
    return out


def drop_previous_section5_official(entries):
    return [
        e
        for e in entries
        if not any(
            o.get("source") == SECTION5_OFFICIAL_SOURCE
            for o in (e.get("occurrences") or [])
        )
    ]


OFFICIAL = [
    # 5M1 記事
    ("5M1", "upcoming", "〈形〉まもなくやってくる"),
    ("5M1", "festival", "〈名〉催し；祭り；フェスティバル"),
    ("5M1", "a variety of ...", "〈表現〉さまざまな…"),
    ("5M1", "include", "〈動〉…を含む"),
    ("5M1", "workshop", "〈名〉ワークショップ；体験教室"),
    ("5M1", "organizer", "〈名〉主催者"),
    ("5M1", "relate to ...", "〈表現〉…に関係がある；…のことを述べている"),
    ("5M1", "arrange", "〈動〉…を手配［準備］する（≒ organize）"),
    ("5M1", "co-ordinate", "〈動〉…を調整する"),
    ("5M1", "specific", "〈形〉特定の；明確な"),
    ("5M1", "time frame", "〈名〉時間枠；期間"),
    ("5M1", "advertise", "〈動〉…を宣伝する"),
    ("5M1", "allow", "〈動〉〈時間〉を見ておく［見込んでおく］"),
    ("5M1", "actual", "〈形〉実際の"),
    ("5M1", "be superior to ...", "〈表現〉…より優れている"),
    ("5M1", "accessible", "〈形〉行きやすい"),
    ("5M1", "visible", "〈形〉人目に付く；目立つ"),
    ("5M1", "accommodate", "〈動〉…を収容する"),
    ("5M1", "authorities", "〈名〉当局；公共事業機関"),
    ("5M1", "regulations", "〈名〉規則；規定"),
    ("5M1", "trash disposal", "〈名〉ゴミ処理"),
    ("5M1", "medical attention", "〈名〉医療；治療"),
    ("5M1", "handling", "〈名〉取り扱い"),
    ("5M1", "storage", "〈名〉貯蔵"),
    ("5M1", "safety", "〈名〉安全"),
    ("5M1", "require", "〈動〉…を要求する"),
    ("5M1", "label", "〈名〉ラベル"),
    ("5M1", "allergy", "〈名〉アレルギー"),
    ("5M1", "make sure (that) ...", "〈表現〉…を確かめる［確実にする］"),
    ("5M1", "last", "〈動〉続く"),
    ("5M1", "untidy", "〈形〉乱雑な"),
    ("5M1", "properly", "〈副〉きちんと"),
    ("5M1", "afterward", "〈副〉その後で"),
    ("5M1", "essential", "〈形〉必要不可欠な"),
    ("5M1", "guarantee", "〈動〉…を保証する"),
    ("5M1", "successful", "〈形〉成功した"),
    ("5M1", "vital", "〈形〉きわめて重要な"),
    ("5M1", "secret ingredient", "〈名〉秘密の材料；隠し味"),
    ("5M1", "positive", "〈形〉肯定的な；前向きの"),
    # 5M2 調査結果
    ("5M2", "attend", "〈動〉出席する；通う；行く"),
    ("5M2", "baked goods", "〈名〉焼き菓子"),
    ("5M2", "flower arrangement", "〈名〉生け花"),
    ("5M2", "respondent", "〈名〉回答者"),
    ("5M2", "multiple", "〈形〉多数の"),
    ("5M2", "how about ...?", "〈表現〉…はいかがですか〈提案〉"),
    (
        "5M2",
        "animals for children to play with",
        "〈名〉子どもが一緒に遊べる動物",
    ),
    ("5M2", "florist", "〈名〉花屋"),
    ("5M2", "look forward to ...", "〈表現〉…を楽しみに待つ"),
    ("5M2", "be made of ...", "〈表現〉…で作られて［できて］いる"),
    ("5M2", "crowded", "〈形〉混み合った"),
    ("5M2", "vending machine", "〈名〉自動販売機"),
    ("5M2", "out of ...", "〈表現〉…がなくなって"),
    ("5M2", "provide", "〈動〉…を供給する"),
    ("5M2", "uneven", "〈形〉でこぼこの"),
    ("5M2", "twist", "〈動〉…をひねる；くじく"),
    ("5M2", "thankfully", "〈副〉ありがたいことに"),
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
                        "source": SECTION5_OFFICIAL_SOURCE,
                    }
                ],
            }
        )
    return entries


def main():
    data = json.loads(VOCAB_FILE.read_text(encoding="utf-8"))
    old = data.get("entries") or []
    stripped = strip_section5_vocab_only(old)
    stripped = drop_previous_section5_official(stripped)
    official = build_official_entries()

    meta = data.get("meta") or {}
    meta["section5_official"] = {
        "label": "2025追試験 大問5（主な語句・表現・画像準拠）",
        "parts": {
            "5M1": "記事",
            "5M2": "調査結果",
        },
        "count": len(OFFICIAL),
    }

    data["entries"] = stripped + official
    data.pop("by_section", None)

    VOCAB_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {VOCAB_FILE}")
    print(f"  Section-5 official cards: {len(official)}.")


if __name__ == "__main__":
    main()
