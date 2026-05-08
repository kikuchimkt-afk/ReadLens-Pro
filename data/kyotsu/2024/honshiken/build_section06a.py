"""
Build section 6A (第6問A: Perceptions of Time + Your notes 枠) for kyotsu/2024/honshiken/data.json

ソース: data/kakomon/2024/data.json の "6A" を取り込み、以下の変換を行う:
  - passages[0] (paragraphs[i].en/ja 段落単位文字列) → 文単位の sentence 配列に分割
    （viewer.js のホバーで英文1文 ↔ 日本語1文の対応表示にするため）
  - section.notes (outline_by_paragraph / original_examples) → passages[1] = is_notes passage
  - 問1 ([39][40] 両方正解で3点) → choices_39 / choices_40 形式に分割
  - explanation.evidence_sentences の段落 ID を、当該段落の全文 ID に展開
"""

import copy
import json
import os
import re


LABEL_BY_NUM = {1: "①", 2: "②", 3: "③", 4: "④", 5: "⑤", 6: "⑥"}

# 英文と日本語文の数が一致しない段落を、英文ごとの日本語文数で揃えるためのオーバーライド。
# 6a_p2: 英文5「To answer, ..., which is estimating ... from memory.」が日本語2文に分かれている
PARA_JA_MERGE = {
    "6a_p2": [1, 1, 1, 1, 2, 1],
}


def split_en_sentences(en: str) -> list:
    """文末記号 . ! ? の後（閉じクォートを含む）+ 空白 + 大文字または開きクォート の位置で分割。"""
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
    """日本語文を「。？！」の直後で分割し、句読点を末尾に保持。"""
    parts = re.split(r"(?<=[。？！])", ja.strip())
    return [p.strip() for p in parts if p.strip()]


def paragraphs_to_sentence_arrays(src_paragraphs: list) -> list:
    """[{id, en, ja}, ...] を [[{id, en, ja}, ...], ...] (段落=文の配列) に変換する。"""
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
    """段落 ID (例 '6a_p1') を含む evidence を、当該段落の全文 ID に展開する。"""
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
    """記事 passage の paragraphs を文単位の配列形式に変換し、framed を付与する。"""
    p = copy.deepcopy(src_passage)
    p["paragraphs"] = paragraphs_to_sentence_arrays(src_passage["paragraphs"])
    p["framed"] = True
    return p


def build_notes_passage(src_notes: dict) -> dict:
    """ソースの notes を viewer.js 6A 用の is_notes passage 形式へ変換。"""
    return {
        "id": src_notes.get("id", "notes_6a"),
        "is_notes": True,
        "framed": True,
        "no_divider": True,
        "notes_caption": {"en": "Your notes:", "ja": "あなたのノート:"},
        "notes_title": {
            "en": src_notes["title"]["en"],
            "ja": src_notes["title"]["ja"],
        },
        "outline_by_paragraph": copy.deepcopy(src_notes["outline_by_paragraph"]),
        "original_examples": copy.deepcopy(src_notes["original_examples"]),
    }


def build_section_6a(src_section: dict) -> dict:
    sec = copy.deepcopy(src_section)

    for field in ("pdf_pages", "passage_images", "explanation_images", "vocabulary"):
        sec.pop(field, None)

    src_article = sec["passages"][0]
    article_passage = build_article_passage(src_article)

    src_notes = sec.pop("notes", None)
    if not src_notes:
        raise RuntimeError("Source section 6A must contain 'notes'")
    notes_passage = build_notes_passage(src_notes)

    sec["passages"] = [article_passage, notes_passage]

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

        # 単一の数値 answer の場合は choices に is_correct を付与
        if isinstance(ans, int):
            for i, c in enumerate(q.get("choices", []), start=1):
                c["is_correct"] = (i == ans)
            continue

        # 複数空所 (問1: {"39":6, "40":2}) → choices_NN 形式に分割
        if isinstance(ans, dict):
            slots = sorted(int(k) for k in ans.keys())
            choices_src = q.get("choices", [])
            if not choices_src:
                raise RuntimeError(f"{qid}: choices が空です")

            def make_choices(correct_num: int):
                return [
                    {**copy.deepcopy(c), "is_correct": (i + 1 == correct_num)}
                    for i, c in enumerate(choices_src)
                ]

            q["answer_numbers"] = slots
            new_answer = {}
            for slot in slots:
                correct = int(ans[str(slot)])
                q[f"choices_{slot}"] = make_choices(correct)
                new_answer[str(slot)] = LABEL_BY_NUM[correct]
            q["answer"] = new_answer
            q["answer_note"] = "両方正解で3点"
            q.pop("choices", None)

    return sec


def main():
    base_dir = os.path.dirname(__file__)
    kakomon_path = os.path.join(base_dir, "..", "..", "..", "kakomon", "2024", "data.json")
    honshiken_path = os.path.join(base_dir, "data.json")

    with open(kakomon_path, "r", encoding="utf-8") as f:
        kakomon_data = json.load(f)

    src_section = next(
        (s for s in kakomon_data.get("sections", []) if str(s.get("section_number")) == "6A"),
        None,
    )
    if not src_section:
        print("Section 6A not found in kakomon 2024 data.")
        return

    section_6a = build_section_6a(src_section)

    if os.path.exists(honshiken_path):
        with open(honshiken_path, "r", encoding="utf-8") as f:
            honshiken_data = json.load(f)
    else:
        honshiken_data = {"exam_info": {}, "sections": []}

    sections = [s for s in honshiken_data.get("sections", []) if str(s.get("section_number")) != "6A"]
    sections.append(section_6a)

    def sort_key(s):
        n = s.get("section_number")
        return str(n) if isinstance(n, str) else f"{int(n):02d}"

    sections.sort(key=sort_key)
    honshiken_data["sections"] = sections

    exam_info = honshiken_data.setdefault("exam_info", {})
    implemented = exam_info.setdefault("implemented_sections", [])
    if "6A" not in implemented:
        implemented.append("6A")
        implemented.sort(key=lambda x: str(x) if isinstance(x, str) else f"{int(x):02d}")

    with open(honshiken_path, "w", encoding="utf-8") as f:
        json.dump(honshiken_data, f, ensure_ascii=False, indent=2)

    print("Section 6A added successfully!")


if __name__ == "__main__":
    main()
