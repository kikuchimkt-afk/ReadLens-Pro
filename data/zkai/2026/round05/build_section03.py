# -*- coding: utf-8 -*-
"""Z会 実戦模試 2026 第5回 第3問（グランド・シアターの舞台裏）を data.json にマージする。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUOTED = "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子"

section_03 = {
    "section_number": 3,
    "title": "第3問",
    "points": 9,
    "points_per_question": 3,
    "description": "長文読解（劇場の職場見学・校新）",
    "situation": {
        "en": (
            "You are going to participate in a workplace tour. As preparation, you are reading an article in the school "
            "newspaper written by Hilda, who took part in it last year."
        ),
        "ja": (
            "あなたは職場見学に参加します。準備として，昨年参加したヒルダが書いた学校新聞の記事を読んでいます。"
        ),
    },
    "passages": [
        {
            "id": "hilda_grand_theater_newspaper",
            "framed": True,
            "title": {
                "en": "<strong>Behind the Scenes at the Grand Theater</strong>",
                "ja": "<strong>グランド・シアターの舞台裏</strong>",
            },
            "paragraph_classes": [
                "para-indent",
                "para-indent",
                "para-indent",
                "para-indent",
                "para-indent",
            ],
            "paragraphs": [
                [
                    {
                        "id": "hilda_p1_s1",
                        "en": (
                            "For our school's workplace tour, we went on a behind-the-scenes tour of the Grand Theater."
                        ),
                        "ja": "職場見学で，私たちはグランド・シアターの舞台裏ツアーに参加した。",
                    },
                    {
                        "id": "hilda_p1_s2",
                        "en": (
                            "As we walked in, I noticed a busy atmosphere, with people setting up the ticket machines in "
                            "the ticket sellers' booths."
                        ),
                        "ja": "中に入ると，人々がチケット売り場に発券機を設置しており，忙しげな雰囲気だと気づいた。",
                    },
                    {
                        "id": "hilda_p1_s3",
                        "en": (
                            "Our guide, Ms. Chen, greeted us with a smile and mentioned that because it was Tuesday, "
                            "tickets were half-price."
                        ),
                        "ja": "ガイドのチェンさんは笑顔で迎え，火曜日なのでチケットは半額だと話した。",
                    },
                    {
                        "id": "hilda_p1_s4",
                        "en": "She expected to fill every seat in the theater.",
                        "ja": "彼女は劇場のすべての席が埋まると予測していた。",
                    },
                ],
                [
                    {
                        "id": "hilda_p2_s1",
                        "en": (
                            "Our first stop was the main stage, where some actors were rehearsing for the afternoon "
                            "performance."
                        ),
                        "ja": "最初の見学先は本舞台で，俳優たちが午後の公演のリハーサルをしていた。",
                    },
                    {
                        "id": "hilda_p2_s2",
                        "en": (
                            "Ms. Chen encouraged us to imagine ourselves as actors in a 1920s city scene, with tall "
                            "painted buildings and bright shop signs."
                        ),
                        "ja": (
                            "チェンさんは，背の高い塗りの建物と明るい店の看板がある1920年代の街の場面にいる俳優に"
                            "なったつもりになるよう勧めた。"
                        ),
                    },
                    {
                        "id": "hilda_p2_s3",
                        "en": (
                            "We were all interested in the old-style streetlamps and storefronts on the backdrop."
                        ),
                        "ja": "私たちは皆，背景幕の旧式の街灯や店先に興味を引かれた。",
                    },
                    {
                        "id": "hilda_p2_s4",
                        "en": (
                            "Ms. Chen explained that the following day, they would close the theater to repair any "
                            "damage to the set and make sure it's all in good shape."
                        ),
                        "ja": (
                            "チェンさんは，翌日には劇場を閉館してセットの損傷を修復し，すべてが良好な状態になるよう"
                            "確かめるのだと説明した。"
                        ),
                    },
                ],
                [
                    {
                        "id": "hilda_p3_s1",
                        "en": (
                            "Next, we climbed up to the lighting room, where a technician showed us how she creates the "
                            "atmosphere for each scene with different colors and brightness."
                        ),
                        "ja": (
                            "次に照明室に上ると，技術者が場面ごとにさまざまな色と明るさで雰囲気をどう作るかを"
                            "見せてくれた。"
                        ),
                    },
                    {
                        "id": "hilda_p3_s2",
                        "en": (
                            "She adjusted the lights from a sunny afternoon to a calm evening with just a few switches."
                        ),
                        "ja": "彼女はほんのいくつかのスイッチで，照明を晴れた午後から静かな夕方へと変えた。",
                    },
                    {
                        "id": "hilda_p3_s3",
                        "en": (
                            "Ms. Chen told us that the lights were very important because without them, the stage would "
                            "feel empty and flat."
                        ),
                        "ja": (
                            "チェンさんによると照明はとても重要で，それがなければステージは空虚で平板に感じられるという。"
                        ),
                    },
                ],
                [
                    {
                        "id": "hilda_p4_s1",
                        "en": (
                            "Behind the stage there was a room with 'props' written on the door."
                        ),
                        "ja": "ステージの裏には，ドアに「props」と書かれた部屋があった。",
                    },
                    {
                        "id": "hilda_p4_s2",
                        "en": (
                            "Inside, we saw shelves full of interesting items, from old-fashioned clocks to fake food."
                        ),
                        "ja": "中には昔風の時計から作り物の食べ物まで，おもしろい品が並んだ棚があった。",
                    },
                    {
                        "id": "hilda_p4_s3",
                        "en": (
                            "Ms. Chen picked up a glass bottle that was actually soft and light."
                        ),
                        "ja": "チェンさんは，見た目はガラス瓶だが実は柔らかく軽いものを手に取った。",
                    },
                    {
                        "id": "hilda_p4_s4",
                        "en": (
                            "We learned that many of these props look real but are made to be safe and easy to carry."
                        ),
                        "ja": (
                            "小道具の多くは本物のように見えるが，安全で持ち運びしやすいように作られていると知った。"
                        ),
                    },
                    {
                        "id": "hilda_p4_s5",
                        "en": (
                            "Then she pointed out some posters stacked by the wall and told us that the current play "
                            "would end this week."
                        ),
                        "ja": (
                            "それから彼女は壁際に積まれたポスターを指し，現在の演目が今週で終わると教えてくれた。"
                        ),
                    },
                    {
                        "id": "hilda_p4_s6",
                        "en": (
                            "Next week, they would put up some new posters to publicize the upcoming show."
                        ),
                        "ja": "来週は次の公演を宣伝するために新しいポスターを貼る予定だという。",
                    },
                ],
                [
                    {
                        "id": "hilda_p5_s1",
                        "en": "We left before the show.",
                        "ja": "私たちは開演前に会場を後にした。",
                    },
                    {
                        "id": "hilda_p5_s2",
                        "en": (
                            "As I stepped onto the street, I looked at the front of the theater."
                        ),
                        "ja": "通りに出ると，私は劇場の正面を見上げた。",
                    },
                    {
                        "id": "hilda_p5_s3",
                        "en": "Ms. Chen's prediction was right!",
                        "ja": "チェンさんの予測は当たっていた！",
                    },
                    {
                        "id": "hilda_p5_s4",
                        "en": "I thought about everything I'd learned.",
                        "ja": "ここで学んだことをすべて思い返した。",
                    },
                    {
                        "id": "hilda_p5_s5",
                        "en": (
                            "Seeing all the work that went into each part of the production made me appreciate it even "
                            "more."
                        ),
                        "ja": (
                            "作品の各部分に注がれた仕事を見て，私はそのすばらしさをさらに実感した。"
                        ),
                    },
                ],
            ],
            "images": [
                {
                    "paragraph_index": 1,
                    "src": "images/grand_theater_stage.png",
                    "position": "float-right",
                    "alt": "Actors on stage with 1920s street backdrop",
                    "max_width": 240,
                }
            ],
        }
    ],
    "questions": [
        {
            "question_id": "問1",
            "question_type": "ordering",
            "answer_numbers": [9, 10, 11, 12],
            "stem": {
                "en": (
                    "Hilda's article also included student comments (① ~ ④) describing the events in the theater tour. "
                    "Put the comments in the order in which the events happened. [ 9 ] → [ 10 ] → [ 11 ] → [ 12 ]"
                ),
                "ja": (
                    "ヒルダの記事には，劇場ツアーでの出来事を説明した生徒のコメント（①〜④）も含まれていた。"
                    "コメントを出来事が起きた順に並べよ。［9］→［10］→［11］→［12］"
                ),
            },
            "choices": [
                {
                    "label": "①",
                    "en": (
                        "Being able to change day to night so easily for the production must make the controllers feel "
                        "very powerful."
                    ),
                    "ja": (
                        "作品のために昼から夜へと容易に変えられるので，操作担当者はとても影響力があると感じているに"
                        "違いない。"
                    ),
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": (
                        "I had never considered working as a performer until Ms. Chen suggested we do so."
                    ),
                    "ja": (
                        "チェンさんにそうするように提案されるまで，演者の仕事をするなんて考えたこともなかった。"
                    ),
                    "is_correct": True,
                },
                {
                    "label": "③",
                    "en": (
                        "I thought it would be easier to let people reserve and pay for their seats using smartphones."
                    ),
                    "ja": "スマートフォンで席を予約して支払いをもらえるようにした方が簡単だろうと思った。",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": (
                        "It was hard to believe the objects actors use on stage are often imitations."
                    ),
                    "ja": "俳優が舞台で使う物が作り物であることが多いとは信じがたいことだった。",
                    "is_correct": True,
                },
            ],
            "answer": "③→②→①→④",
            "answer_sequence": ["③", "②", "①", "④"],
            "explanation": {
                "quoted_ja": (
                    "正解の順序は③→②→①→④。③は入館直後の発券機，②は本舞台での俳優になりきる提案，"
                    "①は照明室，④は小道具部屋の見学に対応する。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": [
                    "hilda_p1_s2",
                    "hilda_p2_s2",
                    "hilda_p3_s2",
                    "hilda_p4_s3",
                ],
                "instructor_note": {
                    "ja": (
                        "並べ替えは「本文の見学順」と「コメント中の手がかり語」をペアにするのが最短。"
                        "一度，見学ステップを番号付きメモ（入口→舞台→照明→小道具）にしてから各コメントを振り分けると取り違えにくい。"
                    ),
                    "points": [
                        "③はチケット／発券機（入館直後），②は俳優の気持ちになりきる誘い（本舞台），①は昼夜の照明操作（照明室），④は小道具・模造品（props 部屋）。",
                        "lighting / controllers は①に，imitations / objects on stage は④に固定すると迷いが減る。",
                        "時間副詞（next, then）より「話題の語彙一致」を優先するのがコツ。",
                    ],
                },
            },
        },
        {
            "question_id": "問2",
            "answer_number": 13,
            "stem": {
                "sentences": [
                    {
                        "id": "hilda_q2_stem",
                        "en": (
                            "From the tour, Hilda did <strong><u>not</u></strong> learn about [ 13 ] of the theater."
                        ),
                        "ja": (
                            "ツアーを通じて，ヒルダが劇場の［13］について<strong><u>知らなかった</u></strong>のは"
                            "次のうちどれか。"
                        ),
                    }
                ]
            },
            "choices": [
                {
                    "label": "①",
                    "en": "a maintenance plan",
                    "ja": "整備の計画",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "advertising materials",
                    "ja": "広告資材",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "the reservations system",
                    "ja": "予約システム",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "the storage space",
                    "ja": "保管スペース",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。本文に「予約のしかた」は出てこない。①はセット修復，②はポスター，④は小道具部屋が根拠。"
                    "発券機はあくまで発券であり予約システムそのものではない。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["hilda_p2_s4", "hilda_p4_s5", "hilda_p4_s1"],
                "instructor_note": {
                    "ja": (
                        "NOT-learn 型は，本文で「説明された／触れた」テーマかどうかを機械的にチェックする。"
                        "一度，選択肢の名詞（maintenance, advertising, reservations, storage）ごとに該当段落を探し，ヒットしなければ候補になる。"
                    ),
                    "points": [
                        "①セット修復・翌日閉館，②ポスターと次公演の宣伝，④小道具の棚＝保管スペースのように読める記述はある。",
                        "③ reservations は本文に語が出ず，ticket machines も「発券」であり予約システム全体を指すとは限らない。",
                        "「説明がなかった」と「筆者が知らなかった」を同一視しない（ヒルダが聞いた範囲＝本文に載った範囲）。",
                    ],
                },
            },
        },
        {
            "question_id": "問3",
            "answer_number": 14,
            "stem": {
                "en": "When she left the theater, Hilda most likely saw [ 14 ].",
                "ja": "劇場を出たとき，ヒルダが最もありそうに見たものは［14］である。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "a long line of people",
                    "ja": "人々の長い列",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "actors arriving for work",
                    "ja": "仕事場に到着する俳優たち",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "posters for the next production",
                    "ja": "次の作品のポスター",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "some bright streetlamps",
                    "ja": "明るい街灯",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①。最終段落で Ms. Chen's prediction was right とあり，第１段落で全席が埋まると予測していた。"
                    "正面から見てその予測が当たったなら行列が見えるのが自然。③はまだ貼られていない。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["hilda_p1_s4", "hilda_p5_s2", "hilda_p5_s3"],
                "instructor_note": {
                    "ja": (
                        "most likely は本文の因果のつながりで組み立てる。前半の予測（満席）と結末の確認（予測どおり）を一文でつなぐと答えが絞られる。"
                    ),
                    "points": [
                        "half-price Tuesday と fill every seat が，開演前のにぎわい（列）と整合しやすい。",
                        "俳優はすでに舞台でリハーサル中なので「これから出勤」は時系列と矛盾しやすい。",
                        "次回公演ポスターは来週貼る予定で，まだ表に出ていない文脈。街灯は舞台セットの話と外景を混同しない。",
                    ],
                },
            },
        },
    ],
    "vocabulary": {
        "passage": {
            "label_ja": "主な語彙・表現",
            "items": [
                {"en": "behind-the-scenes", "ja": "舞台裏の"},
                {"en": "atmosphere", "ja": "雰囲気"},
                {"en": "set up ~", "ja": "〜を設置する"},
                {"en": "fill", "ja": "〜をいっぱいにする"},
                {"en": "rehearse", "ja": "リハーサルをする"},
                {"en": "storefront", "ja": "店先"},
                {"en": "backdrop", "ja": "背景幕"},
                {"en": "in good shape", "ja": "状態がよい"},
                {"en": "technician", "ja": "技術者"},
                {"en": "adjust", "ja": "〜を調整する"},
                {"en": "switch", "ja": "スイッチ"},
                {"en": "fake", "ja": "にせの，模造の"},
                {"en": "stack", "ja": "〜を積み重ねる"},
                {"en": "put up ~", "ja": "〜を貼り出す"},
                {"en": "publicize", "ja": "〜を宣伝する"},
                {"en": "prediction", "ja": "予測"},
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
    data["sections"] = [s for s in data["sections"] if s.get("section_number") != 3]
    data["sections"].append(section_03)
    data["sections"].sort(key=lambda s: s.get("section_number", 0))
    impl = data.setdefault("exam_info", {}).setdefault("implemented_sections", [])
    if 3 not in impl:
        impl.append(3)
        impl.sort()
    data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Merged section 3 →", data_path)


if __name__ == "__main__":
    main()
