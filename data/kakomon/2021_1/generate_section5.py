import json

section5 = {
    "section_number": 5,
    "title": "第5問",
    "points": 15,
    "pdf_pages": [21, 22, 23, 24, 25],
    "passage_images": [
        "images/mondai_p21.png",
        "images/mondai_p22.png",
        "images/mondai_p23.png",
        "images/mondai_p24.png",
        "images/mondai_p25.png"
    ],
    "explanation_images": [
        "images/kaitou_p13.png",
        "images/kaitou_p14.png",
        "images/kaitou_p15.png",
        "images/kaitou_p16.png",
        "images/kaitou_p17.png"
    ],
    "situation": {
        "en": "Using an international news article, you are going to participate in an English oral presentation contest. Read the following French news article to prepare the content of your talk.",
        "ja": "国際報道を使用して，あなたは英語の口頭プレゼンテーションコンテストに参加します。話す内容の準備のために，次のフランスのニュース記事を読みなさい。"
    },
    "passages": [
        {
            "id": "news_article",
            "title": {"en": "Meet Aston", "ja": "アストンを紹介します"},
            "paragraphs": [
                [
                    {"id": "5_s1", "en": "Five years ago, Sabine Rouas lost her horse.", "ja": "5年前，サビーヌ・ルアスは自分の馬を亡くした。"},
                    {"id": "5_s2", "en": "The horse had died of old age, and she had spent 20 years together with it.", "ja": "老衰で亡くなるまで，彼女はその馬と一緒に20年を過ごした。"},
                    {"id": "5_s3", "en": "At that time, she felt she could never have another horse.", "ja": "その当時，彼女は馬をもう二度と飼うことはできないだろうと感じていた。"},
                    {"id": "5_s4", "en": "She spent many hours gazing at the dairy cows on a nearby farm out of loneliness.", "ja": "寂しさから，彼女は近くの牧場の乳牛を眺めて何時間も過ごした。"},
                    {"id": "5_s5", "en": "Then, one day, she asked the farmer if she could help him take care of the dairy cows.", "ja": "それから，ある日，彼女は牧場主に乳牛たちの世話を手伝わせてくれないかとたずねた。"}
                ],
                [
                    {"id": "5_s6", "en": "The farmer agreed, and Sabine started work.", "ja": "牧場主が同意したので，サビーヌは働き始めた。"},
                    {"id": "5_s7", "en": "She quickly grew fond of one of the dairy cows.", "ja": "彼女はすぐに1頭の乳牛と友情を楽しんだ。"},
                    {"id": "5_s8", "en": "That dairy cow was pregnant, so she spent more time with it than the others.", "ja": "その乳牛は妊娠していたので，彼女は他の乳牛よりも多くの時間をその乳牛と過ごした。"},
                    {"id": "5_s9", "en": "After the calf was born, it started to follow Sabine around.", "ja": "子牛が生まれたあと，その子牛はサビーヌのあとをついて歩き始めた。"},
                    {"id": "5_s10", "en": "Unfortunately, the farmer had no interest in keeping the male calf on his dairy farm.", "ja": "残念ながら，その牧場主は雄牛の子を酪農場に置いておくことに興味がなかった。"},
                    {"id": "5_s11", "en": "The farmer was planning to sell the baby bull, called Three-oh-nine, to the meat market.", "ja": "牧場主はその309と呼ばれる赤ちゃんの雄牛を肉市場に売る計画を立てていた。"},
                    {"id": "5_s12", "en": "Sabine couldn't allow that to happen, so she decided to buy the calf and its mother.", "ja": "サビーヌはそんなことをさせるわけにはいかないと決心して，子牛とその母牛を買うことができるかどうか牧場主にたずねた。"},
                    {"id": "5_s13", "en": "The farmer agreed, so she bought the two.", "ja": "牧場主が同意したので，彼女は2頭を買った。"},
                    {"id": "5_s14", "en": "Sabine then started taking 309 for walks to town.", "ja": "それからサビーヌは309を町まで散歩させ始めた。"},
                    {"id": "5_s15", "en": "About nine months later, a permit was finally issued to move the cattle, so they moved to Sabine's farm.", "ja": "約9か月後，ついにその牛たちを移動させる許可が出たので，牛たちはサビーヌの牧場へ移動した。"}
                ],
                [
                    {"id": "5_s16", "en": "Soon after, Sabine was given a pony.", "ja": "その後すぐに，サビーヌは1頭のポニーを譲られた。"},
                    {"id": "5_s17", "en": "At first, she wasn't sure she wanted the pony, but her sad memories of the horse were fading, so she accepted the pony and named it Leon.", "ja": "最初，彼女はそのポニーを飼いたいかどうか確信が持てなかったが，彼女の馬の思い出がもうつらいものではなくなっていたので，そのポニーを受け入れ，レオンと名づけた。"},
                    {"id": "5_s18", "en": "Then she decided to return to her old hobby and started to train Leon in show jumping.", "ja": "それから彼女は昔の趣味に戻ると決め，レオンに障害飛び越えの調教を始めた。"},
                    {"id": "5_s19", "en": "Three-oh-nine, who she had renamed Aston, spent most of his time with Leon and the two became best friends.", "ja": "彼女がアストンと改名した309は，ほとんどの時間をレオンと過ごし，2頭は親友になった。"},
                    {"id": "5_s20", "en": "However, Sabine noticed that Aston was paying close attention to Leon's daily training routines, and she hadn't expected Aston to learn some of the tricks.", "ja": "しかし，サビーヌはアストンがレオンに日常的に行うトレーニングに細心の注意を払うことも，アストンがいくつかの技を習得することも予想していなかった。"},
                    {"id": "5_s21", "en": "The young bull immediately responded to Sabine's voice commands, and learned to walk, gallop, stop, back up, and change direction, just like a horse.", "ja": "その若い雄牛はすぐにサビーヌの声に命令に従って，歩く，疾走する，止まる，後ずさりする，向きを変えるということを馬のように習得した。"},
                    {"id": "5_s22", "en": "And despite weighing 1,300 kilograms, it took him just 18 months to learn how to leap over one-meter-high horse jumps with Sabine on his back.", "ja": "そして体重が1,300キロあるにもかかわらず，たった18か月でサビーヌを背中に乗せて1メートルの高さの障害物を飛び越えるようになった。"},
                    {"id": "5_s23", "en": "Without watching Leon, Aston would never have learned these things.", "ja": "レオンを見ていなければ，アストンは決してそれらのことを覚えなかっただろう。"},
                    {"id": "5_s24", "en": "On top of that, Aston learned to understand distance and adjust his stride before the jump.", "ja": "その上，アストンは距離を理解し，ジャンプの前に歩幅を調整することができた。"},
                    {"id": "5_s25", "en": "He also noticed his faults and corrected them without any help from Sabine.", "ja": "彼はまたサビーヌの助けなしで自分の過ちに気づき，修正していた。"},
                    {"id": "5_s26", "en": "That is the highest Olympic standard that only the very best horses can achieve.", "ja": "それは最高のオリンピック基準の馬だけができることなのだ。"}
                ],
                [
                    {"id": "5_s27", "en": "Now, Sabine and Aston travel to weekend fairs and horse shows around Europe to display their skills.", "ja": "現在，サビーヌとアストンは技を披露するためにヨーロッパ中の週末フェアやホースショーに行っている。"},
                    {"id": "5_s28", "en": "\"We are receiving great reviews,\" she says.", "ja": "「私たちは好評を得ているのよ。」と彼女は言う。"},
                    {"id": "5_s29", "en": "\"Most people are very surprised and initially a little frightened. Because he's big. Much bigger than a horse.\"", "ja": "「たいていの人々はとても驚いて，最初は少し怖がります。だって彼は大きいから。馬よりもずっと大きいから。」"}
                ],
                [
                    {"id": "5_s30", "en": "\"Look!\" Sabine shows a smartphone photo of Aston.", "ja": "「見て！」とサビーヌはスマートフォンのアストンの写真を見せる。"},
                    {"id": "5_s31", "en": "She continues, \"When Aston was very small, I put a leash on him and walked him like a dog to get him used to people. That's probably why he doesn't dislike people.\"", "ja": "そして彼女は「アストンがとっても小さかったとき，彼に犬のようにリードをつけて散歩させたものよ。人間に慣れさせるためにね。たぶん，だから彼は人を嫌がらなくなったのね。」と続ける。"},
                    {"id": "5_s32", "en": "\"He's very gentle, and children especially love to see him and want to get close to him.\"", "ja": "「彼はとてもおとなしいから，特に子どもたちは彼を見るのがとても好きで，彼の近くに寄りたがるのよ。」"}
                ],
                [
                    {"id": "5_s33", "en": "In the past few years, the news of a huge bull that does show jumping has spread rapidly.", "ja": "この数年間で，障害飛び越えをする巨大な雄牛のニュースは急速に広まった。"},
                    {"id": "5_s34", "en": "Aston is now the focus of online followers who are growing in number.", "ja": "今やアストンは増え続けるオンラインフォロワーたちの大きな関心となっている。"},
                    {"id": "5_s35", "en": "Aston and Sabine sometimes need to travel 200 to 300 kilometers away from home, which means they need to stay overnight.", "ja": "アストンとサビーヌはときどき家から200から300キロの旅をする必要があり，それは彼らが宿泊しなければならないことを意味する。"},
                    {"id": "5_s36", "en": "Aston has to sleep in a horse stable, but it's really not big enough for him.", "ja": "アストンは馬小屋で寝なければならず，それは彼には本当に十分な大きさではないのだ。"}
                ],
                [
                    {"id": "5_s37", "en": "\"He doesn't like it. So I have to sleep with him in the stable,\" Sabine says.", "ja": "「彼はそれが好きじゃないのよ。だから私は彼と一緒に馬小屋で寝なければいけないの。」とサビーヌは言う。"},
                    {"id": "5_s38", "en": "\"But you know, when he wakes up, he changes his posture and is very careful not to crush me. He is very kind.\"", "ja": "「でもね，彼が目を覚まして態勢を変えるとき，私を潰さないようにとても気をつけるのよ。彼はとても優しいの。」"},
                    {"id": "5_s39", "en": "\"He sometimes gets lonely and doesn't like to be away from Leon for too long. But other than that, he's very happy.\"", "ja": "「彼はときどき寂しがるし，レオンとあまり長い間離れているのは好きじゃないのよ。でもそれ以外は，彼はとても幸せよ。」"}
                ]
            ]
        }
    ],
    "questions": [
        {
            "question_id": "問1",
            "answer_number": 30,
            "stem": {
                "en": "What is the best title for your presentation?",
                "ja": "「あなたのプレゼンテーションに最もふさわしいタイトルはどれですか。」"
            },
            "choices": [
                {"label": "①", "en": "An animal lover saves a pony's life", "ja": "「動物愛護者がポニーの命を救う」", "is_correct": False},
                {"label": "②", "en": "Aston's summer show jumping tour", "ja": "「アストンの夏の障害飛び越えツアー」", "is_correct": False},
                {"label": "③", "en": "Meet Aston, a bull that acts like a horse", "ja": "「馬のようにふるまう雄牛，アストンを紹介します」", "is_correct": True},
                {"label": "④", "en": "The relationship between a farmer and a cow", "ja": "「ある牧場主とある乳牛との関係」", "is_correct": False}
            ],
            "answer": "③",
            "explanation": {
                "ja": "正解は③。記事の段落ごとの概要は以下の通り。・第1段落：自分の馬を亡くしたサビーヌが，近所の牧場主に乳牛の世話を手伝わせてくれないかとたずねた。・第2段落：サビーヌは牧場で働き始め，妊娠した乳牛を世話するようになる。生まれた309と呼ばれる雄牛はサビーヌになつく。309が肉市場に売られる前に，彼女は牧場主から309と母牛を買い取り，自分の牧場へ連れて行った。・第3段落：サビーヌは1頭のポニーを引き取り，レオンと名づけ，障害飛び越えの調教を始めた。309はアストンと改名され，レオンの調教を見ることで，いくつもの馬術を覚えてしまった。さらに，距離を把握して歩幅を調整するという最高レベルの技までできるようになった。・第4段落：現在，サビーヌとアストンは技を披露するためにヨーロッパ中の週末フェアやホースショーに行き，人気を博している。・第5段落：サビーヌは，アストンが小さいとき，人間に慣れさせるためにリードをつけて散歩させたので，人を嫌がらなくなったのだと考えている。・第6段落：障害飛び越えをする雄牛，アストンのニュースは広まり，オンラインフォロワーも増えている。宿泊を伴うショーに出ることもあり，その際，アストンは狭い馬小屋で寝なければならない。・第7段落：アストンは狭い馬小屋で寝ることや，レオンと長く離れているのは好きではないが，それ以外はとても幸せなのだ，とサビーヌは考えている。以上のタイトルとしては，③のMeet Astonの「アストンに会ってください」→「アストンを紹介させてください」と命令形で読者に訴えかけるタイトルが，馬のように障害飛び越えをするめずらしい雄牛，アストンを紹介している全体の内容に合致する。したがって，③が正解。①については，サビーヌが命を助けたのは雄牛のアストンで，ポニーではないので不適当。②については，アストンが障害飛び越えショーに出るようになったことは第4段落以降に書かれていることであり，全体のタイトルとしてはふさわしくないので，不適当。④については，Farmerとしてこの記事に登場するのは，サビーヌの近所の牧場主であり，Cowは乳牛のこと。牧場主と乳牛の関係については特に述べられていないので，④も不適当。",
                "evidence_sentences": ["5_s19", "5_s21", "5_s22"]
            }
        },
        {
            "question_id": "問2",
            "answer_number": 31,
            "stem": {
                "en": "Which is the best combination for the \"Who's Who?\" slide?",
                "ja": "「『誰が誰？』のスライドの最もよい組み合わせはどれですか。」"
            },
            "choices": [
                {"label": "①", "en": "(Main) 309, Aston, Farmer / (Supporting) Sabine, Pony", "ja": "「(主役）309，アストン，牧場主（脇役）サビーヌ，ポニー」", "is_correct": False},
                {"label": "②", "en": "(Main) Aston, Aston's mother, Sabine / (Supporting) 309, Farmer", "ja": "「（主役）アストン，アストンの母，サビーヌ（脇役）309，牧場主」", "is_correct": False},
                {"label": "③", "en": "(Main) Aston, Leon, Farmer / (Supporting) Aston's mother, Sabine", "ja": "「（主役）アストン，レオン，牧場主（脇役）アストンの母，サビーヌ」", "is_correct": False},
                {"label": "④", "en": "(Main) Aston, Sabine, Pony / (Supporting) Aston's mother, Farmer", "ja": "「（主役）アストン，サビーヌ，ポニー（脇役）アストンの母，牧場主」", "is_correct": True}
            ],
            "answer": "④",
            "explanation": {
                "ja": "正解は④。登場人物のうち，主役3名，脇役2名を選ぶ問題。問1で見たように，この話は「サビーヌが309と呼ばれていた雄牛のアストンを引き取り，そのアストンがポニーのレオンの調教を見て馬術を習得し，今は2人でショーに出演するためにヨーロッパ中を回っている。」というものであるから，まずアストンとサビーヌはともに主役に入っていなければならない。もう1名の主役は，アストンの友達で，アストンが馬術を覚えるきっかけになった，ポニーのレオンである。その他の登場人物は，アストンの母の乳牛と牧場主であるが，2人とも話の前半に出てきただけで，その後の展開には関係していないので，脇役である。したがって，正解は④。Leon が the pony と言い換えられていることに注意。その他の選択肢については，第3段落第4文に，Three-oh-nine, who she had renamed Aston（彼女がアストンと改名した309）とあることから，309とアストンは同じ雄牛。それなのに，①は主役に309とアストンの両方が入っており，脇役に309とアストンを別々のものとして扱っているので，①と②は不適当だとわかる。そして，サビーヌが脇役に入っている③も不適当。",
                "evidence_sentences": ["5_s19"]
            }
        },
        {
            "question_id": "問3",
            "answer_number": 32,
            "answer_numbers": [32, 33, 34, 35],
            "stem": {
                "en": "To complete the \"Before becoming famous\" slide, choose four events and put them in order.",
                "ja": "「「有名になる前のあらすじ」のスライドを完成させるために，4つの出来事を選んで順番に並べなさい。」"
            },
            "choices": [
                {"label": "①", "en": "Aston learns to jump.", "ja": "「アストンがジャンプを覚える。」", "is_correct": False},
                {"label": "②", "en": "Sabine and Aston travel hundreds of km together.", "ja": "「サビーヌとアストンが一緒に数百キロを旅する。」", "is_correct": False},
                {"label": "③", "en": "Sabine buys 309 and its mother.", "ja": "「サビーヌが309とその母牛を買う。」", "is_correct": False},
                {"label": "④", "en": "Sabine starts working at a nearby farm.", "ja": "「サビーヌが近所の農場に働きにいく。」", "is_correct": False},
                {"label": "⑤", "en": "Sabine takes 309 for walks.", "ja": "「サビーヌが309を散歩させる。」", "is_correct": False}
            ],
            "answers_32_35": ["④", "③", "⑤", "①"],
            "answer": "④→③→⑤→①",
            "explanation": {
                "ja": "正解は④→③→⑤→①。記事中から選択肢に該当する箇所を抜き出し，時系列に並べると以下のようになる。・第2段落第1文：The farmer agreed, and Sabine started work.（牧場主が同意したので，サビーヌは働き始めた。）…④・第2段落第8文：The farmer agreed, and she bought them (= three-oh-nine and his mother).（牧場主が同意したので，彼女はそれら（＝309と母牛）を買った。）…③・第2段落第9文：Sabine then started taking 309 for walks to town.（それからサビーヌは309を町まで散歩させ始めた。）…⑤・第3段落第8文：it took him just 18 months to learn how to leap over one-meter-high horse jumps with Sabine on his back（アストンはたった18か月でサビーヌを背中に乗せて1メートルの高さの障害物を飛び越えるようになった）…①。②の該当箇所としては第6段落第2文に，Aston and Sabine sometimes need to travel 200 or 300 kilometers away from home（アストンとサビーヌはときどき家から200から300キロの旅をする必要がある）とあるが，これは有名になった後のことなので、②はどこにも入らない。したがって，正解は④→③→⑤→①。",
                "evidence_sentences": ["5_s6", "5_s13", "5_s14", "5_s22"]
            }
        },
        {
            "question_id": "問4",
            "answer_number": 36,
            "answer_numbers": [36, 37],
            "stem": {
                "en": "Choose two items that best match the \"Aston's Abilities\" slide. (Order doesn't matter.)",
                "ja": "「『アストンの能力』のスライドに最も合う2つの項目を選びなさい。（順不同）」"
            },
            "choices": [
                {"label": "①", "en": "Fixes his own mistakes himself.", "ja": "「自分自身で過ちを正す。」", "is_correct": True},
                {"label": "②", "en": "Jumps alongside the pony.", "ja": "「ポニーと横並びでジャンプする。」", "is_correct": False},
                {"label": "③", "en": "Lets a rider on his back to jump.", "ja": "「騎手を背中に乗せてジャンプする。」", "is_correct": True},
                {"label": "④", "en": "Learns tricks faster than a horse.", "ja": "「馬よりも速く技を習得する。」", "is_correct": False},
                {"label": "⑤", "en": "Poses for photos.", "ja": "「写真用にポーズをとる。」", "is_correct": False}
            ],
            "answers_36_37": ["①", "③"],
            "answer": "①・③（順不同）",
            "explanation": {
                "ja": "正解は①と③。第3段落第11文にHe (= Aston) also noticed his faults and corrected them without any help from Sabine.（彼（＝アストン）はまたサビーヌの助けなしで自分の過ちに気づき，修正していた。）とあるので，①が正解。また第3段落第8文に，it took him just 18 months to learn how to leap over one-meter-high horse jumps with Sabine on his back.（たった18か月でサビーヌを背中に乗せて1メートルの高さの障害物を飛び越えるようになった）とあるので，③も正解。第3段落に，アストンはポニーのレオンの調教を見てジャンプなどの技を覚えたことが書かれているが，レオンと横並びでジャンプしたり，レオンより早く技を覚えたという記述はないので，②と④は不適当。⑤のようなことは本文にまったく書かれていないのでこれも不適当。",
                "evidence_sentences": ["5_s25", "5_s22"]
            }
        },
        {
            "question_id": "問5",
            "answer_number": 38,
            "stem": {
                "en": "Choose the best item for the \"Aston Now\" section.",
                "ja": "「『アストンの今』のスライドに最も合う項目を選びなさい。」"
            },
            "choices": [
                {"label": "①", "en": "He goes to events with Sabine and Leon.", "ja": "「彼はサビーヌとレオンと一緒にイベントに行く。」", "is_correct": False},
                {"label": "②", "en": "He is becoming an online celebrity.", "ja": "「彼はオンラインの人気者になりつつある。」", "is_correct": True},
                {"label": "③", "en": "He is performing tricks in a bigger stable.", "ja": "「彼はより大きな馬小屋で技を披露している。」", "is_correct": False},
                {"label": "④", "en": "He sleeps next to Leon every night.", "ja": "「彼は毎晩レオンの隣で寝ている。」", "is_correct": False}
            ],
            "answer": "②",
            "explanation": {
                "ja": "正解は②。第6段落第1～2文に，In the past few years, the news of a huge bull that does show jumping has spread rapidly. Aston is now the focus of online followers who are growing in number.（この数年間で，障害飛び越えをする巨大な雄牛のニュースは急速に広まった。今やアストンは増え続けるオンラインフォロワーたちの大きな関心となっている。）とあるので，②が正解。①については，サビーヌとアストンがショーに出るために旅をすることは書かれているが，レオンも一緒に行くとは書かれていないので，不適当。③については，第6段落第4文に Aston has to sleep in a horse stable, but it's really not big enough for him.（アストンは馬小屋で寝なければならず，それは彼には本当に十分な大きさではない）とあり，「大きな馬小屋」とは逆なので不適当。④については，アストンが毎晩レオンの隣で寝るとは書かれていないので不適当。",
                "evidence_sentences": ["5_s33", "5_s34"]
            }
        }
    ]
}

with open("section5.json", "w", encoding="utf-8") as f:
    json.dump(section5, f, ensure_ascii=False, indent=2)

print("Section 5 generated successfully!")
