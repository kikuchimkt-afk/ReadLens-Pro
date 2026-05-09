# -*- coding: utf-8 -*-
"""2024 共通テスト本試験 大問5 公式単語リストを vocabulary_explanations_only_all_sections.json に反映する。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB_FILE = ROOT / "data/kyotsu/2024/honshiken/vocabulary_explanations_only_all_sections.json"

VOCAB_ONLY_SOURCES = frozenset({"vocabulary_seed", "vocabulary", "section_vocabulary"})
SECTION5_OFFICIAL_SOURCE = "kyotsu2024_section5_official"


def strip_section5_vocab_only(entries):
    """大問5（数値5）かつ語彙シード系のみの occurrence を除去。"""
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
    """再実行時用：過去に追加した大問5公式エントリを除去。"""
    out = []
    for e in entries:
        occs = list(e.get("occurrences") or [])
        if any(o.get("source") == SECTION5_OFFICIAL_SOURCE for o in occs):
            continue
        out.append(e)
    return out


# 出典画像の § 区分 — 5A〜5G（5D は §4 直前の語群）
OFFICIAL = [
    # 5A §1
    ("5A", "family business", "〈名〉家族経営の事業；家業"),
    ("5A", "recover", "〈動〉回復する"),
    ("5A", "eventually", "〈副〉結局；ついに"),
    ("5A", "retire", "〈動〉引退する；身を引く"),
    ("5A", "regular customer", "〈名〉常連客"),
    ("5A", "occasionally", "〈副〉時折"),
    ("5A", "daydream", "〈動〉空想する"),
    # 5B §2
    ("5B", "vibrate", "〈動〉振動する"),
    ("5B", "Congratulations!", "〈表現〉おめでとう"),
    ("5B", "reunion", "〈名〉同窓会"),
    ("5B", "make it", "〈表現〉出席する；来る"),
    ("5B", "graduate", "〈動〉卒業する"),
    # 5C §3
    ("5C", "shortly before ...", "〈表現〉…する少し前に"),
    ("5C", "drama club", "〈名〉演劇部"),
    ("5C", "inseparable", "〈形〉離れていられない"),
    ("5C", "enroll in ...", "〈表現〉…に入学する"),
    ("5C", "preparatory school", "〈名〉予備校"),
    ("5C", "on the other hand", "〈接続〉他方"),
    ("5C", "career", "〈名〉仕事"),
    ("5C", "try out for ...", "〈表現〉…の選考試験を受ける"),
    ("5C", "acting role", "〈名〉芝居の役"),
    ("5C", "reject", "〈動〉…を却下する"),
    ("5C", "offer one's sympathy", "〈表現〉同情の気持ちを表す"),
    ("5C", "abandon", "〈動〉…を捨てる"),
    ("5C", "cannot resist -ing", "〈表現〉－することを我慢できない"),
    ("5C", "serve", "〈動〉〈飲食物を〉出す"),
    ("5C", "bold", "〈形〉はっきりした；強い"),
    ("5C", "flavor", "〈名〉風味"),
    ("5C", "recommend", "〈動〉…を勧める"),
    ("5C", "brand", "〈名〉銘柄"),
    ("5C", "help-wanted", "〈形〉求人広告の"),
    ("5C", "apply", "〈動〉応募する"),
    ("5C", "hire", "〈動〉…を雇う"),
    ("5C", "become fascinated by ...", "〈表現〉…に魅了される"),
    ("5C", "anniversary", "〈名〉記念日"),
    ("5C", "employment", "〈名〉雇用"),
    ("5C", "have something to do with ...", "〈表現〉…と関係がある"),
    ("5C", "What are you waiting for?", "〈表現〉何をぐずぐずしているの；さっさと始めたら"),
    # 5D §4 前（続き）
    ("5D", "encouragement", "〈名〉励まし"),
    ("5D", "inspire", "〈動〉…を鼓舞する"),
    ("5D", "roaster", "〈名〉焙煎機"),
    ("5D", "proudly", "〈副〉誇りを持って"),
    ("5D", "publicity", "〈名〉広告；宣伝"),
    # 5E §4
    ("5E", "headline", "〈名〉見出し"),
    ("5E", "reflect on ...", "〈表現〉…を熟考する"),
    ("5E", "make-up", "〈名〉化粧（品）"),
    ("5E", "cosmetics", "〈名〉化粧品"),
    ("5E", "advertise for ...", "〈表現〉…を求めて広告を出す"),
    ("5E", "employee", "〈名〉社員；従業員"),
    ("5E", "tough", "〈形〉難しい；つらい"),
    ("5E", "door to door", "〈表現〉家から家へ；戸別に"),
    ("5E", "lift her spirits", "〈表現〉彼女を元気づける"),
    ("5E", "workshop", "〈名〉講習会"),
    ("5E", "be suited for ...", "〈表現〉…に適している"),
    ("5E", "promote", "〈動〉…を昇進させる"),
    ("5E", "steadily", "〈副〉着実に"),
    ("5E", "climb one's way up the company ladder", "〈表現〉会社の出世の階段を登る"),
    ("5E", "vice-president", "〈名〉副社長"),
    ("5E", "struggle", "〈動〉格闘する；もがく"),
    ("5E", "be absorbed", "〈表現〉熱中している"),
    ("5E", "glance", "〈動〉ちらっと見る"),
    ("5E", "article", "〈名〉記事"),
    # 5F §5
    ("5F", "in ages", "〈表現〉長い間"),
    ("5F", "Same here.", "〈表現〉私も同じだ"),
    ("5F", "pity", "〈名〉残念なこと"),
    ("5F", "wordlessly", "〈副〉言葉を用いずに"),
    ("5F", "guilt", "〈名〉罪悪感；うしろめたさ"),
    # 5G §6
    ("5G", "payback", "〈名〉お返し；仕返し"),
    ("5G", "incredibly", "〈副〉信じられないくらい"),
    ("5G", "identify", "〈動〉…を特定する"),
    ("5G", "strength", "〈名〉強み；長所"),
    ("5G", "make use of ...", "〈表現〉…を利用［活用］する"),
    ("5G", "proof", "〈名〉証拠"),
    ("5G", "gift", "〈名〉（天賦の）才能"),
    ("5G", "irony", "〈名〉皮肉"),
    ("5G", "ideal", "〈形〉理想的な"),
    ("5G", "degree", "〈名〉学位"),
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
    old_entries = data.get("entries") or []
    stripped = strip_section5_vocab_only(old_entries)
    stripped = drop_previous_section5_official(stripped)
    official = build_official_entries()

    meta = data.get("meta") or {}
    meta["section5_official"] = {
        "label": "2024本試験 大問5（画像・主な語句・表現に準拠）",
        "parts": {
            "5A": "§1",
            "5B": "§2",
            "5C": "§3",
            "5D": "§4前",
            "5E": "§4",
            "5F": "§5",
            "5G": "§6",
        },
        "count": len(OFFICIAL),
    }

    data["entries"] = stripped + official
    data.pop("by_section", None)
    VOCAB_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {VOCAB_FILE}")
    print(f"  Appended {len(official)} official section-5 cards (stripped old numeric-5 vocab-only occs).")


if __name__ == "__main__":
    main()
