# -*- coding: utf-8 -*-
"""Z会 実戦模試 2026 第5回 第2問（Ten-Minute Community Challenge・環境クラブ）を data.json にマージする。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUOTED = "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子"

section_02 = {
    "section_number": 2,
    "title": "第2問",
    "points": 10,
    "points_per_question": 2,
    "description": "長文読解（地域のごみ拾いブログ・フィードバック）",
    "situation": {
        "en": (
            "You are a member of the environmental club. The members are making plans for a new volunteer event "
            "and you have been asked to come up with suggestions. To get ideas, you are reading a blog about "
            "a community service project a student introduced at her school."
        ),
        "ja": (
            "あなたは環境クラブのメンバーです。メンバーが新しいボランティアイベントの計画を立てていて，"
            "あなたは提案を出すように言われています。アイデアを得るために，ある生徒が自分の学校に導入した"
            "社会奉仕プロジェクトに関するブログを読んでいます。"
        ),
    },
    "passages": [
        {
            "id": "ten_minute_challenge_blog",
            "framed": True,
            "title": {
                "en": "<strong>Ten-Minute Community Challenge</strong>",
                "ja": "<strong>10分間地域チャレンジ</strong>",
            },
            "paragraph_classes": ["para-indent", "para-indent"],
            "paragraphs": [
                [
                    {
                        "id": "tmc_s1",
                        "en": "Arriving at school used to make me sad.",
                        "ja": "以前は，学校に着くと悲しくなったものです。",
                    },
                    {
                        "id": "tmc_s2",
                        "en": (
                            "There are several convenience stores and cafes in the area and people often drop litter "
                            "on the ground — cans, bottles, sweet wrappers, plastic bags, etc."
                        ),
                        "ja": (
                            "地域にはいくつかのコンビニエンスストアやカフェがあり，"
                            "缶やビン，お菓子の包装紙，ビニール袋などのゴミを人々がよく地面に落とします。"
                        ),
                    },
                    {
                        "id": "tmc_s3",
                        "en": "Last year, I decided to do something.",
                        "ja": "昨年，私はあることをしようと決めました。",
                    },
                    {
                        "id": "tmc_s4",
                        "en": (
                            "I put up posters asking students to come to school ten minutes earlier than usual for one week "
                            "and use the extra time to pick up a few pieces of litter."
                        ),
                        "ja": (
                            "１週間，いつもより10分早く登校し，その時間でごみを少し拾うように生徒に頼むポスターを貼りました。"
                        ),
                    },
                    {
                        "id": "tmc_s5",
                        "en": "It worked!",
                        "ja": "これがうまくいきました！",
                    },
                    {
                        "id": "tmc_s6",
                        "en": "An average of 150 students (10% of the school) took part each day.",
                        "ja": "毎日平均150人の生徒（全校の10％）が参加しました。",
                    },
                    {
                        "id": "tmc_s7",
                        "en": "Nearly a third of that number participated the whole week.",
                        "ja": "そのうちのほぼ3分の1が一週間を通して参加しました。",
                    },
                    {
                        "id": "tmc_s8",
                        "en": "There were even a few teachers.",
                        "ja": "教師も数名いました。",
                    },
                    {
                        "id": "tmc_s9",
                        "en": "Within three days, the area around the school was already much nicer.",
                        "ja": "３日以内に，学校周辺はすでにずっとすっきりした様子になりました。",
                    },
                    {
                        "id": "tmc_s10",
                        "en": "By the end, it was perfect.",
                        "ja": "最終日には，完璧でした。",
                    },
                    {
                        "id": "tmc_s11",
                        "en": "Surprisingly, since this event the area has stayed litter-free.",
                        "ja": "驚いたことに，このイベント以降，その地域にはごみが落ちていません。",
                    },
                    {
                        "id": "tmc_s12",
                        "en": "Why is this?",
                        "ja": "なぜでしょうか。",
                    },
                    {
                        "id": "tmc_s13",
                        "en": "Feedback from the event seems to give the answer:",
                        "ja": "イベントへの感想が答えを教えてくれそうです。",
                    },
                ],
                [
                    {
                        "id": "tmc_head_fb",
                        "en": (
                            '<span style="display:block;text-align:center;margin:0.6em 0">'
                            "<strong><u>Feedback from the students and the local community</u></strong></span>"
                        ),
                        "ja": (
                            '<span style="display:block;text-align:center;margin:0.6em 0">'
                            "<strong><u>生徒と地域社会からの意見</u></strong></span>"
                        ),
                    },
                    {
                        "id": "tmc_fb_bt",
                        "en": (
                            "<strong>BT:</strong> I hadn't realised how unhappy this problem was making me. "
                            "I can finally walk to school with a big smile on my face."
                        ),
                        "ja": (
                            "<strong>BT:</strong> この問題が自分をどれだけ不幸にしていたか，気づいていませんでした。"
                            "ようやく笑顔で学校まで歩いていけます。"
                        ),
                    },
                    {
                        "id": "tmc_fb_ak",
                        "en": (
                            "<strong>AK:</strong> Great project! As an adult living near the school, I was so happy to see "
                            "school students helping the community. I joined in and got some neighbours involved, too. "
                            "We still do it twice a week."
                        ),
                        "ja": (
                            "<strong>AK:</strong> すばらしい企画です！学校の近くに住む大人として，"
                            "生徒が地域のために動くのを見られてとてもうれしかった。私も参加して近所の人にも声をかけました。"
                            "今でも週に2回続けています。"
                        ),
                    },
                    {
                        "id": "tmc_fb_rn",
                        "en": (
                            "<strong>RN:</strong> We appreciate the difference it has made. My friends and I would have "
                            "joined in but we didn't see the poster."
                        ),
                        "ja": (
                            "<strong>RN:</strong> 変化に感謝しています。友人たちと私も参加したかったのですが，"
                            "ポスターを見ていませんでした。"
                        ),
                    },
                    {
                        "id": "tmc_fb_cf",
                        "en": (
                            "<strong>CF:</strong> This project helped me understand how action by a high school student "
                            "can have a big impact."
                        ),
                        "ja": (
                            "<strong>CF:</strong> このプロジェクトで，高校生の行動が大きな影響を持ちうると理解できました。"
                        ),
                    },
                    {
                        "id": "tmc_fb_wl",
                        "en": (
                            "<strong>WL:</strong> I am so thankful. I've lived here for 15 years and I feel I can be "
                            "proud of this town again."
                        ),
                        "ja": (
                            "<strong>WL:</strong> とても感謝しています。15年ここに住んでいますが，"
                            "再びこの町を誇りに思えます。"
                        ),
                    },
                ],
            ],
        }
    ],
    "questions": [
        {
            "question_id": "問1",
            "answer_number": 4,
            "stem": {
                "en": "The aim of the activity was to [ 4 ].",
                "ja": "この活動の目的は［4］ことであった。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "get students to support the community",
                    "ja": "生徒に地域を支援させる",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "help locals to know each other",
                    "ja": "地元の人たちがお互いを知るのを助ける",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "improve the school playground",
                    "ja": "学校の運動場を改善する",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "make the environment look nicer",
                    "ja": "環境をよりよく見えるようにする",
                    "is_correct": True,
                },
            ],
            "answer": "④",
            "explanation": {
                "quoted_ja": (
                    "正解は④。ポスターで登校を早めてごみを拾うよう呼びかけており，周辺の見た目の改善が直接のねらい。"
                    "①は結果としての側面で目的の言い換えとしては広すぎる場合がある。②③は本文にない。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["tmc_s4", "tmc_s2"],
                "instructor_note": {
                    "ja": (
                        "ブログ前半で筆者が実際に仕掛けた行動（ポスター・早朝登校・ごみ拾い）が何をねらっているかを一文で言い切った選択肢を選ぶ。"
                        "抽象的な「地域支援」より，見える成果（きれいになる／環境の見た目）に直結する語を優先する。"
                    ),
                    "points": [
                        "pick up litter / nicer / litter-free などの語群が，設問の aim と輪郭を共有しているかを確認する。",
                        "①②は「良いこと」としては正しそうだが，本文が強調しているのは対人仲介より環境物理の改善。③運動場は本文にない。",
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
                        "id": "tmc_q2_stem",
                        "en": (
                            "One <strong><u>fact</u></strong> about the Ten-Minute Community Challenge is that [ 5 ]."
                        ),
                        "ja": (
                            "『10分間地域チャレンジ』に関する<strong><u>事実</u></strong>として正しいのは［5］である。"
                        ),
                    }
                ]
            },
            "choices": [
                {
                    "label": "①",
                    "en": "it only lasted for three days",
                    "ja": "続いたのは3日間だけであった",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "only students picked up litter",
                    "ja": "ごみを拾ったのは生徒だけであった",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "the number of students who worked the whole week was around 50",
                    "ja": "一週間ずっと取り組んだ生徒の数は約50人であった",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "the teachers were happy that the town looked cleaner",
                    "ja": "教師たちは町がきれいになったことをうれしく思っていた",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。150人の約3分の1が一週間参加＝約50人。①は活動期間は1週間。②は教師も参加。④は教師の感情は本文にない。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["tmc_s6", "tmc_s7"],
                "instructor_note": {
                    "ja": (
                        "fact 問題は「本文のどの数値・期間と矛盾しないか」だけを見る。推測・評価・感情表現は除外。"
                        "割合表現（10％／a third／150）をメモしながら，選択肢の数字を再計算する癖をつける。"
                    ),
                    "points": [
                        "150人の約1/3は約50。③だけが算術と本文記述の両方を満たす。",
                        "活動は one week なので only three days は矛盾。教師の参加は even a few teachers で示され②は誤り。",
                        "④は教師の心情について本文は述べておらず，fact としては根拠なし。",
                    ],
                },
            },
        },
        {
            "question_id": "問3",
            "answer_number": 6,
            "stem": {
                "en": "From the blog, we know that it is most likely true that [ 6 ].",
                "ja": "このブログから，次のうち最も可能性が高く言えるのは［6］である。",
            },
            "info_options": [
                {
                    "label": "A",
                    "en": "more people may have wanted to take part",
                    "ja": "もっと多くの人が参加したかった可能性がある",
                },
                {
                    "label": "B",
                    "en": "students encouraged the locals to join in",
                    "ja": "生徒が地域の人々に参加を呼びかけた",
                },
                {
                    "label": "C",
                    "en": "students like picking up garbage",
                    "ja": "生徒はごみ拾いが好きである",
                },
                {
                    "label": "D",
                    "en": "the author didn't expect teachers to join in",
                    "ja": "筆者は教師の参加を期待していなかった",
                },
            ],
            "choices": [
                {
                    "label": "①",
                    "en": "A and B",
                    "ja": "A と B",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "A and C",
                    "ja": "A と C",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "A and D",
                    "ja": "A と D",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "B and C",
                    "ja": "B と C",
                    "is_correct": False,
                },
                {
                    "label": "⑤",
                    "en": "B and D",
                    "ja": "B と D",
                    "is_correct": False,
                },
                {
                    "label": "⑥",
                    "en": "C and D",
                    "ja": "C と D",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③（AとD）。RNはポスターを見ず参加できなかったとあり参加意欲があった層がいたと読める（A）。"
                    "There were even a few teachers の even から筆者は教師の参加を強く期待していなかった（D）。"
                    "B・Cは本文が支持しない。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["tmc_fb_rn", "tmc_s8"],
                "instructor_note": {
                    "ja": (
                        "likely true は「本文から合理的に言える」レベル。各選択肢を一文ずつ本文に当て，矛盾がないか／言い過ぎないかを確認する。"
                        "組み合わせ問題は，まず候補（A〜D）ごとに単独判定してから AND を取る。"
                    ),
                    "points": [
                        "RN の didn't see the poster は「参加したかった層がいた」余地を残す（A）。",
                        "There were even a few teachers の even は「予想以上に教師も」と読み取れ，筆者が教師参加を前提にしていなかったニュアンスを示唆しやすい（D）。",
                        "Bの locals への呼びかけは本文に明示されず，Cの「ごみ拾いが好き」は動機の断定として強すぎる。",
                    ],
                },
            },
        },
        {
            "question_id": "問4",
            "answer_number": 7,
            "stem": {
                "en": "One of the participants' opinions about the Ten-Minute Community Challenge is that [ 7 ].",
                "ja": "『10分間地域チャレンジ』についての参加者の意見の1つは［7］ということである。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "everyone should take part in the challenge",
                    "ja": "誰もがチャレンジに参加すべきである",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "locals have always been happy to live in the area",
                    "ja": "地域の人々はずっとこの地域に住んで幸せだと思っている",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "one person can make a difference to the community",
                    "ja": "一人でも地域に変化をもたらしうる",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "the challenge should have started 15 years ago",
                    "ja": "このチャレンジは15年前から始めるべきだった",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。CFの発言が高校生の行動の impact を述べ，個人の力が地域を変えるという趣旨に合う。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["tmc_fb_cf"],
                "instructor_note": {
                    "ja": (
                        "意見欄は発言者ごとに「主張の核」を一行で抜き出し，設問の語句（one person's opinion / impact など）と照合する。"
                        "選択肢が一般論に逃げていないか（本文の具体的エピソードと結びつくか）も見る。"
                    ),
                    "points": [
                        "CF は high school student's action と impact を同一文で結んでおり，個人の行動がコミュニティに波及するという③の骨格に合う。",
                        "WL の 15 years は在住年数の事実であって，チャレンジが「15年前からあるべきだった」という意味ではない。",
                        "① everyone must は強い規範で，フィードバックのトーンともずれる。② locals always happy は本文が述べる不幸の対象が曖昧で根拠不足。",
                    ],
                },
            },
        },
        {
            "question_id": "問5",
            "answer_number": 8,
            "stem": {
                "en": "The author's question is answered by [ 8 ].",
                "ja": "筆者の質問に答えているのは［8］である。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "AK",
                    "ja": "AK",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "BT",
                    "ja": "BT",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "CF",
                    "ja": "CF",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "RN",
                    "ja": "RN",
                    "is_correct": False,
                },
                {
                    "label": "⑤",
                    "en": "WL",
                    "ja": "WL",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①（AK）。筆者の問いは litter-free が続く理由。AKは近所も巻き込み週2回続けているため，継続的な清掃で綺麗が保たれると読める。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["tmc_s11", "tmc_s12", "tmc_fb_ak"],
                "instructor_note": {
                    "ja": (
                        "設問文の The author's question が本文のどこを指すか（通常は直前の疑問文）を必ず確認する。"
                        "その疑問に「原因・仕組み」を答えている発言を選ぶ。"
                    ),
                    "points": [
                        "Why is this?（ごみが続かない理由）に対し，AK は近隣を巻き込み週2回拾い続けるという「継続行動」で答えている。",
                        "RN は参加できなかった理由（ポスター未閲覧）であって，Beautification が続くメカニズムの説明ではない。",
                        "BT・CF は感情や気づきの表明に寄り，「なぜ続くか」の因果説明としては弱い。",
                    ],
                },
            },
        },
    ],
    "vocabulary": {
        "passage": {
            "label_ja": "主な語彙・表現",
            "items": [
                {"en": "community service", "ja": "社会奉仕"},
                {"en": "litter", "ja": "ごみ"},
                {"en": "participate", "ja": "参加する"},
                {"en": "appreciate", "ja": "〜に感謝する；〜を正当に評価する"},
                {"en": "local（問1②）", "ja": "（通例複数形で）地元の人たち"},
                {"en": "last（問2①）", "ja": "（期間が）続く"},
                {"en": "attendee（問2）", "ja": "出席者；来場者"},
            ],
        }
    },
}


def main():
    data_path = ROOT / "data.json"
    if not data_path.exists():
        print("ERROR: data.json が見つかりません。")
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
