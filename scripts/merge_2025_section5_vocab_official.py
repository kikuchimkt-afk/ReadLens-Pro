# -*- coding: utf-8 -*-
"""
2025 共通テスト本試験 大問5（主な語句・表現）を vocabulary_explanations_only_all_sections.json に登録する。

区分: 5T1=リード文, 5T2=「あなた」のメール, 5T3=ライアン教授のメール
（2024 の 5A–5G / § 表記と衝突しないよう T1–T3 を使用）
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/honshiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION5_OFFICIAL_SOURCE = "kyotsu2025_section5_official"


def strip_section5_vocab_only(entries):
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        filtered = [
            o
            for o in occs
            if not (
                o.get("section_number") in (5, "5")
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
    # 5T1 リード文
    ("5T1", "organize", "〈動〉…を準備［計画］する"),
    ("5T1", "conference", "〈名〉会議"),
    ("5T1", "charge", "〈名〉責任；管理"),
    # 5T2 「あなた」のメール
    ("5T2", "representative", "〈名〉代表"),
    ("5T2", "promote", "〈動〉…を促進する"),
    ("5T2", "civil servant", "〈名〉公務員"),
    ("5T2", "division", "〈名〉部局；課"),
    ("5T2", "opening [closing] address", "〈名〉開会［閉会］の辞"),
    ("5T2", "break", "〈名〉休憩"),
    ("5T2", "preserve", "〈動〉…を保存する"),
    ("5T2", "hand down A to B", "〈表現〉AをBに伝える"),
    ("5T2", "craftsmanship", "〈名〉職人の技能"),
    ("5T2", "moderator", "〈名〉司会者"),
    ("5T2", "conservation", "〈名〉保存"),
    ("5T2", "mayor", "〈名〉市長"),
    ("5T2", "confirm", "〈動〉確認する"),
    ("5T2", "following", "〈形〉次の"),
    ("5T2", "registration", "〈名〉登録"),
    ("5T2", "seven days before ...", "〈表現〉…の7日前に"),
    ("5T2", "participant", "〈名〉参加者"),
    ("5T2", "Below is ...", "〈表現〉下にあるのは…だ"),
    ("5T2", "cafeteria", "〈名〉食堂"),
    ("5T2", "reception", "〈名〉もてなし；歓迎会"),
    ("5T2", "remaining", "〈形〉残りの"),
    ("5T2", "set", "〈動〉…を設定する；決める"),
    ("5T2", "look forward to -ing", "〈表現〉-するのを楽しみに待つ"),
    ("5T2", "With regards", "〈表現〉かしこ；敬具；よろしく"),
    # 5T3 ライアン教授のメール
    ("5T3", "draft", "〈名〉草案"),
    ("5T3", "venue", "〈名〉開催地"),
    ("5T3", "capacity", "〈名〉収容能力"),
    ("5T3", "reserve", "〈動〉…を予約する；取っておく"),
    ("5T3", "for free", "〈表現〉無料で"),
    ("5T3", "parking lot", "〈名〉駐車場"),
    ("5T3", "permit", "〈名〉許可証"),
    ("5T3", "with regard to ...", "〈表現〉…に関して"),
    ("5T3", "recipe", "〈名〉調理法"),
    ("5T3", "update", "〈動〉…を更新する"),
    ("5T3", "details", "〈名〉詳細な情報"),
    ("5T3", "as for ...", "〈表現〉…については"),
    ("5T3", "rethink", "〈動〉…を再考する"),
    ("5T3", "attach", "〈動〉…を添付する"),
    ("5T3", "attachment", "〈名〉添付ファイル"),
    ("5T3", "diagram", "〈名〉図"),
    ("5T3", "seating arrangements", "〈名〉座席配置"),
    ("5T3", "face inward", "〈表現〉内側を向く"),
    ("5T3", "set up", "〈表現〉設置する；設置（名）"),
    ("5T3", "assistance", "〈名〉援助"),
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
        "label": "2025本試験 大問5（主な語句・表現・画像準拠）",
        "parts": {
            "5T1": "リード文",
            "5T2": "「あなた」のメール",
            "5T3": "ライアン教授のメール",
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
