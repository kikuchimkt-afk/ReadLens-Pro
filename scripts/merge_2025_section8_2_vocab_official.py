# -*- coding: utf-8 -*-
"""
2025 共通テスト本試験 大問8（主な語句・表現・8-2相当）を vocabulary_explanations_only_all_sections.json に登録する。

区分: 8N1=エッセイのアウトライン, 8N2=資料A, 8N3=資料B
（8-1の 8M1–6 と併存する。再実行時は kyotsu2025_section8_2_official のみ差し替え）
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/honshiken/vocabulary_explanations_only_all_sections.json"

SECTION8_2_OFFICIAL_SOURCE = "kyotsu2025_section8_2_official"


def drop_previous_section8_2_official(entries):
    return [
        e
        for e in entries
        if not any(
            o.get("source") == SECTION8_2_OFFICIAL_SOURCE
            for o in (e.get("occurrences") or [])
        )
    ]


OFFICIAL = [
    # 8N1 エッセイのアウトライン
    ("8N1", "reconsideration", "〈名〉再考"),
    ("8N1", "without doubt", "〈表現〉疑いなく；確かに"),
    ("8N1", "frontline", "〈名〉最前線"),
    ("8N1", "priority", "〈名〉優先事項"),
    ("8N1", "following", "〈形〉次にあげる"),
    ("8N1", "based on ...", "〈表現〉…に基づいて"),
    ("8N1", "aspect", "〈名〉面；相"),
    ("8N1", "prioritize A over B", "〈表現〉BよりもAを優先させる"),
    # 8N2 資料A
    ("8N2", "connection", "〈名〉関係；関連"),
    ("8N2", "emission", "〈名〉排出（量）"),
    ("8N2", "emit", "〈動〉…を排出する"),
    ("8N2", "(space)craft", "〈名〉宇宙船（複数形も (space)craft）"),
    ("8N2", "insignificant", "〈形〉重要でない；ささいな"),
    ("8N2", "atmosphere", "〈名〉大気（圏）"),
    ("8N2", "damaging", "〈形〉ダメージを与える；有害な"),
    ("8N2", "the contribution to A of B", "〈表現〉BがAの一因となっていること"),
    ("8N2", "greenhouse effect", "〈名〉温室効果"),
    ("8N2", "thermosphere", "〈名〉熱圏"),
    ("8N2", "quantity", "〈名〉量"),
    ("8N2", "debris", "〈名〉破片；残骸"),
    ("8N2", "junk", "〈動〉…を廃棄する"),
    ("8N2", "artificial satellite", "〈名〉人工衛星"),
    ("8N2", "on the rise", "〈表現〉上昇中で"),
    ("8N2", "up to ...", "〈表現〉最大…"),
    ("8N2", "pose a risk to ...", "〈表現〉…に危険をもたらす"),
    ("8N2", "potential", "〈形〉潜在的な"),
    ("8N2", "obstacle", "〈名〉障害物"),
    ("8N2", "astronomical observation", "〈名〉天体観測"),
    # 8N3 資料B
    ("8N3", "costly", "〈形〉費用のかかる"),
    ("8N3", "compare A with B", "〈表現〉AをBと比較する"),
    ("8N3", "annual budget", "〈名〉年間予算"),
    ("8N3", "institution", "〈名〉団体；機関"),
    ("8N3", "investment", "〈名〉投資"),
    ("8N3", "relieve", "〈動〉…を軽減［緩和］する"),
    ("8N3", "hunger", "〈名〉飢餓"),
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
                        "source": SECTION8_2_OFFICIAL_SOURCE,
                    }
                ],
            }
        )
    return entries


def main():
    data = json.loads(VOCAB_FILE.read_text(encoding="utf-8"))
    old = data.get("entries") or []
    stripped = drop_previous_section8_2_official(old)
    official = build_official_entries()

    meta = data.get("meta") or {}
    meta["section8_2_official"] = {
        "label": "2025本試験 大問8（主な語句・表現・8-2画像準拠）",
        "parts": {
            "8N1": "エッセイのアウトライン",
            "8N2": "資料A",
            "8N3": "資料B",
        },
        "count": len(OFFICIAL),
    }

    data["entries"] = stripped + official
    data.pop("by_section", None)

    VOCAB_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {VOCAB_FILE}")
    print(f"  Section-8 (8-2) official cards: {len(official)}.")


if __name__ == "__main__":
    main()
