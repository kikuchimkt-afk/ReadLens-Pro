import json

section3 = {
    "section_number": 3,
    "title": "第3問",
    "points": 15,
    "pdf_pages": [11, 12, 13, 14, 15],
    "passage_images": [
        "images/mondai_p11.png",
        "images/mondai_p12.png",
        "images/mondai_p13.png",
        "images/mondai_p14.png",
        "images/mondai_p15.png"
    ],
    "explanation_images": [
        "images/kaitou_p7.png",
        "images/kaitou_p8.png",
        "images/kaitou_p9.png",
        "images/kaitou_p10.png",
        "images/kaitou_p11.png"
    ],
    "sub_sections": [
        {
            "sub_section": "A",
            "situation": {
                "en": "You are planning to stay at a hotel in the UK and found useful information in the Q&A section of a travel support website.",
                "ja": "あなたはイギリスのホテルに滞在することを計画中です。あなたは旅行支援サイトのよくある質問のコーナーで役立つ情報を見つけました。"
            },
            "passages": [
                {
                    "id": "qa_post",
                    "title": {
                        "en": "Q&A: Hollytree Hotel in Castleton",
                        "ja": "Q&A: キャッスルトンのホーリーツリー・ホテル"
                    },
                    "paragraphs": [
                        [
                            {"id": "3a_s1", "en": "I stayed at the Hollytree Hotel in Castleton in March 2021 and am thinking about a stay at the hotel. Would you recommend this hotel, and is it easy to get there from Paxton Airport? (Liz)", "ja": "私は2021年3月にキャッスルトンのホーリーツリー・ホテルへの滞在を考えています。このホテルはおすすめですか，またパクストン空港からそこへ行くのは簡単ですか？（リズ）"}
                        ],
                        [
                            {"id": "3a_s2", "en": "Yes, I strongly recommend the Hollytree Hotel.", "ja": "はい，私はホーリーツリー・ホテルを強くおすすめします。"},
                            {"id": "3a_s3", "en": "I have stayed there twice.", "ja": "私はそこに2度滞在したことがあります。"},
                            {"id": "3a_s4", "en": "It's inexpensive, and the service is brilliant!", "ja": "値段は高くはなく，サービスは最高です！"},
                            {"id": "3a_s5", "en": "There's also a wonderful free breakfast.", "ja": "美味しい無料の朝食もあります。"}
                        ],
                        [
                            {"id": "3a_s6", "en": "Let me tell you about my experiences getting there.", "ja": "そこへ近くまでの私の体験を紹介させてください。"},
                            {"id": "3a_s7", "en": "On my first trip, I used the underground.", "ja": "最初の訪問では，私は地下鉄を使いました。"},
                            {"id": "3a_s8", "en": "The underground is cheap and convenient.", "ja": "地下鉄は安くて便利です。"},
                            {"id": "3a_s9", "en": "Trains run every 5 minutes.", "ja": "電車は5分おきに走っています。"},
                            {"id": "3a_s10", "en": "From the airport, I took the Red Line to Mossfield.", "ja": "空港から，私はレッド線を使ってモスフィールドへ行きました。"},
                            {"id": "3a_s11", "en": "Transferring to the Orange Line for Victoria should normally take about seven minutes, but the directions weren't clear and I needed an extra five minutes.", "ja": "オレンジ線に乗り換えてビクトリアへ行くのに普通は約7分かかりますが，行き方がわかりにくく，私は5分よけいにかかりました。"},
                            {"id": "3a_s12", "en": "From Victoria Station, I took the city bus to the hotel, which took 10 minutes.", "ja": "ビクトリア駅からホテルまでバスで10分でした。"}
                        ],
                        [
                            {"id": "3a_s13", "en": "The second time, I used the express bus to Victoria, so there was no anxiety about transfers.", "ja": "2度目はビクトリア行きの高速バスを使ったので，乗り換えの不安はありませんでした。"},
                            {"id": "3a_s14", "en": "But I found a notice saying there would be roadworks until summer 2021.", "ja": "しかし，2021年の夏まで道路工事があるという告知を見つけました。"},
                            {"id": "3a_s15", "en": "Now it takes three times as long as usual to get to the hotel by city bus.", "ja": "現在，市バスでホテルに到着するのに通常の3倍の時間がかかります。"},
                            {"id": "3a_s16", "en": "You can also walk there, but the weather was bad, so I took the bus.", "ja": "歩いて行くこともできますが，天気が悪かったので私はバスに乗りました。"},
                            {"id": "3a_s17", "en": "Enjoy your stay! (Alex)", "ja": "楽しい滞在を！（アレックス）"}
                        ]
                    ]
                }
            ],
            "questions": [
                {
                    "question_id": "問1",
                    "answer_number": 16,
                    "stem": {
                        "en": "From Alex's answer, you learn that Alex [ 16 ].",
                        "ja": "「アレックスの回答から，あなたはアレックスが[ 16 ]とわかります。」"
                    },
                    "choices": [
                        {"label": "①", "en": "appreciates the hotel's convenient location", "ja": "「そのホテルの便利な立地を高く評価している」", "is_correct": False},
                        {"label": "②", "en": "got lost on the first trip to Castleton at Victoria Station", "ja": "「キャッスルトンへの最初の旅行で，ビクトリア駅で迷った」", "is_correct": False},
                        {"label": "③", "en": "thinks the hotel is good value for money", "ja": "「そのホテルはお金を払う値打ちがあると考えている」", "is_correct": True},
                        {"label": "④", "en": "used the same route from the airport both times", "ja": "「2度とも空港から同じルートを使った」", "is_correct": False}
                    ],
                    "answer": "③",
                    "explanation": {
                        "ja": "正解は③。Answerの第1段落の第1文に，I strongly recommend the Hollytree Hotel（私はホーリーツリー・ホテルを強くおすすめします）とあり，続く第3〜4文でその理由として，It's inexpensive, and the service is brilliant! There's also a wonderful free breakfast.（値段は高くはなく，サービスは最高です！美味しい無料の朝食もあります。）とあるので，③が正解。good value for moneyは「支払う価値がある；お値打ち品」という意味。①については，「便利な立地」とは言っておらず，空港からホテルまでも乗り換えが必用なので，①は不適当。②については，第3段落第3〜4文に，I took the Red Line to Mossfield. Transferring to the Orange Line for Victoria should normally take about seven minutes, but the directions weren't clear and I needed an extra five minutes.（私はレッド線を使ってモスフィールドへ行きました。オレンジ線に乗り換えてビクトリアへ行くのに普通は約7分かかりますが，案内がわかりにくく，私は5分よけいにかかりました。）とあり，迷ったのはビクトリア駅ではなくモスフィールド駅だったので，②も不適当。④については，Answerの第3段落の最初の訪問の行程をまとめると「空港から地下鉄をモスフィールド駅で乗り換えてビクトリア駅へ。ビクトリア駅から市バスでホテルへ行った。」となり，第4段落の2度目の行程をまとめると「空港から高速バスでビクトリア駅へ。そこから市バスでホテルへ行った。」となる。異なるルートを使っているので，④も不適当。",
                        "evidence_sentences": ["3a_s4", "3a_s5"]
                    }
                },
                {
                    "question_id": "問2",
                    "answer_number": 17,
                    "stem": {
                        "en": "You are departing the airport by public transport at 2 p.m. on March 15, 2021. What is the fastest way to get to the hotel?",
                        "ja": "「あなたは2021年3月15日午後2時に空港から公共交通機関で出発するところです。ホテルまでの最速の行き方は何ですか。」"
                    },
                    "choices": [
                        {"label": "①", "en": "Express bus and city bus", "ja": "「高速バスと市バス」", "is_correct": False},
                        {"label": "②", "en": "Express bus and walking", "ja": "「高速バスと徒歩」", "is_correct": True},
                        {"label": "③", "en": "Underground and city bus", "ja": "「地下鉄と市バス」", "is_correct": False},
                        {"label": "④", "en": "Underground and walking", "ja": "「地下鉄と徒歩」", "is_correct": False}
                    ],
                    "answer": "②",
                    "explanation": {
                        "ja": "正解は②。選択肢は空港からホテルまでの4つの行き方であり，アクセス図を見ると，空港からビクトリア駅までは「地下鉄を乗り継ぐ方法」と「高速バス」の2つ，そしてビクトリア駅からホテルまでは「市バス」と「徒歩」の2つの行き方があることがわかる。まず，空港からビクトリア駅までを考える。地下鉄を乗り継ぐ場合，図から「レッド線25分」でモスフィールド駅に着き，さらに「オレンジ線」に乗り換えると10分でビクトリア駅に着くことがわかる。乗り換えには，Answerの第3段落第4文に，Transferring to the Orange Line for Victoria should normally take about seven minutes.（オレンジ線に乗り換えてビクトリアへ行くのに普通は約7分かかります）とあるから，7分かかる。地下鉄の所要時間は，乗り換えも含め，25+7+10=42分。一方，高速バスの所要時間は40分であることが表から読み取れる。さらに高速バスの待ち時間をスケジュールから確認すると，始発が午前10時ちょうどで，30分おきに出発することがわかる。空港を午後2時ちょうどには高速バスがあるということだから，待ち時間は無いと考えられる。したがって，40分で行ける高速バスの方が，待ち時間を考えないでも42分かかる地下鉄よりも，ビクトリア駅まで早く着ける。次に，ビクトリア駅からホテルまでのそれぞれの所要時間は「市バス10分」「徒歩20分」であることがわかるが，Answerの第4段落第2～3文に，I found a notice saying there would be roadworks until summer 2021. Now it takes three times as long as usual to get to the hotel by city bus.（私は2021年の夏まで道路工事があるという告知を見つけました。現在，市バスでホテルに到着するのに通常の3倍の時間がかかります。）とあるので，出発日にはまだ道路工事の影響を受けることがわかる。よって，市バスでは10×3=30分となり，ビクトリア駅からホテルまでは，徒歩20分の方が速いことがわかる。したがって，正解は「高速バスと徒歩」の②である。",
                        "evidence_sentences": ["3a_s11", "3a_s14", "3a_s15"]
                    }
                }
            ]
        },
        {
            "sub_section": "B",
            "situation": {
                "en": "Your classmate has shown you a message from a UK exchange student published in the school newsletter.",
                "ja": "クラスメートがあなたにイギリスからの交換留学生によって書かれた学校通信の次のメッセージを見せてきました。"
            },
            "passages": [
                {
                    "id": "newsletter",
                    "title": {
                        "en": "Volunteers Wanted!",
                        "ja": "ボランティア募集！"
                    },
                    "paragraphs": [
                        [
                            {"id": "3b_s1", "en": "Hello everyone. I'm Sarah King, an exchange student from London.", "ja": "みなさん，こんにちは。私はロンドン出身の交換留学生のセーラ・キングです。"},
                            {"id": "3b_s2", "en": "Today I have something important to share with you.", "ja": "今日はみなさんと重要なことを共有したいと思います。"}
                        ],
                        [
                            {"id": "3b_s3", "en": "You may have heard of the Sakura International Centre.", "ja": "みなさんはサクラ国際センターのことを聞いたことがあるかもしれません。"},
                            {"id": "3b_s4", "en": "It provides valuable opportunities for Japanese and foreign residents to get to know each other.", "ja": "それは日本人と外国人の住民がお互いに知り合うための貴重な機会を提供しています。"},
                            {"id": "3b_s5", "en": "Popular events like cooking classes and karaoke contests are held monthly.", "ja": "料理教室やカラオケ大会のような人気のイベントが毎月開かれています。"},
                            {"id": "3b_s6", "en": "However, there is a serious problem.", "ja": "けれども深刻な問題があります。"},
                            {"id": "3b_s7", "en": "The building is getting old and needs expensive repairs.", "ja": "建物が古くなってきていて，お金のかかる修理が必要なのです。"},
                            {"id": "3b_s8", "en": "Many volunteers are needed to help raise funds to maintain the centre.", "ja": "センターを維持するための募金の手助けのために，たくさんのボランティアが必要とされています。"}
                        ],
                        [
                            {"id": "3b_s9", "en": "I learnt about that problem a few months ago.", "ja": "私はその問題を数か月前に知りました。"},
                            {"id": "3b_s10", "en": "When I was shopping in town, I saw some people taking part in a fund-raising campaign.", "ja": "町で買い物をしているときに，私は数人の人が募金運動に参加しているのを見ました。"},
                            {"id": "3b_s11", "en": "I spoke to the leader of the campaign, Katy, and she explained the situation.", "ja": "私はその運動のリーダーのケイティに話しかけ，彼女は状況を説明してくれました。"},
                            {"id": "3b_s12", "en": "When I donated some money, she thanked me.", "ja": "私がお金を寄付すると，彼女は私にお礼を言いました。"},
                            {"id": "3b_s13", "en": "She told me that they had asked the town mayor for financial assistance, but their request had been rejected.", "ja": "彼女は私に，町長に資金援助を願い出たけれど，そのお願いは断られてしまったと言いました。"},
                            {"id": "3b_s14", "en": "There was no choice but to start the fund-raising campaign.", "ja": "彼女らは募金活動を始める以外に選択肢がなかったのです。"}
                        ],
                        [
                            {"id": "3b_s15", "en": "Last month, I attended a lecture on art at the centre.", "ja": "先月，私はそのセンターの芸術についての講義に出席しました。"},
                            {"id": "3b_s16", "en": "I saw that there were still people trying to raise money, and I decided to help.", "ja": "私はまだ人々が募金をしようとしているのを見て，手伝うことを決めました。"},
                            {"id": "3b_s17", "en": "When I joined the campaigners asking passers-by to donate, Katy was delighted.", "ja": "私が通行人に寄付を求める彼女たちに加わったとき，ケイティは喜びました。"},
                            {"id": "3b_s18", "en": "We asked enthusiastically, but there were too few people to collect much money.", "ja": "私たちは熱心にお願いしましたが，参加者がとても少なすぎてたくさんのお金を集めることができませんでした。"},
                            {"id": "3b_s19", "en": "With a tearful face, Katy told me that the building would not be able to be used much longer.", "ja": "泣きそうな顔で，ケイティは私に，その建物をもうあまり長く使うことができないだろうと言いました。"},
                            {"id": "3b_s20", "en": "I felt the need to do more.", "ja": "私はもっと何かをする必要を感じました。"},
                            {"id": "3b_s21", "en": "Then the idea came to me that other students might be willing to help.", "ja": "そのとき，ほかにも進んで手伝ってくれる学生がいるかもしれないという考えが浮かびました。"},
                            {"id": "3b_s22", "en": "Katy was delighted to hear this.", "ja": "ケイティはこれを聞いて喜びました。"}
                        ],
                        [
                            {"id": "3b_s23", "en": "Now I'm asking you to join me in the fund-raising campaign to help the Sakura International Centre.", "ja": "今，私はみなさんにサクラ国際センターを手助けする募金運動に加わってくれるようお願いしています。"},
                            {"id": "3b_s24", "en": "Please email me today!", "ja": "今日，私にメールをください！"},
                            {"id": "3b_s25", "en": "As an exchange student, my time in Japan is limited, but I want to make the most of it.", "ja": "交換留学生として私が日本にいる時間は限られていますが，私はできる限りのことをしたいです。"},
                            {"id": "3b_s26", "en": "By working together, we can really make a difference.", "ja": "一緒に活動すれば，私たちは本当に何かを変えられるかもしれません。"}
                        ]
                    ]
                }
            ],
            "questions": [
                {
                    "question_id": "問1",
                    "answer_number": 18,
                    "answer_numbers": [18, 19, 20, 21],
                    "stem": {
                        "en": "Put the following events in the order they happened. [ 18 ] - [ 21 ]",
                        "ja": "「次の出来事を起こった順に並べなさい。[ 18 ] - [ 21 ]」"
                    },
                    "choices": [
                        {"label": "①", "en": "Sarah attended an event at the centre.", "ja": "「セーラはセンターのイベントに出席した。」", "is_correct": False},
                        {"label": "②", "en": "Sarah donated money to the centre.", "ja": "「セーラはセンターにお金を寄付した。」", "is_correct": False},
                        {"label": "③", "en": "Sarah made a suggestion to Katy.", "ja": "「セーラはケイティに提案をした。」", "is_correct": False},
                        {"label": "④", "en": "The campaigners asked the mayor for aid.", "ja": "「運動参加者は町長に援助をお願いした。」", "is_correct": False}
                    ],
                    "answers_18_21": ["④", "②", "①", "③"],
                    "answer": "④→②→①→③",
                    "explanation": {
                        "ja": "正解は④→②→①→③。まず第3段落を見てみよう。第4～5文に，She (= Katy) thanked me when I donated some money. She (= Katy) told me that they had asked the town mayor for financial assistance, but their request had been rejected.（私がお金を寄付すると，ケイティは私にお礼を言いました。ケイティは私に，町長に資金援助を願い出たけれど，そのお願いは断られてしまったと言いました。）とある。ここでお金を寄付したことはdonatedと過去形で，資金援助を願い出たことは主節がtoldと過去形で，that節中で had asked と過去完了形（had＋過去分詞）で表されている。それは過去完了形で表した「資金援助を願い出た」というthat節の時点よりさらに前に起こっていたことで，②→④の順だとわかる。第3段落第1文に，a few months ago（2, 3か月前に）とあることから，セーラがケイティに会って話を聞き，お金を寄付したのは2，3か月前である。続く第4段落第1文に，Last month, I attended a lecture on art at the center.（先月，私はそのセンターの芸術についての講義に出席しました。）とあり，これが①の「センターのイベントに出席」に当たる。この段落では，その後セーラも募金に加わるようになったが，募金を求める人数が少ないため，あまりお金が集まらなかったことが述べられている。そして最後の2文で，the idea came to me that other students might be willing to help. Katy was delighted to hear this.（ほかにも進んで手伝ってくれる学生がいるかもしれないという考えが浮かびました。ケイティはこれを聞いて喜びました。）と，セーラがケイティに学生ボランティアを募集しようと提案したことが読み取れ，これが③に当たる。したがって，正解は④→②→①→③。",
                        "evidence_sentences": ["3b_s12", "3b_s13", "3b_s15", "3b_s21"]
                    }
                },
                {
                    "question_id": "問2",
                    "answer_number": 22,
                    "stem": {
                        "en": "From Sarah's message, you learn that the Sakura International Centre is [ 22 ].",
                        "ja": "「セーラのメッセージから，あなたはサクラ国際センターは[ 22 ]と知りました。」"
                    },
                    "choices": [
                        {"label": "①", "en": "providing financial support to people living abroad", "ja": "「海外居住者に金銭的な援助をしている」", "is_correct": False},
                        {"label": "②", "en": "offering chances to develop friendships", "ja": "「友情をはぐくむ機会を提供している」", "is_correct": True},
                        {"label": "③", "en": "publishing a newsletter for life in the community", "ja": "「その地域社会に会報を発行している」", "is_correct": False},
                        {"label": "④", "en": "sending exchange students to the UK", "ja": "「イギリスに交換留学生を送っている」", "is_correct": False}
                    ],
                    "answer": "②",
                    "explanation": {
                        "ja": "正解は②。第2段落第2文に，It (= Sakura International Centre) provides valuable opportunities for Japanese and foreign residents to get to know each other.（サクラ国際センターは日本人と外国人の住民がお互いに知り合うための貴重な機会を提供しています。）とあるので，②が正解。本文のto get to know each otherが，選択肢ではto develop friendshipsと言い換えられている。ほかの選択肢に関しては，本文にまったく記載がないので，①，③，④は不適当。",
                        "evidence_sentences": ["3b_s4"]
                    }
                },
                {
                    "question_id": "問3",
                    "answer_number": 23,
                    "stem": {
                        "en": "After reading Sarah's message, you decided to help the campaign. What should you do first?",
                        "ja": "「セーラのメッセージを読んだあと，あなたはその運動を手伝う決心をしました。あなたが最初にすべきことは何ですか。」"
                    },
                    "choices": [
                        {"label": "①", "en": "Advertise the centre's events at school.", "ja": "「そのセンターでイベントを宣伝する。」", "is_correct": False},
                        {"label": "②", "en": "Contact Sarah for further information.", "ja": "「もっと情報を得るためにセーラに連絡する。」", "is_correct": True},
                        {"label": "③", "en": "Organise volunteer activities at school.", "ja": "「学校でボランティア活動を組織する。」", "is_correct": False},
                        {"label": "④", "en": "Start a new fund-raising campaign.", "ja": "「新たな募金運動を始める。」", "is_correct": False}
                    ],
                    "answer": "②",
                    "explanation": {
                        "ja": "正解は②。セーラは第5段落第1～2文で，I'm asking you to join me in the fund-raising campaign to help the Sakura International Centre. Please email me today!（私はみなさんにサクラ国際センターを手助けする募金運動に加わってくれるようお願いしています。今日，私にメールをください！）と述べているので，Please email meをContact Sarah for further information.と言い換えている②が正解。ほかの選択肢に関しては本文に記載がないので，①，③，④は不適当。",
                        "evidence_sentences": ["3b_s23", "3b_s24"]
                    }
                }
            ]
        }
    ]
}

with open("section3.json", "w", encoding="utf-8") as f:
    json.dump(section3, f, ensure_ascii=False, indent=2)

print("Section 3 generated successfully!")
