# -*- coding: utf-8 -*-
"""Z会 実戦模試 2026 第1回 第8問（ドギーバッグ・エッセイ構成）を data.json にマージする。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


section_08 = {
    "section_number": 8,
    "title": "第8問",
    "points": 18,
    "description": "レポート構成（ドギーバッグ）：意見読解・立場・情報源活用",
    "situation": {
        "en": (
            "You are working on an essay about whether all restaurants in Japan should be required to provide doggy bags. "
            "You will follow the steps below:"
        ),
        "ja": (
            "あなたは，日本のすべての飲食店に食べ残しの持ち帰り用の袋（ドギーバッグ）の提供を義務付けるべきかどうかについての"
            "エッセイに取り組んでいます。あなたは以下のステップに従います。"
        ),
        "steps": [
            {
                "en": "Step 1: Read and understand various views regarding making restaurants provide doggy bags.",
                "ja": "ステップ1：飲食店に持ち帰り用の袋の提供を義務付けることに関するさまざまな見解を読んで理解する。",
            },
            {
                "en": "Step 2: Take a position on whether all restaurants in Japan should be required to provide doggy bags.",
                "ja": "ステップ2：日本のすべての飲食店に持ち帰り用の袋の提供を義務付けるべきかどうかについて判断する。",
            },
            {
                "en": "Step 3: Create an outline for an essay using additional sources.",
                "ja": "ステップ3：追加の資料を使ってエッセイの概要を作成する。",
            },
        ],
    },
    "passages": [
        {
            "id": "step1_opinions",
            "title": {
                "en": "[Step 1] Read various viewpoints about requiring restaurants to provide doggy bags",
                "ja": "［ステップ1］持ち帰り用の袋の義務化に関するさまざまな見解を読む",
            },
            "layout": "speaker_boxes",
            "paragraphs": [
                [
                    {
                        "id": "z8_a_h",
                        "en": "Author A (Environmental advocate)",
                        "ja": "筆者A（環境保護活動家）",
                    },
                    {
                        "id": "z8_a_s1",
                        "en": (
                            "Providing doggy bags at restaurants may significantly help reduce food waste. "
                            "Many customers want to take home leftovers but feel awkward asking for a bag, "
                            "especially at relatively high-end restaurants."
                        ),
                        "ja": (
                            "飲食店で持ち帰り用の袋を提供することは，食品廃棄を大きく減らすのに役立つかもしれない。"
                            "多くの客は食べ残しを家に持ち帰りたいと思っているが，袋を頼むのは気まずく感じることが多く，"
                            "とりわけ比較的高級な飲食店ではそうである。"
                        ),
                    },
                    {
                        "id": "z8_a_s2",
                        "en": (
                            "If doggy bags were standard, people wouldn't need to feel embarrassed, "
                            "and more leftover food could be saved rather than thrown out with the trash."
                        ),
                        "ja": (
                            "もし持ち帰り用の袋が当たり前になれば，人々は恥ずかしい思いをする必要はなく，"
                            "より多くの食べ残しをゴミとして捨てるのではなく保存できるだろう。"
                        ),
                    },
                    {
                        "id": "z8_a_s3",
                        "en": (
                            "With this small step, we can contribute to the goal of environmental protection by reducing waste "
                            "and making better use of resources."
                        ),
                        "ja": (
                            "この小さな一歩で，廃棄を減らし資源をより有効に使うことによって，"
                            "環境保護という目標に貢献できる。"
                        ),
                    },
                    {
                        "id": "z8_a_s4",
                        "en": (
                            "If all restaurants provide doggy bags, people will be able to protect the environment more easily "
                            "without much effort."
                        ),
                        "ja": (
                            "すべての飲食店が持ち帰り用の袋を提供すれば，人々はあまり労力をかけずに"
                            "より容易に環境を守ることができるだろう。"
                        ),
                    },
                ],
                [
                    {
                        "id": "z8_b_h",
                        "en": "Author B (Restaurant owner)",
                        "ja": "筆者B（飲食店オーナー）",
                    },
                    {
                        "id": "z8_b_s1",
                        "en": "Offering doggy bags could improve customer satisfaction and potentially boost business.",
                        "ja": "持ち帰り用の袋を提供することで顧客満足度が向上し，商売を繁盛させる可能性がある。",
                    },
                    {
                        "id": "z8_b_s2",
                        "en": (
                            "Customers appreciate when they can take home extra food instead of feeling like they have to waste it. "
                            "This simple option could attract more diners, as many would choose a restaurant that is more environmentally friendly."
                        ),
                        "ja": (
                            "客は，余分な食べ物を無駄にしなければならないと感じるのではなく持ち帰れるときに感謝する。"
                            "このシンプルな選択肢はより多くの客を引き寄せるかもしれない。というのも多くの人はより環境に配慮した飲食店を選ぶからである。"
                        ),
                    },
                    {
                        "id": "z8_b_s3",
                        "en": (
                            "Some casual restaurant owners might worry about extra costs, but in reality, this change could be beneficial for them. "
                            "Especially at casual restaurants where portions are often large, customer satisfaction will increase."
                        ),
                        "ja": (
                            "一部のカジュアルな飲食店のオーナーは追加費用を心配するかもしれないが，実際にはこの変更は彼らにとって利益になる可能性がある。"
                            "とりわけ料理の量が多いことが多いカジュアルな店では，満足する客が増えるだろう。"
                        ),
                    },
                    {
                        "id": "z8_b_s4",
                        "en": "It seems like a win-win solution for us.",
                        "ja": "私たちにとっては双方に利益をもたらす解決策のように思える。",
                    },
                ],
                [
                    {
                        "id": "z8_c_h",
                        "en": "Author C (Health inspector)",
                        "ja": "筆者C（衛生検査官）",
                    },
                    {
                        "id": "z8_c_s1",
                        "en": (
                            "Requiring restaurants to provide doggy bags raises practical concerns about food safety. "
                            "Once food leaves a restaurant, it may not be refrigerated properly, "
                            "which can lead to the growth of bacteria that are harmful to health."
                        ),
                        "ja": (
                            "飲食店に持ち帰り用の袋の使用を強制することは，食品安全上の現実的な懸念を生じさせる。"
                            "いったん食べ物が飲食店の外に出たら，適切に冷蔵保存されず，健康に害をなす細菌の増殖につながる可能性がある。"
                        ),
                    },
                    {
                        "id": "z8_c_s2",
                        "en": (
                            "In other words, if leftovers are not handled properly at home, customers may become ill. "
                            "Because restaurants cannot control how leftovers are stored after customers take them home, "
                            "encouraging them to give out food in doggy bags could result in more cases of food poisoning."
                        ),
                        "ja": (
                            "言い換えれば，食べ残しが家で適切に扱われないと，客が病気になる可能性がある。"
                            "飲食店は，食べ残しが持ち帰られたあとにどのように保存されるかを管理することはできないため，"
                            "持ち帰り用の袋で食品を渡すことを彼らに奨励すれば，食中毒の事例の増加につながるかもしれない。"
                        ),
                    },
                    {
                        "id": "z8_c_s3",
                        "en": (
                            "It is far too dangerous to require restaurants to take actions that may harm public health."
                        ),
                        "ja": "公衆衛生を害する可能性のある行動をとるよう飲食店に要求するのは実に危険すぎる。",
                    },
                ],
                [
                    {
                        "id": "z8_d_h",
                        "en": "Author D (Chef)",
                        "ja": "筆者D（シェフ）",
                    },
                    {
                        "id": "z8_d_s1",
                        "en": (
                            "Making doggy bags a requirement may harm high-end dining experiences. "
                            "As a chef, I carefully plan portion sizes and presentation in all my dishes. "
                            "That precise presentation is a big part of the meal's appeal."
                        ),
                        "ja": (
                            "持ち帰り用の袋を必須にすることは，高級な食事体験に悪影響を及ぼすかもしれない。"
                            "私はシェフとして，すべての料理の分量と盛り付けを注意深く計画している。"
                            "その正確な盛り付けは，食事の魅力の大きな部分を占めている。"
                        ),
                    },
                    {
                        "id": "z8_d_s2",
                        "en": (
                            "Having to provide doggy bags would disrupt this balance and completely change how customers experience the food. "
                            "For high-class restaurants, where the focus is on a special dining experience, "
                            "making restaurants provide doggy bags wouldn't work."
                        ),
                        "ja": (
                            "持ち帰り用の袋を提供しなければならないことは，このバランスを崩し，お客様が料理を体験する様子を完全に変えてしまうだろう。"
                            "重視する点が特別な食事体験である高級飲食店では，飲食店に持ち帰り用の袋を提供させることはうまくいかないだろう。"
                        ),
                    },
                    {
                        "id": "z8_d_s3",
                        "en": (
                            "They might make sense for casual places, but from my perspective, "
                            "they could damage the atmosphere and the art that chefs work to create."
                        ),
                        "ja": (
                            "持ち帰り用の袋はカジュアルな店では理に適うかもしれないが，私の見方では，"
                            "シェフが努力して作り出す雰囲気や芸術を損なう可能性がある。"
                        ),
                    },
                ],
                [
                    {
                        "id": "z8_e_h",
                        "en": "Author E (Customer)",
                        "ja": "筆者E（顧客）",
                    },
                    {
                        "id": "z8_e_s1",
                        "en": (
                            "I like the idea of taking food home instead of letting it go to waste, "
                            "but I also worry about the possible effect on prices and portion sizes."
                        ),
                        "ja": (
                            "食べ物を無駄にしないで家に持ち帰るという考え方は好きだが，"
                            "価格や料理の量へ起こり得る影響も心配だ。"
                        ),
                    },
                    {
                        "id": "z8_e_s2",
                        "en": (
                            "If restaurants are required to provide doggy bags, they might start offering larger portions "
                            "and charging more to cover costs, which would be a huge downside."
                        ),
                        "ja": (
                            "もし飲食店が持ち帰り用の袋の提供を義務付けられたら，より多い分量を提供するようになるかもしれないし，"
                            "費用をまかなうために値上げするようになるかもしれない。これは大きなマイナス面だ。"
                        ),
                    },
                    {
                        "id": "z8_e_s3",
                        "en": (
                            "As a customer, I don't want to end up paying extra or dealing with oversized meals "
                            "just so I can bring more food home to eat later."
                        ),
                        "ja": (
                            "客としては，あとで食べる食べ物をより多く持ち帰るためだけに，多く支払ったり，特大サイズの食事に対処したりしたくない。"
                        ),
                    },
                    {
                        "id": "z8_e_s4",
                        "en": (
                            "While it's a convenient option, I think it should remain just that — an option, not a requirement."
                        ),
                        "ja": (
                            "便利な選択肢ではあるけれど，あくまでも選択肢のままにしておくべきで，必須条件にすべきではないと思う。"
                        ),
                    },
                ],
            ],
            "inline_solve_markers": [
                {
                    "after_paragraph": 4,
                    "question_ids": ["問1", "問2"],
                    "answer_numbers": [38, 39],
                },
                {
                    "after_paragraph": 4,
                    "marker_type": "navigate",
                    "action_ja": "解答が終わったら本文に戻り、Step 2 に進みます。",
                },
            ],
        },
        {
            "id": "step3_outline",
            "title": {
                "en": "[Step 3] Create an outline using Sources A and B",
                "ja": "［ステップ3］資料AとBを用いて概要を作成する",
            },
            "subtitle": {
                "id": "z8_step3_outline_label",
                "en": "Outline of your essay:",
                "ja": "あなたのエッセイの概要：",
            },
            "layout": "essay_outline_box",
            "paragraphs": [
                [
                    {
                        "id": "z8_eo_title",
                        "en": "We Should Require All Restaurants in Japan to Offer Doggy Bags",
                        "ja": "日本のすべての飲食店に持ち帰り用の袋の提供を義務付けるべきである",
                        "role": "outline_title",
                    }
                ],
                [
                    {
                        "id": "z8_eo_in_h",
                        "en": "Introduction",
                        "ja": "導入",
                        "role": "outline_subheader",
                    }
                ],
                [
                    {
                        "id": "z8_eo_in1",
                        "en": (
                            "Food loss is a huge problem in the world today. "
                            "By creating laws that make restaurants provide doggy bags to customers, "
                            "we can reduce food loss while improving people's lives."
                        ),
                        "ja": (
                            "食品廃棄は今日の世界で大きな問題である。"
                            "飲食店が持ち帰り用の袋を客に提供することを義務付ける法律を作ることで，"
                            "人々の生活を向上させながら食品廃棄を減らすことができる。"
                        ),
                    }
                ],
                [
                    {
                        "id": "z8_eo_bd_h",
                        "en": "Body",
                        "ja": "本文",
                        "role": "outline_subheader",
                    }
                ],
                [
                    {
                        "id": "z8_eo_r1",
                        "en": "Reason 1: [From Step 2]",
                        "ja": "理由1：［ステップ2より］",
                        "role": "outline_line",
                    }
                ],
                [
                    {
                        "id": "z8_eo_r2",
                        "en": "Reason 2: [Based on Source A] ([43])",
                        "ja": "理由2：［資料Aに基づいて］（[43]）",
                        "role": "outline_line",
                    }
                ],
                [
                    {
                        "id": "z8_eo_r3",
                        "en": "Reason 3: [Based on evidence ([44]) from Source B]",
                        "ja": "理由3：［資料Bからの論拠（[44]）に基づいて］",
                        "role": "outline_line",
                    }
                ],
                [
                    {
                        "id": "z8_eo_co_h",
                        "en": "Conclusion",
                        "ja": "結論",
                        "role": "outline_subheader",
                    }
                ],
                [
                    {
                        "id": "z8_eo_co1",
                        "en": "That's why doggy bags need to become available in all dining establishments.",
                        "ja": "こういうわけで，すべての飲食施設で持ち帰り用の袋を利用できるようにする必要がある。",
                    }
                ],
            ],
            "inline_solve_markers": [
                {
                    "after_paragraph": 8,
                    "question_ids": ["問3"],
                    "answer_numbers": [40, 41, 42],
                },
                {
                    "after_paragraph": 8,
                    "marker_type": "navigate",
                    "action_ja": "解答が終わったら本文に戻り、資料Aを読みます。",
                },
            ],
        },
        {
            "id": "source_a",
            "title": {"en": "Source A", "ja": "資料A"},
            "paragraphs": [
                [
                    {
                        "id": "z8_sa_p1_s1",
                        "en": (
                            "Introducing doggy bags at restaurants may benefit not only the environment but also the health of everyday diners. "
                            "By providing a way to take leftovers home, restaurants could encourage customers to eat smaller portions during meals "
                            "instead of pressuring them to finish everything on their plates."
                        ),
                        "ja": (
                            "飲食店で持ち帰り用の袋を導入することは，環境だけでなく，日々外食をする人の健康にも利点があるかもしれない。"
                            "食べ残しを家に持ち帰る手段を提供することで，飲食店は客に皿の上のものをすべて食べ切るよう無理強いするのではなく，"
                            "食事中に食べすぎないよう促すことができるだろう。"
                        ),
                    },
                    {
                        "id": "z8_sa_p1_s2",
                        "en": (
                            "This shift may help reduce overeating, which is linked to various health issues. "
                            "According to supporters of this new push for doggy bag laws, allowing customers to save extra food for later "
                            "can encourage a more thoughtful approach to dining."
                        ),
                        "ja": (
                            "この変更は，さまざまな健康問題に関連している過食を減らすのに役立つかもしれない。"
                            "持ち帰り用の袋に関する法律の，この新しい推進運動の支持者によれば，"
                            "客が余分な食べ物をあとに取っておけるようになれば，より配慮をもって食事に取り組めるようになる。"
                        ),
                    },
                    {
                        "id": "z8_sa_p1_s3",
                        "en": (
                            "For example, if a customer were given the option to take home their extra meat and potatoes from a heavy meal, "
                            "they would be less likely to overeat in the first place."
                        ),
                        "ja": (
                            "例えば，ボリュームのある食事で余った肉やポテトを持ち帰る選択肢が与えられたら，"
                            "客はそもそも食べすぎる可能性は低くなるだろう。"
                        ),
                    },
                ],
                [
                    {
                        "id": "z8_sa_p2_s1",
                        "en": (
                            "Supporters point out that using doggy bags could lead to the average consumer making better dietary choices "
                            "and becoming more aware of their eating habits."
                        ),
                        "ja": (
                            "支持者たちは，持ち帰り用の袋を使用することで，一般消費者がより良い食事を選択し，"
                            "食習慣をもっと意識するようになる可能性があると指摘する。"
                        ),
                    },
                    {
                        "id": "z8_sa_p2_s2",
                        "en": (
                            "This small step towards improving our health could also go a long way to preventing food loss."
                        ),
                        "ja": "健康増進に向けたこの小さな一歩は，食品廃棄の防止にも大いに役立つだろう。",
                    },
                ],
            ],
            "inline_solve_markers": [
                {
                    "after_paragraph": 1,
                    "question_ids": ["問4"],
                    "answer_numbers": [43],
                },
                {
                    "after_paragraph": 1,
                    "marker_type": "navigate",
                    "action_ja": "解答が終わったら本文に戻り、資料Bを読みます。",
                },
            ],
        },
        {
            "id": "source_b",
            "title": {"en": "Source B", "ja": "資料B"},
            "paragraphs": [
                [
                    {
                        "id": "z8_sb_s1",
                        "en": (
                            "A recent survey highlights the main reasons why people consume leftovers. "
                            "Saving money tops the list at 31%, followed closely by saving time at 26%. "
                            "The findings suggest that offering doggy bags may not only prevent food waste "
                            "but also support the customers' desires to get the most out of their meals."
                        ),
                        "ja": (
                            "最近の調査で，人々が食べ残しを消費する主な理由が強調された。"
                            "「お金の節約」が31%で一覧のトップ，僅差で「時間の節約」が26%で続いた。"
                            "この調査結果は，持ち帰り用の袋を提供することが，食品廃棄を防ぐだけでなく，"
                            "食事を最大限に活用したいという顧客の欲求を支援するかもしれないと示唆している。"
                        ),
                    },
                ]
            ],
            "graph_image": {
                "src": "images/q08_source_b_pie_chart.png",
                "after_paragraph": 1,
                "alt": "Top Reasons for Eating Restaurant Leftovers",
            },
            "inline_solve_markers": [
                {
                    "after_paragraph": 0,
                    "question_ids": ["問5"],
                    "answer_numbers": [44],
                },
            ],
        },
    ],
    "questions": [
        {
            "question_id": "問1",
            "answer_number": 38,
            "points": 3,
            "step": 1,
            "question_text": {
                "en": "Both Authors B and D mention that [38].",
                "ja": "筆者BとDはともに [38] と言及している。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "casual dining establishments might benefit more from doggy bags",
                    "ja": "カジュアルな食事施設は，持ち帰り用の袋の恩恵をより多く受けるかもしれない",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "customers are very concerned about how doggy bags impact the dining experience",
                    "ja": "客は持ち帰り用の袋が食事体験にどのような影響を与えるか非常に関心を持っている",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "providing doggy bags could lead to increased costs for restaurants",
                    "ja": "持ち帰り用の袋の提供は飲食店の費用増につながる可能性がある",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "the use of doggy bags lines up with environmental goals",
                    "ja": "持ち帰り用の袋の使用は環境保護という目標に合致している",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①。筆者Bの意見の第4文に Some casual restaurant owners might worry about extra costs, but in reality, "
                    "this change could be beneficial for them. とあり，続く文でカジュアル店でのメリットを述べている。"
                    "筆者Dの最終文に They might make sense for casual places とあり，①に一致する。"
                ),
                "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第1回 解説冊子",
                "evidence_sentences": ["z8_b_s3", "z8_d_s3"],
                "instructor_note": {
                    "ja": "両者に共通するのは「カジュアル店ではドギーバッグが理にかなう」という点。費用増に言及するのは主にB，体験への関心は主にDの別要素。",
                    "points": [
                        "B: casual owners / costs のあと in reality beneficial…",
                        "D: high-end では難しいが casual places では make sense。",
                    ],
                },
            },
        },
        {
            "question_id": "問2",
            "answer_number": 39,
            "points": 3,
            "step": 1,
            "question_text": {
                "en": "Author C implies that [39].",
                "ja": "筆者Cは [39] と暗示している。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "customers need to be educated on how to store leftovers safely",
                    "ja": "客は食べ残しを安全に保存する方法について教育される必要がある",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "requiring doggy bags might help maintain public health",
                    "ja": "持ち帰り用の袋を義務付けることは公衆衛生の維持に役立つかもしれない",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "requiring restaurants to provide doggy bags may lead to more cases of food poisoning",
                    "ja": "飲食店に持ち帰り用の袋の提供を義務付けることは，より多くの食中毒事例につながるかもしれない",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "restaurants should provide doggy bags only when customers request them",
                    "ja": "飲食店は客が求めたときにだけ持ち帰り用の袋を提供すべきだ",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。衛生検査官の筆者Cは，持ち帰り後の保存を店が管理できないことと，"
                    "doggy bags で食品を渡すよう奨励すると食中毒が増える可能性を結びつけている。②は逆の主張。①④は本文の焦点とずれる。"
                ),
                "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第1回 解説冊子",
                "evidence_sentences": ["z8_c_s2"],
                "instructor_note": {
                    "ja": "imply 題は否定的帰結を選ぶ。food poisoning / public health の対比に注意。",
                    "points": ["encouraging … doggy bags → more cases of food poisoning を言い換えた③。"],
                },
            },
        },
        {
            "question_id": "問3",
            "step": 2,
            "points": 6,
            "points_note": "［40］〜［42］はすべて正解で得点。［40］［41］は順不同。",
            "pre_header": {
                "en": "[Step 2] Take a position",
                "ja": "［ステップ2］立場を決める",
            },
            "answer_numbers": [40, 41, 42],
            "unordered_slots": [40, 41],
            "stem": {
                "en": (
                    "Now that you understand the various viewpoints, you have taken a position on whether all restaurants in Japan "
                    "should be required to provide doggy bags, and have written it out as below. "
                    "Choose the best options to complete [40] — [42]. "
                    "(You must have all of [40] — [42] correct to get points.)"
                ),
                "ja": (
                    "さまざまな見解を理解したうえで，日本のすべての飲食店に持ち帰り用の袋の提供を義務付けるべきかについて判断し，"
                    "それを以下のように書いた。"
                    "［40］〜［42］を完成させるのに最適な選択肢を選びなさい。"
                    "（［40］〜［42］はすべて正解でなければ配点されない。）"
                ),
            },
            "position_box": {
                "en": (
                    "Your position: All restaurants in Japan should be required to provide doggy bags.\n"
                    "  • Authors [40] and [41] support your position.\n"
                    "  • The main argument of the two authors: [42]"
                ),
                "ja": (
                    "あなたの立場：日本のすべての飲食店に持ち帰り用の袋の提供を義務付けるべきである。\n"
                    "  • 筆者 [40] と [41] はあなたの立場を支持する。\n"
                    "  • この2人の筆者の主な論拠： [42]"
                ),
            },
            "choices_40": [
                {"label": "①", "en": "A", "ja": "A", "is_correct": True},
                {"label": "②", "en": "B", "ja": "B", "is_correct": True},
                {"label": "③", "en": "C", "ja": "C", "is_correct": False},
                {"label": "④", "en": "D", "ja": "D", "is_correct": False},
                {"label": "⑤", "en": "E", "ja": "E", "is_correct": False},
            ],
            "choices_41": [
                {"label": "①", "en": "A", "ja": "A", "is_correct": True},
                {"label": "②", "en": "B", "ja": "B", "is_correct": True},
                {"label": "③", "en": "C", "ja": "C", "is_correct": False},
                {"label": "④", "en": "D", "ja": "D", "is_correct": False},
                {"label": "⑤", "en": "E", "ja": "E", "is_correct": False},
            ],
            "choices_42": [
                {
                    "label": "①",
                    "en": "Customers would appreciate restaurants providing doggy bags as an environmentally friendly option.",
                    "ja": "環境に優しい選択肢として，客は持ち帰り用の袋を提供する飲食店を評価するだろう。",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "Providing doggy bags would benefit all dining restaurants where portion sizes are typically larger.",
                    "ja": "持ち帰り用の袋の提供は，料理の量が概して多いすべての飲食店にとって有益だろう。",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "Requiring doggy bags could create extra costs for restaurants, especially high-end ones.",
                    "ja": "持ち帰り用の袋を義務付けることは，飲食店，特に高級飲食店にとって余分な費用を生む可能性がある。",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "Requiring doggy bags would encourage restaurants to offer smaller portions to avoid waste.",
                    "ja": "持ち帰り用の袋を義務化することで，飲食店が無駄をなくすために，提供する料理の分量を少なくするようになるだろう。",
                    "is_correct": False,
                },
            ],
            "answer": {"40": "①", "41": "②", "42": "①"},
            "answer_note": "［40］と［41］には A（①）と B（②）が順不同で入る。",
            "explanation": {
                "quoted_ja": (
                    "正解は［40］①／［41］②（順不同），［42］①。"
                    "義務化を明確に支持するのは環境面のAとビジネス上のメリットを述べるB。"
                    "［42］は両者に共通する「環境に配慮した選択肢として利用者が評価する」という論点が①に相当。"
                ),
                "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第1回 解説冊子",
                "evidence_sentences": ["z8_a_s2", "z8_a_s4", "z8_b_s1", "z8_b_s2"],
                "instructor_note": {
                    "ja": "駿台大問8と同型：Step2のメモは本文ではなく設問ブロックの position_box に載せる。",
                    "points": [
                        "C・D・Eはいずれも『全面的義務化賛成』ではないので［40］［41］から除外。",
                        "［42］は②〜④のように対象を広げすぎ／別筆者の論点にずれる選択肢を落とす。",
                    ],
                },
            },
        },
        {
            "question_id": "問4",
            "answer_number": 43,
            "points": 3,
            "step": 3,
            "question_text": {
                "en": "Based on Source A, which of the following is the most appropriate for Reason 2? [43]",
                "ja": "資料Aに基づくと，理由2として最も適当なものは次のうちどれか。［43］",
            },
            "choices": [
                {
                    "label": "①",
                    "en": (
                        "Allowing customers to take home leftovers could make restaurants seem more customer-friendly and environmentally "
                        "responsible, helping their image with health-conscious customers."
                    ),
                    "ja": (
                        "客が食べ残しを家に持ち帰れるようにすることで，レストランが客により優しく，環境保護により強い責任を持っていると思われ，"
                        "健康志向の客に対するイメージアップに役立つ。"
                    ),
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": (
                        "Giving customers doggy bags might promote healthier habits by encouraging them to eat smaller portions at meals, "
                        "which can reduce overeating."
                    ),
                    "ja": (
                        "客に持ち帰り用の袋を提供することで，客が食事中により少ない量を食べるよう促し，より健康な習慣を促進できるかもしれず，"
                        "それによって過食を減らすことができる。"
                    ),
                    "is_correct": True,
                },
                {
                    "label": "③",
                    "en": (
                        "Offering doggy bags helps restaurant owners because it could promote sales by making their establishments "
                        "more attractive to customers who care about waste reduction."
                    ),
                    "ja": (
                        "持ち帰り用の袋を提供することは，食品廃棄の削減を気にする客を店により強く惹きつけることで，売上を伸ばすことができるので，"
                        "飲食店のオーナーを助けることになる。"
                    ),
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": (
                        "Providing doggy bags may encourage customers to take leftovers home, which can help reduce food waste "
                        "by limiting the amount of food thrown away by restaurants."
                    ),
                    "ja": (
                        "持ち帰り用の袋を提供することで客が食べ残しを家に持ち帰ることを促す可能性があり，それは，飲食店に廃棄される食品の量を制限することで，"
                        "食品廃棄を減らすのに役立ちうる。"
                    ),
                    "is_correct": False,
                },
            ],
            "answer": "②",
            "explanation": {
                "quoted_ja": (
                    "正解は②。資料Aの主線は環境に加え「健康」「食事中の量」「過食」。"
                    "冒頭が benefit … health で，本文も smaller portions / reduce overeating を繰り返す。①③はイメージ・売上に寄りすぎ，④は理由2の「健康」軸より環境寄り。"
                ),
                "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第1回 解説冊子",
                "evidence_sentences": ["z8_sa_p1_s1", "z8_sa_p1_s2"],
            },
        },
        {
            "question_id": "問5",
            "answer_number": 44,
            "points": 3,
            "step": 3,
            "question_text": {
                "en": (
                    'For Reason 3, you have decided to write, "Customers would appreciate the option to make the most of their meals." '
                    "Based on Source B, which option best supports this statement? [44]"
                ),
                "ja": (
                    "理由3として，あなたは『食事を最大限に活用するために，客はその選択肢を喜ぶだろう。』と書くことにした。"
                    "資料Bに基づくと，この意見を最もよく支持する選択肢はどれか。［44］"
                ),
            },
            "choices": [
                {
                    "label": "①",
                    "en": (
                        "According to the survey, people choose to eat leftovers to avoid waste, suggesting that preventing food waste "
                        "is a higher priority than saving money."
                    ),
                    "ja": (
                        "調査によると，人々は無駄を避けるために食べ残しを食べることを選択しており，"
                        "食品廃棄の防止が節約より優先されることを示している。"
                    ),
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": (
                        "According to the survey, people choose to eat leftovers to avoid waste, suggesting that they prefer "
                        "to enjoy their delicious meals in restaurants."
                    ),
                    "ja": (
                        "調査によると，人々は無駄を避けるために食べ残しを食べることを選択しており，"
                        "飲食店でおいしい食事を楽しむことを好んでいることを示している。"
                    ),
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": (
                        "Many customers prefer to save money, time and effort by eating leftovers, as shown by survey data indicating "
                        "that these are the top three reasons for eating leftovers."
                    ),
                    "ja": (
                        "多くの客は食べ残しを食べることでお金と時間と労力を節約することを好み，"
                        "これは食べ残しを食べる理由の上位3つであると示す調査データに見られる通りである。"
                    ),
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": (
                        "People save time and effort by consuming leftovers at home, indicating that reducing food waste is less of "
                        "a priority for customers than convenience."
                    ),
                    "ja": (
                        "食べ残しを自宅で消費することで人々は時間と労力を節約でき，"
                        "客にとって食品廃棄の削減は利便性よりも優先度が低いことを示している。"
                    ),
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。資料Bの円グラフで save money / time / effort が上位3つ。"
                    "「食事を最大限に活用する」＝金・時間・手間の節約といった実利的動機と結びつく。①は優先順位の比較がグラフと一致しない，②④は誘読に注意。"
                ),
                "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第1回 解説冊子",
                "evidence_sentences": ["z8_sb_s1"],
            },
        },
    ],
    "vocabulary": {
        "passage": {
            "label_ja": "主な語句・表現",
            "items": [
                {"en": "doggy bag", "ja": "飲食店などで食べ残したものの持ち帰り袋"},
                {"en": "viewpoint", "ja": "見解；観点"},
                {"en": "outline", "ja": "概要"},
                {"en": "additional", "ja": "追加の"},
                {"en": "source", "ja": "（研究・調査の）資料；出典；情報源"},
                {"en": "environmental advocate", "ja": "環境保護活動家"},
                {"en": "awkward", "ja": "気まずい"},
                {"en": "boost business", "ja": "商売を繁盛させる"},
                {"en": "environmentally friendly", "ja": "環境に優しい"},
                {"en": "in reality", "ja": "実際には"},
                {"en": "food safety", "ja": "食品安全"},
                {"en": "food poisoning", "ja": "食中毒"},
                {"en": "high-end", "ja": "高価格帯の"},
                {"en": "downside", "ja": "マイナス面"},
                {"en": "food loss", "ja": "食品廃棄"},
                {"en": "shift", "ja": "変更；転換"},
                {"en": "highlight", "ja": "〜を強調する"},
                {"en": "desire", "ja": "欲求"},
                {"en": "get the most out of ~", "ja": "〜を最大限に活用する"},
            ],
        },
        "questions_and_choices": {
            "items": [
                {"en": "be concerned about ~（問1②）", "ja": "〜に関心がある"},
                {"en": "line up with ~（問1④）", "ja": "〜と合致する"},
                {"en": "imply（問2）", "ja": "〜を暗示する"},
                {"en": "maintain（問2②）", "ja": "〜を維持する"},
                {"en": "appropriate（問4）", "ja": "適切な"},
                {"en": "statement（問5）", "ja": "意見"},
                {"en": "indicate（問5③）", "ja": "〜を示す"},
            ],
        },
    },
}


def main():
    data_path = ROOT / "data.json"
    with open(data_path, encoding="utf-8") as f:
        data = json.load(f)
    data["sections"] = [s for s in data["sections"] if s.get("section_number") != 8]
    data["exam_info"]["implemented_sections"] = [1, 2, 3, 4, 5, 6, 7, 8]
    data["sections"].append(section_08)
    data["sections"].sort(key=lambda s: s.get("section_number", 0))
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Merged section 8 →", data_path)


if __name__ == "__main__":
    main()
