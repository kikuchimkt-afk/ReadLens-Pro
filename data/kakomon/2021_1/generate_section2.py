import json

section2 = {
    "section_number": 2,
    "title": "第2問",
    "points": 20,
    "pdf_pages": [5, 6, 7, 8, 9, 10],
    "passage_images": [
        "images/mondai_p5.png",
        "images/mondai_p6.png",
        "images/mondai_p7.png",
        "images/mondai_p8.png",
        "images/mondai_p9.png",
        "images/mondai_p10.png"
    ],
    "explanation_images": [
        "images/kaitou_p4.png",
        "images/kaitou_p5.png",
        "images/kaitou_p6.png",
        "images/kaitou_p7.png"
    ],
    "sub_sections": [
        {
            "sub_section": "A",
            "situation": {
                "en": "You are a student at a UK school festival band competition, and to understand the rankings and explain them, you are examining all the judges' scores and comments.",
                "ja": "あなたはイギリスの学園祭のバンドコンクールを担当する学生として，順位を理解し，説明するために，3人の審査員の得点とコメントをすべて精査しています。"
            },
            "passages": [
                {
                    "id": "scores_table",
                    "title": {
                        "en": "Judges' Final Average Scores",
                        "ja": "審査員の最終平均点"
                    },
                    "paragraphs": [
                        [
                            {"id": "2a_s1", "en": "Green Forest: Performance 3.9, Singing 4.6, Song Originality 5.0, Total 13.5", "ja": "Green Forest: パフォーマンス 3.9, 歌唱力 4.6, 曲の独創性 5.0, 合計 13.5"},
                            {"id": "2a_s2", "en": "Silent Hill: Performance 4.9, Singing 4.4, Song Originality 4.2, Total 13.5", "ja": "Silent Hill: パフォーマンス 4.9, 歌唱力 4.4, 曲の独創性 4.2, 合計 13.5"},
                            {"id": "2a_s3", "en": "Mountain Pear: Performance 3.9, Singing 4.9, Song Originality 4.7, Total 13.5", "ja": "Mountain Pear: パフォーマンス 3.9, 歌唱力 4.9, 曲の独創性 4.7, 合計 13.5"},
                            {"id": "2a_s4", "en": "Thousand Ants: (Did not perform)", "ja": "Thousand Ants:（出演せず）"}
                        ]
                    ]
                },
                {
                    "id": "individual_comments",
                    "title": {
                        "en": "Judges' Individual Comments",
                        "ja": "審査員の個別コメント"
                    },
                    "paragraphs": [
                        [
                            {"id": "2a_s5", "en": "Mr Hobbs: Silent Hill are great performers and they really seemed connected with the audience. Mountain Pear have great voices, but they were not exciting on stage. I loved Green Forest's original song. It was amazing!", "ja": "ホッブズ氏: Silent Hillは素晴らしいパフォーマーであり，本当に観客とつながっているように見えました。Mountain Pearの歌唱力は素晴らしかったですが，舞台上で盛り上げてはいませんでした。私は，Green Forestのオリジナルの歌がとても気に入りました。それは素晴らしかったです！"},
                            {"id": "2a_s6", "en": "Ms Leigh: Silent Hill are great performers and put on a wonderful first performance. The audience's reaction to their music was incredible. I really think Silent Hill is going to be popular! Mountain Pear have great voices, but they were not exciting on stage. Green Forest performed a fantastic new song, but I think they need to practice more.", "ja": "リー氏: Silent Hillは素晴らしいパフォーマンスをしました。観客の彼らの音楽への反応は信じられないほどでした。私は本当にSilent Hillは人気が出ると思います！Mountain Pearは素晴らしい声ですが，舞台上で盛り上げてはいませんでした。Green Forestはすてきな新曲を披露しましたが，もっと練習が必要だと思います。"},
                            {"id": "2a_s7", "en": "Ms Wells: Green Forest released a new song. I loved it! I think it could be a big hit! Whether it's Pacer, Speeder, or Zoomer, you'll love being a TQ Fan Club member.", "ja": "ウェルズ氏: Green Forestは新曲を出しました。私はとても気に入りました！私はそれが大ヒットするかもしれないと思います。"}
                        ]
                    ]
                },
                {
                    "id": "shared_evaluation",
                    "title": {
                        "en": "Judges' Shared Evaluation (Summary by Mr Hobbs)",
                        "ja": "審査員の共有評価（ホッブズ氏による要約）"
                    },
                    "paragraphs": [
                        [
                            {"id": "2a_s8", "en": "Each band's total score is the same, but they each have different strengths. Ms Leigh and I believe that performance is the most important quality in a band, and we agree. Ms Wells also agrees with this. Therefore, the winner is easy to determine.", "ja": "各バンドの合計得点は同じですが，それぞれのバンドはとても異なっています。リー氏と私はパフォーマンスがバンドの最も重要な資質であると意見が一致しています。ウェルズ氏も賛同しています。それゆえに，優勝は簡単に決定できます。"},
                            {"id": "2a_s9", "en": "For determining 2nd and 3rd place, Ms Wells suggested that song originality should be more important than good singing. Ms Leigh and I agreed on this opinion.", "ja": "2位と3位を決めるにあたり，ウェルズ氏は曲の独創性は歌唱力よりも重要であるべきだと提案しました。リー氏と私はこの意見に賛同しました。"}
                        ]
                    ]
                }
            ],
            "questions": [
                {
                    "question_id": "問1",
                    "answer_number": 6,
                    "stem": {
                        "en": "According to the judges' final average scores, which band sang the best?",
                        "ja": "「審査員の最終平均点によれば，どのバンドが最も上手に歌いましたか。」"
                    },
                    "choices": [
                        {"label": "①", "en": "Green Forest", "ja": "「Green Forest」", "is_correct": False},
                        {"label": "②", "en": "Mountain Pear", "ja": "「Mountain Pear」", "is_correct": True},
                        {"label": "③", "en": "Silent Hill", "ja": "「Silent Hill」", "is_correct": False},
                        {"label": "④", "en": "Thousand Ants", "ja": "「Thousand Ants」", "is_correct": False}
                    ],
                    "answer": "②",
                    "explanation": {
                        "ja": "正解は②。「審査員の最終平均点」の表に注目。Singing（歌唱力）の項目を見ると，最も高得点なのはMountain Pearなので，②が正解。",
                        "evidence_sentences": ["2a_s3"]
                    }
                },
                {
                    "question_id": "問2",
                    "answer_number": 7,
                    "stem": {
                        "en": "Which judge described both positive and critical comments about a band?",
                        "ja": "「どの審査員が肯定的なコメントと批判的なコメントの両方を述べましたか。」"
                    },
                    "choices": [
                        {"label": "①", "en": "Mr Hobbs", "ja": "「ホッブズ氏」", "is_correct": False},
                        {"label": "②", "en": "Ms Leigh", "ja": "「リー氏」", "is_correct": True},
                        {"label": "③", "en": "Ms Wells", "ja": "「ウェルズ氏」", "is_correct": False},
                        {"label": "④", "en": "No one", "ja": "「誰もいない」", "is_correct": False}
                    ],
                    "answer": "②",
                    "explanation": {
                        "ja": "正解は②。「審査員の個別コメント」の表に注目。Ms Leighは Mountain Pear have great voices, but they were not exciting on stage. Green Forest performed a fantastic new song, but I think they need to practice more.（Mountain Pearは素晴らしい声ですが，舞台上で盛り上げてはいませんでした。Green Forestはすてきな新曲を披露しましたが，もっと練習が必要だと思います。）と2つのバンドについて肯定的なコメントと否定的なコメントの両方を述べているので，②が正解で，④は不適当。Mr HobbsとMs Wellsは肯定的なコメントしか述べていないので，①と③も不適当。",
                        "evidence_sentences": ["2a_s6"]
                    }
                },
                {
                    "question_id": "問3",
                    "answer_number": 8,
                    "stem": {
                        "en": "One fact from the judges' individual comments is [ 8 ].",
                        "ja": "「審査員の個別のコメントからの1つの事実は，[ 8 ]ということです。」"
                    },
                    "choices": [
                        {"label": "①", "en": "all judges praised Green Forest's song", "ja": "「すべての審査員がGreen Forestの曲をほめた」", "is_correct": True},
                        {"label": "②", "en": "Green Forest needs to practice more", "ja": "「Green Forestはもっと練習が必要だ」", "is_correct": False},
                        {"label": "③", "en": "Mountain Pear can sing very well", "ja": "「Mountain Pearは歌をとても上手に歌える」", "is_correct": False},
                        {"label": "④", "en": "Silent Hill has a promising future", "ja": "「Silent Hillは前途有望だ」", "is_correct": False}
                    ],
                    "answer": "①",
                    "explanation": {
                        "ja": "正解は①。事実は何かを答える問題なので，個人の主観の入った意見を述べているものは不適当である。「審査員の個別コメント」を見ると，ホッブズ氏は，I loved Green Forest's original song. It was amazing!（私はGreen Forestのオリジナルの曲がとても気に入りました。それは素晴らしかったです！），リー氏は，Green Forest performed a fantastic new song（Green Forestはすてきな新曲を披露しました），ウェルズ氏は，I think it（= Green Forest's new song）could be a big hit!（私はそれが大ヒットするかもしれないと思います）と全員がGreen Forestの曲をほめているという事実が読み取れるので，①が正解。②と④はホッブズ氏とリー氏の主観的な意見なので，不適当。",
                        "evidence_sentences": ["2a_s5", "2a_s6", "2a_s7"]
                    }
                },
                {
                    "question_id": "問4",
                    "answer_number": 9,
                    "stem": {
                        "en": "One opinion from the judges' individual comments and shared evaluation is [ 9 ].",
                        "ja": "「審査員の個別のコメントと共有評価からの1つの意見は，[ 9 ]ということです。」"
                    },
                    "choices": [
                        {"label": "①", "en": "each band received the same total score", "ja": "「評価を受けた各バンドは同じ合計点を取った」", "is_correct": False},
                        {"label": "②", "en": "Ms Wells' suggestion about originality was agreed upon", "ja": "「独創性に関するウェルズ氏の提案は賛同を得た」", "is_correct": False},
                        {"label": "③", "en": "Silent Hill was truly connected with the audience", "ja": "「Silent Hillは本当に観客とつながっていた」", "is_correct": True},
                        {"label": "④", "en": "the judges' comments revealed the rankings", "ja": "「審査員のコメントは順位を明らかにした」", "is_correct": False}
                    ],
                    "answer": "③",
                    "explanation": {
                        "ja": "正解は③。意見は何かを答える問題なので，客観的な事実を述べているものは不適当である。「審査員の個別コメント」のホッブズ氏の欄の第1文に，Silent Hill are great performers and they really seemed connected with the audience.（Silent Hillは素晴らしいパフォーマーであり，本当に観客とつながっているように見えました。）とあり，これはホッブズ氏の主観の入った意見なので，③が正解。「審査員の共有評価」の第1段落第1文に，Each band's total score is the same（各バンドの合計得点は同じ）とあり，これは客観的な事実なので，①は不適当。「審査員の共有評価」の第2段落に，Ms Wells suggested that song originality should be more important than good singing. Ms Leigh and I agreed on this opinion.（ウェルズ氏は曲の独創性は歌唱力よりも重要であるべきだと提案しました。リー氏と私はこの意見に賛同しました。）とあるが，賛同したことは客観的な事実なので，②も不適当。④の「審査員のコメントは順位を明らかにした」は，「審査員のコメントにより順位がわかる」ということであり，これは客観的な事実なので，④も不適当。",
                        "evidence_sentences": ["2a_s5"]
                    }
                },
                {
                    "question_id": "問5",
                    "answer_number": 10,
                    "stem": {
                        "en": "What is the final ranking based on the judges' shared evaluation?",
                        "ja": "「審査員の共有評価に基づく最終順位は次のうちどれですか。」"
                    },
                    "choices": [
                        {"label": "①", "en": "(1st) Green Forest / (2nd) Mountain Pear / (3rd) Silent Hill", "ja": "「（1位）Green Forest／（2位）Mountain Pear／（3位）Silent Hill」", "is_correct": False},
                        {"label": "②", "en": "(1st) Green Forest / (2nd) Silent Hill / (3rd) Mountain Pear", "ja": "「（1位）Green Forest／（2位）Silent Hill／（3位）Mountain Pear」", "is_correct": False},
                        {"label": "③", "en": "(1st) Mountain Pear / (2nd) Green Forest / (3rd) Silent Hill", "ja": "「（1位）Mountain Pear／（2位）Green Forest／（3位）Silent Hill」", "is_correct": False},
                        {"label": "④", "en": "(1st) Mountain Pear / (2nd) Silent Hill / (3rd) Green Forest", "ja": "「（1位）Mountain Pear／（2位）Silent Hill／（3位）Green Forest」", "is_correct": False},
                        {"label": "⑤", "en": "(1st) Silent Hill / (2nd) Green Forest / (3rd) Mountain Pear", "ja": "「（1位）Silent Hill／（2位）Green Forest／（3位）Mountain Pear」", "is_correct": True},
                        {"label": "⑥", "en": "(1st) Silent Hill / (2nd) Mountain Pear / (3rd) Green Forest", "ja": "「（1位）Silent Hill／（2位）Mountain Pear／（3位）Green Forest」", "is_correct": False}
                    ],
                    "answer": "⑤",
                    "explanation": {
                        "ja": "正解は⑤。複数の資料から答えを導き出す問題。「審査員の共有評価」から順位付けの方法を読み取り，「審査員の最終平均点」から得点を読み取る。「審査員の共有評価」の第1段落第2〜4文から，「パフォーマンス」の得点が最も高いバンドが優勝したことがわかる。「審査員の最終平均点」の「パフォーマンス」の欄を見ると，得点が最も高いのはSilent Hillなのでこれが1位。残り2つのバンドの「パフォーマンス」は同点である。さらに「審査員の共有評価」の第2段落から，残りの2つのうち「曲の独創性」の得点が高いほうが2位を獲得したことが読み取れる。「審査員の最終平均点」の「歌の独創性」の得点は，Mountain PearよりもGreen Forestのほうが高いので，Green Forestが2位でMountain Pearが3位。したがって，正解は⑤。",
                        "evidence_sentences": ["2a_s8", "2a_s9", "2a_s2"]
                    }
                }
            ]
        },
        {
            "sub_section": "B",
            "situation": {
                "en": "You are an exchange student currently studying at a UK school. You have heard about a change in school policy and are reading a discussion about the policy on an online forum.",
                "ja": "あなたは交換留学生として今勉強しているイギリスの学校で，学校方針の転換について聞いたところです。あなたはオンラインフォーラムでその方針についての討論を読んでいるところです。"
            },
            "passages": [
                {
                    "id": "forum_post_1",
                    "title": {
                        "en": "New School Policy <Posted September 21, 2020>",
                        "ja": "新しい学校方針 ＜2020年9月21日投稿＞"
                    },
                    "paragraphs": [
                        [
                            {"id": "2b_s1", "en": "Dear Dr Burger,\nOn behalf of all the students, welcome to St Mark's School.", "ja": "バーガー博士様\n全学生を代表し，セント・マークス校へようこそ。"},
                            {"id": "2b_s2", "en": "Since you are the first headteacher with a business background, we hope your experience will help our school.", "ja": "あなたはビジネスの歴史を持つ最初の校長先生であると伺いましたので，あなたのご経験が私たちの学校に役立つことを願っています。"},
                            {"id": "2b_s3", "en": "I'd like to share one concern about the changes you are proposing to our after-school activities schedule.", "ja": "あなたが放課後の活動スケジュールに提案されている変更について，一つの懸念をお伝えしたいと思います。"},
                            {"id": "2b_s4", "en": "I realise that saving energy is important and from now it will be getting darker earlier, which is easy to understand.", "ja": "エネルギーを節約することは重要であり，今後暗くなるのがより早くなっていくことはよくわかります。"},
                            {"id": "2b_s5", "en": "Is this why you have made the schedule an hour and a half shorter?", "ja": "このことがスケジュールを1時間半短縮した理由ですか？"},
                            {"id": "2b_s6", "en": "Students at St Mark's School take both their studies and after-school activities very seriously.", "ja": "セント・マークス校の学生は勉強と放課後の活動の両方にとても真剣に取り組んでいます。"},
                            {"id": "2b_s7", "en": "A number of students have told me that they want to stay at school until 6 p.m. as they have always done.", "ja": "多くの学生が，従来やってきたように午後6時まで学校にいたいと私に言ってきています。"},
                            {"id": "2b_s8", "en": "So I would like to ask you to think again about this sudden change in policy.\nRegards,\nKen Roberts\nStudent Council President", "ja": "そういうわけで，この突然の方針転換についてご再考をお願いしたいと思っています。\n敬具\nケン・ロバーツ\n生徒会長"}
                        ]
                    ]
                },
                {
                    "id": "forum_post_2",
                    "title": {
                        "en": "Re: New School Policy <Posted September 22, 2020>",
                        "ja": "Re: 新しい学校方針 ＜2020年9月22日投稿＞"
                    },
                    "paragraphs": [
                        [
                            {"id": "2b_s9", "en": "Dear Ken,\nThank you very much for your kind post.", "ja": "親愛なるケン\n親切な投稿に大変感謝します。"},
                            {"id": "2b_s10", "en": "You have raised some important concerns, especially about energy costs and students' views on school activities.", "ja": "あなたはいくつかの重要な懸念，特にエネルギーコストと学校活動に関する学生の意見について表明してくれました。"},
                            {"id": "2b_s11", "en": "The new policy has nothing to do with saving energy.", "ja": "新しい方針はエネルギーの節約とは何の関係もありません。"},
                            {"id": "2b_s12", "en": "The decision was made based on a 2019 police report.", "ja": "その決定は，2019年の警察の報告に基づいてなされました。"},
                            {"id": "2b_s13", "en": "The report showed that our city has become less safe due to a 5% increase in serious crimes.", "ja": "その報告によると，重大犯罪が5%増加したため，私たちの市の安全性が低下したそうです。"},
                            {"id": "2b_s14", "en": "I would like to protect our students, so I would like them to return home before it gets dark.", "ja": "私は学生を守りたいので，暗くなる前に帰宅してほしいのです。"},
                            {"id": "2b_s15", "en": "Regards,\nP.E. Burger, PhD\nHeadteacher", "ja": "敬具\nP.E.バーガー博士\n校長"}
                        ]
                    ]
                }
            ],
            "questions": [
                {
                    "question_id": "問1",
                    "answer_number": 11,
                    "stem": {
                        "en": "Ken thinks the new policy is [ 11 ].",
                        "ja": "「ケンは新しい方針は[ 11 ]と思っています。」"
                    },
                    "choices": [
                        {"label": "①", "en": "to allow students to study more", "ja": "「学生をもっと勉強させることができる」", "is_correct": False},
                        {"label": "②", "en": "to possibly improve school safety", "ja": "「学校の安全性を向上させられるかもしれない」", "is_correct": False},
                        {"label": "③", "en": "to be introduced immediately", "ja": "「ただちに導入されるべきだ」", "is_correct": False},
                        {"label": "④", "en": "to reduce after-school activity time", "ja": "「放課後の活動時間を減らすだろう」", "is_correct": True}
                    ],
                    "answer": "④",
                    "explanation": {
                        "ja": "正解は④。ケンは投稿の第2段落第3文で，Is this why you have made the schedule an hour and a half shorter?（このことがスケジュールを1時間半短縮した理由ですか？）とバーガー博士に問いかけ，続けて「この学校の学生は勉強と放課後活動の両方に真剣に取り組んでおり，多くの学生が従来通りの時間まで学校にいたいと述べている」と伝えている。したがって，新しい方針は放課後活動の時間を短縮するものだとわかるので，④が正解。①は不適当。②については，バーガー博士の第2段落第4文で，I would like to protect our students（私は学生を守りたい）と書いておりバーガー博士の考えではあるが，ケンの考えではないので，これも不適当。ケンは投稿の第2段落最終文で，I would like to ask you to think again about this sudden change in policy（この突然の方針転換についてご再考をお願いしたいと思っています）と求めているので，④も不適当。",
                        "evidence_sentences": ["2b_s5", "2b_s7"]
                    }
                },
                {
                    "question_id": "問2",
                    "answer_number": 12,
                    "stem": {
                        "en": "One fact stated in Ken's post to the forum is [ 12 ].",
                        "ja": "「ケンのフォーラムへの投稿で述べられている1つの事実は[ 12 ]ということです。」"
                    },
                    "choices": [
                        {"label": "①", "en": "the policy needs further discussion", "ja": "「その方針についてさらに議論する必要がある」", "is_correct": False},
                        {"label": "②", "en": "the headteacher's experience is improving the school", "ja": "「校長の経験は学校を向上させている」", "is_correct": False},
                        {"label": "③", "en": "the school should think about students' activities", "ja": "「学校は学生の活動について考えるべきだ」", "is_correct": False},
                        {"label": "④", "en": "students who don't welcome the new policy exist", "ja": "「新しい方針を歓迎しない学生がいる」", "is_correct": True}
                    ],
                    "answer": "④",
                    "explanation": {
                        "ja": "正解は④。事実は何かを答える問題なので，個人の主観の入った意見を述べているものは不適当である。ケンの投稿の第2段落第5文に，A number of students have told me that they want to stay at school until 6:00 pm as they have always done.（多くの学生が，従来やってきたように午後6時まで学校にいたいと私に言ってきています。）とあり，これは「放課後の活動時間を1時間半短縮するという新しい方針を歓迎していない学生が多数いる」という客観的事実を示しているので，④が正解。ケンの投稿の第1段落第2文に，we hope your experience will help our school（あなたのご経験が私たちの学校に役立つことを願っています）とあるが，これはケンの願望であり，客観的事実ではないので，②は不適当。同じくケンの投稿の第2段落の最終文のI would like to ask you to think again about this sudden change in policy（この突然の方針転換についてご再考をお願いしたいと思っています）から，「放課後の学生の活動を含む新しい方針についてさらなる議論・再考が必要」と求めているので，①と③も不適当。",
                        "evidence_sentences": ["2b_s7"]
                    }
                },
                {
                    "question_id": "問3",
                    "answer_number": 13,
                    "stem": {
                        "en": "Who thinks the aim of the policy is to save energy?",
                        "ja": "「その方針の目的はエネルギーの節約だと考えているのは誰ですか。」"
                    },
                    "choices": [
                        {"label": "①", "en": "Dr Burger", "ja": "「バーガー博士」", "is_correct": False},
                        {"label": "②", "en": "Ken", "ja": "「ケン」", "is_correct": True},
                        {"label": "③", "en": "The city", "ja": "「市」", "is_correct": False},
                        {"label": "④", "en": "The police", "ja": "「警察」", "is_correct": False}
                    ],
                    "answer": "②",
                    "explanation": {
                        "ja": "正解は②。ケンの第2段落第2文で，I realise that saving energy is important and from now it will be getting darker earlier（エネルギーを節約することは重要であり，今後暗くなるのがより早くなっていくことはよくわかります）と述べている。この方針変更の目的はエネルギーの節約であると考えているのはケンだと言えるので，②が正解。バーガー博士は投稿の第2段落第1文で，The new policy has nothing to do with saving energy.（新しい方針はエネルギーの節約とは何の関係もありません。）と述べているので，①は不適当。市や警察が学校の方針についたといったことは，どちらの投稿でも触れられていないから，③と④も不適当。",
                        "evidence_sentences": ["2b_s4"]
                    }
                },
                {
                    "question_id": "問4",
                    "answer_number": 14,
                    "stem": {
                        "en": "Dr Burger is [ 14 ] and trying to decide on a new policy based on that.",
                        "ja": "「バーガー博士は[ 14 ]という事実に基づいて新しい方針を決めようとしている。」"
                    },
                    "choices": [
                        {"label": "①", "en": "It is important to go home early", "ja": "「早く帰宅することは重要だ」", "is_correct": False},
                        {"label": "②", "en": "The city's safety has declined", "ja": "「市の安全性が低下してしまった」", "is_correct": True},
                        {"label": "③", "en": "The school must save electricity", "ja": "「学校は電気を節約しなければならない」", "is_correct": False},
                        {"label": "④", "en": "Students need protection", "ja": "「学生は保護を必要としている」", "is_correct": False}
                    ],
                    "answer": "②",
                    "explanation": {
                        "ja": "正解は②。事実を答える問題なので，個人の主観の入った意見は不適当である。バーガー博士の投稿の第2段落第2〜3文に，The decision was made based on a 2019 police report. The report showed that our city has become less safe due to a 5% increase in serious crimes.（その決定は，2019年の警察の報告に基づいてなされました。その報告によると，重大犯罪が5%増加したため，私たちの市の安全性が低下しました。）とあり，「市の安全性低下」は客観的な事実なので，②が正解。バーガー博士は続く第4文で，I would like to protect our students, so I would like them to return home before it gets dark.（私は学生を守りたいので，暗くなる前に帰宅してほしいのです。）と述べており，これはバーガー博士の願望であり，客観的事実ではないので，①と④は不適当。新しい方針の目的は，学校の電気代の削減や，学校での活動にかかる予算の削減や，学生の学習時間確保のためではないので，③も不適当。",
                        "evidence_sentences": ["2b_s12", "2b_s13"]
                    }
                },
                {
                    "question_id": "問5",
                    "answer_number": 15,
                    "stem": {
                        "en": "If Ken were to help oppose the new policy, what would you research?",
                        "ja": "「ケンが新しい方針に反対するのを手助けするとしたら，あなたは何を調べますか。」"
                    },
                    "choices": [
                        {"label": "①", "en": "The relationship between crime rates and the local area.", "ja": "「犯罪率と地元地域との関係」", "is_correct": True},
                        {"label": "②", "en": "The school's energy budget and electricity bills.", "ja": "「学校のエネルギー予算と電気代」", "is_correct": False},
                        {"label": "③", "en": "The school's activity time versus its budget.", "ja": "「学校の活動時間の長さに対する予算」", "is_correct": False},
                        {"label": "④", "en": "After-school study time for students.", "ja": "「放課後の活動をする学生の学習時間」", "is_correct": False}
                    ],
                    "answer": "①",
                    "explanation": {
                        "ja": "正解は①。問4で見たように，バーガー博士が新しい方針を決めた目的は「市内で重大犯罪が増加し，安全性が低下したので，学生を早く帰宅させたい」ということである。これを覆すためには，「学校の地元地域は犯罪率が高くなく，安全である」ということを証明すればよいので，①が正解。新しい方針の目的は，学校の電気代の削減や，学校での活動にかかる予算の削減や，学生の学習時間確保のためではないので，②，③，④は不適当。またバーガー博士は投稿の第2段落第1文で，The new policy has nothing to do with saving energy.（新しい方針はエネルギーの節約とは何の関係もありません。）と述べているので，③も不適当。",
                        "evidence_sentences": ["2b_s13", "2b_s14"]
                    }
                }
            ]
        }
    ]
}

with open("section2.json", "w", encoding="utf-8") as f:
    json.dump(section2, f, ensure_ascii=False, indent=2)

print("Section 2 generated successfully!")
