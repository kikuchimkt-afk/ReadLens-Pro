# -*- coding: utf-8 -*-
"""Build Section 7 and merge into data.json for 2025 Honshiken."""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from build_s7_passages import get_passages
from build_s7_questions import get_questions

DATA_JSON = os.path.join(os.path.dirname(__file__), "data.json")

def get_vocabulary():
    return {
        "p1": {
            "label_ja": "第1段落（If you ever spend ...）",
            "items": [
                {"en": "during the day", "ja": "日中は；昼間は"},
                {"en": "active", "ja": "〈形〉活動的な"},
                {"en": "on the other hand", "ja": "他方；それに対して"},
                {"en": "awake", "ja": "〈形〉目が覚めて"}
            ]
        },
        "p2": {
            "label_ja": "第2段落（Sleep is essential ...）",
            "items": [
                {"en": "essential", "ja": "〈形〉必要不可欠な"},
                {"en": "function", "ja": "〈動〉働く；機能する"},
                {"en": "efficiently", "ja": "〈副〉効率的に"},
                {"en": "central nervous system", "ja": "中枢神経系"},
                {"en": "define", "ja": "〈動〉…を定義する"},
                {"en": "altered state of consciousness", "ja": "意識変容状態"},
                {"en": "characterize", "ja": "〈動〉…を特徴づける"},
                {"en": "specific", "ja": "〈形〉特定の"},
                {"en": "position", "ja": "〈名〉姿勢"},
                {"en": "response", "ja": "〈名〉反応"},
                {"en": "neuron", "ja": "〈名〉神経単位"},
                {"en": "energize", "ja": "〈動〉…を元気〔活気〕づける"},
                {"en": "differ from species to species", "ja": "種によって異なる"}
            ]
        },
        "p3": {
            "label_ja": "第3段落（Different sleep patterns ...）",
            "items": [
                {"en": "identify", "ja": "〈動〉…を確認する"},
                {"en": "monophasic", "ja": "〈形〉単相の"},
                {"en": "biphasic", "ja": "〈形〉2相の"},
                {"en": "polyphasic", "ja": "〈形〉多相の"},
                {"en": "extended period", "ja": "長期間"},
                {"en": "mammal", "ja": "〈名〉哺乳動物"},
                {"en": "utilize", "ja": "〈動〉…を利用する"},
                {"en": "nap", "ja": "〈名〉うたた寝"}
            ]
        },
        "p4": {
            "label_ja": "第4段落（There are variations ...）",
            "items": [
                {"en": "variation", "ja": "〈名〉変化；変種"},
                {"en": "depending on ...", "ja": "…に応じて"},
                {"en": "diet", "ja": "〈名〉飲食物"},
                {"en": "squirrel", "ja": "〈名〉リス"},
                {"en": "use up", "ja": "使い果たす"},
                {"en": "result in ...", "ja": "…という結果になる"},
                {"en": "carnivorous", "ja": "〈形〉肉食性の"},
                {"en": "satisfy", "ja": "〈動〉…を満たす"},
                {"en": "hunger", "ja": "〈名〉飢え；空腹感"},
                {"en": "herbivore", "ja": "〈名〉草食動物"},
                {"en": "plant-based", "ja": "植物ベースの"},
                {"en": "relatively", "ja": "〈副〉比較的"}
            ]
        },
        "p5": {
            "label_ja": "第5段落（Safety is another variable ...）",
            "items": [
                {"en": "safety", "ja": "〈名〉安全"},
                {"en": "variable", "ja": "〈名〉変数；変化するもの"},
                {"en": "alert", "ja": "〈形〉警戒〔用心〕して"},
                {"en": "ape", "ja": "〈名〉類人猿；サル"},
                {"en": "platform", "ja": "〈名〉高台"},
                {"en": "floor", "ja": "〈名〉底；地面"},
                {"en": "keep A away from B", "ja": "AをBから遠ざけておく"},
                {"en": "shelter", "ja": "〈名〉避難所；住みか"},
                {"en": "predator", "ja": "〈名〉捕食動物"},
                {"en": "as a result", "ja": "その結果"},
                {"en": "in contrast", "ja": "対照的に"},
                {"en": "feel exposed to ...", "ja": "…にさらされていると感じる"},
                {"en": "contribute to ...", "ja": "…の一因となる"}
            ]
        },
        "p6": {
            "label_ja": "第6段落（The animal sleep patterns ...）",
            "items": [
                {"en": "so far", "ja": "これまで"},
                {"en": "typical", "ja": "〈形〉典型的な"},
                {"en": "unihemispheric", "ja": "〈形〉単半球の"},
                {"en": "keep O open", "ja": "Oを開けたままでいる"},
                {"en": "surroundings", "ja": "〈名〉環境"},
                {"en": "revive", "ja": "〈動〉…を生き返らせる；回復させる"},
                {"en": "watch out for ...", "ja": "…を警戒する"},
                {"en": "threat", "ja": "〈名〉脅威；おびやかすもの"},
                {"en": "outer edge", "ja": "外縁部"},
                {"en": "with both eyes closed", "ja": "両目を閉じたままで"}
            ]
        },
        "p7": {
            "label_ja": "第7段落（Besides the types ...）",
            "items": [
                {"en": "besides", "ja": "〈副〉…に加えて"},
                {"en": "hibernation", "ja": "〈名〉冬眠"},
                {"en": "inactive", "ja": "〈形〉不活発な"},
                {"en": "scarce", "ja": "〈形〉乏しい"},
                {"en": "heart rate", "ja": "心拍数"},
                {"en": "breathing", "ja": "〈名〉呼吸"},
                {"en": "jellyfish", "ja": "〈名〉クラゲ"},
                {"en": "relaxation", "ja": "〈名〉くつろぎ；弛緩"},
                {"en": "responsive", "ja": "〈形〉よく反応する；敏感な"}
            ]
        },
        "p8": {
            "label_ja": "最終段落（As shown above, ...）",
            "items": [
                {"en": "as shown above", "ja": "上に示されたように"},
                {"en": "play an important role in ...", "ja": "…において重要な役割を果たす"}
            ]
        }
    }

def build_section7():
    return {
        "section_number": 7,
        "title": "第7問",
        "points": 16,
        "description": "長文読解（記事＋プレゼンアウトライン）",
        "situation": {
            "en": "You are preparing a presentation for a science project on animal habits. You found some interesting information in the article below and are now making your outline.",
            "ja": "あなたは動物の習慣に関する理科の課題の発表準備をしています。あなたは以下の記事に興味深い情報を見つけたので，今アウトラインを作成しています。"
        },
        "passages": get_passages(),
        "questions": get_questions(),
        "vocabulary": get_vocabulary()
    }

def main():
    with open(DATA_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Remove existing section 7 if any
    data["sections"] = [s for s in data["sections"] if s["section_number"] != 7]

    # Add section 7
    sec7 = build_section7()
    data["sections"].append(sec7)

    # Sort sections by number
    def sort_key(s):
        n = s["section_number"]
        return int(n) if isinstance(n, int) else 99
    data["sections"].sort(key=sort_key)

    # Update implemented_sections
    impl = sorted(set(s["section_number"] for s in data["sections"]))
    data["exam_info"]["implemented_sections"] = impl

    with open(DATA_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Section 7 added. Total sections: {len(data['sections'])}")
    print(f"implemented_sections: {data['exam_info']['implemented_sections']}")
    # Quick validation
    s7 = [s for s in data["sections"] if s["section_number"] == 7][0]
    print(f"  Passages: {len(s7['passages'])}")
    print(f"  Questions: {len(s7['questions'])}")
    print(f"  Vocabulary groups: {len(s7['vocabulary'])}")

if __name__ == "__main__":
    main()
