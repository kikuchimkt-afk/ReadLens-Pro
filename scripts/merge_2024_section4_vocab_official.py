# -*- coding: utf-8 -*-
"""2024 共通テスト本試験 大問4 公式単語リストを vocabulary_explanations_only_all_sections.json に反映する。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2024/honshiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})


def parse_section_order(value):
    raw = str(value or "").strip()
    import re

    m = re.match(r"^(\d+)([A-Za-z]*)$", raw)
    if not m:
        return (2**31, raw.upper(), raw)
    return (int(m.group(1)), (m.group(2) or "").upper(), raw)


def sort_key_occ(occ):
    a = parse_section_order(occ.get("section_number"))
    an = str(occ.get("answer_number") or "")
    return (a[0], a[1], an)


def strip_section4_vocab_only(entries):
    """大問4かつ語彙シード系のみの occurrence を除去。occurrences が空になったエントリは削除。"""
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


# 画像リスト（2024 大問4）— 出現順: 4A リード → 4B 記事 → 4C アンケート → 4D 資料
OFFICIAL = [
    # 4A リード文
    ("4A", "based on ...", "〈表現〉…に基づいて"),
    ("4A", "following", "〈形〉次に来る；下記の"),
    ("4A", "questionnaire", "〈名〉アンケート"),
    ("4A", "handout", "〈名〉プリント；資料"),
    # 4B 記事
    ("4B", "framework", "〈名〉枠組み；フレームワーク"),
    ("4B", "aspect", "〈名〉側面"),
    ("4B", "complexity", "〈名〉複雑さ"),
    ("4B", "have to do with ...", "〈表現〉…と関係がある"),
    ("4B", "furnishings", "〈名〉備え付け家具；備品"),
    ("4B", "uninteresting", "〈形〉面白くない；退屈な"),
    ("4B", "on the other hand", "〈接続〉他方；それに対して"),
    ("4B", "in addition", "〈接続〉加えて；さらに"),
    ("4B", "visually", "〈副〉視覚的に"),
    ("4B", "distracting", "〈形〉気を散らせる"),
    ("4B", "display", "〈動〉…を展示［掲示］する"),
    ("4B", "item", "〈名〉項目；事項"),
    ("4B", "consideration", "〈名〉考慮すべきこと"),
    ("4B", "ownership", "〈名〉所有（者であること）；オーナーシップ"),
    ("4B", "flexibility", "〈名〉柔軟性；フレキシビリティ"),
    ("4B", "refer to ...", "〈表現〉…のことを言う；…を表す［示す］"),
    ("4B", "personalized", "〈形〉個人向けにした"),
    ("4B", "suitable", "〈形〉適した"),
    ("4B", "storage space", "〈名〉収納スペース"),
    ("4B", "allow for ...", "〈表現〉…を考慮に入れる；…を可能にさせる"),
    ("4B", "relate to ...", "〈表現〉…に関係がある"),
    ("4B", "quality", "〈名〉質"),
    ("4B", "quantity", "〈名〉量"),
    ("4B", "artificial", "〈形〉人工の"),
    ("4B", "temperature", "〈名〉温度"),
    ("4B", "have difficulty -ing", "〈表現〉－するのに苦労する"),
    ("4B", "lack", "〈名〉不足；欠乏"),
    ("4B", "promote", "〈動〉…を促進する"),
    ("4B", "effective", "〈形〉効果的な"),
    ("4B", "install", "〈動〉…を取り付ける"),
    ("4B", "adjustment", "〈名〉調節"),
    ("4B", "be familiar to ...", "〈表現〉…に馴染みがある"),
    ("4B", "priority", "〈名〉優先事項"),
    ("4B", "component", "〈名〉（構成）要素"),
    ("4B", "equally", "〈副〉同様に"),
    ("4B", "hopefully", "〈副〉願わくば；できれば"),
    # 4C アンケートの結果
    ("4C", "match", "〈動〉…と合う"),
    ("4C", "chat", "〈動〉おしゃべりする"),
    ("4C", "check out", "〈表現〉（本を）借りる"),
    ("4C", "respondent", "〈名〉回答者"),
    ("4C", "current", "〈形〉現在の"),
    ("4C", "disorganized", "〈形〉乱雑な"),
    ("4C", "uncomfortable", "〈形〉心地よくない"),
    ("4C", "hardly ever", "〈表現〉めったに…しない"),
    ("4C", "available", "〈形〉利用可能な"),
    ("4C", "phrase", "〈名〉言い回し；表現"),
    # 4D 資料
    ("4D", "improvement", "〈名〉改善"),
    ("4D", "recommendation", "〈名〉勧め；提案"),
    ("4D", "cover A with B", "〈表現〉AをBでおおう"),
    ("4D", "rug", "〈名〉じゅうたん"),
    ("4D", "replace", "〈動〉…を取り替える"),
    ("4D", "place", "〈動〉…を置く"),
    ("4D", "issue", "〈名〉問題"),
    ("4D", "majority", "〈名〉大多数"),
    ("4D", "mention", "〈動〉…を話に出す；…に触れる"),
    ("4D", "motivate O to -", "〈表現〉Oを励まして－させる"),
    ("4D", "location", "〈名〉位置；所在地"),
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
                        "source": "kyotsu2024_section4_official",
                    }
                ],
            }
        )
    return entries


def main():
    data = json.loads(VOCAB_FILE.read_text(encoding="utf-8"))
    old_entries = data.get("entries") or []
    stripped = strip_section4_vocab_only(old_entries)
    official_keys = {t[1].strip().lower() for t in OFFICIAL}
    stripped = [
        e
        for e in stripped
        if e.get("term_en", "").strip().lower() not in official_keys
    ]
    official = build_official_entries()

    meta = data.get("meta") or {}
    meta["section4_official"] = {
        "label": "2024本試験 大問4（画像・出題局語彙リストに準拠）",
        "parts": {
            "4A": "リード文",
            "4B": "記事",
            "4C": "アンケートの結果",
            "4D": "資料",
        },
        "count": len(OFFICIAL),
    }

    data["entries"] = stripped + official
    # 旧生成物のインデックス（entries と重複することがあり、アプリは entries のみ参照）
    data.pop("by_section", None)
    VOCAB_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {VOCAB_FILE}")
    print(f"  Removed section-4 vocab-only occs from old entries; appended {len(official)} official cards.")


if __name__ == "__main__":
    main()
