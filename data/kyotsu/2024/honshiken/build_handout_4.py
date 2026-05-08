import json
import os

def main():
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, 'data.json')

    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for sec in data.get('sections', []):
        if sec.get('section_number') == 4:
            passages = sec.get('passages', [])
            for sub in sec.get('subsections', []):
                passages.extend(sub.get('passages', []))
            
            for p in passages:
                if p.get('id') == 'handout_4':
                    p['is_handout'] = True
                    # Remove framed, paragraphs, sentences
                    if 'framed' in p: del p['framed']
                    if 'paragraphs' in p: del p['paragraphs']
                    if 'sentences' in p: del p['sentences']
                    
                    p['sections_content'] = [
                        {
                            "heading": {
                                "en": "SIN Framework",
                                "ja": "SIN フレームワーク"
                            },
                            "items": [
                                {
                                    "en": "What it is: [24]",
                                    "ja": "どういうものか：[24]"
                                },
                                {
                                    "en": "SIN = Stimulation, Individualization, Naturalness",
                                    "ja": "SIN = 「刺激 (Stimulation)」, 「個別化 (Individualization)」, 「自然らしさ (Naturalness)」"
                                }
                            ]
                        },
                        {
                            "heading": {
                                "en": "Design Recommendations Based on SIN and Questionnaire Results",
                                "ja": "SIN とアンケート結果に基づくデザインの推奨案"
                            },
                            "sub_items": [
                                {
                                    "label": {
                                        "en": "Stimulation:",
                                        "ja": "「刺激」："
                                    },
                                    "content": {
                                        "en": "Cover the floor with a colorful rug and [25].",
                                        "ja": "床に色彩豊かな絨毯を敷いて，[25]。"
                                    }
                                },
                                {
                                    "label": {
                                        "en": "Individualization:",
                                        "ja": "「個別化」："
                                    },
                                    "content": {
                                        "en": "Replace room furniture.\n(tables with wheels → easy to move around)",
                                        "ja": "部室の家具類を取り替える。\n(キャスター付きのテーブル→移動が簡単)"
                                    }
                                },
                                {
                                    "label": {
                                        "en": "Naturalness:",
                                        "ja": "「自然らしさ」："
                                    },
                                    "content": {
                                        "en": "[26]\nA. Install blinds on windows.\nB. Make temperature control possible.\nC. Move projector screen away from windows.\nD. Place sofas near walls.\nE. Put floor lamp in darker corner.",
                                        "ja": "[26]\nA. 窓に日除けを取り付ける。\nB. 温度調節を可能にする。\nC. プロジェクターのスクリーンを窓から離す。\nD. ソファを壁の近くに置く。\nE. 暗い方のコーナーにフロアランプを置く。"
                                    }
                                }
                            ]
                        },
                        {
                            "heading": {
                                "en": "Other Issues to Discuss",
                                "ja": "その他の議論すべき問題"
                            },
                            "items": [
                                {
                                    "en": "The majority of members [27] the room, as mentioned in [28]'s comment. How can we improve this?",
                                    "ja": "[28]のコメントが触れているように，部員の大多数が部室[27]。これはどうすれば改善できるか？"
                                },
                                {
                                    "en": "Based on both the graph and [29]'s comment, should we make a rule about language in the room to motivate members to speak English more?",
                                    "ja": "グラフと[29]のコメントに基づいて，部員たちに英語をもっと話そうという気にさせるため，部室内での言葉に関するルールを定める方がよいだろうか？"
                                },
                                {
                                    "en": "S5 doesn't like the location of the room, but we cannot change rooms, so let's think of ways to encourage members to visit the room more often.",
                                    "ja": "S5は部室の場所が好きではないが，部室を変更することはできないので，部員が部室をより頻繁に訪れるのを促す方法を考えよう。"
                                }
                            ]
                        }
                    ]

    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print("Handout layout updated successfully!")

if __name__ == '__main__':
    main()
