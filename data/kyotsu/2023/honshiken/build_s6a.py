# -*- coding: utf-8 -*-
"""Build Section 6A and merge into data.json for 2023 Honshiken."""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from build_s6a_passages import get_passages
from build_s6a_questions import get_questions

DATA_JSON = os.path.join(os.path.dirname(__file__), "data.json")

def get_vocabulary():
    return {
        "p1": {"label_ja": "第1段落（Collecting has existed ...）", "items": [
            {"en": "summarize", "ja": "〈動〉…を要約する"},
            {"en": "proof", "ja": "〈名〉証拠"},
            {"en": "pass down ...", "ja": "…を伝える"},
            {"en": "catch one's eye", "ja": "…の目に留まる"},
            {"en": "over time", "ja": "徐々に"},
            {"en": "leave an impression on ...", "ja": "…に印象を残す"},
            {"en": "modest", "ja": "〈形〉ささやかな"},
            {"en": "trash", "ja": "〈名〉がらくた"},
            {"en": "treasure", "ja": "〈名〉宝物"},
            {"en": "regardless of ...", "ja": "…に関係なく"}
        ]},
        "p2": {"label_ja": "第2段落（In 1988, researchers ...）", "items": [
            {"en": "gather", "ja": "〈動〉…を集める"},
            {"en": "stuff", "ja": "〈名〉物"},
            {"en": "maintain", "ja": "〈動〉…を維持する"},
            {"en": "primary", "ja": "〈形〉第一の"},
            {"en": "youth", "ja": "〈名〉青春時代"},
            {"en": "attachment to ...", "ja": "…への愛着"},
            {"en": "seek", "ja": "〈動〉…を探し求める"},
            {"en": "autograph", "ja": "〈名〉（有名人の）サイン"}
        ]},
        "p3": {"label_ja": "第3段落（For some individuals ...）", "items": [
            {"en": "appreciate", "ja": "〈動〉…の真価を認める"},
            {"en": "fame", "ja": "〈名〉名声"},
            {"en": "similarly", "ja": "〈副〉同様に"},
            {"en": "playing cards", "ja": "トランプ"}
        ]},
        "p4": {"label_ja": "第4段落（Perhaps the easiest motivation ...）", "items": [
            {"en": "purchase", "ja": "〈動〉…を購入する"},
            {"en": "put up ...", "ja": "…を飾る"},
            {"en": "gaze at ...", "ja": "…をじっと見る"},
            {"en": "vinyl", "ja": "〈名〉ビニール"},
            {"en": "monetary", "ja": "〈形〉金銭的な"},
            {"en": "treasured", "ja": "〈形〉貴重な，秘蔵の"},
            {"en": "specifically", "ja": "〈副〉明確に"},
            {"en": "investment", "ja": "〈名〉投資"},
            {"en": "in mint condition", "ja": "新品同様で"},
            {"en": "ensure", "ja": "〈動〉…を保証する"}
        ]},
        "p5": {"label_ja": "第5段落（This behavior of collecting ...）", "items": [
            {"en": "distant", "ja": "〈形〉遠い"},
            {"en": "advance", "ja": "〈名〉進歩"},
            {"en": "have an influence on ...", "ja": "…に影響を与える"},
            {"en": "physical constraint", "ja": "物理的制約"},
            {"en": "vast", "ja": "〈形〉膨大な"}
        ]},
        "questions": {"label_ja": "設問・選択肢", "items": [
            {"en": "evaluate", "ja": "〈動〉…を評価する"},
            {"en": "roughly", "ja": "〈副〉大体"},
            {"en": "desire", "ja": "〈名〉願望"},
            {"en": "reminder", "ja": "〈名〉思い出させる人・物"},
            {"en": "precious", "ja": "〈形〉貴重な"},
            {"en": "profit", "ja": "〈名〉利益"}
        ]}
    }

def build_section6a():
    return {
        "section_number": "6A",
        "title": "第6問 A",
        "points": 12,
        "description": "長文読解（記事＋メモ）",
        "situation": {
            "en": "You are in a discussion group in school. You have been asked to summarize the following article. You will speak about it, using only notes.",
            "ja": "あなたは学校で討論グループに所属している。次の記事を要約するように頼まれている。あなたはその記事について，メモだけを見て話すことになっている。"
        },
        "passages": get_passages(),
        "questions": get_questions(),
        "vocabulary": get_vocabulary()
    }

def main():
    with open(DATA_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    data["sections"] = [s for s in data["sections"] if str(s["section_number"]) != "6A"]
    data["sections"].append(build_section6a())
    
    # Sort section_number properly. "6A" comes after 5.
    def sort_key(s):
        num = s["section_number"]
        if isinstance(num, int):
            return num
        if num == "6A": return 6.1
        if num == "6B": return 6.2
        return 99

    data["sections"].sort(key=sort_key)
    impl = sorted(set(s["section_number"] for s in data["sections"]), key=lambda x: x if isinstance(x, int) else (6.1 if x == "6A" else (6.2 if x == "6B" else 99)))
    data["exam_info"]["implemented_sections"] = impl
    data["exam_info"]["format"] = "6AB"
    if "section_list" not in data["exam_info"]:
        data["exam_info"]["section_list"] = [1, 2, 3, 4, 5, "6A", "6B"]
    
    with open(DATA_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"Section 6A added. Total sections: {len(data['sections'])}")
    print(f"implemented_sections: {data['exam_info']['implemented_sections']}")

if __name__ == "__main__":
    main()
