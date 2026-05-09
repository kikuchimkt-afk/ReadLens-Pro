# -*- coding: utf-8 -*-
"""2024 共通テスト本試験 大問6A 公式単語リストを vocabulary_explanations_only_all_sections.json に反映する。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2024/honshiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION6A_OFFICIAL_SOURCE = "kyotsu2024_section6a_official"


def strip_section6a_vocab_only(entries):
    """大問6A（6A）かつ語彙シード系のみの occurrence を除去。"""
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        filtered = [
            o
            for o in occs
            if not (
                o.get("section_number") in ("6A", "6a")
                and o.get("source") in VOCAB_ONLY_SOURCES
            )
        ]
        if not filtered:
            continue
        ne = dict(e)
        ne["occurrences"] = filtered
        out.append(ne)
    return out


def drop_previous_section6a_official(entries):
    """再実行：過去に追加した大問6A公式エントリを除去。"""
    return [
        e
        for e in entries
        if not any(
            o.get("source") == SECTION6A_OFFICIAL_SOURCE
            for o in (e.get("occurrences") or [])
        )
    ]


# 画像リスト — 6Aa〜6Af（第1段落…最終段落）
OFFICIAL = [
    # 6Aa 第1段落
    ("6Aa", "come to mind", "〈表現〉思い浮かぶ"),
    ("6Aa", "philosopher", "〈名〉哲学者"),
    ("6Aa", "measure", "〈動〉…を測定する"),
    ("6Aa", "known", "〈形〉既知の"),
    ("6Aa", "biological", "〈形〉生物学的な"),
    ("6Aa", "mental process", "〈名〉心理作用；精神過程"),
    ("6Aa", "instead", "〈副〉代わりに"),
    ("6Aa", "psychological", "〈形〉心理的な"),
    ("6Aa", "perceive", "〈動〉知覚する"),
    # 6Ab 第2段落
    ("6Ab", "estimate", "〈名・動〉見積もり；…を見積もる"),
    ("6Ab", "participant", "〈名〉参加者"),
    ("6Ab", "fixed", "〈形〉一定の"),
    ("6Ab", "memorize", "〈動〉…を記憶する"),
    ("6Ab", "afterwards", "〈副〉後になって"),
    ("6Ab", "based on ...", "〈表現〉…に基づいて"),
    ("6Ab", "retrieve", "〈動〉取り戻す；回収する"),
    ("6Ab", "the opposite", "〈名〉正反対のこと"),
    # 6Ac 第3段落
    ("6Ac", "actively", "〈副〉積極的に；能動的に"),
    ("6Ac", "keep track of ...", "〈表現〉…の経過を追う；…の記録をつける"),
    ("6Ac", "instead of ...", "〈表現〉…の代わりに"),
    ("6Ac", "recall", "〈動〉…を思い出す"),
    ("6Ac", "perform", "〈動〉…を遂行する"),
    ("6Ac", "complete", "〈動〉…を完成する"),
    ("6Ac", "challenging", "〈形〉やりがいのある；きつい"),
    ("6Ac", "focus", "〈名〉焦点；集中"),
    # 6Ad 第4段落
    ("6Ad", "emotional", "〈形〉感情の"),
    ("6Ad", "state", "〈名〉状態"),
    ("6Ad", "influence", "〈動〉…に影響を及ぼす"),
    ("6Ad", "awareness", "〈名〉意識；認識"),
    ("6Ad", "pass by", "〈表現〉過ぎ去る"),
    (
        "6Ad",
        "in what seemed to be the blink of an eye",
        "〈表現〉目の瞬き［一瞬］と思える（短い）時間のうちに",
    ),
    ("6Ad", "be focused on ...", "〈表現〉…に集中している"),
    ("6Ad", "wait for O to-", "〈表現〉Oが-するのを待つ"),
    ("6Ad", "boredom", "〈名〉退屈"),
    ("6Ad", "affect", "〈動〉…に影響する"),
    ("6Ad", "perception", "〈名〉知覚"),
    ("6Ad", "unpleasant", "〈形〉不快な"),
    ("6Ad", "perceive O to be ...", "〈表現〉Oが…であるのに気づく"),
    ("6Ad", "in reality", "〈表現〉実際に"),
    # 6Ae 第5段落
    ("6Ae", "constantly", "〈副〉絶えず"),
    ("6Ae", "encounter", "〈動〉…に遭遇する"),
    ("6Ae", "memorable", "〈形〉記憶に残る"),
    ("6Ae", "creep by", "〈表現〉徐々に過ぎる"),
    ("6Ae", "anticipate", "〈動〉…を予期する；心待ちにする"),
    ("6Ae", "upcoming", "〈形〉まもなくやって来る"),
    ("6Ae", "rarely", "〈副〉めったに…しない"),
    ("6Ae", "frequent", "〈形〉頻繁に起こる"),
    ("6Ae", "be the case", "〈表現〉真相［事実］である"),
    ("6Ae", "routine", "〈名〉決まってすること"),
    ("6Ae", "shake up", "〈表現〉再編［刷新］する"),
    ("6Ae", "drastic", "〈形〉徹底的な"),
    ("6Ae", "relocate", "〈動〉（新しい場所に）移転［移住］する"),
    ("6Ae", "passage", "〈名〉（時の）経過"),
    ("6Ae", "generally speaking", "〈表現〉一般的に言って"),
    ("6Ae", "accelerate", "〈動〉加速する"),
    ("6Ae", "mature", "〈動〉成長する；大人になる"),
    # 6Af 最終段落
    ("6Af", "knowledge", "〈名〉知識"),
    ("6Af", "deal with ...", "〈表現〉…を扱う［処理する］"),
    ("6Af", "engaging", "〈形〉興味をそそる"),
    ("6Af", "ease", "〈動〉…を和らげる"),
    ("6Af", "occasion", "〈名〉時；場合"),
    ("6Af", "be reminded of ...", "〈表現〉…が思い出される"),
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
                        "source": SECTION6A_OFFICIAL_SOURCE,
                    }
                ],
            }
        )
    return entries


def main():
    data = json.loads(VOCAB_FILE.read_text(encoding="utf-8"))
    old_entries = data.get("entries") or []
    stripped = strip_section6a_vocab_only(old_entries)
    stripped = drop_previous_section6a_official(stripped)
    official = build_official_entries()

    meta = data.get("meta") or {}
    meta["section6a_official"] = {
        "label": "2024本試験 大問6A（主な語句・表現に準拠）",
        "parts": {
            "6Aa": "第1段落",
            "6Ab": "第2段落",
            "6Ac": "第3段落",
            "6Ad": "第4段落",
            "6Ae": "第5段落",
            "6Af": "最終段落",
        },
        "count": len(OFFICIAL),
    }

    data["entries"] = stripped + official
    data.pop("by_section", None)
    VOCAB_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {VOCAB_FILE}")
    print(f"  Appended {len(official)} official section-6A cards.")


if __name__ == "__main__":
    main()
