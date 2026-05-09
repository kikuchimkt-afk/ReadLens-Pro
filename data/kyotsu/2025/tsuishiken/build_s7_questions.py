# -*- coding: utf-8 -*-
"""Section 7 questions for 2025 Tsuishiken."""

def get_questions():
    return [
        {"question_id":"問1","answer_number":32,
         "stem":{"en":"You are adding details to the title of your presentation outline. Choose the best option for [32].","ja":"あなたは発表のタイトルに細かい説明を加えることにしている。[32]に入れるのに最適な選択肢を選びなさい。"},
         "choices":[
             {"label":"\u2460","en":"Health benefits and drawbacks","ja":"健康に有利な点と不利な点","is_correct":False},
             {"label":"\u2461","en":"Characteristics, Sources, and Daily Uses","ja":"特徴，源，日常の用途","is_correct":True},
             {"label":"\u2462","en":"Ingredients, Cleaning Systems, and Consumption","ja":"成分，清掃システム，消費","is_correct":False},
             {"label":"\u2463","en":"Location, Types of Rivers, and Issues","ja":"場所，川の種類，起こりうる問題","is_correct":False}
         ],
         "answer":"\u2461",
         "explanation":{
             "quoted_ja":"正解は\u2461。「硬水と軟水」の記事の内容を全体的にまとめた表現を選ぶ。第1段落は序論であるが，その最終文（In fact, ...）に「実は(A)水の構成（the makeup of water）や，(B)水が硬水や軟水になる仕組み（how it becomes hard or soft）や，(C)それぞれの種類の適切な用途（suitable uses for each type）にははっきりした違いがある」とあり，この文が第2段落以降の展開を予告していることに注意したい。この内容に最も近いのが\u2461で，\u2461の中の「特徴（Characteristics）」が下線部(A)に，「源（Sources）」が下線部(B)に，「日常の用途（Daily Uses）」が下線部(C)に対応していると考えられるので，\u2461が正解となる。他の選択肢はいずれも本文の構成を正しく反映していないため，正解にはなれない。",
             "quoted_source":"共通テスト 2025年度 追試験 英語（リーディング） 問題・解説",
             "evidence_sentences":["s7t_p1_s4"],
             "instructor_note":{
                 "ja":"記事全体の構成を把握し，タイトルに最もふさわしい要約を選ぶ問題です。第1段落最終文が『予告文（thesis statement）』の役割を果たしている点に注目しましょう。",
                 "points":[
                     "s7t_p1_s4 の In fact, ... が記事全体の3本柱（makeup / how it becomes hard or soft / suitable uses）を提示している。",
                     "②の Characteristics = makeup，Sources = how it becomes hard or soft，Daily Uses = suitable uses for each type にそれぞれ対応。",
                     "①の罠: Health benefits は第4段落で触れられるが，記事全体のテーマではない。",
                     "③の罠: Cleaning Systems は第5・6段落の一部に過ぎず，Consumption は記事で扱われていない。",
                     "④の罠: Rivers（川）は本文に登場しない。水道水（tap water）と混同させる引っかけ。"
                 ]
             }
         }},
        {"question_id":"問2","answer_number":33,
         "stem":{"en":"Choose the best option for completing the table in your outline. [33]","ja":"アウトラインの中の表を完成するのに最適な選択肢を選びなさい。[33]"},
         "choices":[
             {"label":"\u2460","en":"(1) Soft Water  (2) Moderately Hard Water  (3) Hard Water  (4) Very Hard Water","ja":"(1) 軟水  (2) 中程度の硬水  (3) 硬水  (4) 非常な硬水","is_correct":False},
             {"label":"\u2461","en":"(1) Soft Water  (2) Moderately Hard Water  (3) Very Hard Water  (4) Hard Water","ja":"(1) 軟水  (2) 中程度の硬水  (3) 非常な硬水  (4) 硬水","is_correct":False},
             {"label":"\u2462","en":"(1) Very Hard Water  (2) Moderately Hard Water  (3) Soft Water  (4) Hard Water","ja":"(1) 非常な硬水  (2) 中程度の硬水  (3) 軟水  (4) 硬水","is_correct":False},
             {"label":"\u2463","en":"(1) Hard Water  (2) Soft Water  (3) Very Hard Water  (4) Moderately Hard Water","ja":"(1) 硬水  (2) 軟水  (3) 非常な硬水  (4) 中程度の硬水","is_correct":False}
         ],
         "answer":"\u2460",
         "explanation":{
             "quoted_ja":"正解は\u2460。第2段落第3文（According to the World Health Organization ...）から第7文（In contrast, ...）に，「世界保健機構（WHO）によると，これらのミネラルを1リットルあたり60ミリグラム（mg/L）以上含む水は，一般に硬水と考えられている。この「硬水」はさらに細分化することができる。(A) 60\u2013120mg/Lを含む水は「中程度の硬水」で，(B) 120\u2013180 mg/Lを含む水は「硬水」である。(C)含有量が180mg/Lを超える水は，「非常な硬水」に分類される。これに対して，(D)ミネラル含有量が少ない（60mg/L未満）水は「軟らかい」と言われる。下線部(A)から表の(2)が「中程度の硬水（Moderately Hard Water）」で，下線部(B)から(3)が「硬水（Hard Water）」で，下線部(C)から(4)が「非常な硬水（Very Hard Water）」で，下線部(D)から(1)が「軟水（Soft Water）」であることがわかる。",
             "quoted_source":"共通テスト 2025年度 追試験 英語（リーディング） 問題・解説",
             "evidence_sentences":["s7t_p2_s3","s7t_p2_s4","s7t_p2_s5","s7t_p2_s6","s7t_p2_s7"],
             "instructor_note":{
                 "ja":"本文中の数値情報を表と照合する問題です。WHO基準の4段階分類（< 60 / 60-120 / 120-180 / > 180 mg/L）を正確に読み取りましょう。",
                 "points":[
                     "表の列(1)は < 60 mg/L → s7t_p2_s7 の In contrast, ... below 60 mg/L ... soft に対応 → Soft Water。",
                     "表の列(2)は 60-120 mg/L → s7t_p2_s5 の moderately hard に対応 → Moderately Hard Water。",
                     "表の列(3)は 120-180 mg/L → s7t_p2_s5 の hard に対応 → Hard Water。",
                     "表の列(4)は > 180 mg/L → s7t_p2_s6 の very hard に対応 → Very Hard Water。",
                     "数値の並びが昇順（小→大）であることに気づけば，硬度も段階的に上がる（soft → very hard）ので，①が唯一の正解とすぐに判断できる。"
                 ]
             }
         }},
        {"question_id":"問3","answer_number":34,
         "stem":{"en":"Choose the best option for [34].","ja":"[34]に入れるのに最適な選択肢を選びなさい。"},
         "choices":[
             {"label":"\u2460","en":"Determining regional water differences was difficult.","ja":"水の地域別の違いを決定するのは難しかった。","is_correct":False},
             {"label":"\u2461","en":"Japanese water was the softest among all the water studied.","ja":"日本の水は，研究されたすべての水の中で最も軟かった。","is_correct":False},
             {"label":"\u2462","en":"Regional water hardness was affected by the quality of raw water.","ja":"地域による水の硬度は原水の質によって影響を受けた。","is_correct":True},
             {"label":"\u2463","en":"Water purification efforts in Europe were different from those in Japan.","ja":"ヨーロッパにおける浄水場の持ち方は日本とは異なっていた。","is_correct":False}
         ],
         "answer":"\u2462",
         "explanation":{
             "quoted_ja":"正解は\u2462。第2段落最終文（The researchers found ...）に，「水の硬度を決めるのは，浄化の過程や水の輸送に用いる管よりも，原水，つまり浄化されていない水の質である（water hardness depended more on the quality of the raw, or unpurified, water）というところをこの研究者たちは発見した」とあることから，下線部の内容と合っている\u2462が正解となる。他の選択肢のようなことは記事からは読み取れない。",
             "quoted_source":"共通テスト 2025年度 追試験 英語（リーディング） 問題・解説",
             "evidence_sentences":["s7t_p2_s10"],
             "instructor_note":{
                 "ja":"研究結果の要約を選ぶ問題です。s7t_p2_s10 の depended more on A than B（BよりAに依存する）という比較構文が鍵です。",
                 "points":[
                     "③: s7t_p2_s10 の the quality of the raw, or unpurified, water が raw water の質に対応。研究結果を端的に要約している。",
                     "①の罠: 研究者たちは 27ヵ国の比較で地域差を明らかにしており，difficult とは述べていない。",
                     "②の罠: 日本の水は on the soft side（やや軟水寄り）であって，the softest（最も軟かい）とは述べていない。程度の誇張に注意。",
                     "④の罠: ヨーロッパと日本の浄水の努力の違いは本文で述べられていない。hardness depended more on raw water than purification process であって，浄水方法の国際比較は行っていない。"
                 ]
             }
         }},
        {"question_id":"問4","answer_number":35,
         "stem":{"en":"After finding the heading \u201cFactors Affecting the Hardness of Water,\u201d you spotted an error in your presentation outline. Which of the following should you get rid of? [35]","ja":"「水の硬度に影響する要因」という見出しを見つけた後に，あなたは発表のアウトラインの誤りを見つけた。次の中で取り除くべきものはどれか。[35]"},
         "choices":[
             {"label":"\u2460","en":"A","ja":"A","is_correct":False},
             {"label":"\u2461","en":"B","ja":"B","is_correct":False},
             {"label":"\u2462","en":"C","ja":"C","is_correct":True},
             {"label":"\u2463","en":"D","ja":"D","is_correct":False}
         ],
         "answer":"\u2462",
         "explanation":{
             "quoted_ja":"正解は\u2462。「水の硬度に影響する要因（Factors Affecting the Hardness of Water）」については，記事の第3段落（There are several variables ...）がそれに対応している。その第1文と第2文（These include ...）に，「原水のミネラル含有量に影響を及ぼす変動要素はいくつかある。この中には，(ア)地下の岩や石の種類（the kinds of rock in the ground），(イ)地域の降雨または降雪の量（the amount of rain or snow that falls in a region），(ウ)都市化（urbanization）が含まれる」とあり，水の硬度に影響を及ぼす主たる要因として，下線部(ア)，(イ)，(ウ)の3つが挙げられている。そして(ア)については続く第3文（Areas where water is ...）で，(イ)については第4文（In addition, ...）で，(ウ)については第5文（The movement of ...）でより具体的に説明されている。この3つを，アウトラインの中のAからDの4つの項目と比較すると，(ウ)はDに，(イ)はBに，(ウ)はAに対応していることがわかる。それに対してCの「雨滴に含まれる物質」については本文に対応する記述がないことから，これが取り除くべき項目となる。",
             "quoted_source":"共通テスト 2025年度 追試験 英語（リーディング） 問題・解説",
             "evidence_sentences":["s7t_p3_s1","s7t_p3_s2","s7t_p3_s3","s7t_p3_s4","s7t_p3_s5"],
             "instructor_note":{
                 "ja":"アウトラインの項目が本文の内容と合っているか照合し，不適切なものを消去する問題です。本文で挙げられた3要因と選択肢A〜Dの対応を1つずつ確認しましょう。",
                 "points":[
                     "A: Increased human activities → s7t_p3_s5 の The movement of more people and industries into cities（都市化）に対応。",
                     "B: Regional climate → s7t_p3_s4 の places where there is a lot of snow ... especially when it melts in spring（降雪量・融雪）に対応。",
                     "D: Underground conditions → s7t_p3_s3 の water is taken from underground sources（地下水源の岩石）に対応。",
                     "C: Substances in raindrops（雨滴に含まれる物質）→ 本文では rain or snow の『量』は述べているが，雨滴の中の『物質』については一切言及がない。rain を含むので紛らわしいが，内容が異なる。"
                 ]
             }
         }},
        {"question_id":"問5","answer_number":36,
         "answer_numbers":[36,37],"unordered_slots":[36,37],
         "stem":{"en":"Choose the best options for [36] and [37]. (The order does not matter.)","ja":"[36]と[37]に入れるべき最適な選択肢を選びなさい（順序は問わない）。"},
         "choices_36":[
             {"label":"\u2460","en":"Hard water can completely get rid of a film of soap.","ja":"硬水は石けんの膜を完全に取り除くことができる。","is_correct":False},
             {"label":"\u2461","en":"Home remedies are ineffective at making water softer.","ja":"家庭での対処法は水を軟らかくするのに効果がない。","is_correct":False},
             {"label":"\u2462","en":"Minerals in hard water can positively affect our health.","ja":"硬水中のミネラルは私たちの健康にプラスの影響を与えることができる。","is_correct":True},
             {"label":"\u2463","en":"Soft water can help reduce household energy costs.","ja":"軟水は家庭のエネルギー代を減らすのに役立つことができる。","is_correct":True},
             {"label":"\u2464","en":"Water stains are effective at improving the use of appliances.","ja":"水のしみは器具の使用を改善するのに効果がある。","is_correct":False}
         ],
         "choices_37":[
             {"label":"\u2460","en":"Hard water can completely get rid of a film of soap.","ja":"硬水は石けんの膜を完全に取り除くことができる。","is_correct":False},
             {"label":"\u2461","en":"Home remedies are ineffective at making water softer.","ja":"家庭での対処法は水を軟らかくするのに効果がない。","is_correct":False},
             {"label":"\u2462","en":"Minerals in hard water can positively affect our health.","ja":"硬水中のミネラルは私たちの健康にプラスの影響を与えることができる。","is_correct":True},
             {"label":"\u2463","en":"Soft water can help reduce household energy costs.","ja":"軟水は家庭のエネルギー代を減らすのに役立つことができる。","is_correct":True},
             {"label":"\u2464","en":"Water stains are effective at improving the use of appliances.","ja":"水のしみは器具の使用を改善するのに効果がある。","is_correct":False}
         ],
         "answer":{"36":"\u2462","37":"\u2463"},
         "answer_note":"[36]と[37]は順不同。両方正解で得点",
         "explanation":{
             "quoted_ja":"正解は\u2462と\u2463。\u2462については，第4段落最終文（Despite these negative aspects, ...）に「こういった否定的な面はあるものの，硬水は味の試験では評価がより高くなる傾向があり，日々のミネラル摂取量を増やすため，健康にとって有益なものになりうる（hard water ... could be beneficial for our health because it boosts our daily mineral intake）」とあるのと合っている。\u2463については，第5段落第1文（If the water ...）と第2文（We will use ...）に「家庭で使う水が軟水であれば，お金の節約になるかもしれない（If the water we use at home is soft, it could save us money）。泡がより効率よくとれるので，清掃に使う水や電気の量が減るだろう（We will use less water and electricity for cleaning）」とあるのと合っている。他の選択肢を正解とする根拠はない。",
             "quoted_source":"共通テスト 2025年度 追試験 英語（リーディング） 問題・解説",
             "evidence_sentences":["s7t_p4_s6","s7t_p5_s1","s7t_p5_s2"],
             "instructor_note":{
                 "ja":"『私たちの日常生活への影響』の見出しにふさわしい項目を2つ選ぶ問題です。第4〜6段落から硬水・軟水それぞれのプラス面を正しく読み取りましょう。",
                 "points":[
                     "③: s7t_p4_s6 の could be beneficial for our health because it boosts our daily mineral intake が positively affect our health に対応。Despite ... のあとの逆接に注意。",
                     "④: s7t_p5_s1 の it could save us money + s7t_p5_s2 の less water and electricity が reduce household energy costs に対応。",
                     "①の罠: s7t_p4_s3 で硬水は石けんの膜が落ちにくい（don't wash away easily）と述べており，completely get rid of は真逆。",
                     "②の罠: s7t_p6_s2-s4 で boiling や vinegar / baking soda が対処法として有効と述べており，ineffective は本文と矛盾する。",
                     "⑤の罠: s7t_p4_s4-s5 で硬水の白いしみ（spots）や水あか（limescale）は器具を損なうと述べており，improving ではなく damaging。"
                 ]
             }
         }}
    ]
