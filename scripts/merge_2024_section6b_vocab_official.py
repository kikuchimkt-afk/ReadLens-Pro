# -*- coding: utf-8 -*-
"""2024 共通テスト本試験 大問6B 主な語句・表現を vocabulary_explanations_only_all_sections.json に反映する。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2024/honshiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION6B_OFFICIAL_SOURCE = "kyotsu2024_section6b_official"


def strip_section6b_vocab_only(entries):
    """大問6B（6B）かつ語彙シード系のみの occurrence を除去。"""
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        filtered = [
            o
            for o in occs
            if not (
                o.get("section_number") in ("6B", "6b")
                and o.get("source") in VOCAB_ONLY_SOURCES
            )
        ]
        if not filtered:
            continue
        ne = dict(e)
        ne["occurrences"] = filtered
        out.append(ne)
    return out


def drop_previous_section6b_official(entries):
    return [
        e
        for e in entries
        if not any(
            o.get("source") == SECTION6B_OFFICIAL_SOURCE
            for o in (e.get("occurrences") or [])
        )
    ]


OFFICIAL = [
    # 6Ba 第1段落
    ("6Ba", "touch", "〈名〉ちょっと手を加えること"),
    ("6Ba", "bite into ...", "〈表現〉…をかじる"),
    ("6Ba", "burn", "〈動〉ヒリヒリする"),
    ("6Ba", "on fire", "〈表現〉火がついて"),
    ("6Ba", "sensation", "〈名〉感覚；感じ"),
    ("6Ba", "at the same time", "〈表現〉同時に；その反面"),
    ("6Ba", "spiciness / spicy", "〈名・形〉香辛料のきいた；ピリッとした"),
    # 6Bb 第2段落
    ("6Bb", "unlike", "〈前〉…とは違って"),
    ("6Bb", "saltiness / salty", "〈名・形〉塩気のある；塩辛い"),
    ("6Bb", "sourness / sour", "〈名・形〉酸っぱい"),
    ("6Bb", "heat", "〈名〉熱；辛さ"),
    ("6Bb", "bite", "〈名〉辛さ"),
    ("6Bb", "be derived from ...", "〈表現〉…に由来する"),
    ("6Bb", "compound", "〈名〉化合物"),
    ("6Bb", "element", "〈名〉要素；成分"),
    ("6Bb", "lingering", "〈形〉なかなか消えない"),
    ("6Bb", "trigger", "〈動〉…を誘発する；始動させる"),
    ("6Bb", "receptor", "〈名〉受容器［体］"),
    ("6Bb", "induce", "〈動〉…を誘発する"),
    ("6Bb", "interestingly", "〈副〉興味深いことに"),
    ("6Bb", "variety", "〈名〉種類"),
    ("6Bb", "depend on ...", "〈表現〉…によって決まる"),
    ("6Bb", "measure", "〈動〉…を測定する"),
    ("6Bb", "range from A to B", "〈表現〉AからBにわたる"),
    ("6Bb", "up to ...", "〈表現〉最大［最高］…"),
    # 6Bc 第3段落
    ("6Bc", "root", "〈名〉根"),
    ("6Bc", "rank", "〈動〉…をランクづけする"),
    ("6Bc", "compare A to B", "〈表現〉AをBになぞらえる"),
    ("6Bc", "tolerate", "〈動〉…を許容する；…への耐性がある"),
    ("6Bc", "flavored with ...", "〈表現〉…で味付けされた［風味を添えた］"),
    ("6Bc", "density", "〈名〉密度；濃度"),
    ("6Bc", "vaporize", "〈動〉蒸発［気化］する"),
    ("6Bc", "deliver A to B", "〈表現〉A〈打撃・攻撃など〉をBに加える"),
    ("6Bc", "blast", "〈名〉強いひと吹き"),
    # 6Bd 第4段落
    ("6Bd", "consume", "〈動〉…を消費する；食べる"),
    ("6Bd", "positive", "〈形〉肯定的な；プラスの"),
    ("6Bd", "effect", "〈名〉影響；効果"),
    ("6Bd", "benefit", "〈名〉恩恵；利点"),
    ("6Bd", "activate", "〈動〉…を活性化する"),
    ("6Bd", "injury", "〈名〉負傷；けが"),
    ("6Bd", "strangely", "〈副〉奇妙なことに"),
    ("6Bd", "go away", "〈表現〉消えていく"),
    ("6Bd", "cease to -", "〈表現〉-しなくなる"),
    ("6Bd", "turn on", "〈表現〉スイッチを入れる；刺激する"),
    ("6Bd", "long-term", "〈形〉長期の"),
    ("6Bd", "exposure to ...", "〈表現〉…にさらされる［触れる］こと"),
    ("6Bd", "temporarily", "〈副〉一時的に"),
    ("6Bd", "ease", "〈動〉…を和らげる"),
    ("6Bd", "muscle ache", "〈名〉筋肉痛"),
    # 6Be 第5段落
    ("6Be", "accelerate", "〈動〉…を加速する"),
    ("6Be", "metabolism", "〈名〉新陳代謝"),
    ("6Be", "analyze", "〈動〉…を分析する"),
    ("6Be", "reduced", "〈形〉減少した"),
    ("6Be", "appetite", "〈名〉食欲"),
    ("6Be", "heart rate", "〈名〉心拍数"),
    ("6Be", "convert A into B", "〈表現〉AをBに変える"),
    ("6Be", "fat", "〈名〉脂肪"),
    ("6Be", "weight-loss", "〈形〉減量の"),
    ("6Be", "ingredient", "〈名〉成分"),
    # 6Bf 第6段落
    ("6Bf", "be connected with ...", "〈表現〉…と関係［関連］がある"),
    ("6Bf", "food safety", "〈名〉食の安全"),
    ("6Bf", "refrigerated", "〈形〉冷蔵された"),
    ("6Bf", "microorganism", "〈名〉微生物"),
    ("6Bf", "multiply", "〈動〉繁殖する"),
    ("6Bf", "chemical", "〈名〉化学物質"),
    ("6Bf", "antibacterial", "〈形〉抗菌性の"),
    ("6Bf", "property", "〈名〉特性"),
    ("6Bf", "as a result", "〈接続〉その結果"),
    ("6Bf", "last", "〈動〉〈ある期間〉もつ"),
    ("6Bf", "food-borne", "〈形〉食物が媒介する"),
    ("6Bf", "have a tendency to -", "〈表現〉-する傾向がある"),
    ("6Bf", "be tolerant of ...", "〈表現〉…に対して耐性がある"),
    ("6Bf", "due to ...", "〈表現〉…のせいで"),
    ("6Bf", "refrigerator", "〈名〉冷蔵庫"),
    ("6Bf", "be likely to -", "〈表現〉-しそうだ；-する可能性が高い"),
    ("6Bf", "food poisoning", "〈名〉食中毒"),
    # 6Bg 第7段落
    ("6Bg", "discomfort", "〈名〉苦痛（からくる不快感）"),
    ("6Bg", "in large quantities", "〈表現〉大量に"),
    ("6Bg", "upset", "〈形〉不調な"),
    ("6Bg", "diarrhea", "〈名〉下痢"),
    ("6Bg", "numb", "〈形〉感覚のない；麻痺した"),
    ("6Bg", "symptom", "〈名〉症状"),
    ("6Bg", "heart attack", "〈名〉心臓麻痺"),
    # 6Bh 最終段落（「go away」は第4段落と訳が異なるため別カード）
    ("6Bh", "go away", "〈表現〉消えゆく"),
    ("6Bh", "despite", "〈前〉…にもかかわらず"),
    ("6Bh", "negative", "〈形〉否定的な；マイナスの"),
    ("6Bh", "flavorful", "〈形〉風味に富む"),
    ("6Bh", "you might want to -", "〈表現〉-する方がいい"),
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
                        "source": SECTION6B_OFFICIAL_SOURCE,
                    }
                ],
            }
        )
    return entries


def main():
    data = json.loads(VOCAB_FILE.read_text(encoding="utf-8"))
    old = data.get("entries") or []
    stripped = strip_section6b_vocab_only(old)
    stripped = drop_previous_section6b_official(stripped)
    official = build_official_entries()

    meta = data.get("meta") or {}
    meta["section6b_official"] = {
        "label": "2024本試験 大問6B（主な語句・表現に準拠）",
        "parts": {
            "6Ba": "第1段落",
            "6Bb": "第2段落",
            "6Bc": "第3段落",
            "6Bd": "第4段落",
            "6Be": "第5段落",
            "6Bf": "第6段落",
            "6Bg": "第7段落",
            "6Bh": "最終段落",
        },
        "count": len(OFFICIAL),
    }

    data["entries"] = stripped + official
    data.pop("by_section", None)
    VOCAB_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {VOCAB_FILE}")
    print(f"  Appended {len(official)} official section-6B cards.")


if __name__ == "__main__":
    main()
