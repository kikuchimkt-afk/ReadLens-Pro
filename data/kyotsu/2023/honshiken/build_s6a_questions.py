# -*- coding: utf-8 -*-
"""Questions for 2023 Honshiken Section 6A."""

def get_questions():
    return [
        {
            "question_id": "問1",
            "answer_number": 39,
            "stem": {
                "en": "Choose the best option for [39].",
                "ja": "[39]に最も適切な選択肢を選びなさい。"
            },
            "choices": [
                {"label": "\u2460", "en": "a great place for people to sell things to collectors at a high price is a yard sale", "ja": "人々が物をコレクターに高額で売るのに絶好の場所はヤードセールだ", "is_correct": False},
                {"label": "\u2461", "en": "people can evaluate items incorrectly and end up paying too much money for junk", "ja": "人々は品物を間違って評価し，がらくたに高いお金を払うことになる可能性がある", "is_correct": False},
                {"label": "\u2462", "en": "something not important to one person may be of value to someone else", "ja": "ある人にとっては重要でない物でも，誰か他の人にとっては価値のある物かもしれない", "is_correct": True},
                {"label": "\u2463", "en": "things once collected and thrown in another person's yard may be valuable to others", "ja": "一度は収集して他の人の庭に捨てられた物が，他の人にとっては貴重かもしれない", "is_correct": False}
            ],
            "answer": "\u2462",
            "explanation": {
                "quoted_ja": "本文・全訳の問1の trash と treasure を具体的な説明で言い換えた，\u2462が正解。\n\n[\u2460「人々が物をコレクターに高額で売るのに絶好の場所はヤードセールだ」≫本文にない。\u2461「人々は品物を間違って評価し，がらくたに高いお金を払うことになる可能性がある」≫本文にない。\u2463「一度は収集して他の人の庭に捨てられた物が，他の人にとっては貴重かもしれない」≫「捨てられた物」ではなく「がらくた」が他人には貴重かもしれない。]",
                "quoted_source": "共通テスト 2023年度 本試験 英語（リーディング） 問題・解説",
                "evidence_sentences": ["s6a_p1_s8"],
                "instructor_note": {
                    "ja": "第1段落の教訓をまとめる問題です。具体的なエピソードの後にくる一般化された一文（s6a_p1_s8）を見抜きましょう。",
                    "points": [
                        "s6a_p1_s8 の One person's trash can be another person's treasure.（ある人のがらくたが、別の人の宝物になりうる）の言い換え。",
                        "③の something not important to one person = One person's trash",
                        "③の may be of value to someone else = can be another person's treasure に対応する。"
                    ]
                }
            }
        },
        {
            "question_id": "問2",
            "answer_number": 40,
            "stem": {
                "en": "Choose the best option for [40].",
                "ja": "[40]に最も適切な選択肢を選びなさい。"
            },
            "choices": [
                {"label": "\u2460", "en": "About two thirds of children do not collect ordinary things.", "ja": "子供の約3分の2は普通の物を集めない。", "is_correct": False},
                {"label": "\u2461", "en": "Almost one third of adults start collecting things for pleasure.", "ja": "大人の約3分の1が楽しみのために収集を始める。", "is_correct": False},
                {"label": "\u2462", "en": "Approximately 10% of kids have collections similar to their friends.", "ja": "子供のおよそ10%は友達とよく似たコレクションを持っている。", "is_correct": False},
                {"label": "\u2463", "en": "Roughly 30% of people keep collecting into adulthood.", "ja": "大体30%の人が，大人になっても収集を続ける。", "is_correct": True}
            ],
            "answer": "\u2463",
            "explanation": {
                "quoted_ja": "本文・全訳の問2参照。「約3分の1」を「大体30%」と言い換えた\u2463が正解。\n\n[\u2460「子供の約3分の2は普通の物を集めない。」≫10歳以下の子供の90%が何かを集めている。\u2461「大人の約3分の1が楽しみのために収集を始める。」≫収集を続ける大人が約3分の1。\u2462「子供のおよそ10%は友達とよく似たコレクションを持っている。」≫本文にない。]",
                "quoted_source": "共通テスト 2023年度 本試験 英語（リーディング） 問題・解説",
                "evidence_sentences": ["s6a_p2_s3", "s6a_p2_s4"],
                "instructor_note": {
                    "ja": "第2段落の数値データを言い換えた選択肢を選ぶ問題です。割合の表現の言い換え（分数・パーセンテージ）に注意しましょう。",
                    "points": [
                        "s6a_p2_s4 の approximately one third of adults（成人の約3分の1）が、Roughly 30% of people に言い換えられている。",
                        "s6a_p2_s4 の maintain this behavior（この行動を維持する）が、keep collecting into adulthood（大人になっても収集を続ける）に言い換えられている。",
                        "②の罠: start collecting（収集を始める）ではなく、幼少期から「続けている」のが1/3。"
                    ]
                }
            }
        },
        {
            "question_id": "問3",
            "answer_number": 41,
            "answer_numbers": [41, 42],
            "unordered_slots": [41, 42],
            "stem": {
                "en": "Choose the best options for [41] and [42]. (The order does not matter.)",
                "ja": "[41]と[42]に最も適切な選択肢を選びなさい。（順不同）"
            },
            "choices_41": [
                {"label": "\u2460", "en": "desire to advance technology", "ja": "科学技術を進歩させるという願望", "is_correct": False},
                {"label": "\u2461", "en": "fear of missing unexpected opportunities", "ja": "思いがけない機会を逃すことの不安", "is_correct": False},
                {"label": "\u2462", "en": "filling a sense of emptiness", "ja": "むなしさを満たすこと", "is_correct": False},
                {"label": "\u2463", "en": "reminder of precious events", "ja": "貴重な出来事を思い出させる物", "is_correct": True},
                {"label": "\u2464", "en": "reusing objects for the future", "ja": "将来のための物の再使用", "is_correct": False},
                {"label": "\u2465", "en": "seeking some sort of profit", "ja": "ある種の利益追求", "is_correct": True}
            ],
            "choices_42": [
                {"label": "\u2460", "en": "desire to advance technology", "ja": "科学技術を進歩させるという願望", "is_correct": False},
                {"label": "\u2461", "en": "fear of missing unexpected opportunities", "ja": "思いがけない機会を逃すことの不安", "is_correct": False},
                {"label": "\u2462", "en": "filling a sense of emptiness", "ja": "むなしさを満たすこと", "is_correct": False},
                {"label": "\u2463", "en": "reminder of precious events", "ja": "貴重な出来事を思い出させる物", "is_correct": True},
                {"label": "\u2464", "en": "reusing objects for the future", "ja": "将来のための物の再使用", "is_correct": False},
                {"label": "\u2465", "en": "seeking some sort of profit", "ja": "ある種の利益追求", "is_correct": True}
            ],
            "answer": {"41": "\u2463", "42": "\u2465"},
            "answer_note": "順不同・両方正解で得点",
            "explanation": {
                "quoted_ja": "本文・全訳の問3\u2463にあげられた収集品は，家族や特別な出来事の思い出にまつわる物であり，これは\u2463に当てはまる。問3\u2465には投資として金銭的価値が出そうな物を集めることが書かれており，\u2465に一致する。\n\n[\u2460「科学技術を進歩させるという願望」≫本文にない。\u2461「思いがけない機会を逃すことの不安」≫本文にない。\u2462「むなしさを満たすこと」≫本文にない。\u2464「将来のための物の再使用」≫本文にない。]",
                "quoted_source": "共通テスト 2023年度 本試験 英語（リーディング） 問題・解説",
                "evidence_sentences": ["s6a_p2_s7", "s6a_p4_s4", "s6a_p4_s6"],
                "instructor_note": {
                    "ja": "メモの「収集の理由」欄に列挙されている項目（歴史への興味、子供時代に興奮したことなど）以外の理由を、第2・第4段落から見つけ出す問題です。",
                    "points": [
                        "④: s6a_p2_s7 の greeting cards from friends ... dried flowers from special events ... old photos（手紙や特別な出来事の花や古い写真）が、reminder of precious events（貴重な出来事を思い出させる物）に対応。",
                        "⑥: s6a_p4_s4 の collect objects specifically as an investment（明確に投資として物を集める）と s6a_p4_s6 の ensure some financial security（経済的な安定を保証する）が、seeking some sort of profit（ある種の利益追求）に対応。"
                    ]
                }
            }
        },
        {
            "question_id": "問4",
            "answer_number": 43,
            "stem": {
                "en": "Choose the best option for [43].",
                "ja": "[43]に最も適切な選択肢を選びなさい。"
            },
            "choices": [
                {"label": "\u2460", "en": "Collections will likely continue to change in size and shape.", "ja": "コレクションは規模や形態が変化し続けると思われる。", "is_correct": True},
                {"label": "\u2461", "en": "Collectors of mint-condition games will have more digital copies of them.", "ja": "新品同様のゲームのコレクターは，より多くのデジタルコピーを所有することになるだろう。", "is_correct": False},
                {"label": "\u2462", "en": "People who have lost their passion for collecting will start again.", "ja": "収集への情熱を失った人が再開するだろう。", "is_correct": False},
                {"label": "\u2463", "en": "Reasons for collecting will change because of advances in technology.", "ja": "科学技術の進歩で，収集の理由は変わるだろう。", "is_correct": False}
            ],
            "answer": "\u2460",
            "explanation": {
                "quoted_ja": "本文・全訳の問4参照。科学技術の進化によって，デジタル・ライブラリーのような，30年前は想像もできなかった新しいコレクションが可能になったように，将来のコレクションの「形態と規模」は，科学技術によって想像できないほど変化するだろうと書いてある。したがって\u2460が正解。\n\n[\u2461「新品同様のゲームのコレクターは，より多くのデジタルコピーを所有することになるだろう。」≫本文にない。\u2462「収集への情熱を失った人が再開するだろう。」≫本文にない。\u2463「科学技術の進歩で，収集の理由は変わるだろう。」≫収集の理由は変わらないだろうと書かれている。]",
                "quoted_source": "共通テスト 2023年度 本試験 英語（リーディング） 問題・解説",
                "evidence_sentences": ["s6a_p5_s5"],
                "instructor_note": {
                    "ja": "最終段落（未来のコレクション）の要約を選ぶ問題です。本文の記述と矛盾する選択肢（④など）に注意しましょう。",
                    "points": [
                        "s6a_p5_s5 の the form and scale that the next generation's collections will take（次世代のコレクションが持つ形態と規模）が、選択肢①の size and shape に対応。",
                        "④の罠: s6a_p5_s2 で the reasons why people keep things will likely remain the same（人々が物を保持する理由は同じままであろう）と明言されており、reasons will change という④は本文と真っ向から矛盾します。"
                    ]
                }
            }
        }
    ]
