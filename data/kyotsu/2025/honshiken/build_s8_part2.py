# -*- coding: utf-8 -*-
# Part2: Questions + Explanations for Section 8
import json

def get_questions():
    return [
        {
            "question_id":"問1","answer_number":38,
            "stem":{"en":"Which of the following best expresses Meilin's opinion? [38]","ja":"「Meilinの意見を最も適切に表しているものは次のどれか」[38]"},
            "choices":[
                {"label":"①","en":"Caution is critical.","ja":"警戒がきわめて重要だ。","is_correct":True},
                {"label":"②","en":"Invention is invaluable.","ja":"発明は非常に貴重だ。","is_correct":False},
                {"label":"③","en":"Science is superior.","ja":"科学は優れている。","is_correct":False},
                {"label":"④","en":"Trust is treasure.","ja":"信頼は宝だ。","is_correct":False}
            ],
            "answer":"①",
            "explanation":{
                "quoted_ja":"正解は①。Meilinの意見の第1文（As the famous physicist, ...）に「有名な物理学者スティーブン・ホーキングがかつて言ったように，この地球上における人類の存在の証拠を遠い宇宙にまで知らしめるのはおそらく危険（dangerous）でしょう」とあることからわかるように，Meilinは宇宙探検について前向きな姿勢を示していないことから，①が正解となる。②の「発明」や，③の「科学」や，④の「信頼」を重視するような意見をMeilinは述べていないので，これらはいずれも正解にはなれない。",
                "quoted_source":"共通テスト 2025年度 本試験 解説",
                "evidence_sentences":["s8_s13","s8_s14","s8_s15","s8_s16"],
                "instructor_note":{
                    "ja":"各意見者の主張を端的に要約したフレーズを選ぶ問題です。",
                    "points":[
                        "s8_s13の「it is probably dangerous to broadcast into deep space evidence of the existence of humans」がMeilinの核心的主張。dangerousという語から「警戒（Caution）」が導かれます。",
                        "s8_s15の「the greatest threat associated with space exploration」でthreatという語も「警戒が重要」を支持します。",
                        "テクニック: 短い格言風の選択肢では，各選択肢のキーワード（Caution/Invention/Science/Trust）と本文中の主張を照合します。Meilinの文にはdangerous, threat, aggressiveなど警戒を示す語が多く，①のCautionと一致します。"
                    ]
                }
            }
        },
        {
            "question_id":"問2","answer_number":39,
            "stem":{"en":"Both Christine and Victor mention that space exploration [39].","ja":"「ChristineとVictorは2人とも宇宙探検は[39]と述べている」"},
            "choices":[
                {"label":"①","en":"has economic impacts and provides opportunities for private corporations to make money","ja":"経済に影響を与え，民間企業がお金を稼ぐ機会を与えてくれる","is_correct":True},
                {"label":"②","en":"is gaining popularity and that salaries for people working in the industry are above average","ja":"人気が高まりつつあり，この産業で働く人々の給料は平均を上回っている","is_correct":False},
                {"label":"③","en":"is politically challenging as it requires coordination among countries with different policies","ja":"政策が異なる国々の間の協力を必要とすることから，政治的に難しい","is_correct":False},
                {"label":"④","en":"needs global cooperation, especially to operate the International Space Station successfully","ja":"特に国際宇宙ステーションをうまく稼働させるには，世界規模の協力が必要とする","is_correct":False}
            ],
            "answer":"①",
            "explanation":{
                "quoted_ja":"正解は①。Christineの意見の第3・4文（More recently, private companies ... / In the future, ...）により最近になって，民間企業が宇宙探検を始めました。ただしこれは主に商業的な理由によるものです。将来は，国や大企業が月や火星の一部に植民地を建設しようとする可能性もあります」とあり，下線部分は①の内容と合っている。また，Victorの意見の第1文（Space exploration has contributed ...）に「宇宙探検は経済成長に大きく貢献してきました」とあり，最終文（In the future, ...）に「将来は，より多くの民間会社が宇宙競争に参加し，宇宙旅行，宇宙での資源採掘，宇宙の植民地化，宇宙の軍事化が増加することにより，さらなる経済成長が確実となるでしょう」とあることから，やはり下線部分は①の内容と合っている。②のようなことはChristineの意見に含まれていない。③のようなことは2人とも述べていない。④のようなことはVictorの意見に含まれていない。",
                "quoted_source":"共通テスト 2025年度 本試験 解説",
                "evidence_sentences":["s8_s9","s8_s10","s8_s24","s8_s27"],
                "instructor_note":{
                    "ja":"2人の意見に共通する内容を特定する問題です。",
                    "points":[
                        "Christineのs8_s9「private companies have begun exploring space, though mostly for commercial reasons」とVictorのs8_s27「more private firms entering the space race」が共通して民間企業の参入に言及しています。",
                        "Victorのs8_s24「contributed hugely to economic growth」が「economic impacts」に対応し，Christineのs8_s9「commercial reasons」が「opportunities to make money」に対応します。",
                        "テクニック: 「Both A and B mention」型の問題では，片方にしか書かれていない情報を含む選択肢を消去法で除外します。②の「salaries above average」はVictorのみ，④の「ISS」はChristineのみの情報です。"
                    ]
                }
            }
        },
        {
            "question_id":"問3","answer_number":40,
            "answer_numbers":[40,41,42],
            "unordered_slots":[40,41],
            "stem":{"en":"Now that you have understood the various opinions, you have taken a position on space exploration and written some notes below. Choose the best options to complete [40]—[42]. (You must have all of [40]—[42] correct to get points.)","ja":"「あなたはいろいろな意見を理解したので，宇宙探検についての見解を固めて，下のようなメモを作成した。[40]—[42]を埋めるのに最も適当な選択肢を選びなさい。（[40]—[42]の全問に正解した場合にのみ点数を与える。）」"},
            "position_box":{"en":"POSITION: Space exploration is not a good idea.\n• [40] and [41] opinions support this the most.\n• An argument common to these two people is that [42].","ja":"見解：宇宙探検は勧められない。\n・[40]意見と[41]意見がこれを最も支持している。\n・この2人に共通する主張は，[42]ということである。"},
            "choices_40":[
                {"label":"①","en":"Apu's","ja":"Apuの"},
                {"label":"②","en":"Christine's","ja":"Christineの"},
                {"label":"③","en":"Meilin's","ja":"Meilinの"},
                {"label":"④","en":"Naomi's","ja":"Naomiの"},
                {"label":"⑤","en":"Victor's","ja":"Victorの"}
            ],
            "choices_41":[
                {"label":"①","en":"Apu's","ja":"Apuの"},
                {"label":"②","en":"Christine's","ja":"Christineの"},
                {"label":"③","en":"Meilin's","ja":"Meilinの"},
                {"label":"④","en":"Naomi's","ja":"Naomiの"},
                {"label":"⑤","en":"Victor's","ja":"Victorの"}
            ],
            "choices_42":[
                {"label":"①","en":"military conflict in outer space is something we should try hard to avoid","ja":"宇宙空間での軍事紛争は，私たちが全力で回避しなければならないものだ"},
                {"label":"②","en":"space exploration exposes people to a lot of danger and is too risky","ja":"宇宙探検は人々を多くの危険にさらすのでリスクが高すぎる"},
                {"label":"③","en":"the possibility of alien invasion is too great to be ignored and must be addressed","ja":"異星人による侵略の可能性は看過するには大きすぎるので，取り組みが必要だ"},
                {"label":"④","en":"the risk of death for people in the industry is extremely high compared with other jobs","ja":"宇宙産業における人間の死のリスクは，他の仕事と比べてきわめて高い"}
            ],
            "answer":{"40":"③","41":"④","42":"②"},
            "answer_note":"[40]と[41]は順不同",
            "explanation":{
                "quoted_ja":"[40]と[41]の正解は③・④。[42]の正解は②。「宇宙探検は勧められない」という見解と基本的に同じ趣旨の意見を述べている人物を選ぶ。5人のうち，DavidとIndiraとYoは動物園について否定的な見解を抱いているのではなく，MeilinとNaomiが宇宙探検に否定的である。Meilinは異星人による地球侵略の可能性という観点から，宇宙探検は「おそらく危険だ（probably dangerous）」という見解であり，③が正解の1つとなる。またNaomiは宇宙探検における死亡率の高さを問題視して，最終文ではWhy should the space industry（tolerate such a high level of danger）?と述べている。これは修辞疑問文で，「なぜ宇宙産業だけが例外なのか〔容認すべきではない〕」という意味なので，やはり基本的に「宇宙探検は勧められない」という見解であることがわかる。したがって④がもう1つの正解となる。①のApuや⑤のVictorは「宇宙探検は勧められない」という趣旨の意見を述べていないので，正解にはなれない。②のChristineは最終文（While financial cooperation ...）で「資金面で協力したり威信を高めるのは喜ぶべきことですが，商業的・軍事的に宇宙空間を不適切に利用することは喜べません」と述べて宇宙探検の功罪両方について指摘しているので，必ずしも「宇宙探検は勧められない」と考えているわけではない。[42]の選択肢：[40]と[41]で選んだMeilinとNaomiに共通する主張を選ぶ。Meilinは異星人による地球侵略の可能性という観点から，宇宙探検は危険だと考えているので，②の内容と合っている。またNaomiについては，死亡率の高さを根拠にして宇宙探検の危険度の高さを訴えていることから，やはり②と合っている。①の「宇宙空間での軍事紛争」や③の「異星人による侵略の可能性」についてはNaomiが全く触れていない。④の「宇宙産業における人間の死のリスク」についてはMeilinが全く触れていない。",
                "quoted_source":"共通テスト 2025年度 本試験 解説",
                "evidence_sentences":["s8_s13","s8_s15","s8_s16","s8_s21","s8_s22"],
                "instructor_note":{
                    "ja":"Step 2の見解に合致する意見者を選び，さらに共通する主張を特定する複合問題です。",
                    "points":[
                        "【重要】Step 2のポジションは「Space exploration is not a good idea」（宇宙探検は勧められない）です。これに賛同する人物を選ぶ必要があります。",
                        "Meilinは「危険（dangerous/threat）」，Naomiは「死亡率（fatality rate 2.9%）」の観点からそれぞれ否定的であり，両者に共通するのは「宇宙探検は危険でリスクが高い」という主張です。",
                        "②が正解となる理由：「exposes people to a lot of danger and is too risky」は，Meilinの「異星人からの脅威」とNaomiの「高い死亡率」の両方を包括する上位概念です。③はMeilinのみ，④はNaomiのみに対応するため不適切。",
                        "テクニック: [42]では2人の主張の「共通項」を探す必要があります。個別の論点（③alien invasion, ④death risk）ではなく，両者を包含する抽象的な表現（②danger/risky）を選びます。"
                    ]
                }
            }
        },
        {
            "question_id":"問4","answer_number":43,
            "stem":{"en":"Based on Source A, which of the following is the most appropriate for REASON 2? [43]","ja":"「資料Aに基づけば，理由2として最適なものは次のどれか」[43]"},
            "choices":[
                {"label":"①","en":"CO2 emissions produced by spacecraft are huge and are damaging outer space.","ja":"宇宙船が生み出すCO2の排出量は莫大で，宇宙空間にダメージを与えている。","is_correct":False},
                {"label":"②","en":"It is difficult to update spacecraft with new engines that emit fewer harmful gases.","ja":"排出するガスがより少ない新しいエンジンを使って宇宙船をより新しく改良するのは難しい。","is_correct":False},
                {"label":"③","en":"Space debris poses risks to humans due to potential collision with airplanes.","ja":"宇宙ゴミは飛行機と衝突する可能性があるので人間にとって危険である。","is_correct":False},
                {"label":"④","en":"Space exploration is polluting the environment of both the Earth and the thermosphere.","ja":"宇宙探検は地球と熱圏の両方の環境を汚染している。","is_correct":True}
            ],
            "answer":"④",
            "explanation":{
                "quoted_ja":"正解は④。資料A（Source A）の内容と合うものを選ぶ。同資料の第4文（More and more spacecraft ...）に「ますます多くの宇宙船が宇宙に送り出されており，これは地球にダメージを与えます」と述べられている。また，第6文（Second, space exploration ...）には「第2に，宇宙探検は熱圏（地球に近い宇宙環境）にダメージを与えています」とある。したがって下線部の内容と合っている④が正解となる。①については，宇宙船が排出するCO2が地球にダメージを与えることは資料Aからは読み取れるが，それが宇宙空間にダメージを与えるとは述べられていない。②のようなことは資料Aからは読み取れない。③のように宇宙ゴミが「飛行機（airplanes）」と衝突する可能性があるとは資料Aでは述べられていない。",
                "quoted_source":"共通テスト 2025年度 本試験 解説",
                "evidence_sentences":["s8_s42","s8_s44","s8_s45","s8_s46","s8_s47"],
                "instructor_note":{
                    "ja":"資料Aの論旨を正確に要約した選択肢を選ぶ問題です。",
                    "points":[
                        "資料Aは2つの論点で構成されています：(1) CO2排出→地球温暖化（s8_s42〜s8_s45），(2) 宇宙ゴミ→熱圏への影響（s8_s46〜s8_s49）。④はこの両方を「Earth and the thermosphere」で正確にカバーしています。",
                        "①の誤り：CO2が「outer space」にダメージを与えるとは書かれていません。CO2の影響は地球の大気・温度に及ぶものです。",
                        "③の誤り：宇宙ゴミが衝突する対象は「future spaceflight」（s8_s49）であり，「airplanes」ではありません。",
                        "テクニック: 資料の要約問題では，本文に書かれていない語（airplanes, outer space等）が選択肢に紛れていないか注意深く確認します。"
                    ]
                }
            }
        },
        {
            "question_id":"問5","answer_number":44,
            "stem":{"en":"For REASON 3, you have decided to write The cost of space exploration is high and the money could be used instead to solve major world problems. Based on Source B, which option best supports this statement? [44]","ja":"「理由3として，あなたは『宇宙探検の費用は高く，そのお金は代わりに世界の主要な問題を解決するのに使うことができるだろう』と書くことに決めた。資料Bに基づけば，この意見を最も適切に支持している選択肢はどれか」[44]"},
            "choices":[
                {"label":"①","en":"The amount of money that governments around the world spend on space exploration could not only reduce hunger but also make primary education available in developing countries.","ja":"世界中の政府が宇宙探検に費やすお金（＝1,030億米ドル）があれば，途上国において飢餓を減らす（＝400億米ドル）だけでなく，初等教育を受けられるようにする（＝540億米ドル）こともできるだろう。","is_correct":True},
                {"label":"②","en":"The data show that it costs less to ensure clean water for people in developing countries than for governments around the world to explore space.","ja":"このデータによれば，世界中の政府が宇宙探検を行うのにかかるお金（＝1,030億米ドル）よりも，途上国の人々のために浄水を確保するのにかかるお金（＝1,500億米ドル）の方が少ない。","is_correct":False},
                {"label":"③","en":"With less than half the money that governments spend on space exploration, it would be possible to address the problem of educational inequality in the developing world.","ja":"政府が宇宙探検に使うお金の半分（＝1,030÷2＝515億米ドル）未満で，途上国における教育の不平等の問題に対処（＝540億米ドル）できるだろう。","is_correct":False},
                {"label":"④","en":"With the money currently invested in space exploration, we could provide sufficient food, basic education, and enough clean water in developing countries.","ja":"現在宇宙探検に投資されているお金（＝1,030億米ドル）があれば，途上国で十分な食料（＝400億米ドル），基礎教育（＝540億米ドル），十分な浄水（＝1,500億米ドル）を供給できるだろう。","is_correct":False}
            ],
            "answer":"①",
            "explanation":{
                "quoted_ja":"正解は①。各選択肢中の下線部の内容を，資料Bのグラフを参照して金額に換算したものをカッコ内に示してある。これにより，正しいことを述べているのは①のみであるとわかる。①：飢餓の緩和400億＋基礎教育の提供540億＝940億 ＜ 宇宙探検1,030億なので正しい。②：浄水の確保1,500億 ＞ 宇宙探検1,030億なので「costs less」は誤り。③：宇宙探検の半分は515億だが，基礎教育は540億なので「less than half」では足りない。④：400＋540＋1,500＝2,440億 ＞ 1,030億なので3つ全ては賄えない。",
                "quoted_source":"共通テスト 2025年度 本試験 解説",
                "evidence_sentences":["s8_s50","s8_s51"],
                "instructor_note":{
                    "ja":"グラフの数値を使って選択肢の正誤を判定する問題です。",
                    "points":[
                        "グラフの数値：宇宙探検への政府投資＝103（10億ドル），浄水供給＝150，基礎教育供給＝54，飢餓緩和＝40",
                        "①の検証：飢餓40＋教育54＝94 ＜ 宇宙探検103 → 正しい。宇宙探検の費用で飢餓と教育の両方に対処できる。",
                        "②の検証：浄水150 ＞ 宇宙探検103 → 「costs less」は誤り。浄水の方が高い。",
                        "③の検証：宇宙探検の半分＝51.5だが，教育は54 → 「less than half」では足りない。",
                        "④の検証：40＋54＋150＝244 ＞ 103 → 3項目すべてを賄えない。",
                        "テクニック: グラフ問題では，選択肢に含まれる数量表現（not only...but also, less than, enough等）を数値で検算することが決定的に重要です。"
                    ]
                }
            }
        }
    ]

if __name__=='__main__':
    qs = get_questions()
    print(f'questions OK, count: {len(qs)}')
    for q in qs:
        print(f"  {q['question_id']} -> {q['answer']}")
