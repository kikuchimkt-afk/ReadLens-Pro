# -*- coding: utf-8 -*-
"""Build Section 7 and merge into data.json for 2025 Tsuishiken."""
import json,sys,os
sys.path.insert(0,os.path.dirname(__file__))
from build_s7_passages import get_passages
from build_s7_questions import get_questions

DATA_JSON=os.path.join(os.path.dirname(__file__),"data.json")

def get_vocabulary():
    return {
        "p1":{"label_ja":"第1段落（Every day water flows ...）","items":[
            {"en":"flow","ja":"〈動〉流れる"},{"en":"pipe","ja":"〈名〉管；パイプ"},
            {"en":"bathing","ja":"〈名〉水浴び；入浴"},{"en":"liquid","ja":"〈名〉液体"},
            {"en":"distinct","ja":"〈形〉はっきりわかる"},{"en":"makeup","ja":"〈名〉構造；構成"}
        ]},
        "p2":{"label_ja":"第2段落（Natural water in the form of ...）","items":[
            {"en":"in the form of ...","ja":"…の形をして；…状の"},
            {"en":"absorb","ja":"〈動〉…を吸収する"},{"en":"calcium","ja":"〈名〉カルシウム"},
            {"en":"magnesium","ja":"〈名〉マグネシウム"},{"en":"according to ...","ja":"…によると"},
            {"en":"contain","ja":"〈動〉…を含む"},{"en":"milligram","ja":"〈名〉ミリグラム"},
            {"en":"mineral","ja":"〈名〉鉱物；ミネラル"},{"en":"per liter","ja":"1リットルにつき"},
            {"en":"further","ja":"〈副〉それ以上に"},{"en":"subdivide","ja":"〈動〉…を細分化する"},
            {"en":"moderately","ja":"〈副〉適度に"},{"en":"classify A as B","ja":"AをBとして分類する"},
            {"en":"in contrast","ja":"対照的に"},{"en":"content","ja":"〈名〉含有量"},
            {"en":"vary","ja":"〈動〉異なる；変化する"},{"en":"location","ja":"〈名〉場所"},
            {"en":"compare A with B","ja":"AをBと比較する"},{"en":"determine","ja":"〈動〉…を特定[確定]する"},
            {"en":"on the ... side","ja":"多少…気味で"},{"en":"whereas","ja":"〈接〉…だが一方"},
            {"en":"depend more on A than (on) B","ja":"BよりもAに依存する"},
            {"en":"raw water","ja":"原水"},{"en":"unpurified","ja":"〈形〉未浄化の"},
            {"en":"purification","ja":"〈名〉浄化"},{"en":"process","ja":"〈名〉過程"},
            {"en":"transportation","ja":"〈名〉輸送"}
        ]},
        "p3":{"label_ja":"第3段落（There are several variables ...）","items":[
            {"en":"variable","ja":"〈名〉変化するもの；不確定要素"},
            {"en":"affect","ja":"〈動〉…に影響する"},{"en":"include","ja":"〈動〉…を含む"},
            {"en":"region","ja":"〈名〉地域；地方"},{"en":"urbanization","ja":"〈名〉都市化"},
            {"en":"underground","ja":"〈形〉地下の"},{"en":"source","ja":"〈名〉（水）源"},
            {"en":"dissolve","ja":"〈動〉溶ける"},{"en":"in addition","ja":"さらに；加えて"},
            {"en":"movement","ja":"〈名〉移動"},{"en":"industry","ja":"〈名〉産業；工業"},
            {"en":"A as well as B","ja":"Bと同様にAも；AのほかにBも"},
            {"en":"infrastructure","ja":"〈名〉インフラ"}
        ]},
        "p4":{"label_ja":"第4段落（Since the properties ...）","items":[
            {"en":"property","ja":"〈名〉特質；特性"},{"en":"differ","ja":"〈動〉異なる"},
            {"en":"soap","ja":"〈名〉石けん"},{"en":"detergent","ja":"〈名〉洗剤"},
            {"en":"lather","ja":"〈名〉（石けんなどによる）泡"},{"en":"bubble","ja":"〈名〉泡"},
            {"en":"skin","ja":"〈名〉皮膚；肌"},{"en":"spot","ja":"〈名〉斑点；しみ"},
            {"en":"cutlery","ja":"〈名〉（ナイフ・フォーク・スプーンなどの）食卓用器具"},
            {"en":"limescale","ja":"〈名〉水あか"},{"en":"substance","ja":"〈名〉物質"},
            {"en":"restrict","ja":"〈動〉…を制限する；妨げる"},{"en":"discolor","ja":"〈動〉…を退色[変色]させる"},
            {"en":"damage","ja":"〈動〉…を損なう"},{"en":"appliance","ja":"〈名〉器具"},
            {"en":"as well","ja":"…もまた"},{"en":"despite","ja":"〈前〉…にもかかわらず"},
            {"en":"aspect","ja":"〈名〉側面"},{"en":"rate","ja":"〈動〉格付けされる"},
            {"en":"beneficial","ja":"〈形〉有益な"},{"en":"boost","ja":"〈動〉…を増大させる"},
            {"en":"intake","ja":"〈名〉摂取量"}
        ]},
        "p5":{"label_ja":"第5段落（If the water ...）","items":[
            {"en":"electricity","ja":"〈名〉電気"},{"en":"rinse out","ja":"水洗いで落ちる"},
            {"en":"efficiently","ja":"〈副〉効率的に"},{"en":"last","ja":"〈動〉もつ；使える"},
            {"en":"wear out","ja":"すり減る"},{"en":"tap water","ja":"水道水"},
            {"en":"soften","ja":"〈動〉…を軟らかくする"},{"en":"device","ja":"〈名〉装置"},
            {"en":"attach A to B","ja":"AをBに取り付ける"},{"en":"remove","ja":"〈動〉…を取り除く"},
            {"en":"filter","ja":"〈動〉…をろ過する"},{"en":"filtration","ja":"〈名〉ろ過"},
            {"en":"bead","ja":"〈名〉ビーズ；じゅず玉"},
            {"en":"positively charged","ja":"正電気を帯びた"},{"en":"potassium ion","ja":"カリウムイオン"},
            {"en":"attract","ja":"〈動〉…を引きつける"},{"en":"salty","ja":"〈形〉塩辛い"}
        ]},
        "p6":{"label_ja":"第6段落（If water filtration systems ...）","items":[
            {"en":"costly","ja":"〈形〉費用がかかる"},{"en":"maintain","ja":"〈動〉…を維持する"},
            {"en":"remedy","ja":"〈名〉解決策；改善法"},{"en":"solve","ja":"〈動〉…を解決する"},
            {"en":"boil","ja":"〈動〉…を沸かす"},{"en":"vinegar","ja":"〈名〉酢"},
            {"en":"baking soda","ja":"重曹"},{"en":"react","ja":"〈動〉反応する"},
            {"en":"neutralize","ja":"〈動〉…を中和する"},{"en":"supplement","ja":"〈名〉補足するもの"}
        ]},
        "p7":{"label_ja":"最終段落（Now that we know ...）","items":[
            {"en":"now that ...","ja":"今や…なので"},{"en":"mix","ja":"〈名〉混合（物）；組み合わせ"}
        ]},
        "outline":{"label_ja":"発表のアウトライン","items":[
            {"en":"result","ja":"〈名〉結果"},{"en":"factor","ja":"〈名〉要因；要素"},
            {"en":"increased","ja":"〈形〉増加した"},{"en":"regional","ja":"〈形〉地域による"},
            {"en":"climate","ja":"〈名〉気候"},{"en":"raindrop","ja":"〈名〉雨滴"}
        ]},
        "questions":{"label_ja":"設問文・選択肢","items":[
            {"en":"details","ja":"〈名〉詳細な情報"},{"en":"characteristic","ja":"〈名〉特徴"},
            {"en":"ingredient","ja":"〈名〉材料"},{"en":"consumption","ja":"〈名〉消費"},
            {"en":"spot","ja":"〈動〉…を見つける"},{"en":"get rid of ...","ja":"…を取り除く"},
            {"en":"ineffective","ja":"〈形〉効果がない"},{"en":"positively","ja":"〈副〉肯定的に；よい方向に"},
            {"en":"effective","ja":"〈形〉効果的な"},{"en":"improve","ja":"〈動〉…を改善する"}
        ]}
    }

def build_section7():
    return {
        "section_number":7,"title":"第7問","points":15,
        "description":"長文読解（記事＋発表アウトライン）",
        "situation":{
            "en":"You are preparing for a presentation in your science class. You found an interesting article and are now creating an outline.",
            "ja":"あなたは理科のクラスでの発表の準備をしています。下の記事の中に興味深い情報を見つけたので，現在アウトラインを作成しています。"
        },
        "passages":get_passages(),
        "questions":get_questions(),
        "vocabulary":get_vocabulary()
    }

def main():
    with open(DATA_JSON,"r",encoding="utf-8") as f:
        data=json.load(f)
    data["sections"]=[s for s in data["sections"] if s["section_number"]!=7]
    data["sections"].append(build_section7())
    data["sections"].sort(key=lambda s:int(s["section_number"]) if isinstance(s["section_number"],int) else 99)
    impl=sorted(set(s["section_number"] for s in data["sections"]))
    data["exam_info"]["implemented_sections"]=impl
    with open(DATA_JSON,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)
    print(f"Section 7 added. Total sections: {len(data['sections'])}")
    print(f"implemented_sections: {data['exam_info']['implemented_sections']}")

if __name__=="__main__":
    main()
