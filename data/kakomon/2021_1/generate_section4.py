import json

section4 = {
    "section_number": 4,
    "title": "第4問",
    "points": 16,
    "pdf_pages": [16, 17, 18, 19, 20],
    "passage_images": [
        "images/mondai_p16.png",
        "images/mondai_p17.png",
        "images/mondai_p18.png",
        "images/mondai_p19.png",
        "images/mondai_p20.png"
    ],
    "explanation_images": [
        "images/kaitou_p11.png",
        "images/kaitou_p12.png",
        "images/kaitou_p13.png"
    ],
    "situation": {
        "en": "Your English teacher Emma has asked you and your classmate Natsuki to help plan the schedule for a day when students from a sister school will visit. You are reading the email exchange between Natsuki and Emma to draft a schedule.",
        "ja": "英語の先生のエマがあなたとクラスメートのナツキに，姉妹校から来る生徒たちを接待する日のスケジュールを計画するのを手伝ってくれるように頼みました。あなたはスケジュールの草案を作成するために，ナツキとエマのメールのやり取りを読んでいます。"
    },
    "passages": [
        {
            "id": "natsuki_email",
            "title": {"en": "Natsuki's Email", "ja": "ナツキのメール"},
            "paragraphs": [
                [
                    {"id": "4_s1", "en": "Hello Emma,", "ja": "こんにちはエマ"},
                    {"id": "4_s2", "en": "I have some ideas and questions about the schedule for the day when 12 guests will visit next month.", "ja": "来月12人のゲストと出かける日のスケジュールについて，いくつかの考えや質問があります。"},
                    {"id": "4_s3", "en": "As you said, students from both schools will give presentations in the assembly hall starting at 10 a.m.", "ja": "先生が言ったように，午前10時から講堂で両校の生徒がプレゼンテーションを行うことになっていますよね。"},
                    {"id": "4_s4", "en": "I was looking at the train timetable. Will they arrive at Azuma station at 9:39 a.m., and then take a taxi from the station to school?", "ja": "それで，私は添付の時刻表を見ていました。彼らは午前9時39分にアズマ駅に到着し，それから学校へタクシーに乗ってくるのですか？"}
                ],
                [
                    {"id": "4_s5", "en": "We've talked about the afternoon activities too.", "ja": "私たちは午後の活動についても話し合ってきました。"},
                    {"id": "4_s6", "en": "How about seeing something science-related?", "ja": "科学に関連するものを見るのはどうですか？"},
                    {"id": "4_s7", "en": "We've discussed two options, but if a third is needed, please let me know.", "ja": "2つの考えがありますが，3つ目が必要な場合はお知らせください。"},
                    {"id": "4_s8", "en": "Have you heard about the special exhibition coming to the Westside Aquarium next month?", "ja": "ウエストサイド水族館で来月行われる特別展示について聞いたことがありますか？"},
                    {"id": "4_s9", "en": "It's about new food supplements made from sea plankton.", "ja": "それは海のプランクトンから作られる新しい栄養補助食品についてです。"},
                    {"id": "4_s10", "en": "That's a great option, I think.", "ja": "それっていい選択肢だと思います。"},
                    {"id": "4_s11", "en": "Since it's popular, the best time to visit will be when it is least busy.", "ja": "人気があるので，一番混んでいない時間帯に行くのがベストでしょうね。"},
                    {"id": "4_s12", "en": "I'll attach a graph I found on the aquarium's website.", "ja": "水族館のホームページで見つけたグラフを添付します。"}
                ],
                [
                    {"id": "4_s13", "en": "Eastside Botanical Garden is working with a local university to develop interesting ways to generate electricity from plants.", "ja": "イーストサイド植物園は，地元の大学と協力して植物から電気を生み出すおもしろい方法を開発しています。"},
                    {"id": "4_s14", "en": "Luckily, the professor in charge will give a short talk about it on that day in the early afternoon!", "ja": "運がいいことに，担当教授がその日の午後の早い時間にそれについて短い話をしてくれます！"},
                    {"id": "4_s15", "en": "Would you like to go?", "ja": "行きませんか？"}
                ],
                [
                    {"id": "4_s16", "en": "Everyone wants souvenirs, right?", "ja": "みんなおみやげを買いたくなりますよね？"},
                    {"id": "4_s17", "en": "I think West Mall, next to Hibari Station, is the best, but you don't want to carry souvenirs all day.", "ja": "ヒバリ駅の隣のウエストモールが一番いいと思いますが，おみやげを一日中持ち歩きたくないですよね。"},
                    {"id": "4_s18", "en": "Everyone visiting Azuma will want to see the symbol of the town, the statue in Azuma Memorial Park next to our school.", "ja": "最後に，アズマを訪れるみんな，町のシンボルで，学校の隣にあるアズマ記念公園の像を見るべきだと思うんですが，いいスケジュールが立てられません。"},
                    {"id": "4_s19", "en": "So could you let me know about the lunch plans?", "ja": "それから，昼食の予定をどうするか教えてもらえませんか？"}
                ]
            ]
        },
        {
            "id": "emma_email",
            "title": {"en": "Emma's Reply", "ja": "エマの返信"},
            "paragraphs": [
                [
                    {"id": "4_s20", "en": "Hello Natsuki,", "ja": "こんにちはナツキ"},
                    {"id": "4_s21", "en": "Thank you for your email! You're doing a great job.", "ja": "メールをありがとう！がんばっていますね。"},
                    {"id": "4_s22", "en": "To answer your question, the students will arrive at the station at 9:20 a.m., and they will take the school bus.", "ja": "質問への答えですが，生徒たちは午前9時20分に駅に着いて，それからスクールバスに乗ります。"}
                ],
                [
                    {"id": "4_s23", "en": "The two main afternoon destinations, the aquarium and the botanical garden, are good ideas.", "ja": "2つのメインの午後の訪問先，水族館と植物園は良い考えですね。"},
                    {"id": "4_s24", "en": "Both schools place emphasis on science education, and the purpose of this program is to improve the scientific knowledge of the students.", "ja": "両校とも科学教育に重点を置いているし，このプログラムの目的は生徒の科学的な知識を向上させることだから。"},
                    {"id": "4_s25", "en": "But it would be wise to have a third option ready, just in case.", "ja": "でも，念のために3つ目の案を用意するのが賢明でしょうね。"}
                ],
                [
                    {"id": "4_s26", "en": "Let's go buy souvenirs at the end of the day.", "ja": "その日の最後におみやげを買いに行きましょう。"},
                    {"id": "4_s27", "en": "We can take the bus to the mall arriving there at 5:00 p.m.", "ja": "モールに午後5時に着くバスに乗ることができます。"},
                    {"id": "4_s28", "en": "This will allow almost an hour shopping and our guests can still be back at the hotel by 6:30 p.m. for dinner, as the hotel is only a few minutes' walk from Kaede Station.", "ja": "そうすればほぼ1時間買い物ができて，ゲストは午後6時30分までに夕食を食べにホテルに戻ることができます。ホテルはカエデ駅から徒歩でたった数分だから。"}
                ],
                [
                    {"id": "4_s29", "en": "For lunch, the school cafeteria will provide boxed lunches.", "ja": "昼食については，学校の食堂がお弁当を用意してくれます。"},
                    {"id": "4_s30", "en": "We can eat under the statue you mentioned.", "ja": "あなたが言った像の下で食べることができますね。"},
                    {"id": "4_s31", "en": "If it rains, let's eat inside.", "ja": "もし雨が降ったら，屋内で食べましょう。"},
                    {"id": "4_s32", "en": "Thank you for your suggestions. Could you two draft a schedule?", "ja": "提案をどうもありがとう。あなたたち二人でスケジュールの草案を作ってくれませんか？"},
                    {"id": "4_s33", "en": "Best,\nEmma", "ja": "よろしくね，\nエマ"}
                ]
            ]
        }
    ],
    "questions": [
        {
            "question_id": "問1",
            "answer_number": 24,
            "answer_numbers": [24, 25],
            "stem": {
                "en": "The guests from the sister school will arrive on train [ 24 ] and return to the hotel on train [ 25 ].",
                "ja": "「姉妹校のゲストは[ 24 ]番の電車で到着し，[ 25 ]番の電車に乗ってホテルに戻ります。」"
            },
            "choices": [
                {"label": "①", "en": "109", "ja": "「109」", "is_correct": False},
                {"label": "②", "en": "110", "ja": "「110」", "is_correct": False},
                {"label": "③", "en": "111", "ja": "「111」", "is_correct": False},
                {"label": "④", "en": "238", "ja": "「238」", "is_correct": False},
                {"label": "⑤", "en": "239", "ja": "「239」", "is_correct": False},
                {"label": "⑥", "en": "240", "ja": "「240」", "is_correct": False}
            ],
            "answers_24_25": ["①", "⑤"],
            "answer": "[ 24 ] ① / [ 25 ] ⑤",
            "explanation": {
                "ja": "正解は[ 24 ]①，[ 25 ]⑤。到着については，ナツキのメールの第1段落第4文のWill they arrive at Azuma station at 9:39 a.m. …?（彼らは午前9時39分にアズマ駅に到着しますか？）という質問に対し，エマはメールの第1段落第3文で，they'll arrive at the station at 9:20 a.m.（彼らは午前9時20分に駅に到着します）と答えている。Train Timetableを見ると，アズマ駅に9:20分に着く電車は109番の電車なので，[ 24 ]には①が入る。ホテルに戻るまでの予定については，エマのメールの第3段落第2～3文にWe can take the bus to the mall arriving there at 5:00 p.m. This will allow almost an hour shopping and our guests can still be back at the hotel by 6:30 p.m. for dinner, as the hotel is only a few minutes' walk from Kaede Station.（モールに午後5時に着くバスに乗ることができます。そうすればほぼ1時間買い物ができて，ゲストは午後6時30分までに夕食を食べにホテルに戻ることができます。ホテルはカエデ駅から徒歩でたった数分だから。）とある。モールの場所については，ナツキのメールの第5段落第2文に，West Mall, next to Hibari Station（ウエストモール，ヒバリ駅の隣）とあるので，モールはヒバリ駅の隣にあることがわかる。ホテルに戻る電車は，以上の情報を整理すると，午後5時からほぼ1時間モールで買い物をするので，午後6時近くにヒバリ駅を出て，カエデ駅に6時半より前に着く電車をTrain Timetableで探せばよいことがわかる。Train Timetableを見ると，ヒバリ駅を18:00に出て，カエデ駅に18:22に着く239番の電車がある。この電車なら1時間近い買い物の時間も取れることができ，カエデ駅から数分歩いても18:30までにホテルに戻れる。したがって，[ 25 ]には⑤が入る。",
                "evidence_sentences": ["4_s22", "4_s27", "4_s28"]
            }
        },
        {
            "question_id": "問2",
            "answer_number": 26,
            "stem": {
                "en": "Which is the most appropriate to complete the draft schedule?",
                "ja": "「スケジュールの草案を完成するのに最も適切なものはどれですか。」"
            },
            "choices": [
                {"label": "①", "en": "D→A→B→C", "ja": "「D→A→B→C」", "is_correct": False},
                {"label": "②", "en": "D→B→A→C", "ja": "「D→B→A→C」", "is_correct": True},
                {"label": "③", "en": "D→B→C→A", "ja": "「D→B→C→A」", "is_correct": False},
                {"label": "④", "en": "D→C→A→B", "ja": "「D→C→A→B」", "is_correct": False}
            ],
            "answer": "②",
            "explanation": {
                "ja": "正解は②。まず，すべての選択肢でDが1番目になっていることに気づこう。水族館については，ナツキのメールの第3段落第4文に，Since it's (= Westside Aquarium is) popular, the best time to visit will be when it is least busy.（それ（＝ウエストサイド水族館）は人気があるので，一番混んでいない時間帯に行くのがベストでしょうね。）とある。添付のグラフを見ると，最も空いているのは15:00～16:00なので，Aは3番目に入る。植物園については，ナツキのメールの第4段落第2文に，the professor in charge will give a short talk about it on that day in the early afternoon!（担当教授がその日の午後の早い時間にそれについて短い話をしてくれます！）とある。13:30は午後の早い時間なので，Bは2番目に入る。したがって正解は②のD→B→A→C。",
                "evidence_sentences": ["4_s11", "4_s14"]
            }
        },
        {
            "question_id": "問3",
            "answer_number": 27,
            "stem": {
                "en": "Where will the guests have lunch?",
                "ja": "「ゲストはどこで昼食を食べるでしょうか。」"
            },
            "choices": [
                {"label": "①", "en": "At the botanical garden", "ja": "「植物園で」", "is_correct": False},
                {"label": "②", "en": "At the school, next to the park", "ja": "「学校の隣の公園で」", "is_correct": True},
                {"label": "③", "en": "At the station park", "ja": "「駅の隣の公園で」", "is_correct": False},
                {"label": "④", "en": "At the school yard", "ja": "「校庭で」", "is_correct": False}
            ],
            "answer": "②",
            "explanation": {
                "ja": "正解は②。エマのメールの第4段落第2～3文に，We can eat under the statue you mentioned. If it rains, let's eat inside.（あなたが言った像の下で食べることができますね。もし雨が降ったら，屋内で食べましょう。）とあるので，雨が降らなければ，ナツキがメールで挙げた像のある場所で昼食を食べると思われる。像のある場所は，ナツキのメールの第6段落第1文によると the statue in Azuma Memorial Park next to our school（学校の隣にあるアズマ記念公園の像） なので，②が正解。①は「植物園」，③は「駅の隣の公園」で不適当。植物園や校庭で昼食を食べるとはどこにも述べられていないので，①と④も不適当。",
                "evidence_sentences": ["4_s30", "4_s18"]
            }
        },
        {
            "question_id": "問4",
            "answer_number": 28,
            "stem": {
                "en": "The guest will not use [ 28 ] for travel on that day.",
                "ja": "「ゲストはその日，[ 28 ]移動しない予定です。」"
            },
            "choices": [
                {"label": "①", "en": "a bus", "ja": "「バスで」", "is_correct": False},
                {"label": "②", "en": "a taxi", "ja": "「タクシーで」", "is_correct": True},
                {"label": "③", "en": "a train", "ja": "「電車で」", "is_correct": False},
                {"label": "④", "en": "on foot", "ja": "「徒歩で」", "is_correct": False}
            ],
            "answer": "②",
            "explanation": {
                "ja": "正解は②。ゲストが使わない移動手段を選ぶ。問1でも見たように，ナツキのメールの第1段落最終文で，「彼らは午前9時39分にアズマ駅に到着し，それから学校へタクシーに乗ってくるのですか？」と質問しているが，それに対してエマはメールの第1段落第3文で，they'll arrive at the station at 9:20 a.m., and they will take the school bus.（彼らは午前9時20分に駅に着いて，それからスクールバスに乗ります。）と答えている。電車とバスは使う。バスはモールに行くときにも使い，電車はモールからホテルに戻るのにも使う。徒歩については問1で見たが，エマのメールの第3段落第3文に hotel is only a few minutes' walk from Kaede Station （ホテルはカエデ駅から徒歩でたった数分だ）とあるように，ゲストはその日の最後に，カエデ駅から数分歩いてホテルに戻るので，徒歩の移動がある。したがって，使わない移動手段はタクシーなので，正解は②。",
                "evidence_sentences": ["4_s22", "4_s28"]
            }
        },
        {
            "question_id": "問5",
            "answer_number": 29,
            "stem": {
                "en": "Which is the best option as a third activity for the program?",
                "ja": "「3つ目の選択肢として，どれがあなたのプログラムに最適ですか。」"
            },
            "choices": [
                {"label": "①", "en": "Hibari Amusement Park", "ja": "「ヒバリ遊園地」", "is_correct": False},
                {"label": "②", "en": "Hibari Art Museum", "ja": "「ヒバリ美術館」", "is_correct": False},
                {"label": "③", "en": "Hibari Castle", "ja": "「ヒバリ城」", "is_correct": False},
                {"label": "④", "en": "Hibari Space Center", "ja": "「ヒバリ宇宙センター」", "is_correct": True}
            ],
            "answer": "④",
            "explanation": {
                "ja": "正解は④。設問で問われている a third option とは，水族館と植物園に加えて，念のために用意しておく3つ目の訪問先のこと。エマのメールの第2段落第1文に both schools place emphasis on science education, and the purpose of this program is to improve the scientific knowledge of the students（両校とも科学教育に重点を置いているし，このプログラムの目的は生徒の科学的な知識を向上させることです）とあるので，科学に関連した訪問先がよい。選択肢の中で科学に関連しているものは宇宙センターである。したがって，④が正解。",
                "evidence_sentences": ["4_s24"]
            }
        }
    ]
}

with open("section4.json", "w", encoding="utf-8") as f:
    json.dump(section4, f, ensure_ascii=False, indent=2)

print("Section 4 generated successfully!")
