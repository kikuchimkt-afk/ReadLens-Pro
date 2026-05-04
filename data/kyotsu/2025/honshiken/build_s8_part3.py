# -*- coding: utf-8 -*-
# Part3: Vocabulary + Final builder
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_s8_part1 import get_passages
from build_s8_part2 import get_questions

def get_vocab():
    return {"passage":{"label_ja":"主な語句・表現","items":[
        {"en":"exploration","ja":"探検"},{"en":"require O","ja":"Oを必要とする"},
        {"en":"lead to ...","ja":"…をもたらす"},{"en":"invention","ja":"発明（品）"},
        {"en":"boost O","ja":"Oを高める；増やす"},{"en":"humanity","ja":"人類"},
        {"en":"surgery","ja":"外科手術"},{"en":"solar cell","ja":"太陽電池"},
        {"en":"come out of ...","ja":"…から生じる"},
        {"en":"CEO","ja":"最高経営責任者（chief executive officer）"},
        {"en":"rely on ...","ja":"…に依存する"},{"en":"cooperation","ja":"協力"},
        {"en":"launch O","ja":"Oを打ち上げる"},{"en":"costs involved","ja":"必要となる費用"},
        {"en":"prestige","ja":"威信；名声"},{"en":"commercial","ja":"商業的な"},
        {"en":"colonize O","ja":"Oに植民地を建設する"},{"en":"Mars","ja":"火星"},
        {"en":"corporation","ja":"法人；大企業"},{"en":"military","ja":"軍事的な"},
        {"en":"physicist","ja":"物理学者"},{"en":"broadcast O","ja":"Oを放送する；…を伝える"},
        {"en":"existence","ja":"存在"},{"en":"intelligent","ja":"知能の高い"},
        {"en":"alien","ja":"異星人（の）"},{"en":"anything like ...","ja":"いくらかでも…のような"},
        {"en":"conquer O","ja":"Oを征服する"},{"en":"threat","ja":"脅威"},
        {"en":"associated with ...","ja":"…と関連づけられる"},{"en":"likelihood","ja":"可能性"},
        {"en":"aggressive","ja":"攻撃的な"},
        {"en":"likely","ja":"たぶん"},{"en":"if not ...","ja":"…ではないにしても"},
        {"en":"... or so","ja":"…かそこら"},{"en":"oxygen","ja":"酸素"},
        {"en":"survival","ja":"生存"},{"en":"astronaut","ja":"宇宙飛行士"},
        {"en":"fatality rate","ja":"死亡率"},{"en":"tolerate O","ja":"Oを大目に見る；我慢する"},
        {"en":"analyst","ja":"分析者；アナリスト"},
        {"en":"contribute (A) to B","ja":"（Aの分だけ）Bに貢献する"},
        {"en":"provide A for B","ja":"AをBに供給する"},
        {"en":"estimate O","ja":"Oを見積もる"},{"en":"billion","ja":"10億"},
        {"en":"ensure O","ja":"Oを確実にする；保証する"},
        {"en":"private firm","ja":"民間会社（企業）"},
        {"en":"mining","ja":"採掘；鉱業"},{"en":"militarization","ja":"軍事化"},
        {"en":"reconsideration","ja":"再考"},{"en":"without doubt","ja":"疑いなく；確かに"},
        {"en":"frontline","ja":"最前線"},{"en":"priority","ja":"優先事項"},
        {"en":"following","ja":"次にあげる"},{"en":"based on ...","ja":"…に基づいて"},
        {"en":"aspect","ja":"面；側"},{"en":"prioritize A over B","ja":"BよりもAを優先する"},
        {"en":"connection","ja":"関係；関連"},{"en":"emission","ja":"排出（量）"},
        {"en":"emit O","ja":"Oを排出する"},{"en":"(space)craft","ja":"宇宙船"},
        {"en":"insignificant","ja":"重要でない；ささいな"},
        {"en":"atmosphere","ja":"大気（圏）"},{"en":"damaging","ja":"ダメージを与える；有害な"},
        {"en":"the contribution to A of B","ja":"BがAの一因となっていること"},
        {"en":"greenhouse effect","ja":"温室効果"},{"en":"thermosphere","ja":"熱圏"},
        {"en":"debris","ja":"破片；残骸"},{"en":"junk O","ja":"Oを廃棄する"},
        {"en":"artificial satellite","ja":"人工衛星"},{"en":"on the rise","ja":"上昇中で"},
        {"en":"up to ...","ja":"最大…まで"},
        {"en":"pose a risk to ...","ja":"…に危険をもたらす"},
        {"en":"potential","ja":"潜在的な"},{"en":"obstacle","ja":"障害物"},
        {"en":"astronomical observation","ja":"天体観測"},
        {"en":"costly","ja":"費用のかかる"},{"en":"compare A with B","ja":"AをBと比較する"},
        {"en":"annual budget","ja":"年間予算"},{"en":"institution","ja":"団体；機関"},
        {"en":"investment","ja":"投資"},{"en":"relieve O","ja":"Oを軽減（緩和）する"},
        {"en":"hunger","ja":"飢餓"}
    ]}}

def build():
    section = {
        "section_number": 8,
        "title": "第8問",
        "points": 17,
        "description": "エッセイ作成（意見読解＋資料活用）",
        "situation": {
            "en": "You are working on an essay about space exploration. You will follow the steps below:\nStep 1: Read a range of opinions gathered from the Internet about exploring outer space.\nStep 2: Take a position on space exploration.\nStep 3: Create an outline of your essay using additional sources.",
            "ja": "あなたは宇宙探検についてのエッセイに取り組んでいて，以下のステップに従う。\nステップ1：宇宙空間の探検に関する幅広い意見をインターネットから集めて読む。\nステップ2：宇宙探検に関する見解を固める。\nステップ3：さらなる資料を利用してエッセイのアウトラインを作成する。"
        },
        "passages": get_passages(),
        "questions": get_questions(),
        "vocabulary": get_vocab()
    }
    data = {
        "exam_info": {
            "title": "共通テスト 2025年度 本試験",
            "publisher": "大学入試センター",
            "year": 2025,
            "round": "本試験",
            "subject": "英語（リーディング）",
            "time_limit_minutes": 80,
            "implemented_sections": [8]
        },
        "sections": [section]
    }
    out = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'Built {out}')
    print(f'  Sections: {len(data["sections"])}')
    print(f'  Questions: {len(section["questions"])}')
    print(f'  Vocab items: {len(get_vocab()["passage"]["items"])}')

if __name__ == '__main__':
    build()
