# -*- coding: utf-8 -*-
"""Z会 実戦模試 2026 第1回 第7問 を data.json にマージする。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def para(rows):
    return [{"id": i, "en": e, "ja": j} for i, e, j in rows]


# 本文は問題冊子・解説の趣旨に沿って清書（ユーザ提供画像の英文に準拠）
ARTICLE = [
    para(
        [
            ("uv_p1_s1", "We are surrounded by light every day.", "私たちは日々光に囲まれている。"),
            (
                "uv_p1_s2",
                "In fact, many different kinds of light shape our world in ways that we do not always think about.",
                "実際，さまざまな種類の光が，私たちがいつも意識しているとは限らない形で世界を形づくっている。",
            ),
            (
                "uv_p1_s3",
                "Not only does light help us see, but it also makes us feel happier and helps us sleep better.",
                "光は見るのを助けるだけでなく，気持ちをより明るくさせ，よりよく眠るのにも役立ってくれる。",
            ),
            (
                "uv_p1_s4",
                "Among the many kinds of light, ultraviolet (UV) light is particularly interesting, as it affects our lives in many different ways.",
                "多くの種類の光の中でも，紫外線はとりわけ興味深く，私たちの生活にさまざまな形で影響を及ぼす。",
            ),
        ]
    ),
    para(
        [
            (
                "uv_p2_s1",
                "UV light is a type of radiation that comes from the sun, and it is divided into three types: UVA, UVB, and UVC.",
                "紫外線は太陽由来の放射線の一種であり，UVA，UVB，UVCの3種類に分けられる。",
            ),
            (
                "uv_p2_s2",
                "UVA makes up about 95% of the UV radiation that reaches Earth and gives off the least amount of energy.",
                "UVAは地球に届く紫外線の約95％を占め，最もエネルギー放出量が少ない。",
            ),
            (
                "uv_p2_s3",
                "However, it is potentially harmful because it can penetrate, or reach, deep into human skin.",
                "しかし，ヒトの肌の奥深くまで浸透する，つまり届く可能性があるので，有害になりうる。",
            ),
            (
                "uv_p2_s4",
                "UVB is mostly blocked by the atmosphere, making up the remaining 5% of the radiation Earth receives.",
                "UVBは大気によってほとんど遮られ，地球が受ける放射線の残りの約5％を占める。",
            ),
            (
                "uv_p2_s5",
                "Exposure to UVB increases the risk of cellular damage and DNA mutations in living organisms.",
                "UVBへのさらされは，生物における細胞障害やDNA突然変異のリスクを高める。",
            ),
            (
                "uv_p2_s6",
                "UVC, on the other hand, gives off the most energy and is the most dangerous.",
                "一方，UVCは最も多くのエネルギーを放出し，最も危険である。",
            ),
            (
                "uv_p2_s7",
                "However, it is completely blocked by the Earth's atmosphere.",
                "しかし，それは地球の大気によって完全に遮断される。",
            ),
            (
                "uv_p2_s8",
                "People only encounter UVC from special products like sanitizing lamps.",
                "ヒトがUVCに触れるのは，殺菌灯など特別な製品からだけである。",
            ),
            (
                "uv_p2_s9",
                "Besides, these products are typically built with features to protect us from the radiation.",
                "しかも，そのような製品は通常，放射線から私たちを守る機能が組み込まれている。",
            ),
        ]
    ),
    para(
        [
            (
                "uv_p3_s1",
                "One of the benefits of UV light is that it helps our bodies produce vitamin D, which is important for our health.",
                "紫外線の利点のひとつは，健康に欠かせないビタミンDを私たちの体内でつくるのを助けることである。",
            ),
            (
                "uv_p3_s2",
                "Vitamin D helps the absorption of calcium, which is responsible for building strong bones and muscles.",
                "ビタミンDはカルシウムの吸収を助け，強い骨や筋肉をつくるうえで必要である。",
            ),
            (
                "uv_p3_s3",
                "It also helps improve heart function, reduces symptoms of depression (a medical condition that makes a person feel sad or hopeless), and strengthens the immune system, which keeps us healthy.",
                "また心臓のはたらきを改善し，うつ（人を悲観的・絶望的な気持ちにさせる医学的状態）の症状を減らし，私たちを健康に保つ免疫システムを強化するのにも役立つ。",
            ),
            (
                "uv_p3_s4",
                "We can get a small amount of vitamin D from food, but the best natural source of it is sunlight.",
                "ビタミンDは食べ物からも少量摂れるが，最もよい天然の供給源は日光である。",
            ),
        ]
    ),
    para(
        [
            (
                "uv_p4_s1",
                "While UV light is beneficial, it can also be harmful.",
                "紫外線には有益な面もあるが，有害になりうる面もある。",
            ),
            (
                "uv_p4_s2",
                "Too much UV light damages all skin types, causing early aging, wrinkles, and sometimes even cancer.",
                "紫外線を浴びすぎるとあらゆる肌タイプにダメージを与え，早期老化やしわの原因になり，ときにはがんにつながることもある。",
            ),
            (
                "uv_p4_s3",
                "However, not all skin is affected in the same way.",
                "しかし，肌への影響はすべて同じというわけではない。",
            ),
            (
                "uv_p4_s4",
                "For instance, lighter skin burns quickly in the sun, while darker skin absorbs more UV light and burns less easily.",
                "たとえば，色の薄い肌は日光ですぐに赤くなるが，色の濃い肌はより多くの紫外線を吸収し，赤くなりにくい。",
            ),
            (
                "uv_p4_s5",
                "Too much UV light can also affect our eyes, increasing the risk of cataracts, a condition where the lens of the eye becomes cloudy.",
                "紫外線を浴びすぎると目にも影響が及び，眼球の水晶体が濁る白内障のリスクが高まる。",
            ),
            (
                "uv_p4_s6",
                "Over time, it can also break down proteins in the eyes, possibly leading to loss of sight.",
                "時間が経つにつれ，目の中のたんぱく質を分解し，視力喪失につながることもある。",
            ),
        ]
    ),
    para(
        [
            (
                "uv_p5_s1",
                "The same qualities of UV light that create risks for us can also be used to make us safer.",
                "私たちにリスクをもたらす紫外線の性質は，私たちをより安全にするためにも利用できる。",
            ),
            (
                "uv_p5_s2",
                "For example, humans can create UVC light and use it to kill germs, tiny harmful organisms.",
                "たとえば，ヒトはUVC光を人工的につくり，有害な微小生物である細菌などを殺すのに使うことができる。",
            ),
            (
                "uv_p5_s3",
                "Hospitals have been using this method to clean equipment, and even the air inside of rooms for decades.",
                "病院では何十年も前からこの方法で器具や室内の空気さえも清浄にしてきた。",
            ),
            (
                "uv_p5_s4",
                "The UVC light destroys the ability of germs to reproduce, limiting their ability to spread.",
                "UVC光は細菌などの繁殖能力を破壊し，その拡散を抑える。",
            ),
        ]
    ),
    para(
        [
            (
                "uv_p6_s1",
                "Despite the effectiveness of using UVC light to clean rooms, it is necessary to understand some of the possible risks.",
                "部屋の清浄にUVC光を使うことは効果的だが，考えられるリスクを理解しておくことも必要である。",
            ),
            (
                "uv_p6_s2",
                "When using UV light indoors, chemical reactions happen.",
                "屋内で紫外線を使うと，化学反応が起こる。",
            ),
            (
                "uv_p6_s3",
                "These reactions turn the oxygen in a room into ozone, which is a dangerous type of gas.",
                "その反応によって室内の酸素がオゾンという危険な気体に変わる。",
            ),
            (
                "uv_p6_s4",
                "The ozone created can lead to more chemical reactions that produce other dangerous chemicals.",
                "できあがったオゾンがさらなる化学反応を引き起こし，ほかの有害な化学物質を生み出すことがある。",
            ),
            (
                "uv_p6_s5",
                "As rooms often have limited airflow, these harmful substances can build up.",
                "室内では空気の流れが限られることが多いので，これらの有害物質が蓄積しうる。",
            ),
            (
                "uv_p6_s6",
                "Over time, the air becomes dangerous to breathe.",
                "時間が経つにつれ，息をするのに危険な空気になる。",
            ),
            (
                "uv_p6_s7",
                "When using UV light indoors, you must make sure enough fresh air is provided.",
                "屋内で紫外線を使うときは，十分な新鮮な空気が供給されるようにしなければならない。",
            ),
        ]
    ),
    para(
        [
            (
                "uv_p7_s1",
                "UV light is everywhere, so it is important to understand how it affects us and what we can do to protect ourselves.",
                "紫外線はどこにでもあるので，それが私たちにどう影響するか，そして自分をどう守れるかを理解することが重要である。",
            ),
            (
                "uv_p7_s2",
                "Although it is not realistic or healthy to avoid UV light completely, there are ways to minimize its risks.",
                "紫外線を完全に避けることは現実的でも健康的でもないが，そのリスクを最小限に抑える方法はある。",
            ),
            (
                "uv_p7_s3",
                "For example, when spending time outdoors, you should use sunscreen, which can help block harmful UV light.",
                "たとえば屋外で過ごすときには有害な紫外線を遮るのに役立つ日焼け止めを使うべきである。",
            ),
            (
                "uv_p7_s4",
                "Additionally, hats and sunglasses are also great for protecting the skin and eyes.",
                "さらに帽子やサングラスも皮膚や目を守るのにすぐれたものである。",
            ),
            (
                "uv_p7_s5",
                "UV rays can also penetrate clouds and still cause harm, so these precautions should be taken no matter the weather.",
                "紫外線は雲を通過して害を及ぼすこともあるので，天気に関係なくこれらの予防措置をとるべきである。",
            ),
            (
                "uv_p7_s6",
                "Finally, if you are using UV light inside, remember to keep a window open to reduce the effects of harmful gases.",
                "最後に，屋内で紫外線を使うときは，有害なガスの影響を軽減するために窓を開けておくことを忘れないようにしよう。",
            ),
        ]
    ),
    para(
        [
            (
                "uv_p8_s1",
                "UV light is both our friend and our enemy.",
                "紫外線は私たちの味方でもあり敵でもある。",
            ),
            (
                "uv_p8_s2",
                "It can bring us great health benefits, but if we are not careful, it can also cause great harm.",
                "健康に大きな利益をもたらしてくれるが，注意を怠れば大きな害をもたらすこともある。",
            ),
        ]
    ),
]

section_07 = {
    "section_number": 7,
    "title": "第7問",
    "points": 16,
    "description": "長文読解（紫外線・アウトライン）",
    "situation": {
        "en": "You are preparing a presentation for a science project on ultraviolet light. You found some interesting information in the article below and are now making your outline.",
        "ja": "あなたは，紫外線に関する科学プロジェクトの発表を準備しています。あなたは以下の記事に興味深い情報を見つけ，現在概要を作成しています。",
    },
    "passages": [
        {
            "id": "uv_article",
            "title": {"en": "Ultraviolet Light", "ja": "紫外線"},
            "paragraphs": ARTICLE,
        },
        {
            "id": "uv_outline",
            "presentation_outline": {
                "label_outside_box": {
                    "en": "Your presentation outline",
                    "ja": "発表用の概要",
                },
                "title": {"en": "UV Light", "ja": "紫外線"},
                "blocks": [
                    {
                        "type": "center_slot",
                        "heading": {"en": "The Reach of UV", "ja": "UVの到達範囲"},
                        "center_slot": 32,
                    },
                    {
                        "type": "underlined_heading",
                        "heading": {
                            "en": "Benefit of UV: helps our bodies produce vitamin D",
                            "ja": "UVの利点：体がビタミンDを生成するのを助ける",
                        },
                    },
                    {
                        "type": "adaptations_heading",
                        "heading": {"en": "Benefits of Vitamin D", "ja": "ビタミンDの利点"},
                        "slot_after_heading": 33,
                        "lines": [
                            {"en": "A. Blocks calcium absorption", "ja": "A. カルシウムの吸収を防ぐ"},
                            {"en": "B. Boosts the immune system", "ja": "B. 免疫システムを強化する"},
                            {"en": "C. Improves mood", "ja": "C. 気分を改善する"},
                            {"en": "D. Lowers heart-disease risk", "ja": "D. 心臓病のリスクを下げる"},
                            {"en": "E. Strengthens bones and muscles", "ja": "E. 骨と筋肉を強化する"},
                        ],
                    },
                    {
                        "type": "section_heading_lines",
                        "heading": {"en": "Dangers of UV Light", "ja": "UV光の危険性"},
                        "bullets": [
                            {
                                "en": "Too much sun can [34].",
                                "ja": "過剰な太陽光は [34]。",
                            },
                            {
                                "en": "Too much sun can [35].",
                                "ja": "過剰な太陽光は [35]。",
                            },
                        ],
                    },
                    {
                        "type": "section_heading_lines",
                        "heading": {"en": "UV and Cleaning", "ja": "UVと浄化"},
                        "bullets": [{"en": "Kills germs", "ja": "細菌を殺す"}],
                    },
                    {
                        "type": "section_heading_lines",
                        "heading": {"en": "UV Indoors", "ja": "室内でのUV"},
                        "bullets": [{"en": "UV light [36].", "ja": "UV光は [36]。"}],
                    },
                    {
                        "type": "slot_heading_list",
                        "slot": 37,
                        "lines": [
                            {"en": "Sunscreen", "ja": "日焼け止め"},
                            {"en": "Hats", "ja": "帽子"},
                            {"en": "Sunglasses", "ja": "サングラス"},
                            {"en": "Airflow", "ja": "空気の流れ"},
                        ],
                    },
                ],
            },
        },
    ],
    "questions": [
        {
            "question_id": "問1",
            "answer_number": 32,
            "points": 3,
            "stem": {
                "en": "You want to use a figure to show how far UV light penetrates as described in the article. Choose the best option for [32].",
                "ja": "記事で説明されているとおり，紫外線がどれだけ届くかを示す図を使いたい。［32］に最適な選択肢を選びなさい。",
            },
            "figure_image": {
                "src": "data/zkai/2026/round01/images/q07_q1_diagram_choices.png",
                "alt": "問1 UVの到達（①〜④）",
            },
            "choices": [
                {"label": "①", "en": "", "ja": "", "is_correct": False},
                {"label": "②", "en": "", "ja": "", "is_correct": False},
                {"label": "③", "en": "", "ja": "", "is_correct": True},
                {"label": "④", "en": "", "ja": "", "is_correct": False},
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": "正解は③。UVA，UVB，UVCの届き方は第2段落に書かれている。地球表面に届く量に注目する。第2文に「UVAは地球に到達する紫外線の約95％を占める」とあるので③か④に絞られる。第4文に「UVBは大気によってほとんど遮断され，地球が受ける放射線の残りの約5％を占める」とある。さらに第7文で「UVCは地球の大気によって完全に遮断される」とあるので，③が正解。",
                "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第1回 解説冊子",
                "evidence_sentences": ["uv_p2_s2", "uv_p2_s4", "uv_p2_s7"],
                "instructor_note": {
                    "ja": "到達量のパーセンテージと，UVCは地表に届かないことを図と対応づける。",
                    "points": [
                        "UVA 約95％ → 地表まで届く主要因。",
                        "UVB 残り約5％・大気でほぼ遮られる → 途中まで。",
                        "UVC 完全遮断 → 大気内で止まる。",
                    ],
                },
            },
        },
        {
            "question_id": "問2",
            "answer_number": 33,
            "points": 3,
            "stem": {
                "sentences": [
                    {
                        "id": "zk_q7_q2_st",
                        "en": 'Under the heading, "Benefits of Vitamin D," you spotted an error in your presentation outline. Which of the following should you <u>remove</u>? [33]',
                        "ja": "見出し『ビタミンDの利点』の下にある発表用の概要に誤りがあることに気づいた。次のうち，<u>削除</u>すべきものはどれか。［33］",
                    }
                ]
            },
            "choices": [
                {"label": "①", "en": "A", "ja": "A", "is_correct": True},
                {"label": "②", "en": "B", "ja": "B", "is_correct": False},
                {"label": "③", "en": "C", "ja": "C", "is_correct": False},
                {"label": "④", "en": "D", "ja": "D", "is_correct": False},
                {"label": "⑤", "en": "E", "ja": "E", "is_correct": False},
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": "正解は①（アイテムAを削除）。ビタミンDの利点は第3段落に書かれている。カルシウムの吸収を助けるのはE，心臓のはたらきを改善するのはD，うつの症状を減らすのはC，免疫システムを強化するのはBと本文と一致する。Aは吸収を妨げるように読めるが，本文は吸収を助けるとあるので誤り。",
                "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第1回 解説冊子",
                "evidence_sentences": ["uv_p3_s2", "uv_p3_s3"],
                "instructor_note": {
                    "ja": "Blocks calcium absorption は helps the absorption の反対。",
                    "points": [
                        "Vitamin D helps the absorption of calcium → E と整合。",
                        "heart function / depression / immune → D,C,B。",
                        "A だけが本文と矛盾。",
                    ],
                },
            },
        },
        {
            "question_id": "問3",
            "answer_numbers": [34, 35],
            "unordered_slots": [34, 35],
            "points": 4,
            "stem": {
                "sentences": [
                    {
                        "id": "zk_q7_q3_a",
                        "en": "Choose the best options for [34] and [35]. (The order does not matter.)",
                        "ja": "［34］と［35］に最適な選択肢を選びなさい。（順不同。）",
                    }
                ]
            },
            "choices_34": [
                {
                    "label": "①",
                    "en": "affect people with lighter skin more severely",
                    "ja": "より明るい肌の人により深刻な影響を与える",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "contribute to the development of vision problems",
                    "ja": "視力問題の発現の一因となる",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "destroy light-sensitive materials in clothing",
                    "ja": "衣類の光に敏感な素材を破壊する",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "help to clear up cloudy spots on the skin",
                    "ja": "肌の曇った部分を解消するのに役立つ",
                    "is_correct": False,
                },
                {
                    "label": "⑤",
                    "en": "lead to darker-skinned people producing excess vitamin D",
                    "ja": "より暗い肌の人が過剰なビタミンDを生成することにつながる",
                    "is_correct": False,
                },
            ],
            "choices_35": [
                {
                    "label": "①",
                    "en": "affect people with lighter skin more severely",
                    "ja": "より明るい肌の人により深刻な影響を与える",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "contribute to the development of vision problems",
                    "ja": "視力問題の発現の一因となる",
                    "is_correct": True,
                },
                {
                    "label": "③",
                    "en": "destroy light-sensitive materials in clothing",
                    "ja": "衣類の光に敏感な素材を破壊する",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "help to clear up cloudy spots on the skin",
                    "ja": "肌の曇った部分を解消するのに役立つ",
                    "is_correct": False,
                },
                {
                    "label": "⑤",
                    "en": "lead to darker-skinned people producing excess vitamin D",
                    "ja": "より暗い肌の人が過剰なビタミンDを生成することにつながる",
                    "is_correct": False,
                },
            ],
            "answer": {"34": "①", "35": "②"},
            "answer_note": "順不同・両スロット正解で満点",
            "explanation": {
                "quoted_ja": "正解は①と②（順不同）。見出しはDangers of UV Light。第4段落に，色の薄い肌と濃い肌の違いと，目への影響（白内障・視力）が書かれている。①はlighter skin burns quickly…に，②はeyes… cataracts… vision に合致する。",
                "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第1回 解説冊子",
                "evidence_sentences": ["uv_p4_s4", "uv_p4_s5", "uv_p4_s6"],
                "instructor_note": {
                    "ja": "危険の列挙：皮膚の差異と眼疾患。衣服やビタミンD過剰は本文にない。",
                    "points": [
                        "①: lighter vs darker skin。",
                        "②: cataracts / eyes → vision problems。",
                        "③④⑤: 記述なしまたは別段落の内容。",
                    ],
                },
            },
        },
        {
            "question_id": "問4",
            "answer_number": 36,
            "points": 3,
            "stem": {
                "en": "Choose the best option for [36].",
                "ja": "［36］に最適な選択肢を選びなさい。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "can cause a chemical reaction that increases room temperature significantly, making the space feel warmer",
                    "ja": "部屋の温度を大幅に上昇させる化学反応を引き起こし，空間を暖かくする可能性がある",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "can help improve ventilation, ensuring that fresh air flows in the room",
                    "ja": "換気の改善に役立ち，新鮮な空気がしっかり部屋に流れ込むようにする",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "can produce chemicals that are not safe, making it dangerous for people to use in an enclosed space",
                    "ja": "安全でない化学物質を生成する可能性があり，密閉空間で人が使用するのは危険である",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "can produce light with more energy, making rooms appear much brighter than usual",
                    "ja": "より多くのエネルギーを持つ光を生成でき，部屋を通常よりはるかに明るくする",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": "正解は③。屋内での紫外線は第6段落に書かれる。化学反応でオゾンなど有害物質が生じ，密閉では蓄積しやすい。換気を確保しろというのは紫外線が換気を「改善する」のではなく必要とするので②は誤り。室温や明るさの記述はないので①④も誤り。",
                "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第1回 解説冊子",
                "evidence_sentences": ["uv_p6_s2", "uv_p6_s3", "uv_p6_s6", "uv_p6_s7"],
                "instructor_note": {
                    "ja": "ozone / dangerous chemicals / enclosed と enclosed の語に注目（問4語注）。",
                    "points": [
                        "②は UV が ventilation を改善するという意味になってしまう。",
                        "本文は fresh air を ensure するよう読者に求める。",
                    ],
                },
            },
        },
        {
            "question_id": "問5",
            "answer_number": 37,
            "points": 3,
            "stem": {
                "en": "Choose the best heading for [37].",
                "ja": "［37］に最適な見出しを選びなさい。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "How to Treat Damaged Skin",
                    "ja": "損傷した肌の治療方法",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "How UV Light Affects People",
                    "ja": "UV光が人に与える影響",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "Ways to Live a Healthy Life",
                    "ja": "健康的な生活を送る方法",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "Ways to Reduce UV Light Risk",
                    "ja": "UV光のリスクを軽減する方法",
                    "is_correct": True,
                },
            ],
            "answer": "④",
            "explanation": {
                "quoted_ja": "正解は④。［37］以下は日焼け止め・帽子・サングラス・空気の流れであり，第7段落第2文の minimize its risks に当たる具体例。①は治療でなく予防。②は影響そのものの列挙ではない。③は漠然としており，ビタミンDや除菌の文脈とも整合しにくい。",
                "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第1回 解説冊子",
                "evidence_sentences": ["uv_p7_s2", "uv_p7_s3", "uv_p7_s4", "uv_p7_s6"],
                "instructor_note": {
                    "ja": "リストはすべて precautions / risk reduction。",
                    "points": [
                        "sunscreen, hats, sunglasses → block / protect。",
                        "Airflow → window open / harmful gases。",
                    ],
                },
            },
        },
    ],
    "vocabulary": {
        "passage": {
            "label_ja": "主な語句・表現",
            "items": [
                {"en": "be surrounded by ~", "ja": "〜に囲まれている"},
                {"en": "shape", "ja": "〜を形作る"},
                {"en": "radiation", "ja": "放射線；光の放射"},
                {"en": "divide A into B", "ja": "AをBに分ける"},
                {"en": "make up ~", "ja": "〜を構成する"},
                {"en": "reach", "ja": "〜に到達する；到達範囲"},
                {"en": "give off ~", "ja": "〜を放出する"},
                {"en": "penetrate", "ja": "浸透する"},
                {"en": "the atmosphere", "ja": "大気；大気圏"},
                {"en": "exposure to ~", "ja": "〜にさらされること"},
                {"en": "mutation", "ja": "突然変異"},
                {"en": "sanitizing lamp", "ja": "殺菌灯"},
                {"en": "absorption", "ja": "吸収"},
                {"en": "be responsible for ~", "ja": "〜の原因・一因である"},
                {"en": "immune system", "ja": "免疫システム"},
                {"en": "cataract", "ja": "白内障"},
                {"en": "loss of sight", "ja": "視力喪失；失明"},
                {"en": "germ", "ja": "細菌；微生物"},
                {"en": "chemical reaction", "ja": "化学反応"},
                {"en": "airflow", "ja": "空気の流れ"},
                {"en": "minimize", "ja": "〜を最小限に抑える"},
                {"en": "sunscreen", "ja": "日焼け止め"},
                {"en": "precaution", "ja": "予防措置"},
                {"en": "no matter ~", "ja": "〜に関係なく"},
            ],
        },
        "questions_and_choices": {
            "items": [
                {"en": "severely（問3①）", "ja": "厳しく；ひどく"},
                {"en": "vision（問3②）", "ja": "視力"},
                {"en": "ventilation（問4②）", "ja": "換気"},
                {"en": "enclosed（問4③）", "ja": "密閉された"},
            ],
        },
    },
}


def main():
    data_path = ROOT / "data.json"
    with open(data_path, encoding="utf-8") as f:
        data = json.load(f)
    data["sections"] = [s for s in data["sections"] if s.get("section_number") != 7]
    data["exam_info"]["implemented_sections"] = [1, 2, 3, 4, 5, 6, 7]
    data["sections"].append(section_07)
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Merged section 7 →", data_path)


if __name__ == "__main__":
    main()
