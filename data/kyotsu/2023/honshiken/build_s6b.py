# -*- coding: utf-8 -*-
"""Build Section 6B and merge into data.json for 2023 Honshiken."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build_s6b_passages import get_passages
from build_s6b_questions import get_questions

DATA_JSON = os.path.join(os.path.dirname(__file__), "data.json")


def get_vocabulary():
    return {
        "p1": {"label_ja": "第1段落", "items": [
            {"en": "passage", "ja": "〈名〉文章"},
            {"en": "extraordinary", "ja": "〈形〉異常な"},
            {"en": "Bactrian camel", "ja": "フタコブラクダ"},
            {"en": "survive", "ja": "〈動〉生き延びる"}
        ]},
        "p2": {"label_ja": "第2段落", "items": [
            {"en": "tardigrade", "ja": "〈名〉クマムシ"},
            {"en": "microscopic", "ja": "〈形〉微細な"},
            {"en": "layer", "ja": "〈名〉層"},
            {"en": "metabolism", "ja": "〈名〉代謝"},
            {"en": "state", "ja": "〈名〉状態"},
            {"en": "soaked", "ja": "〈形〉びしょ濡れの"},
            {"en": "absorb", "ja": "〈動〉吸収する"},
            {"en": "spring back to life", "ja": "復活する"},
            {"en": "matter", "ja": "〈名〉大きな違い"},
            {"en": "ultraviolet radiation", "ja": "紫外線放射"}
        ]},
        "p3": {"label_ja": "第3段落", "items": [
            {"en": "intense", "ja": "〈形〉強烈な"},
            {"en": "cucumber", "ja": "〈名〉キュウリ"},
            {"en": "identify", "ja": "〈動〉識別する"},
            {"en": "primitive", "ja": "〈形〉未発達の"},
            {"en": "vegetation", "ja": "〈名〉植物"},
            {"en": "terminal", "ja": "〈形〉末端の"},
            {"en": "stylet", "ja": "〈名〉口針"},
            {"en": "digestive system", "ja": "消化器官"}
        ]},
        "p4": {"label_ja": "第4段落", "items": [
            {"en": "pharynx", "ja": "〈名〉咽頭"},
            {"en": "digestive juice", "ja": "消化液"},
            {"en": "salivary gland", "ja": "唾液腺"},
            {"en": "esophagus", "ja": "〈名〉食道"},
            {"en": "middle gut", "ja": "〈名〉中腸"},
            {"en": "nutrient", "ja": "〈名〉栄養物"},
            {"en": "anus", "ja": "〈名〉肛門"}
        ]},
        "questions": {"label_ja": "設問・選択肢", "items": [
            {"en": "feature", "ja": "〈名〉特徴"},
            {"en": "exceed", "ja": "〈他〉〜を超える"},
            {"en": "cease", "ja": "〈自〉終わる"},
            {"en": "withstand", "ja": "〈他〉〜に耐える"},
            {"en": "thrive", "ja": "〈自〉繁栄する"},
            {"en": "remarkable", "ja": "〈形〉注目に値する"},
            {"en": "outlive", "ja": "〈他〉〜より長生きする"},
            {"en": "infer", "ja": "〈他〉〜を推察する"}
        ]}
    }


def build_section6b():
    return {
        "section_number": "6B",
        "title": "第6問 B",
        "points": 12,
        "description": "長文読解（記事＋発表スライド）",
        "situation": {
            "en": "You are in a student group preparing for an international science presentation contest. You are using the following passage to create your part of the presentation on extraordinary creatures.",
            "ja": "あなたは，国際科学プレゼンテーションコンテストの準備をしている学生グループに所属している。あなたは，驚異的な生き物に関するプレゼンテーションの自分の担当部分を作成するため，次の文章を使用している。"
        },
        "passages": get_passages(),
        "questions": get_questions(),
        "vocabulary": get_vocabulary()
    }


def main():
    with open(DATA_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    data["sections"] = [s for s in data["sections"] if str(s["section_number"]) != "6B"]
    data["sections"].append(build_section6b())

    def sort_key(s):
        num = s["section_number"]
        if isinstance(num, int):
            return num
        if num == "6A":
            return 6.1
        if num == "6B":
            return 6.2
        return 99

    data["sections"].sort(key=sort_key)
    data["exam_info"]["implemented_sections"] = [s["section_number"] for s in data["sections"]]
    data["exam_info"]["format"] = "6AB"
    data["exam_info"]["section_list"] = [1, 2, 3, 4, 5, "6A", "6B"]

    with open(DATA_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Section 6B added/updated.")


if __name__ == "__main__":
    main()
