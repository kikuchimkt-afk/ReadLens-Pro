"""
Build section 6B (第6問B: Chili Peppers + Presentation slides 枠) for kyotsu/2024/honshiken/data.json

ソース: data/kakomon/2024/data.json の "6B" を取り込み、以下の変換を行う:
  - passages[0] (paragraphs[i].en/ja 段落単位文字列) → 文単位の sentence 配列に分割
    （ホバーで英文1文 ↔ 日本語1文の対応表示にするため）
  - section.presentation_slides (slide_1..slide_6 オブジェクト形式) → passages[1] に
    viewer.js が期待する slides[] 配列形式へ変換
      * Slide 1: title + image (s6b_slide1.png)
      * Slide 2: title + compare_table (chili peppers / wasabi)
      * Slide 3: title + lead (trailing_slot 45) + lettered_bullets A-E
      * Slide 4: title + lead + bullets (is_slot 46, 47)
      * Slide 5: title + center_slot 48
      * Slide 6: title + center_slot 49
  - 問1,2,4,5 (単一空所) → choices に is_correct を付与
  - 問3 ([46][47] 順不同・両方正解で3点) → choices_46 / choices_47 + unordered_slots
  - explanation.evidence_sentences の段落 ID を、当該段落の全文 ID に展開
"""

import copy
import json
import os
import re


LABEL_BY_NUM = {1: "①", 2: "②", 3: "③", 4: "④", 5: "⑤"}

# 第6問B は段落ごとの英・日文数が一致しているため、現状 override は不要。
PARA_JA_MERGE: dict = {}


def split_en_sentences(en: str) -> list:
    s = en.strip()
    res = []
    cur = []
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        cur.append(ch)
        if ch in ".!?":
            j = i + 1
            if j < n and s[j] == '"':
                cur.append(s[j])
                j += 1
            k = j
            while k < n and s[k] in " \t":
                k += 1
            if j < k < n and (s[k].isupper() or s[k] == '"'):
                res.append("".join(cur).strip())
                cur = []
                i = k
                continue
        i += 1
    tail = "".join(cur).strip()
    if tail:
        res.append(tail)
    return res


def split_ja_sentences(ja: str) -> list:
    parts = re.split(r"(?<=[。？！])", ja.strip())
    return [p.strip() for p in parts if p.strip()]


def paragraphs_to_sentence_arrays(src_paragraphs: list) -> list:
    result = []
    for para in src_paragraphs:
        pid = para["id"]
        en_sents = split_en_sentences(para["en"])
        ja_sents = split_ja_sentences(para["ja"])

        merge = PARA_JA_MERGE.get(pid)
        if merge is not None:
            if sum(merge) != len(ja_sents):
                raise RuntimeError(f"{pid}: PARA_JA_MERGE 合計 {sum(merge)} が ja 文数 {len(ja_sents)} と一致しません")
            if len(merge) != len(en_sents):
                raise RuntimeError(f"{pid}: PARA_JA_MERGE 要素数 {len(merge)} が en 文数 {len(en_sents)} と一致しません")
            merged = []
            cursor = 0
            for n_ja in merge:
                merged.append("".join(ja_sents[cursor:cursor + n_ja]))
                cursor += n_ja
            ja_sents = merged
        else:
            if len(en_sents) != len(ja_sents):
                raise RuntimeError(
                    f"{pid}: en 文数 {len(en_sents)} と ja 文数 {len(ja_sents)} が一致しません。PARA_JA_MERGE への登録が必要です。"
                )

        sentences = [
            {"id": f"{pid}_s{idx}", "en": e, "ja": j}
            for idx, (e, j) in enumerate(zip(en_sents, ja_sents), start=1)
        ]
        result.append(sentences)
    return result


def expand_evidence_sentences(src_paragraphs: list, evidences: list) -> list:
    para_ids = {p["id"] for p in src_paragraphs}
    para_count = {}
    for para in src_paragraphs:
        en_sents = split_en_sentences(para["en"])
        para_count[para["id"]] = len(en_sents)

    expanded = []
    for ev in evidences:
        if ev in para_ids:
            for n in range(1, para_count[ev] + 1):
                expanded.append(f"{ev}_s{n}")
        else:
            expanded.append(ev)
    return expanded


def build_article_passage(src_passage: dict) -> dict:
    p = copy.deepcopy(src_passage)
    p["paragraphs"] = paragraphs_to_sentence_arrays(src_passage["paragraphs"])
    p["framed"] = True
    return p


def build_presentation_passage(src_pres: dict) -> dict:
    """ソースの presentation_slides (slide_1..slide_6 オブジェクト) を
    viewer.js が期待する slides[] 配列形式へ変換する。"""

    s1 = src_pres["slide_1"]
    s2 = src_pres["slide_2"]
    s3 = src_pres["slide_3"]
    s4 = src_pres["slide_4"]
    s5 = src_pres["slide_5"]
    s6 = src_pres["slide_6"]

    slides = [
        # Slide 1: タイトル + 画像
        {
            "slide_no": 1,
            "title": {
                "en": s1["title"]["en"].replace("\n", " "),
                "ja": s1["title"]["ja"].replace("\n", " "),
            },
            "image": {
                "src": "images/s6b_slide1.png",
                "alt": "Chili peppers and dish",
            },
        },
        # Slide 2: タイトル + 2列比較表
        {
            "slide_no": 2,
            "title": copy.deepcopy(s2["title"]),
            "compare_table": {
                "columns": copy.deepcopy(s2["content"]["columns"]),
                "rows": [
                    {
                        "left": {
                            "en": s2["content"]["chili_peppers"]["en"][i],
                            "ja": s2["content"]["chili_peppers"]["ja"][i],
                        },
                        "right": {
                            "en": s2["content"]["wasabi"]["en"][i],
                            "ja": s2["content"]["wasabi"]["ja"][i],
                        },
                    }
                    for i in range(3)
                ],
            },
        },
        # Slide 3: タイトル + lead (trailing slot 45) + A〜E の lettered bullets
        {
            "slide_no": 3,
            "title": copy.deepcopy(s3["title"]),
            "lead": {
                "en": s3["content"]["en"].replace(" [45]", "").rstrip(),
                "ja": s3["content"]["ja"].replace("[45]", "").rstrip(),
                "trailing_slot": 45,
            },
            "lettered_bullets": [
                {
                    "letter": item_en.split(".", 1)[0].strip(),
                    "en": item_en.split(".", 1)[1].strip(),
                    "ja": item_ja.split(".", 1)[1].strip() if "." in item_ja else item_ja,
                }
                for item_en, item_ja in zip(s3["items"]["en"], s3["items"]["ja"])
            ],
        },
        # Slide 4: タイトル + lead + bullets (空所スロット 46, 47)
        {
            "slide_no": 4,
            "title": copy.deepcopy(s4["title"]),
            "lead": {
                "en": s4["content"]["en"],
                "ja": s4["content"]["ja"],
            },
            "bullets": [
                {"is_slot": True, "slot": 46},
                {"is_slot": True, "slot": 47},
            ],
        },
        # Slide 5: タイトル + 中央スロット 48
        {
            "slide_no": 5,
            "title": copy.deepcopy(s5["title"]),
            "center_slot": 48,
        },
        # Slide 6: タイトル + 中央スロット 49
        {
            "slide_no": 6,
            "title": copy.deepcopy(s6["title"]),
            "center_slot": 49,
        },
    ]

    return {
        "id": "presentation_6b",
        "framed": True,
        "no_divider": True,
        "presentation_slides": {
            "label_outside_box": {
                "en": "Presentation slides:",
                "ja": "発表用スライド:",
            },
            "slides": slides,
        },
    }


def build_section_6b(src_section: dict) -> dict:
    sec = copy.deepcopy(src_section)

    for field in ("pdf_pages", "passage_images", "explanation_images", "vocabulary"):
        sec.pop(field, None)

    src_article = sec["passages"][0]
    article_passage = build_article_passage(src_article)

    src_pres = sec.pop("presentation_slides", None)
    if not src_pres:
        raise RuntimeError("Source section 6B must contain 'presentation_slides'")
    pres_passage = build_presentation_passage(src_pres)

    sec["passages"] = [article_passage, pres_passage]

    # explanation.evidence_sentences の段落 ID を文 ID に展開
    for q in sec.get("questions", []):
        ev = q.get("explanation", {}).get("evidence_sentences")
        if ev:
            q["explanation"]["evidence_sentences"] = expand_evidence_sentences(
                src_article["paragraphs"], ev
            )

    for q in sec.get("questions", []):
        qid = q.get("question_id")
        ans = q.get("answer")

        # 単一の数値 answer
        if isinstance(ans, int):
            for i, c in enumerate(q.get("choices", []), start=1):
                c["is_correct"] = (i == ans)
            continue

        # 複数空所
        if isinstance(ans, dict):
            slots = sorted(int(k) for k in ans.keys())
            choices_src = q.get("choices", [])
            if not choices_src:
                raise RuntimeError(f"{qid}: choices が空です")

            correct_nums = sorted(int(ans[str(s)]) for s in slots)
            unordered = bool(q.get("unordered"))

            if unordered:
                # 順不同: choices_NN は同じ選択肢で、正解 2 つの両方を is_correct にする
                def make_choices_unordered():
                    return [
                        {**copy.deepcopy(c), "is_correct": (i + 1 in correct_nums)}
                        for i, c in enumerate(choices_src)
                    ]

                q["answer_numbers"] = slots
                q["unordered_slots"] = list(slots)
                for slot in slots:
                    q[f"choices_{slot}"] = make_choices_unordered()
                q["answer"] = {str(slot): LABEL_BY_NUM[int(ans[str(slot)])] for slot in slots}
                q["answer_note"] = "両方正解で3点（順不同）"
            else:
                # 順序付き: 各空所に固有の正解
                def make_choices_for(correct_num: int):
                    return [
                        {**copy.deepcopy(c), "is_correct": (i + 1 == correct_num)}
                        for i, c in enumerate(choices_src)
                    ]

                q["answer_numbers"] = slots
                for slot in slots:
                    q[f"choices_{slot}"] = make_choices_for(int(ans[str(slot)]))
                q["answer"] = {str(slot): LABEL_BY_NUM[int(ans[str(slot)])] for slot in slots}
                q["answer_note"] = "両方正解で3点"

            q.pop("choices", None)
            q.pop("unordered", None)

    return sec


def main():
    base_dir = os.path.dirname(__file__)
    kakomon_path = os.path.join(base_dir, "..", "..", "..", "kakomon", "2024", "data.json")
    honshiken_path = os.path.join(base_dir, "data.json")

    with open(kakomon_path, "r", encoding="utf-8") as f:
        kakomon_data = json.load(f)

    src_section = next(
        (s for s in kakomon_data.get("sections", []) if str(s.get("section_number")) == "6B"),
        None,
    )
    if not src_section:
        print("Section 6B not found in kakomon 2024 data.")
        return

    section_6b = build_section_6b(src_section)

    if os.path.exists(honshiken_path):
        with open(honshiken_path, "r", encoding="utf-8") as f:
            honshiken_data = json.load(f)
    else:
        honshiken_data = {"exam_info": {}, "sections": []}

    sections = [s for s in honshiken_data.get("sections", []) if str(s.get("section_number")) != "6B"]
    sections.append(section_6b)

    def sort_key(s):
        n = s.get("section_number")
        return str(n) if isinstance(n, str) else f"{int(n):02d}"

    sections.sort(key=sort_key)
    honshiken_data["sections"] = sections

    exam_info = honshiken_data.setdefault("exam_info", {})
    implemented = exam_info.setdefault("implemented_sections", [])
    if "6B" not in implemented:
        implemented.append("6B")
        implemented.sort(key=lambda x: str(x) if isinstance(x, str) else f"{int(x):02d}")

    with open(honshiken_path, "w", encoding="utf-8") as f:
        json.dump(honshiken_data, f, ensure_ascii=False, indent=2)

    print("Section 6B added successfully!")


if __name__ == "__main__":
    main()
