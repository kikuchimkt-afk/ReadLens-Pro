# -*- coding: utf-8 -*-
"""
2025 共通テスト追試験 大問7（主な語句・表現）を
data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json に登録する。

区分: 7P1=第1段落 … 7P7=最終段落, 7P8=発表のアウトライン, 7P9=設問文・選択肢
（本試験の 7M1–8 とは別。追試験 JSON 内のみ）
soap/soapy・filter/filtration は公式に合わせ1枚ずつ。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2025/tsuishiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION7_OFFICIAL_SOURCE = "kyotsu2025_tsuishiken_section7_official"
SECTION7_NUMBERS = frozenset(
    {7, "7"}
    | {f"7P{i}" for i in range(1, 10)}
    | {f"7p{i}" for i in range(1, 10)}
)


def strip_section7_vocab_only(entries):
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        filtered = [
            o
            for o in occs
            if not (
                o.get("section_number") in SECTION7_NUMBERS
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
    # 7P1 第1段落
    ("7P1", "flow", "〈動〉流れる"),
    ("7P1", "pipe", "〈名〉管；パイプ"),
    ("7P1", "bathing", "〈名〉水浴び；入浴"),
    ("7P1", "liquid", "〈名〉液体"),
    ("7P1", "distinct", "〈形〉はっきりわかる"),
    ("7P1", "makeup", "〈名〉構造；構成"),
    # 7P2 第2段落
    ("7P2", "in the form of ...", "〈表現〉…の形をして；…状の"),
    ("7P2", "absorb", "〈動〉…を吸収する"),
    ("7P2", "calcium", "〈名〉カルシウム"),
    ("7P2", "magnesium", "〈名〉マグネシウム"),
    ("7P2", "according to ...", "〈表現〉…によると"),
    ("7P2", "contain", "〈動〉…を含む"),
    ("7P2", "milligram", "〈名〉ミリグラム"),
    ("7P2", "mineral", "〈名〉鉱物；ミネラル"),
    ("7P2", "per liter", "〈表現〉1リットルにつき"),
    ("7P2", "further", "〈副〉それ以上に"),
    ("7P2", "subdivide", "〈動〉…を細分化する"),
    ("7P2", "moderately", "〈副〉適度に"),
    ("7P2", "classify A as B", "〈表現〉AをBとして分類する"),
    ("7P2", "in contrast", "〈表現〉対照的に"),
    ("7P2", "content", "〈名〉含有量"),
    ("7P2", "vary", "〈動〉異なる；変化する"),
    ("7P2", "location", "〈名〉場所"),
    ("7P2", "compare A with B", "〈表現〉AをBと比較する"),
    ("7P2", "determine", "〈動〉…を特定［確定］する"),
    ("7P2", "on the ... side", "〈表現〉多少…気味で"),
    ("7P2", "whereas", "〈接〉…だが一方"),
    ("7P2", "tend to -", "〈表現〉-する傾向がある"),
    (
        "7P2",
        "depend more on A than (on) B",
        "〈表現〉BよりもAに依存する",
    ),
    ("7P2", "raw water", "〈名〉原水"),
    ("7P2", "unpurified", "〈形〉未浄化の"),
    ("7P2", "purification", "〈名〉浄化"),
    ("7P2", "process", "〈名〉過程"),
    ("7P2", "transportation", "〈名〉輸送"),
    # 7P3 第3段落
    ("7P3", "variable", "〈名〉変化するもの；不確定要素"),
    ("7P3", "affect", "〈動〉…に影響する"),
    ("7P3", "include", "〈動〉…を含む"),
    ("7P3", "region", "〈名〉地域；地方"),
    ("7P3", "urbanization", "〈名〉都市化"),
    ("7P3", "underground", "〈形〉地下の"),
    ("7P3", "source", "〈名〉（水）源"),
    ("7P3", "dissolve", "〈動〉溶ける"),
    ("7P3", "in addition", "〈表現〉さらに；加えて"),
    ("7P3", "melt", "〈動〉溶ける"),
    ("7P3", "movement", "〈名〉移動"),
    ("7P3", "industry", "〈名〉産業；工業"),
    ("7P3", "A as well as B", "〈表現〉Bと同様にAも；AのほかにBも"),
    ("7P3", "infrastructure", "〈名〉インフラ"),
    # 7P4 第4段落
    ("7P4", "property", "〈名〉特質；特性"),
    ("7P4", "differ", "〈動〉異なる"),
    ("7P4", "soap / soapy", "〈名・形〉石けん／石けんを含んだ"),
    ("7P4", "detergent", "〈名〉洗剤"),
    ("7P4", "lather", "〈名〉〈石けんなどによる〉泡"),
    ("7P4", "bubble", "〈名〉泡"),
    ("7P4", "skin", "〈名〉皮膚；肌"),
    ("7P4", "spot", "〈名〉斑点；しみ"),
    ("7P4", "cutlery", "〈名〉〈ナイフ・フォーク・スプーンなどの〉食卓用器具"),
    ("7P4", "limescale", "〈名〉水あか"),
    ("7P4", "substance", "〈名〉物質"),
    ("7P4", "restrict", "〈動〉…を制限する；妨げる"),
    ("7P4", "discolor", "〈動〉…を退色［変色］させる"),
    ("7P4", "damage", "〈動〉…を損なう"),
    ("7P4", "appliance", "〈名〉器具"),
    ("7P4", "... as well", "〈表現〉…もまた"),
    ("7P4", "despite", "〈前〉…にもかかわらず"),
    ("7P4", "aspect", "〈名〉側面"),
    ("7P4", "rate", "〈動〉格付けされる"),
    ("7P4", "beneficial", "〈形〉有益な"),
    ("7P4", "boost", "〈動〉…を増大させる"),
    ("7P4", "intake", "〈名〉摂取量"),
    # 7P5 第5段落
    ("7P5", "electricity", "〈名〉電気"),
    ("7P5", "rinse out", "〈表現〉水洗いで落ちる"),
    ("7P5", "efficiently", "〈副〉効率的に"),
    ("7P5", "last", "〈動〉もつ；使える"),
    ("7P5", "wear out", "〈表現〉すり減る"),
    ("7P5", "tap water", "〈名〉水道水"),
    ("7P5", "soften", "〈動〉…を軟らかくする"),
    ("7P5", "device", "〈名〉装置"),
    ("7P5", "attach A to B", "〈表現〉AをBに取り付ける"),
    ("7P5", "remove", "〈動〉…を取り除く"),
    ("7P5", "filter / filtration", "〈動・名〉…をろ過する／ろ過"),
    ("7P5", "bead", "〈名〉ビーズ；じゅず玉"),
    ("7P5", "positively charged", "〈形〉正電気を帯びた"),
    ("7P5", "potassium ion", "〈名〉カリウムイオン"),
    ("7P5", "attract", "〈動〉…を引きつける"),
    ("7P5", "salty", "〈形〉塩辛い"),
    # 7P6 第6段落
    ("7P6", "costly", "〈形〉費用のかかる"),
    ("7P6", "maintain", "〈動〉…を維持する"),
    ("7P6", "remedy", "〈名〉解決策；改善法"),
    ("7P6", "solve", "〈動〉…を解決する"),
    ("7P6", "boil", "〈動〉…を沸かす"),
    ("7P6", "vinegar", "〈名〉酢"),
    ("7P6", "baking soda", "〈名〉重曹"),
    ("7P6", "react", "〈動〉反応する"),
    ("7P6", "neutralize", "〈動〉…を中和する"),
    ("7P6", "supplement", "〈名〉補足するもの"),
    # 7P7 最終段落
    ("7P7", "now that ...", "〈表現〉今や…なので"),
    ("7P7", "mix", "〈名〉混合（物）；組み合わせ"),
    # 7P8 発表のアウトライン
    ("7P8", "result", "〈名〉結果"),
    ("7P8", "factor", "〈名〉要因；要素"),
    ("7P8", "increased", "〈形〉増加した"),
    ("7P8", "regional", "〈形〉地域による"),
    ("7P8", "climate", "〈名〉気候"),
    ("7P8", "raindrop", "〈名〉雨滴"),
    # 7P9 設問文・選択肢
    ("7P9", "details", "〈名〉詳細な情報"),
    ("7P9", "characteristic", "〈名〉特徴"),
    ("7P9", "ingredient", "〈名〉材料"),
    ("7P9", "consumption", "〈名〉消費"),
    ("7P9", "spot", "〈動〉…を見つける"),
    ("7P9", "get rid of ...", "〈表現〉…を取り除く"),
    ("7P9", "ineffective", "〈形〉効果がない"),
    ("7P9", "positively", "〈副〉肯定的に；よい方向に"),
    ("7P9", "effective", "〈形〉効果的な"),
    ("7P9", "improve", "〈動〉…を改善する"),
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
        "label": "2025追試験 大問7（主な語句・表現・画像準拠）",
        "parts": {
            "7P1": "第1段落",
            "7P2": "第2段落",
            "7P3": "第3段落",
            "7P4": "第4段落",
            "7P5": "第5段落",
            "7P6": "第6段落",
            "7P7": "最終段落",
            "7P8": "発表のアウトライン",
            "7P9": "設問文・選択肢",
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
