# -*- coding: utf-8 -*-
"""Z会 実戦模試 2026 第3回 第2問（在宅勤務・コメント）を data.json にマージする。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUOTED = "Z会『2026年 共通テスト実戦模試 英語リーディング』第3回 解説冊子"

section_02 = {
    "section_number": 2,
    "title": "第2問",
    "points": 10,
    "points_per_question": 2,
    "description": "短文読解（記事＋ウェブコメント）",
    "situation": {
        "en": (
            "Your English teacher gave you an article to help you prepare for the debate in the next class. "
            "A part of this article with one of the comments is shown below."
        ),
        "ja": (
            "あなたの英語の先生は次の授業での討論の準備に役立つ記事をくれました。"
            "この記事の一部とコメントの1つは下記の通りです。"
        ),
    },
    "passages": [
        {
            "id": "telecommute_article",
            "framed": True,
            "title": {
                "en": "Will Telecommuting Change the Way We Work?",
                "ja": "在宅勤務は私たちの働き方を変えるか？",
            },
            "subtitle": {
                "en": "By Nancy Garcia, Los Angeles\n31 JULY 2018 • 5:17 p.m.",
                "ja": "ロサンゼルス　ナンシー・ガルシア　記\n2018年7月31日　午後5:17",
            },
            "paragraphs": [
                [
                    {
                        "id": "tc_p1_s1",
                        "en": (
                            "The American Community Survey (ACS) updated their statistics on the telecommuting population "
                            "in the USA."
                        ),
                        "ja": "米国コミュニティ調査（ACS）はアメリカ合衆国での在宅勤務人口の統計を更新した。",
                    },
                    {
                        "id": "tc_p1_s2",
                        "en": (
                            "According to the data, the number of people who work at home for more than half of their working time "
                            "using digital telecommunications was, as of 2016, 4.3 million; 3.2% of the total workforce."
                        ),
                        "ja": (
                            "そのデータによると，デジタル遠距離通信を用いて仕事時間の半分より多い時間自宅で仕事をする人々の数は，"
                            "2016年の時点で430万人，労働人口全体の3.2%であった。"
                        ),
                    },
                    {
                        "id": "tc_p1_s3",
                        "en": "This did not include the self-employed.",
                        "ja": "これは個人事業主を含んでいない。",
                    },
                ],
                [
                    {
                        "id": "tc_p2_s1",
                        "en": (
                            "David Howe, a business consultant, emphasizes the advantages of telecommuting, saying, "
                            "'Telecommuting saves employees commuting time, which is useless and painful. "
                            "For parents with small children, it gives them more time to spend with their children. "
                            "For employers, it saves them transportation and utilities costs.'"
                        ),
                        "ja": (
                            "ビジネスコンサルタントのデイビッド・ハウは在宅勤務の利点について次のように力説している。"
                            "「在宅勤務は，被雇用者の無駄で苦痛を伴う通勤時間を省きます。"
                            "小さい子供がいる親にとっては，子供と一緒に過ごす時間が増えます。"
                            "雇用主にとっては，交通費や光熱費の節約になります。」"
                        ),
                    }
                ],
                [
                    {
                        "id": "tc_p3_s1",
                        "en": (
                            "On the other hand, Mary Holden, who has experienced telecommuting, says, "
                            "'Telecommuting has a lot of advantages, but some disadvantages, too. "
                            "For example, telecommuters tend to have less opportunity to meet other people on business, "
                            "and sometimes forget the meaning of their work. "
                            "Additionally, if a teleworker is experienced, there is no problem, but if not, "
                            "it might be difficult for them to communicate with other people about how he or she should be doing the work. "
                            "Furthermore, the increase in working hours and the large decrease in pay per hour are also problems.'"
                        ),
                        "ja": (
                            "一方，在宅勤務を経験したメアリー・ホールデンは，"
                            "「在宅勤務には多くの利点がありますが，いくつか欠点もあります。"
                            "例えば，在宅勤務者は仕事で他の人と会う機会が少ない傾向があり，時として自分の仕事の意義を見失います。"
                            "加えて，在宅勤務者が経験豊かであれば問題ないのですが，そうでなければ，"
                            "彼または彼女がどのようにその仕事をすべきかについて他人とやり取りするのは難しいかもしれません。"
                            "さらに，労働時間の増加と時給の大幅な減少も問題となります。」と話している。"
                        ),
                    }
                ],
            ],
        },
        {
            "id": "angela_comment",
            "framed": True,
            "title": {"en": "15 Comments", "ja": "15のコメント"},
            "subtitle": {"en": "Newest", "ja": "最新"},
            "paragraphs": [
                [
                    {
                        "id": "aj_meta",
                        "en": "Angela Jones   2 August 2018 • 7:20 p.m.",
                        "ja": "アンジェラ・ジョーンズ　2018年8月2日　午後7:20",
                    },
                    {
                        "id": "aj_s1",
                        "en": (
                            "I am also a telecommuter. Despite living in the countryside where I can enjoy the beauty of nature, "
                            "I can earn enough money by telecommuting. If the number of telecommuters increases, "
                            "there will be fewer cars on the road and the trains will be less crowded. "
                            "We can save the environment by just changing the work style."
                        ),
                        "ja": (
                            "私も在宅勤務者です。私は自然の美しさを楽しめる田舎に住んでいますが，"
                            "在宅勤務によって十分な収入を得られています。"
                            "在宅勤務者の数が増えれば，道路上の車は少なくなり，電車の混雑は軽減されるでしょう。"
                            "私たちはただ仕事の仕方を変えるだけで，環境を救うことができるのです。"
                        ),
                    },
                ]
            ],
        },
    ],
    "questions": [
        {
            "question_id": "問1",
            "answer_number": 4,
            "stem": {
                "en": "According to the article, the telecommuting population means the number of people who [ 4 ].",
                "ja": "記事によると，在宅勤務人口とは［4］人々の数を意味している。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "are employed but work at home",
                    "ja": "雇われているが家で働いている",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "aren't employed and work at home using communication devices",
                    "ja": "雇われていないが通信機器を使って家で働いている",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "work at home without using any communication devices",
                    "ja": "通信機器を使わずに家で働いている",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "work during commuting hours using communication devices",
                    "ja": "通勤時間の間に通信機器を使って働いている",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①。第1段落に work at home … using digital telecommunications とあり，かつ "
                    "This did not include the self-employed より被雇用者が対象。②③④はいずれも本文の定義と矛盾する。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["tc_p1_s2", "tc_p1_s3"],
                "instructor_note": {
                    "ja": (
                        "ACS の定義は「雇用されている」「勤務の半分以上を自宅で」「digital telecommunications を使う」の三点セット。This did not include the self-employed が雇用の裏づけになる。"
                        "グラフや見出し語に時間を使う前に，定義の一文を自分の言葉で三要素に分解しておくと選択肢判定が速い。"
                    ),
                    "points": [
                        "定義文は第1段落にまとまっている。選択肢を読む前に，本文から一度マークしておくと速い。",
                        "②は被雇用者が対象なので除外。③は using digital telecommunications と矛盾。④は commute 中の勤務と定義が異なる。",
                        "数字（4.3 million / 3.2%）は正誤を決める材料ではなく，あとから確認する程度でよい。",
                        "self-employed を除外する一文は「誰を数に入れたか」の確認問題にも転用できるので丸ごと暗記しておく価値がある。",
                    ],
                },
            },
        },
        {
            "question_id": "問2",
            "answer_number": 5,
            "stem": {
                "sentences": [
                    {
                        "id": "q2_stem",
                        "en": (
                            'Your team will support the debate topic, "Telecommuting should be promoted." '
                            "In the article, one <strong><u>opinion</u></strong> (not a fact) helpful for your team is that [ 5 ]."
                        ),
                        "ja": (
                            "あなたのチームは討論トピック「在宅勤務は推奨されるべきだ」を支持する。"
                            "記事の中で，あなたたちのチームの手助けとなる（事実ではなく）<strong><u>意見</u></strong>の1つは［5］ということだ。"
                        ),
                    }
                ]
            },
            "choices": [
                {
                    "label": "①",
                    "en": "it is a good way for parents raising children to earn more",
                    "ja": "子供を育てる親たちにとってより多く稼ぐのにうまい方法だ",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "more than 5% of the total workforce work as telecommuters",
                    "ja": "労働人口全体の5%より多くの人が在宅勤務者として働いている",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "the commuting time will be shortened",
                    "ja": "通勤時間は短縮されるだろう",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "you can have more time with your children",
                    "ja": "自分の子供といる時間をより多く持つことができる",
                    "is_correct": True,
                },
            ],
            "answer": "④",
            "explanation": {
                "quoted_ja": (
                    "正解は④。デイビッド・ハウの引用に it gives them more time to spend with their children という意見がある。"
                    "②は3.2%という事実で意見ではない。③は通勤をなくすので「短縮」とは言いにくい。①は時給減など本文のニュアンスと合わない。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["tc_p2_s1"],
                "instructor_note": {
                    "ja": (
                        "fact vs opinion：統計や割合は検証可能な事実。賛成側の論拠として使えるのは，話し手の評価・推奨理由として書かれた文（意見）である。"
                        "設問が opinion と括っている以上，本文に数字だけがある選択肢はまず除外してよい。"
                    ),
                    "points": [
                        "David Howe の引用はメリットの列挙なので，支持側の「意見」はここから拾う。",
                        "②の 5% は本文の 3.2% と矛盾する事実なので，そもそも選択肢として成立しない。",
                        "③は Telecommuting saves employees commuting time ＝通勤を「短くする」ではなく「なくす」ニュアンス。言い換えに注意。",
                        "①は earn more と書いてあるが，Holden は時給の減少にも触れており，親の稼ぎ増しとは読みにくい。",
                        "討論問題では「支持チーム向け」か「反対チーム向け」かを最初にマークし，見出し人物のブロックを間違えない。",
                    ],
                },
            },
        },
        {
            "question_id": "問3",
            "answer_number": 6,
            "stem": {
                "sentences": [
                    {
                        "id": "q3_stem",
                        "en": (
                            'The other team will oppose the debate topic. In the article, one '
                            "<strong><u>opinion</u></strong> (not a fact) helpful for that team is that [ 6 ]."
                        ),
                        "ja": (
                            "もう一方のチームはその討論トピックに反対する。"
                            "記事の中で，そのチームの手助けとなる（事実ではなく）<strong><u>意見</u></strong>の1つは［6］ということだ。"
                        ),
                    }
                ]
            },
            "choices": [
                {
                    "label": "①",
                    "en": "companies have to pay money such as transportation fees for their workers",
                    "ja": "企業は交通費などの費用を自分たちの労働者に支払わなければならない",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "if you are not experienced you may have trouble doing your job efficiently",
                    "ja": "経験不足の人は効率的に仕事をするのが難しい可能性がある",
                    "is_correct": True,
                },
                {
                    "label": "③",
                    "en": "telecommuting usually gives you a strong sense of achievement",
                    "ja": "在宅勤務はたいてい本人に強い達成感をもたらす",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "you will have more opportunities to meet the people with whom you work",
                    "ja": "一緒に働く人たちと会う機会が増えるだろう",
                    "is_correct": False,
                },
            ],
            "answer": "②",
            "explanation": {
                "quoted_ja": (
                    "正解は②。メアリー・ホールデンの引用で，経験がなければやり取りが難しいとする部分が，反対側の論拠になる意見。"
                    "④は本文では機会がlessとあるので誤り。①は雇用主側のメリットの話とズレる。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["tc_p3_s1"],
                "instructor_note": {
                    "ja": (
                        "反対チームの論拠は「デメリット・不安・リスク」を肯定する意見から選ぶ。第3段落（Mary Holden）が中心。"
                        "賛成側のメリット（時間・コスト）と語を対にならべ替えないよう，段落冒頭の名前で区切りをつける。"
                    ),
                    "points": [
                        "①は本文では雇用主が transportation and utilities costs を「節約できる」とある話／選び文の「会社が労働者に交通費を払う」とは別次元の論点。",
                        "④は less opportunity to meet と真逆。③は forget the meaning と「達成感」は結びつけにくい。",
                        "if not, it might be difficult … communicate … と効率・やり取りの難しさに直結するのが②。",
                        "Mary Holden の長い一文は「時給低下」と「コミュニケーションの難しさ」に二分できる。設問が指すのは後半の仕事のしかたの話なら②が核。",
                    ],
                },
            },
        },
        {
            "question_id": "問4",
            "answer_number": 7,
            "stem": {
                "en": "In the 3rd paragraph of the article, Mary Holden refers to the possibility of telecommuters [ 7 ].",
                "ja": "記事の第3段落において，メアリー・ホールデンは在宅勤務者が［7］可能性に言及している。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "completely understanding why they work in the countryside",
                    "ja": "自分たちが田舎で働いている理由を完全に理解している",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "decreasing their chance to have new experiences",
                    "ja": "新しい経験を得る機会を減少させる",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "earning less money despite having longer working hours",
                    "ja": "より長い労働時間にもかかわらず賃金が少ない",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "meeting a lot of people through their job",
                    "ja": "自分たちの仕事を通して多くの人々と会う",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。第3段落に the increase in working hours and the large decrease in pay per hour are also problems とある。"
                    "④は less opportunity to meet と矛盾。①②は該当記述なし。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["tc_p3_s1"],
                "instructor_note": {
                    "ja": (
                        "refer to the possibility of telecommuters ~ は「こうなりうる」という帰結を問う。否定語・対立語とセットで確認する。"
                        "段落が長いときは，課題を「賃金」「時間」「対人面」にタグ付けしてから選択肢へ写す。"
                    ),
                    "points": [
                        "文中のペア：the increase in working hours と the large decrease in pay per hour をセットで覚えると③に直行できる。",
                        "④は meet の機会が less と対立。①の countryside は Holden 段落に登場しない（別パートの話と混同しない）。",
                        "②の new experiences は本文語彙としては弱く，該当記述がないなら消去法でもよい。",
                        "possibility の語に惑わされず，実質は「問題点の列挙」として読むと③④の消し分けが安定する。",
                    ],
                },
            },
        },
        {
            "question_id": "問5",
            "answer_number": 8,
            "stem": {
                "en": "According to her comment, Angela Jones [ 8 ] promoting telecommuting.",
                "ja": "アンジェラ・ジョーンズのコメントによると，彼女は在宅勤務の奨励を［8］。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "has no particular opinion about",
                    "ja": "について特別な意見はない",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "partly disagrees with",
                    "ja": "に部分的に反対だ",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "strongly agrees with",
                    "ja": "に強く賛成だ",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "strongly disagrees with",
                    "ja": "に強く反対だ",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。コメントはメリット（収入，渋滞緩和，環境）のみでデメリットに触れず，推進に積極的な態度。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["aj_s1"],
                "instructor_note": {
                    "ja": (
                        "コメント全体が賛美・メリットの列挙か，批判・条件付きかで賛否を決める。デメリットが一言もなければ「強く賛成」寄りと読むことが多い。"
                        "個人コメント問題は文量が短いので，強調語（strongly / partly）と本文のトーンのギャップにだけ注意すればよい。"
                    ),
                    "points": [
                        "田舎でも収入が得られる／車・電車・環境の3文はいずれも在宅推進の肯定的含意。",
                        "② partly は「良い面も悪い面も」と書いてある場合に検討するが，本文コメントは一方通行。",
                        "設問の promoting はコメント内の動詞 save the environment by changing the work style と呼応する。",
                        "has no particular opinion は「情報がない」と混同しやすいが，コメントが明確に賛意なら①は選ばない。",
                    ],
                },
            },
        },
    ],
    "vocabulary": {
        "passage": {
            "label_ja": "主な語彙・表現",
            "items": [
                {"en": "telecommuting", "ja": "在宅勤務"},
                {"en": "update", "ja": "〜を更新する"},
                {"en": "as of ~", "ja": "〜の時点で"},
                {"en": "utility / utilities", "ja": "（電気・ガス・水道などの）公共設備；光熱費を含む運営コストのイメージも"},
                {"en": "opinion vs fact（問2・問3）", "ja": "意見＝主張・評価；事実＝データ・定義など検証可能な記述"},
                {"en": "save + 人 + 物（問2③の型）", "ja": "save employees commuting time ＝通勤時間という負担を（在宅によって）省く"},
            ],
        }
    },
}


def main():
    data_path = ROOT / "data.json"
    if not data_path.exists():
        print("ERROR: data.json が見つかりません。先に build_section01.py を実行してください。")
        raise SystemExit(1)
    data = json.loads(data_path.read_text(encoding="utf-8"))
    data["sections"] = [s for s in data["sections"] if s.get("section_number") != 2]
    data["sections"].append(section_02)
    data["sections"].sort(key=lambda s: s.get("section_number", 0))
    impl = data.setdefault("exam_info", {}).setdefault("implemented_sections", [])
    if 2 not in impl:
        impl.append(2)
        impl.sort()
    data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Merged section 2 →", data_path)


if __name__ == "__main__":
    main()
