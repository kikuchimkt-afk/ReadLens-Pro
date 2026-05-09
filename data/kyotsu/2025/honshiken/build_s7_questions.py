# -*- coding: utf-8 -*-
"""Section 7 questions for 2025 Honshiken."""

def get_questions():
    return [
        {
            "question_id": "問1",
            "answer_number": 32,
            "stem": {
                "en": "Under the heading, \u201cImportance of Sleep,\u201d you spotted an error in your presentation outline. Which of the following should you <u>remove</u>? [32]",
                "ja": "「睡眠の重要性」の見出しの下にあなたは発表のアウトラインの誤りを見つけた。次の中であなたが削除するべきものはどれか。[32]"
            },
            "choices": [
                {"label": "\u2460", "en": "A", "ja": "A", "is_correct": True},
                {"label": "\u2461", "en": "B", "ja": "B", "is_correct": False},
                {"label": "\u2462", "en": "C", "ja": "C", "is_correct": False},
                {"label": "\u2463", "en": "D", "ja": "D", "is_correct": False}
            ],
            "answer": "\u2460",
            "explanation": {
                "quoted_ja": "正解は\u2460。本文の中で「睡眠の重要性」として挙げられていないものを選ぶ。「睡眠の重要性」については基本的に第2段落（Sleep is essential ...）で述べられている。同段落第1文に「睡眠は動物の体と心の健康（physical and mental health），そして身体の効率的な機能にとって必要不可欠である」とあり，下線部はBの「全般的な健康（overall health）を維持するため」に対応している。同段落第3文（Sleep also gives ...）に「睡眠はまた，(1)脳神経細胞にリセットする機会を与え（gives the brain neurons a chance to reset），(2)身体は活力を得る（the body becomes energized）」とあり，下線部(1)はDの「脳神経細胞をリセットするため（reset the brain neurons）」に，下線部(2)はCの「動物の体を再び元気にするため（refresh the animal\u2019s body）」に対応する。これに対して，Aの「体温を変えるため」は睡眠の重要性として挙げられていないので，これが正解となる。",
                "quoted_source": "『共通テスト 2025年度 本試験』英語（リーディング） 問題・解説",
                "evidence_sentences": ["s7_p2_s1", "s7_p2_s3"],
                "instructor_note": {
                    "ja": "アウトラインの項目が本文の内容と合っているか照合し，不適切なものを消去する問題です。",
                    "points": [
                        "B: s7_p2_s1 の physical and mental health が overall health に対応。",
                        "C: s7_p2_s3 の the body becomes energized が refresh the animal's body に対応。",
                        "D: s7_p2_s3 の gives the brain neurons a chance to reset が reset the brain neurons に対応。",
                        "A: 体温（body temperature）への言及は第2段落に存在しない。第7段落の冬眠で body temperature drops と出るが，それは睡眠の「重要性」ではない。"
                    ]
                }
            }
        },
        {
            "question_id": "問2",
            "answer_number": 33,
            "stem": {
                "en": "You want to use a figure for the biphasic sleep pattern mentioned in the article. Choose the best option for [33].",
                "ja": "あなたは記事で触れられた2相睡眠パターンの図を利用したいと思っている。[33]に入れるのに最適な選択肢を選びなさい。"
            },
            "figure_image": {
                "src": "data/kyotsu/2025/honshiken/images/q07_biphasic_pie_charts.png",
                "alt": "Four pie charts showing different awake/asleep ratios in a 24-hour cycle"
            },
            "choices": [
                {"label": "\u2460", "en": "", "ja": "", "is_correct": False},
                {"label": "\u2461", "en": "", "ja": "", "is_correct": False},
                {"label": "\u2462", "en": "", "ja": "", "is_correct": False},
                {"label": "\u2463", "en": "", "ja": "", "is_correct": True}
            ],
            "answer": "\u2463",
            "explanation": {
                "quoted_ja": "正解は\u2463。「2相睡眠パターン」については，第3段落第4文（Some birds, insects, ...）に「一部の鳥や昆虫や哺乳動物は，ある種の2相睡眠を活用する。これは動物が(A)2つの覚醒・睡眠時間を持っていて（has two waking and sleeping times），(B)1回の睡眠が長く，もう1回が仮眠のような状態になる場合を指す」とある。下線部(A)は，「覚醒時間」と「睡眠時間」が2つずつあるの（has two waking times and two sleeping times）」と同じ意味なので，選択肢の中で「覚醒中（awake）」と「睡眠中（asleep）」の時間帯が1つずつしかない\u2460は誤りとなる。そして下線部(B)の中の「仮眠のような状態（like a nap）」というのは，「睡眠時間が長く，もう1回が短い」ことと考えられるので，残る選択肢の中で(B)の内容に合うのは\u2463のみである。",
                "quoted_source": "『共通テスト 2025年度 本試験』英語（リーディング） 問題・解説",
                "evidence_sentences": ["s7_p3_s4"],
                "instructor_note": {
                    "ja": "本文の定義を図に当てはめる問題です。biphasic＝2区間の覚醒＋2区間の睡眠（長短あり）という条件を正確に読み取ります。",
                    "points": [
                        "\u2460は awake/asleep が各1区間（=monophasic）なので不適。",
                        "\u2461は4等分（=polyphasic 的）で長短の区別がなく不適。",
                        "\u2462は3区間以上に分かれており polyphasic 的で不適。",
                        "\u2463は睡眠が大小2区間＋覚醒も2区間で，s7_p3_s4 の two waking and sleeping times / one sleep being long and the other like a nap に合致。"
                    ]
                }
            }
        },
        {
            "question_id": "問3",
            "answer_number": 34,
            "answer_numbers": [34, 35],
            "unordered_slots": [34, 35],
            "stem": {
                "en": "Choose the best options for [34] and [35]. (The order does not matter.)",
                "ja": "[34]と[35]に入れるのに最適な選択肢を選びなさい（順序は問わない）。"
            },
            "choices_34": [
                {"label": "\u2460", "en": "which burn up energy rapidly tend to sleep more often", "ja": "エネルギーを急速に燃焼させる（動物）はより頻繁に眠る", "is_correct": True},
                {"label": "\u2461", "en": "which continually search for food need longer sleep", "ja": "絶えず食物を探す（動物）はより長い睡眠を必要とする", "is_correct": False},
                {"label": "\u2462", "en": "whose diet has fewer calories can sleep more easily", "ja": "食べる物のカロリーが少ない（動物）はより簡単に眠れる", "is_correct": False},
                {"label": "\u2463", "en": "whose food keeps their stomachs full usually sleep longer", "ja": "食べる物がお腹を満たし続ける（動物）はたいていより長く眠る", "is_correct": True},
                {"label": "\u2464", "en": "whose homes are difficult to get to typically sleep less", "ja": "住みかにたどり着くのが難しい（動物）は一般的に睡眠が少ない", "is_correct": False}
            ],
            "choices_35": [
                {"label": "\u2460", "en": "which burn up energy rapidly tend to sleep more often", "ja": "エネルギーを急速に燃焼させる（動物）はより頻繁に眠る", "is_correct": True},
                {"label": "\u2461", "en": "which continually search for food need longer sleep", "ja": "絶えず食物を探す（動物）はより長い睡眠を必要とする", "is_correct": False},
                {"label": "\u2462", "en": "whose diet has fewer calories can sleep more easily", "ja": "食べる物のカロリーが少ない（動物）はより簡単に眠れる", "is_correct": False},
                {"label": "\u2463", "en": "whose food keeps their stomachs full usually sleep longer", "ja": "食べる物がお腹を満たし続ける（動物）はたいていより長く眠る", "is_correct": True},
                {"label": "\u2464", "en": "whose homes are difficult to get to typically sleep less", "ja": "住みかにたどり着くのが難しい（動物）は一般的に睡眠が少ない", "is_correct": False}
            ],
            "answer": {"34": "\u2460", "35": "\u2463"},
            "answer_note": "順不同・両方正解で得点",
            "explanation": {
                "quoted_ja": "正解は\u2460と\u2463。「睡眠パターンに影響を与える条件」としてふさわしいものを選ぶ。第4段落第2・3文（Smaller animals such as ... / This results in ...）に「リスやハツカネズミなどの小型動物は，素早く頻繁に動くことでエネルギーを使い果たすことが多い。この結果，回数は多いが時間は短い睡眠をとる必要が生じる」とあることから，\u2460は正しいとわかる。また続く第4文（Lions are carnivorous animals ...）に「ライオンは肉食動物で，その食物源が空腹を長期間満たすことから，睡眠時間がより長い」とあることから，\u2463も正しいとわかる。他の選択肢のようなことは，本文では述べられていない。",
                "quoted_source": "『共通テスト 2025年度 本試験』英語（リーディング） 問題・解説",
                "evidence_sentences": ["s7_p4_s2", "s7_p4_s3", "s7_p4_s4"],
                "instructor_note": {
                    "ja": "第4段落の具体例（小型動物・肉食動物・草食動物）から条件を正しく抽出する問題です。",
                    "points": [
                        "\u2460: s7_p4_s2 の use up their energy by moving quickly and frequently が burn up energy rapidly に対応し，s7_p4_s3 の sleep more often に直結。",
                        "\u2463: s7_p4_s4 の satisfy their hunger for longer periods が keeps their stomachs full に対応し，longer sleeping times に直結。",
                        "\u2461の罠: 草食動物は食物を探すが，その結果 sleep less であり need longer sleep ではない。因果の方向が逆。",
                        "\u2462の罠: 低カロリーの食事→食物探しに時間→睡眠が少ない，であって sleep more easily ではない。",
                        "\u2464の罠: 住みかの到達困難さと睡眠量の関係は本文で述べられていない。"
                    ]
                }
            }
        },
        {
            "question_id": "問4",
            "answer_number": 36,
            "stem": {
                "en": "Choose the best option for [36].",
                "ja": "[36]に入れるのに最適な選択肢を選びなさい。"
            },
            "choices": [
                {"label": "\u2460", "en": "can be partially asleep and partially awake while in flight", "ja": "飛行中に部分的に眠り部分的に目覚めていることができる", "is_correct": True},
                {"label": "\u2461", "en": "can have half of their brain sleep, leading to increased heart rate", "ja": "脳の半分を眠らせることにより，心拍数を増やすことができる", "is_correct": False},
                {"label": "\u2462", "en": "can keep both eyes open constantly to watch out for enemies", "ja": "敵を警戒するために絶えず両目を開けておくことができる", "is_correct": False},
                {"label": "\u2463", "en": "can protect the outside members from inside the group", "ja": "群れの内側から外側にいる仲間を守ることができる", "is_correct": False}
            ],
            "answer": "\u2460",
            "explanation": {
                "quoted_ja": "正解は\u2460。半半球睡眠の内容と合っているものを選ぶ。この種の睡眠については第6段落で述べられている。この中の第3・4文（In this type of sleep, ... / While one side of ...）に「この種の睡眠では，群れをなして移動している動物の一部が1つの目を開けたままにしておく。その動物の脳の一方の側は眠るが，もう一方の側は目覚めていて，周囲に気を配り続ける」とあり，第6文（This unihemispheric sleep ...）に「この半半球睡眠は，一部の鳥類が群れをなして長距離を飛んでいる時に起こる」とあることから，下線部の内容と合っている\u2460が正解となる。\u2461は，「心拍数を増やすことができる」の部分が本文では述べられていないので誤りである。\u2462のようなことは本文では述べられていない。\u2463は同段落最終文（Birds flying at ...）に「群れの外縁部を飛んでいる鳥はこの種の睡眠を利用することで，両目を閉じて眠る他の鳥たちを守るのに役立つ」とあるのと合わない。",
                "quoted_source": "『共通テスト 2025年度 本試験』英語（リーディング） 問題・解説",
                "evidence_sentences": ["s7_p6_s3", "s7_p6_s4", "s7_p6_s6"],
                "instructor_note": {
                    "ja": "半半球睡眠（unihemispheric sleep）の特徴を正確に読み取り，選択肢と照合する問題です。",
                    "points": [
                        "\u2460: s7_p6_s3 の keep one eye open + s7_p6_s4 の one side sleeps / other stays awake + s7_p6_s6 の flying long distances が partially asleep and partially awake while in flight に合致。",
                        "\u2461の罠: 脳の半分が眠るのは正しいが，increased heart rate は本文に記述なし。第7段落の冬眠で heart rate が出るが文脈が全く異なる。",
                        "\u2462の罠: keep one eye open であって both eyes open ではない。one が both にすり替えられている。",
                        "\u2463の罠: s7_p6_s7 では outer edge の鳥が inside の鳥を守る。内外が逆転している。"
                    ]
                }
            }
        },
        {
            "question_id": "問5",
            "answer_number": 37,
            "stem": {
                "en": "Choose the best heading for [37].",
                "ja": "[37]に入れるのに最適な見出しを選びなさい。"
            },
            "choices": [
                {"label": "\u2460", "en": "Common Patterns of Sleep", "ja": "睡眠の共通パターン", "is_correct": False},
                {"label": "\u2461", "en": "Natural Sleep Methods", "ja": "自然な睡眠法", "is_correct": False},
                {"label": "\u2462", "en": "Reasons for Sleep", "ja": "睡眠をとる理由", "is_correct": False},
                {"label": "\u2463", "en": "States Similar to Sleep", "ja": "睡眠に似た状態", "is_correct": True}
            ],
            "answer": "\u2463",
            "explanation": {
                "quoted_ja": "正解は\u2463。空所には，「クロクマの冬眠」や「クラゲの弛緩」を具体例とする一般的な表現が入る。この2つはいずれも第7段落の第1文（Besides the types ...）に「上で説明した種類の睡眠以外にも，睡眠に似た活動と考えられるパターン（patterns that can be considered to be sleep-like activities）がある」とあることから，上の2つは下部の具体例ということになる。したがってこの意味に最も近い\u2463が正解となる。",
                "quoted_source": "『共通テスト 2025年度 本試験』英語（リーディング） 問題・解説",
                "evidence_sentences": ["s7_p7_s1"],
                "instructor_note": {
                    "ja": "アウトラインの見出しを本文の段落トピックセンテンスから導出する問題です。",
                    "points": [
                        "s7_p7_s1 の sleep-like activities が States Similar to Sleep に直結。",
                        "\u2460の罠: 冬眠やクラゲの弛緩は「共通パターン」ではなく，本文では典型的な睡眠パターンとは区別されている。",
                        "\u2462の罠: 睡眠の「理由」は第2段落の話題であり，第7段落は睡眠に似た「状態」の話。",
                        "besides が「加えて」の意味で，前の段落群（典型的な睡眠）と区別する接続詞である点に注意。"
                    ]
                }
            }
        }
    ]

if __name__ == '__main__':
    import json
    q = get_questions()
    print(f"Questions: {len(q)}")
    for qq in q:
        print(f"  {qq['question_id']}: answer_number={qq['answer_number']}")
