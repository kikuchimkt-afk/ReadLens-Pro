# -*- coding: utf-8 -*-
"""
2025 共通テスト追試験 大問8（主な語句・表現・8-2画像準拠）を
data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json に登録する。

区分: 8V1=エッセイのアウトライン, 8V2=資料A, 8V3=資料B, 8V4=設問文・選択肢
（本試験の 8N1–3 とは別。positively/positive, extinction/extinct, popular/popularity は1枚ずつ）
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION8_2_OFFICIAL_SOURCE = "kyotsu2025_tsuishiken_section8_2_official"
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
    # 8V1 エッセイのアウトライン
    ("8V1", "positively / positive", "〈副・形〉肯定的に；積極的に／肯定的な；積極的な"),
    ("8V1", "conclusion", "〈名〉結論"),
    ("8V1", "resource", "〈名〉資源；財源"),
    # 8V2 資料A
    ("8V2", "according to ...", "〈表現〉…によると"),
    ("8V2", "publish", "〈動〉…を出版する；発表する"),
    ("8V2", "conservation", "〈名〉保護；保全"),
    ("8V2", "regard A as B", "〈表現〉AをBとみなす"),
    ("8V2", "(be) threatened with ...", "〈表現〉…の危機に瀕している"),
    ("8V2", "extinction / extinct", "〈名・形〉絶滅／絶滅した"),
    ("8V2", "compared to ...", "〈表現〉…と比べて"),
    ("8V2", "approximately", "〈副〉およそ"),
    ("8V2", "prevent O from -ing", "〈表現〉Oが－するのを妨げる"),
    ("8V2", "endangered", "〈形〉絶滅の危機にさらされた"),
    ("8V2", "restore", "〈動〉…を回復する"),
    ("8V2", "method", "〈名〉方法；方式"),
    ("8V2", "adopt", "〈動〉…を採用する"),
    ("8V2", "on-site", "〈形〉現場での"),
    ("8V2", "off-site", "〈形〉現場を離れた"),
    ("8V2", "the former [latter]", "〈表現〉前者［後者］"),
    ("8V2", "preserve", "〈動〉…を保存する"),
    ("8V2", "surroundings", "〈名〉環境"),
    ("8V2", "breed", "〈動〉…を繁殖させる；飼育する"),
    ("8V2", "in captivity", "〈表現〉とらわれの身で；動物園に入れられて"),
    ("8V2", "aim to -", "〈表現〉－しようと試みる"),
    ("8V2", "be involved in ...", "〈表現〉…に参加している［関わっている］"),
    ("8V2", "disappear", "〈動〉姿を消す"),
    ("8V2", "due to ...", "〈表現〉…が原因で"),
    ("8V2", "effort", "〈名〉努力"),
    # 8V3 資料B
    ("8V3", "kid", "〈名〉子ども"),
    ("8V3", "aged X (years)", "〈表現〉X歳の"),
    ("8V3", "check", "〈動〉…にチェックの印をつける"),
    ("8V3", "including", "〈前〉…を含めて"),
    # 8V4 設問文・選択肢
    ("8V4", "rare", "〈形〉珍しい；まれな"),
    ("8V4", "reappear", "〈動〉再び現れる"),
    ("8V4", "fund", "〈動〉…に資金を提供する"),
    ("8V4", "path", "〈名〉（小）道"),
    ("8V4", "thanks to ...", "〈表現〉…のおかげで"),
    ("8V4", "on the rise", "〈表現〉増加している"),
    ("8V4", "broad", "〈形〉広い"),
    ("8V4", "abandoned", "〈形〉捨てられた"),
    ("8V4", "popular / popularity", "〈形・名〉人気のある／人気"),
    ("8V4", "commonly", "〈副〉一般に"),
    ("8V4", "reportedly", "〈副〉伝えられるところによると"),
    ("8V4", "unique", "〈形〉独特の"),
    ("8V4", "a variety of ...", "〈表現〉いろいろの..."),
    ("8V4", "prefer", "〈動〉より好む"),
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
    stripped = strip_section8_vocab_only(old)
    stripped = drop_previous_section8_2_official(stripped)
    official = build_official_entries()

    meta = data.get("meta") or {}
    sis = list(meta.get("sections_in_data") or [])
    if 8 not in sis:
        meta["sections_in_data"] = sorted(set(sis) | {8})

    meta["section8_2_official"] = {
        "label": "2025追試験 大問8（主な語句・表現・8-2画像準拠）",
        "parts": {
            "8V1": "エッセイのアウトライン",
            "8V2": "資料A",
            "8V3": "資料B",
            "8V4": "設問文・選択肢",
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
