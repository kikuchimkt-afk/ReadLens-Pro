"""
Build section 5 (第5問: 物語文「Maki's Kitchen」 + Your notes 枠) for kyotsu/2024/honshiken/data.json

ソース: data/kakomon/2024/data.json の第5問を取り込み、以下の変換を行う:
  - passages[0].sections[] の入れ子構造 → passages[0].paragraphs[] (段落の配列の配列)
    + block_separators で 6 セクション境界に ◆◆◆◆◆ を配置
    + framed: True で外枠
  - section.notes (about_maki 等を含む) → passages[1] = is_notes passage
"""

import copy
import json
import os


# 物語の段落分け（PDF レイアウトに準拠）
# 各段落は対応する文 ID（kakomon ソースの sentence id）の連番リストで定義する。
# block_separators は ◆◆◆◆◆ を表示する段落 index（0 始まり）。
PARAGRAPH_GROUPS = [
    # §1
    ["5_s1", "5_s2", "5_s3", "5_s4", "5_s5", "5_s6"],
    ["5_s7", "5_s8", "5_s9"],
    # §2
    ["5_s10"],
    ["5_s11"],
    ["5_s12"],
    ["5_s13"],
    ["5_s14"],
    # §3
    ["5_s15", "5_s16", "5_s17", "5_s18", "5_s19", "5_s20", "5_s21"],
    ["5_s22", "5_s23", "5_s24", "5_s25", "5_s26"],
    ["5_s27"],
    ["5_s28"],
    ["5_s29", "5_s30"],
    ["5_s31"],
    ["5_s32"],
    ["5_s33"],
    ["5_s34"],
    ["5_s35", "5_s36", "5_s37", "5_s38", "5_s39"],
    # §4
    ["5_s40", "5_s41"],
    ["5_s42", "5_s43", "5_s44", "5_s45"],
    ["5_s46", "5_s47", "5_s48"],
    ["5_s49", "5_s50", "5_s51"],
    ["5_s52", "5_s53"],
    # §5
    ["5_s54"],
    ["5_s55"],
    ["5_s56", "5_s57"],
    # §6
    ["5_s58"],
    ["5_s59"],
    ["5_s60"],
    ["5_s61"],
    ["5_s62"],
    ["5_s63"],
    ["5_s64"],
    ["5_s65"],
]

# ◆◆◆◆◆ は §2/§3/§4/§5/§6 の各先頭段落の前に挿入
BLOCK_SEPARATORS = [2, 7, 17, 22, 25]


def build_paragraphs(sentence_map: dict) -> list:
    paragraphs = []
    for group in PARAGRAPH_GROUPS:
        para = []
        for sid in group:
            if sid not in sentence_map:
                raise KeyError(f"Sentence id not found in source: {sid}")
            s = sentence_map[sid]
            para.append({
                "id": s["id"],
                "en": s["en"],
                "ja": s["ja"],
            })
        paragraphs.append(para)
    return paragraphs


def build_story_passage(src_passage: dict) -> dict:
    sentence_map = {}
    for sec in src_passage.get("sections", []):
        for s in sec.get("sentences", []):
            sentence_map[s["id"]] = s

    paragraphs = build_paragraphs(sentence_map)

    return {
        "id": src_passage.get("id", "story_5"),
        "title": copy.deepcopy(src_passage.get("title")),
        "framed": True,
        "block_separators": list(BLOCK_SEPARATORS),
        "paragraphs": paragraphs,
    }


def build_notes_passage(src_notes: dict) -> dict:
    """
    ソースの notes フィールド（story_outline / about_maki / interpretation はいずれも
    header.{en,ja} と content.{en,ja} のプレーンテキスト形式）を、
    現行ビューアが解釈できる構造に変換する。
    """
    so = src_notes["story_outline"]
    am = src_notes["about_maki"]
    it = src_notes["interpretation"]

    return {
        "id": src_notes.get("id", "notes_5"),
        "is_notes": True,
        "framed": True,
        "no_divider": True,
        "notes_caption": {
            "en": "Your notes:",
            "ja": "あなたのノート:",
        },
        "notes_title": {
            "en": src_notes["title"]["en"],
            "ja": src_notes["title"]["ja"],
        },
        # Story outline: マキ・タクヤ・カスミが高校を卒業する → [30][31][32][33] → マキは…
        "story_outline": {
            "header": copy.deepcopy(so.get("header", {"en": "Story outline", "ja": "ストーリーのアウトライン"})),
            "start": {
                "en": "Maki, Takuya, and Kasumi graduate from high school.",
                "ja": "マキ，タクヤ，カスミが高校を卒業する。",
            },
            "slots": [30, 31, 32, 33],
            "end": {
                "en": "Maki begins to think about a second career.",
                "ja": "マキは第2のキャリアについて考え始める。",
            },
        },
        # About Maki: viewer.js に追加した about_maki ロジック向けの構造
        "about_maki": {
            "heading": copy.deepcopy(am.get("header", {"en": "About Maki", "ja": "マキについて"})),
            "age_slot": 34,
            "occupation": {
                "en": "restaurant owner",
                "ja": "レストランのオーナー",
            },
            "support_heading": {
                "en": "How she supported her friends:",
                "ja": "彼女はどうやって友人を支えたか：",
            },
            "support": [
                {
                    "en": "Provided Takuya with encouragement and [35].",
                    "ja": "タクヤには励ましを与え，[35]。",
                },
                {
                    "en": '" Kasumi " " and [36].',
                    "ja": "カスミには 〃  〃  [36]。",
                },
            ],
        },
        # Interpretation: 既存の is_notes ビューアの interpretation 配列形式に合わせる
        "interpretation": [
            {
                "en": "Kasumi and Takuya experience an uncomfortable silence on the phone because they [37].",
                "ja": "カスミとタクヤは[37]ので，通話中に気まずい沈黙を経験する。",
            },
            {
                "en": ("In the final scene, Kasumi uses the word \"irony\" with Maki. "
                       "The irony is that Maki does not [38]."),
                "ja": "最後の場面で，カスミはマキについて「皮肉」という言葉を使う。皮肉とは，マキが[38]ないということだ。",
            },
        ],
    }


def build_section_5(src_section: dict) -> dict:
    sec = copy.deepcopy(src_section)

    # 不要フィールドの削除（PDF 抽出時のメタ情報）
    for field in ("pdf_pages", "passage_images", "explanation_images", "vocabulary"):
        sec.pop(field, None)

    # 物語 passage を変換
    src_story = sec["passages"][0]
    story_passage = build_story_passage(src_story)

    # notes → is_notes passage を生成
    src_notes = sec.pop("notes", None)
    if not src_notes:
        raise RuntimeError("Source section 5 must contain 'notes'")
    notes_passage = build_notes_passage(src_notes)

    sec["passages"] = [story_passage, notes_passage]

    # 設問ビューア仕様への変換
    LABEL_BY_NUM = {1: "①", 2: "②", 3: "③", 4: "④", 5: "⑤"}

    for q in sec.get("questions", []):
        qid = q.get("question_id")
        ans = q.get("answer")

        # choices に is_correct を補う（単一・配列いずれの answer でも安全側で動くように）
        if qid not in ("問1", "問3") and isinstance(ans, int):
            for i, c in enumerate(q.get("choices", []), start=1):
                c["is_correct"] = (i == ans)

        if qid == "問1":
            # ordering: [30][31][32][33] への 4 つを並べる
            seq = ans if isinstance(ans, list) else []
            q["question_type"] = "ordering"
            q["answer_numbers"] = [30, 31, 32, 33]
            q["answer_sequence"] = list(seq)
            q["answer"] = "→".join(LABEL_BY_NUM[n] for n in seq)
            q["answer_note"] = "全部正解で3点"

        elif qid == "問3":
            # 複数空所: [35] と [36] に同じ 5 択から別々に選ぶ
            choices_src = q.get("choices", [])
            ans_list = ans if isinstance(ans, list) else []
            if len(ans_list) != 2:
                raise RuntimeError("問3 の answer は [n_for_35, n_for_36] の 2 要素である必要があります")

            def make_choices(correct_num: int):
                return [
                    {**copy.deepcopy(c), "is_correct": (i + 1 == correct_num)}
                    for i, c in enumerate(choices_src)
                ]

            q["answer_numbers"] = [35, 36]
            q["choices_35"] = make_choices(ans_list[0])
            q["choices_36"] = make_choices(ans_list[1])
            q["answer"] = {
                "35": LABEL_BY_NUM[ans_list[0]],
                "36": LABEL_BY_NUM[ans_list[1]],
            }
            q["answer_note"] = "両方正解で3点"
            # choices フィールドは複数空所では不要（残しておくとビューアで通常 4 択描画に紛れる）
            q.pop("choices", None)

    return sec


def main():
    base_dir = os.path.dirname(__file__)
    kakomon_path = os.path.join(base_dir, "..", "..", "..", "kakomon", "2024", "data.json")
    honshiken_path = os.path.join(base_dir, "data.json")

    with open(kakomon_path, "r", encoding="utf-8") as f:
        kakomon_data = json.load(f)

    src_section = next(
        (s for s in kakomon_data.get("sections", []) if s.get("section_number") == 5),
        None,
    )
    if not src_section:
        print("Section 5 not found in kakomon 2024 data.")
        return

    section_5 = build_section_5(src_section)

    if os.path.exists(honshiken_path):
        with open(honshiken_path, "r", encoding="utf-8") as f:
            honshiken_data = json.load(f)
    else:
        honshiken_data = {"exam_info": {}, "sections": []}

    sections = [s for s in honshiken_data.get("sections", []) if s.get("section_number") != 5]
    sections.append(section_5)
    sections.sort(key=lambda x: (str(x.get("section_number")) if isinstance(x.get("section_number"), str) else f"{int(x.get('section_number')):02d}"))
    honshiken_data["sections"] = sections

    exam_info = honshiken_data.setdefault("exam_info", {})
    implemented = exam_info.setdefault("implemented_sections", [])
    if 5 not in implemented:
        implemented.append(5)
        implemented.sort(key=lambda x: (str(x) if isinstance(x, str) else f"{int(x):02d}"))

    with open(honshiken_path, "w", encoding="utf-8") as f:
        json.dump(honshiken_data, f, ensure_ascii=False, indent=2)

    print("Section 5 added successfully!")


if __name__ == "__main__":
    main()
