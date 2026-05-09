# -*- coding: utf-8 -*-
"""Build Section 8 and merge into data.json for 2025 Tsuishiken."""
import json,sys,os
sys.path.insert(0,os.path.dirname(__file__))
from build_s8_part1 import get_passages
from build_s8_part2 import get_questions

DATA_JSON=os.path.join(os.path.dirname(__file__),"data.json")

def get_vocabulary():
    return {
        "step1_aya":{"label_ja":"Aya","items":[
            {"en":"advisor","ja":"〈名〉顧問"},{"en":"in terms of ...","ja":"…の点で"},
            {"en":"be unusual in that ...","ja":"…という点で珍しい"},{"en":"in principle","ja":"原則的に"},
            {"en":"apart from ...","ja":"…は別にして"},{"en":"nevertheless","ja":"〈副〉それにもかかわらず"},
            {"en":"boost","ja":"〈動〉…を増大させる"},{"en":"purchase","ja":"〈動〉…を購入する"},
            {"en":"employ","ja":"〈動〉…を雇う"},{"en":"infrastructure","ja":"〈名〉インフラ"},
            {"en":"medical","ja":"〈形〉医療の"},{"en":"benefit","ja":"〈名〉利益；恩恵"},
            {"en":"provide","ja":"〈動〉…を提供する；もたらす"},{"en":"include","ja":"〈動〉…を含む"},
            {"en":"collaborate with A on B","ja":"BをAと共同で行う"}
        ]},
        "step1_david":{"label_ja":"David","items":[
            {"en":"urban","ja":"〈形〉都市の"},{"en":"planner","ja":"〈名〉設計家"},
            {"en":"located","ja":"〈形〉位置して；存在して"},{"en":"ensure (that) ...","ja":"確実に…するようにする"},
            {"en":"economically","ja":"〈副〉経済的に"},{"en":"viable","ja":"〈形〉実行できる"},
            {"en":"man-eating","ja":"〈形〉人喰いの"},{"en":"a sea of ...","ja":"たくさんの…"},
            {"en":"huge","ja":"〈形〉巨大な"},{"en":"risk","ja":"〈名〉危険；リスク"},
            {"en":"bear","ja":"〈名〉クマ"},{"en":"escape","ja":"〈動〉逃げる"},
            {"en":"flooding","ja":"〈名〉洪水"},{"en":"pose","ja":"〈動〉…を引き起こす"},
            {"en":"citizen","ja":"〈名〉国民；市民"},{"en":"safety","ja":"〈名〉安全"}
        ]},
        "step1_indira":{"label_ja":"Indira","items":[
            {"en":"prison","ja":"〈名〉刑務所；監獄"},{"en":"imagine","ja":"〈動〉…を想像する"},
            {"en":"cheetah","ja":"〈名〉チータ"},{"en":"used to -ing","ja":"…することに慣れている"},
            {"en":"distance","ja":"〈名〉距離"},{"en":"lock up","ja":"閉じ込める"},
            {"en":"for the rest of one\u2019s life","ja":"その後死ぬまで"},
            {"en":"relatively","ja":"〈副〉比較的"},{"en":"stimulation","ja":"〈名〉刺激"},
            {"en":"noisy","ja":"〈形〉騒がしい"},{"en":"expose A to B","ja":"AをBにさらす"},
            {"en":"cruel","ja":"〈形〉残酷な"},{"en":"treatment","ja":"〈名〉扱い"}
        ]},
        "step1_kenyatta":{"label_ja":"Kenyatta","items":[
            {"en":"perform","ja":"〈動〉…を行う；果たす"},{"en":"relation","ja":"〈名〉関係"},
            {"en":"politics","ja":"〈名〉政治"},{"en":"whereby","ja":"〈副〉それによって…"},
            {"en":"loan","ja":"〈動〉…を貸し出す"},{"en":"deal","ja":"〈名〉取引"},
            {"en":"be symbolic of ...","ja":"…を象徴する"},{"en":"in demand","ja":"需要がある"},
            {"en":"temporarily","ja":"〈副〉一時的に"},{"en":"swap","ja":"〈動〉交換する"},
            {"en":"treaty","ja":"〈名〉条約；協定"},{"en":"painting","ja":"〈名〉絵"},
            {"en":"promote","ja":"〈動〉…を促進する"},{"en":"mutual","ja":"〈形〉相互の"},
            {"en":"flow","ja":"〈名〉流れ"},{"en":"zoological","ja":"〈形〉動物学の"},
            {"en":"improve","ja":"〈動〉…を改善する"},{"en":"global","ja":"〈形〉全世界の"},
            {"en":"connectivity","ja":"〈名〉接続性"}
        ]},
        "step1_yo":{"label_ja":"Yo","items":[
            {"en":"pandemic","ja":"〈名〉世界的な流行病；パンデミック"},
            {"en":"migration","ja":"〈名〉移住；移動"},{"en":"virus","ja":"〈名〉ウイルス"},
            {"en":"so-called","ja":"〈形〉いわゆる"},{"en":"live","ja":"〈形〉生きている"},
            {"en":"potential","ja":"〈形〉潜在的な"},{"en":"source","ja":"〈名〉源"},
            {"en":"given","ja":"〈前〉…を考慮に入れると"},
            {"en":"disruption","ja":"〈名〉混乱；中断"},{"en":"bring about ...","ja":"…をもたらす"},
            {"en":"guarantee","ja":"〈動〉…を保証する"},{"en":"proper","ja":"〈形〉適切な"},
            {"en":"procedure","ja":"〈名〉方法；手順"},{"en":"leap","ja":"〈名〉跳躍"},
            {"en":"species","ja":"〈名〉（分類上の）種"},{"en":"occur","ja":"〈動〉起こる"}
        ]},
        "step2":{"label_ja":"ステップ2","items":[
            {"en":"actively","ja":"〈副〉積極的に"},{"en":"maintain","ja":"〈動〉…を維持する"},
            {"en":"welfare","ja":"〈名〉幸福"},{"en":"priority","ja":"〈名〉優先事項"},
            {"en":"knowledge","ja":"〈名〉知識"}
        ]},
        "source_a":{"label_ja":"資料A","items":[
            {"en":"according to ...","ja":"…によると"},{"en":"publish","ja":"〈動〉…を出版する；発表する"},
            {"en":"conservation","ja":"〈名〉保護；保全"},
            {"en":"regard A as B","ja":"AをBとみなす"},{"en":"(be) threatened with ...","ja":"…の危機に瀕している"},
            {"en":"extinction","ja":"〈名〉絶滅"},{"en":"approximately","ja":"〈副〉おおよそ"},
            {"en":"prevent O from -ing","ja":"Oが～するのを妨げる"},{"en":"endangered","ja":"〈形〉絶滅の危機にある"},
            {"en":"restore","ja":"〈動〉…を回復する"},{"en":"method","ja":"〈名〉方法；方式"},
            {"en":"adopt","ja":"〈動〉…を採用する"},{"en":"on-site","ja":"〈形〉現場での"},
            {"en":"off-site","ja":"〈形〉現場を離れた"},{"en":"the former [latter]","ja":"前者 [後者]"},
            {"en":"preserve","ja":"〈動〉…を保存する"},{"en":"surroundings","ja":"〈名〉環境"},
            {"en":"breed","ja":"〈動〉…を繁殖させる；飼育する"},
            {"en":"in captivity","ja":"とらわれの身で；動物園に入れられて"},
            {"en":"aim to ...","ja":"…しようと試みる"},{"en":"be involved in ...","ja":"…に参加している [関わっている]"},
            {"en":"disappear","ja":"〈動〉姿を消す"},{"en":"due to ...","ja":"…が原因で"},
            {"en":"effort","ja":"〈名〉努力"}
        ]},
        "source_b":{"label_ja":"資料B","items":[
            {"en":"kid","ja":"〈名〉子ども"},{"en":"aged X (years)","ja":"X歳の"},
            {"en":"check","ja":"〈動〉…にチェックの印をつける"},{"en":"including","ja":"〈前〉…を含めて"}
        ]},
        "questions":{"label_ja":"設問文・選択肢","items":[
            {"en":"rare","ja":"〈形〉珍しい；まれな"},{"en":"reappear","ja":"〈動〉再び現れる"},
            {"en":"fund","ja":"〈動〉…に資金を提供する"},{"en":"path","ja":"〈名〉（小）道"},
            {"en":"on the rise","ja":"増加している"},{"en":"broad","ja":"〈形〉広い"},
            {"en":"abandoned","ja":"〈形〉捨てられた"},{"en":"popular","ja":"〈形〉人気のある"},
            {"en":"commonly","ja":"〈副〉一般に"},{"en":"reportedly","ja":"〈副〉伝えられるところによると"},
            {"en":"unique","ja":"〈形〉独特の"},{"en":"a variety of ...","ja":"いろいろの…"},
            {"en":"prefer","ja":"〈動〉より好む"},
            {"en":"summarize","ja":"〈動〉…を要約する"},{"en":"mistreatment","ja":"〈名〉不当な扱い；虐待"},
            {"en":"observation","ja":"〈名〉観察"},{"en":"suffering","ja":"〈名〉苦しいこと"},
            {"en":"infectious","ja":"〈形〉感染性の"},{"en":"harm","ja":"〈名〉害"},
            {"en":"protect","ja":"〈動〉…を保護する"}
        ]}
    }

def build_section8():
    return {
        "section_number":8,"title":"第8問","points":17,
        "description":"エッセイ型（意見読解＋資料活用＋アウトライン作成）",
        "situation":{
            "en":"You are working on an essay about <strong>zoos</strong>. You will follow the steps below:",
            "ja":"あなたは動物園についてのエッセイに取り組んでいます。あなたは以下のステップに従います：",
            "steps":[
                {"en":"<strong>Step 1</strong>: Read a range of opinions gathered from the Internet about the pros and cons of zoos.","ja":"ステップ1：インターネットから集めた動物園の賛否に関する幅広い意見を読む。"},
                {"en":"<strong>Step 2</strong>: Take a position on zoos.","ja":"ステップ2：動物園に関する見解を固める。"},
                {"en":"<strong>Step 3</strong>: Create an outline of your essay using additional sources.","ja":"ステップ3：さらなる資料を利用してエッセイのアウトラインを作成する。"}
            ]
        },
        "passages":get_passages(),
        "questions":get_questions(),
        "vocabulary":get_vocabulary()
    }

def main():
    with open(DATA_JSON,"r",encoding="utf-8") as f:
        data=json.load(f)
    data["sections"]=[s for s in data["sections"] if s["section_number"]!=8]
    data["sections"].append(build_section8())
    data["sections"].sort(key=lambda s:int(s["section_number"]) if isinstance(s["section_number"],int) else 99)
    impl=sorted(set(s["section_number"] for s in data["sections"]))
    data["exam_info"]["implemented_sections"]=impl
    with open(DATA_JSON,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)
    print(f"Section 8 added. Total sections: {len(data['sections'])}")
    print(f"implemented_sections: {data['exam_info']['implemented_sections']}")
    s8=[s for s in data["sections"] if s["section_number"]==8][0]
    print(f"  Passages: {len(s8['passages'])}")
    print(f"  Questions: {len(s8['questions'])}")

if __name__=="__main__":
    main()
