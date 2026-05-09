# -*- coding: utf-8 -*-
"""Questions for 2023 Honshiken Section 6B."""


def get_questions():
    return [
        {
            "question_id": "問1",
            "answer_number": 44,
            "points": 2,
            "stem": {
                "en": "Which of the following should you not include for [44]?",
                "ja": "「[44]に含めるべきでないものはどれか。」"
            },
            "choices": [
                {"label": "①", "en": "eight short legs", "ja": "8本の短い脚", "is_correct": False},
                {"label": "②", "en": "either blind or sighted", "ja": "目が見えないか見えるかのどちらか", "is_correct": False},
                {"label": "③", "en": "plant-eating or creature-eating", "ja": "植物を食べる，または生き物を食べる", "is_correct": False},
                {"label": "④", "en": "sixteen different types of feet", "ja": "16種類の異なる足のタイプ", "is_correct": True},
                {"label": "⑤", "en": "two stylets rather than teeth", "ja": "歯ではなく2本の針", "is_correct": False}
            ],
            "answer": "④",
            "explanation": {
                "quoted_ja": "本文・全訳の問1①②③⑤に当てはまる。4については「合計16種類の爪」があり，足のタイプが16種類ではないため④が正解。",
                "quoted_source": "共通テスト 2023年度 本試験 英語（リーディング） 問題・解説",
                "evidence_sentences": ["s6b_p4_s1", "s6b_p4_s2", "s6b_p4_s3", "s6b_p4_s4", "s6b_p5_s2"],
                "instructor_note": {
                    "ja": "スライド1の Basic Information に入れる要素を選ぶ問題です。本文の情報をそのまま拾う姿勢で解くと安定します。",
                    "points": [
                        "④が誤り。本文は 16 known claw variations（16種類の爪のバリエーション）であり、\"足のタイプが16種類\" とは言っていない。",
                        "①は s6b_p4_s1 の four short legs on each side（左右に各4本）から合計8本で一致する。",
                        "②は s6b_p4_s4（目の場所はあるが、すべての種に目があるわけではない）に対応する。",
                        "⑤は s6b_p5_s2 の do not have teeth / two sharp needles, called stylets に対応し、本文の言い換えとして正しい。"
                    ]
                }
            }
        },
        {
            "question_id": "問2",
            "answer_number": 45,
            "answer_numbers": [45, 46],
            "unordered_slots": [45, 46],
            "points": 3,
            "stem": {
                "en": "For the Secrets to Survival slide, select two features which best help tardigrades survive. (The order does not matter.)",
                "ja": "「生き残るための秘訣のスライド用に，クマムシが生き残るために最も役立つ特徴を2つ選びなさい。（順不同）」"
            },
            "choices_45": [
                {"label": "①", "en": "In dry conditions, their metabolism drops to less than one percent of normal.", "ja": "乾燥した環境で，代謝が通常の1%未満に落ちる。", "is_correct": True},
                {"label": "②", "en": "Tardigrades in a state of tun are able to survive in temperatures exceeding 151C.", "ja": "休眠状態のクマムシは151℃を超える温度でも生存できる。", "is_correct": False},
                {"label": "③", "en": "The state of tun will cease when the water in a tardigrade's body is above 0.01%.", "ja": "乾燥状態は，体内の水分が0.01%を超えると終わる。", "is_correct": False},
                {"label": "④", "en": "Their shark-like mouths allow them to more easily eat other creatures.", "ja": "サメのような口のおかげで，他の生き物を食べやすくなる。", "is_correct": False},
                {"label": "⑤", "en": "They have an ability to withstand extreme levels of radiation.", "ja": "非常に厳しいレベルの放射線に耐える能力がある。", "is_correct": True}
            ],
            "choices_46": [
                {"label": "①", "en": "In dry conditions, their metabolism drops to less than one percent of normal.", "ja": "乾燥した環境で，代謝が通常の1%未満に落ちる。", "is_correct": True},
                {"label": "②", "en": "Tardigrades in a state of tun are able to survive in temperatures exceeding 151C.", "ja": "休眠状態のクマムシは151℃を超える温度でも生存できる。", "is_correct": False},
                {"label": "③", "en": "The state of tun will cease when the water in a tardigrade's body is above 0.01%.", "ja": "乾燥状態は，体内の水分が0.01%を超えると終わる。", "is_correct": False},
                {"label": "④", "en": "Their shark-like mouths allow them to more easily eat other creatures.", "ja": "サメのような口のおかげで，他の生き物を食べやすくなる。", "is_correct": False},
                {"label": "⑤", "en": "They have an ability to withstand extreme levels of radiation.", "ja": "非常に厳しいレベルの放射線に耐える能力がある。", "is_correct": True}
            ],
            "answer": {"45": "①", "46": "⑤"},
            "answer_note": "順不同・両方正解で得点",
            "explanation": {
                "quoted_ja": "①は本文で代謝が通常の0.01%まで落ちるとあり，1%未満は正しい。⑤は強いX線や紫外線に耐えるとある。②は151℃までで超えるとは書かれていない。③は本文の条件と逆。④は本文にない。",
                "quoted_source": "共通テスト 2023年度 本試験 英語（リーディング） 問題・解説",
                "evidence_sentences": ["s6b_p2_s5", "s6b_p3_s3"],
                "instructor_note": {
                    "ja": "「生存の秘訣」に直接つながる情報を2つ選ぶ設問です。数値・比較表現の読み違いを防ぐのが得点の鍵です。",
                    "points": [
                        "①は s6b_p2_s5 の metabolism drops to 0.01% of normal speed の要約で、1%未満という表現は正しい。",
                        "⑤は s6b_p3_s3 の intense X-rays and ultraviolet radiation に耐えた事実に対応する。",
                        "②の exceed 151C（151℃を超える）は本文不一致。本文は as high as 151C（151℃まで）。",
                        "③は因果が逆。本文は「体内水分を失う→乾燥休眠」であり、水分が増えると休眠が終わるとは書いていない。"
                    ]
                }
            }
        },
        {
            "question_id": "問3",
            "answer_number": 47,
            "points": 2,
            "stem": {
                "en": "Complete the missing labels on the illustration of a tardigrade for the Digestive Systems slide.",
                "ja": "「消化器官のスライド用に，クマムシのイラストの抜けている名前を完成させなさい。」"
            },
            "choices": [
                {"label": "①", "en": "(A) Esophagus (B) Pharynx (C) Middle gut (D) Stylets (E) Salivary gland", "ja": "(A) 食道 (B) 咽頭 (C) 中腸 (D) 口針 (E) 唾液腺", "is_correct": False},
                {"label": "②", "en": "(A) Pharynx (B) Stylets (C) Salivary gland (D) Esophagus (E) Middle gut", "ja": "(A) 咽頭 (B) 口針 (C) 唾液腺 (D) 食道 (E) 中腸", "is_correct": False},
                {"label": "③", "en": "(A) Salivary gland (B) Esophagus (C) Middle gut (D) Stylets (E) Pharynx", "ja": "(A) 唾液腺 (B) 食道 (C) 中腸 (D) 口針 (E) 咽頭", "is_correct": True},
                {"label": "④", "en": "(A) Salivary gland (B) Middle gut (C) Stylets (D) Esophagus (E) Pharynx", "ja": "(A) 唾液腺 (B) 中腸 (C) 口針 (D) 食道 (E) 咽頭", "is_correct": False},
                {"label": "⑤", "en": "(A) Stylets (B) Salivary gland (C) Pharynx (D) Middle gut (E) Esophagus", "ja": "(A) 口針 (B) 唾液腺 (C) 咽頭 (D) 中腸 (E) 食道", "is_correct": False}
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": "本文・全訳の問3(1)からDが口針。問3(2)から，口からつながる咽頭がE，咽頭の上のAが唾液腺，咽頭の先の管Bが食道，その先のCが中腸。よって③が正解。",
                "quoted_source": "共通テスト 2023年度 本試験 英語（リーディング） 問題・解説",
                "evidence_sentences": ["s6b_p5_s2", "s6b_p6_s2", "s6b_p6_s3"],
                "instructor_note": {
                    "ja": "器官名の対応は、本文の『口→咽頭→食道→中腸』という流れを先に確定させると整理しやすくなります。",
                    "points": [
                        "まず s6b_p5_s2 から D = stylets（口針）を固定する。",
                        "次に s6b_p6_s2 より pharynx の上が salivary gland なので A = 唾液腺、E = 咽頭。",
                        "最後に s6b_p6_s3 の after the pharynx, tube called the esophagus から B = 食道、C = 中腸。",
                        "この順で埋めると、語順の暗記ではなく『本文根拠で確定』できる。"
                    ]
                }
            }
        },
        {
            "question_id": "問4",
            "answer_number": 48,
            "points": 2,
            "stem": {
                "en": "Which is the best statement for the final slide?",
                "ja": "「最後のスライドに最適な意見はどれか。」"
            },
            "choices": [
                {"label": "①", "en": "For thousands of years, tardigrades have survived harsh conditions and will live longer than humankind.", "ja": "クマムシは何千年もの間，地上と宇宙で最も過酷な環境を生き延び，人類より長生きするだろう。", "is_correct": False},
                {"label": "②", "en": "Tardigrades are from space and can live in temperatures beyond Arctic foxes and camels, so they are stronger than humans.", "ja": "クマムシは宇宙から来て，ホッキョクギツネやフタコブラクダの限界を超えた気温でも生きられる。だから人類より強い。", "is_correct": False},
                {"label": "③", "en": "Tardigrades are the toughest creatures on earth and can thrive on the moon.", "ja": "クマムシは，疑いなく強い生き物で，月でも繁栄できる。", "is_correct": False},
                {"label": "④", "en": "Tardigrades have survived harsh conditions on earth and at least one trip into space. This remarkable creature might outlive the human species.", "ja": "クマムシは地球上の過酷な状況を生き抜き，少なくとも一度は宇宙へ行った。この注目に値する生物は人類より長生きするかもしれない。", "is_correct": True}
            ],
            "answer": "④",
            "explanation": {
                "quoted_ja": "本文・全訳で，クマムシは地球の過酷な環境を生き抜いていること，また宇宙へ行った事実がある。この2点に一致する④が最適。",
                "quoted_source": "共通テスト 2023年度 本試験 英語（リーディング） 問題・解説",
                "evidence_sentences": ["s6b_p1_s2", "s6b_p3_s2"],
                "instructor_note": {
                    "ja": "Final Statement は『本文にある事実 + 控えめな推量』の形が最も安全です。断定しすぎる選択肢を避けましょう。",
                    "points": [
                        "④は本文事実（地球の過酷環境で生存・宇宙に行った）を押さえた上で、might outlive と控えめに推量している。",
                        "①は『何千年』や断定的な長寿比較が本文不一致。",
                        "②は「宇宙から来た」が本文にない情報で、過剰な飛躍。",
                        "③は「月で繁栄できる（thrive）」まで言い切っており、本文の不明情報を断定している。"
                    ]
                }
            }
        },
        {
            "question_id": "問5",
            "answer_number": 49,
            "points": 3,
            "stem": {
                "en": "What can be inferred about sending tardigrades into space?",
                "ja": "「クマムシを宇宙に送ることについて，何が推察できるか。」"
            },
            "choices": [
                {"label": "①", "en": "Finding out whether tardigrades can survive in space was never thought to be important.", "ja": "クマムシが宇宙で生きていけるかを解明することは，一度も重要だと考えられなかった。", "is_correct": False},
                {"label": "②", "en": "Tardigrades, along with other creatures that have been on earth for millions of years, can withstand X-rays and ultraviolet radiation.", "ja": "クマムシは，数百万年間地球上にいる他の生物と同様に，X線や紫外線に耐えられる。", "is_correct": False},
                {"label": "③", "en": "The Israeli researchers did not expect so many tardigrades to survive the harsh environment of space.", "ja": "イスラエルの研究者は，これほど多くのクマムシが過酷な宇宙環境を生き抜くとは予期していなかった。", "is_correct": False},
                {"label": "④", "en": "The reason why no one has been to see if tardigrades can survive on the moon's surface attracted the author's attention.", "ja": "クマムシが月面で生存できるかどうか誰も調査に行っていない理由が，筆者の関心を引いた。", "is_correct": True}
            ],
            "answer": "④",
            "explanation": {
                "quoted_ja": "本文・全訳の問5参照。クマムシは事故で月に残されたが，誰も生存確認のために採集へ行っていないことを，筆者は『残念だ』と述べている。したがって④が正解。",
                "quoted_source": "共通テスト 2023年度 本試験 英語（リーディング） 問題・解説",
                "evidence_sentences": ["s6b_p3_s4", "s6b_p3_s5"],
                "instructor_note": {
                    "ja": "infer（推察）問題では、筆者の語気に注目すると精度が上がります。本文末の which is a pity が決定打です。",
                    "points": [
                        "s6b_p3_s5 の which is a pity は、筆者が『採集に行けていない状況』を残念に思っている態度を示す。",
                        "④は『その理由が筆者の注意を引いた』という、本文の筆者態度に沿った推察になっている。",
                        "①は『重要と思われなかった』という否定断定で、本文事実（実際に宇宙へ送っている）に反する。",
                        "③は主語の取り違え。2007年の驚きは European researchers であり、Israeli researchers ではない。"
                    ]
                }
            }
        }
    ]
