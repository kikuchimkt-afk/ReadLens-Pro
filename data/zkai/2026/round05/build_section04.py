# -*- coding: utf-8 -*-
"""Z会 実戦模試 2026 第5回 第4問（エッセイ推敲・コミュニティ・ガーデン）を data.json にマージする。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUOTED = "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子"

section_04 = {
    "section_number": 4,
    "title": "第4問",
    "points": 12,
    "points_per_question": 3,
    "description": "エッセイ添削（コミュニティ・ガーデン・先生コメント）",
    "situation": {
        "en": (
            "In English class you are writing an essay on a social issue you are interested in. "
            "This is your most recent draft. You are now working on revisions based on comments from your teacher."
        ),
        "ja": (
            "あなたは英語の授業で，興味のある社会問題に関するエッセイを書いています。"
            "これはあなたの最新の草稿です。今は先生からのコメントをもとに，推敲に取り組んでいるところです。"
        ),
    },
    "passages": [
        {
            "id": "community_gardens_essay",
            "title": {
                "en": "<strong>Gardening and Community Building</strong>",
                "ja": "<strong>ガーデニングと地域づくり</strong>",
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
                        "id": "cg_p1_s1",
                        "en": (
                            "Community gardens are pieces of land owned by local government where community members are "
                            "allowed to grow vegetable or flower gardens in cooperation with their neighbors."
                        ),
                        "ja": (
                            "コミュニティ・ガーデンは地方自治体が所有する土地の一部で，地域住民が近所の人たちと協力して"
                            "野菜や花の菜園を作ることを許可されている場所である。"
                        ),
                    },
                    {
                        "id": "cg_p1_s2",
                        "en": (
                            "To ensure that these gardens continue to exist in the future, it is important that we "
                            "understand their value and their potential."
                        ),
                        "ja": (
                            "このようなガーデンが将来も存続するのを確実にするために，その価値と可能性を理解することが"
                            "重要である。"
                        ),
                    },
                    {
                        "id": "cg_p1_s3",
                        "en": "This essay will discuss some benefits of community gardens.",
                        "ja": "このエッセイでは，コミュニティ・ガーデンのいくつかの利点について論じる。",
                    },
                ],
                [
                    {
                        "id": "cg_p2_s1",
                        "en": (
                            "First, at a time when urban isolation is increasingly common, community gardens offer "
                            "opportunities for friendly interaction, particularly among the elderly."
                        ),
                        "ja": (
                            "第一に，都市部での孤立がますます一般的になっている時代に，コミュニティ・ガーデンは"
                            "特に高齢者間の友好的な交流の機会を提供する。"
                        ),
                    },
                    {
                        "id": "cg_p2_s2",
                        "en": (
                            "Nowadays there are few locations where residents can interact, especially in big cities."
                        ),
                        "ja": "現在，特に大都市では，住民が交流できる場所がほとんどない。",
                    },
                    {
                        "id": "cg_p2_s3",
                        "en": (
                            "[15] So, community gardens may serve as rare community hubs where residents of different "
                            "generations get to know each other."
                        ),
                        "ja": (
                            "[15] だから，コミュニティ・ガーデンは，さまざまな世代の住民が互いに知り合う，"
                            "希少なコミュニティ拠点としての役割を果たすかもしれない。"
                        ),
                        "comment_marker": "(1)",
                        "marker_type": "caret",
                    },
                ],
                [
                    {
                        "id": "cg_p3_s1",
                        "en": (
                            "Second, community gardens provide practical skills and knowledge for gardening and farming "
                            "that residents can make use of."
                        ),
                        "ja": (
                            "第二に，コミュニティ・ガーデンは，住民が活用できるガーデニングや農業の実用的な技術や"
                            "知識を提供する。"
                        ),
                    },
                    {
                        "id": "cg_p3_s2",
                        "en": (
                            "[16] Working on gardens requires teamwork; this will help improve communication skills "
                            "and the individual's sense of responsibility."
                        ),
                        "ja": (
                            "[16] ガーデンでの作業にはチームワークが求められ，これはコミュニケーション技術と個人の"
                            "責任感の向上に役立つだろう。"
                        ),
                        "comment_marker": "(2)",
                        "marker_type": "caret",
                    },
                ],
                [
                    {
                        "id": "cg_p4_s1",
                        "en": "Finally, we are responsible for what we eat.",
                        "ja": "最後に，私たちは自分が食べるものに責任がある。",
                        "comment_marker": "(3)",
                        "underline_word": "we are responsible for what we eat.",
                    },
                    {
                        "id": "cg_p4_s2",
                        "en": (
                            "Community ownership makes nutritious fruits, vegetables, and herbs more affordable."
                        ),
                        "ja": (
                            "コミュニティが所有することで，栄養価の高い果物や野菜，ハーブをより手頃な価格で入手できる。"
                        ),
                    },
                    {
                        "id": "cg_p4_s3",
                        "en": (
                            "This leads to healthier eating habits, especially in areas where fresh produce may be "
                            "limited or expensive."
                        ),
                        "ja": (
                            "これは，特に新鮮な農産物が限られていたり高価だったりする地域で，より健康的な食生活を"
                            "もたらしてくれる。"
                        ),
                    },
                ],
                [
                    {
                        "id": "cg_p5_s1",
                        "en": (
                            "In conclusion, community gardens help the elderly, provide valuable lessons, and lastly, "
                            "enrich our diet."
                        ),
                        "ja": (
                            "結論として，コミュニティ・ガーデンは高齢者を助け，貴重な学びを与え，そして最後に，"
                            "食生活を豊かにしてくれる。"
                        ),
                        "comment_marker": "(4)",
                        "underline_word": "help the elderly,",
                    },
                    {
                        "id": "cg_p5_s2",
                        "en": (
                            "We should do all we can to support them, as they will become more and more important to "
                            "us in later life."
                        ),
                        "ja": (
                            "コミュニティ・ガーデンはこれからの人生で私たちにとってますます重要な存在となるだろうから，"
                            "それを支援するためにできる限りのことをするべきだ。"
                        ),
                    },
                ],
            ],
            "margin_comments": [
                {
                    "marker": "(1)",
                    "en": (
                        "You're missing something here. Add more information to connect the two sentences."
                    ),
                    "ja": "ここに何か足りません。2つの文をつなぐために，間にさらに情報を追加しなさい。",
                },
                {
                    "marker": "(2)",
                    "en": "Insert a connecting expression here.",
                    "ja": "ここに接続表現を挿入しなさい。",
                },
                {
                    "marker": "(3)",
                    "en": "This topic sentence doesn't really match this paragraph. Rewrite it.",
                    "ja": "この主題文はこの段落にあまり合っていません。書き直しなさい。",
                },
                {
                    "marker": "(4)",
                    "en": "The underlined phrase doesn't summarize your essay content enough. Change it.",
                    "ja": "下線部の表現はあなたのエッセイの内容を十分に要約していません。変更しなさい。",
                },
            ],
            "teacher_comment": {
                "title_en": "Overall comments:",
                "title_ja": "総合的なコメント：",
                "en": (
                    "I think this topic is something that will be increasingly important in our aging society. "
                    "There's a community garden in my neighborhood too!"
                ),
                "ja": (
                    "この主題は，高齢化社会でますます重要になるものだと思います。"
                    "私の近所にもコミュニティ・ガーデンがあります！"
                ),
            },
        }
    ],
    "questions": [
        {
            "question_id": "問1",
            "answer_number": 15,
            "stem": {
                "en": "Based on comment (1), which is the best sentence to add? [ 15 ]",
                "ja": "コメント(1)に基づいて，付け加えるのに最も適当な文はどれか。［15］",
            },
            "choices": [
                {
                    "label": "①",
                    "en": (
                        "Besides, gardening is a popular activity that can be enjoyed regardless of age."
                    ),
                    "ja": "その上，ガーデニングは年齢にかかわらず楽しめる人気のある活動である。",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": (
                        "For instance, they teach valuable lessons about how our food is produced."
                    ),
                    "ja": "例えば，それらは食料がどのように生産されるかについて，貴重な知識を与えてくれる。",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": (
                        "Furthermore, community gardens provide people with a chance to be alone."
                    ),
                    "ja": "さらに，コミュニティ・ガーデンは人々に一人になる機会を与える。",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": (
                        "Similarly, community gardens promote sport in urban environments."
                    ),
                    "ja": "同様に，コミュニティ・ガーデンは都市環境におけるスポーツを促進する。",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①。後続の different generations と対応するよう「年齢を問わず」が橋渡しになる。"
                    "③は孤立と段落の交流の主旨に矛盾。②④は次文の hubs / generations と論理的につながらない。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["cg_p2_s2", "cg_p2_s3"],
                "instructor_note": {
                    "ja": (
                        "挿入問題は英語力というより論理の埋め合わせ。前句の「交流できる場がない」と後句の「世代を超えて知り合うハブになる」を橋渡しする情報だけが正解候補になる。"
                    ),
                    "points": [
                        "①の regardless of age は後文の different generations と語彙的にロックするため強い。",
                        "③ alone は交流段落の主旨と真っ向から対立。②は食物教育にずれ，④はスポーツという別話題。",
                        "コメント (1) が要求するのは「追加情報」なので，単なる接続詞だけでは足りない／という説明もセットで覚える。",
                    ],
                },
            },
        },
        {
            "question_id": "問2",
            "answer_number": 16,
            "stem": {
                "en": "Based on comment (2), which is the best expression to add? [ 16 ]",
                "ja": "コメント(2)に基づいて，付け加えるのに最も適当な表現はどれか。［16］",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "Additionally",
                    "ja": "さらに（その上）",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "However",
                    "ja": "しかし",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "In contrast",
                    "ja": "それに対して",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "Therefore",
                    "ja": "したがって",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①（Additionally）。前句の「実用的スキル・知識」に続き，チームワークによる効果を"
                    "さらに付け加える並列・追加の関係。Therefore は因果が強すぎ，However / In contrast は対比で不適切。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["cg_p3_s1", "cg_p3_s2"],
                "instructor_note": {
                    "ja": (
                        "語単位の問題でも，前後が「同じ方向の追加」か「転換」かを見れば半数は切れる。"
                        "段落全体がベネフィットの積み上げなら，追加・累加のコネクター（Additionally / Furthermore / Moreover）をまず疑う。"
                    ),
                    "points": [
                        "前句＝知識・技能の提供，後句＝チームワークで得る力。いずれも参加の学びの列挙なので累加の ①。",
                        "However / In contrast は対立を，Therefore は帰結を導く。ここでは「次の利点」が続くのが自然。",
                        "口語の Plus や What is more も同系統。テスト頻出の接続副詞を意味別に整理しておくと早い。",
                    ],
                },
            },
        },
        {
            "question_id": "問3",
            "answer_number": 17,
            "stem": {
                "en": (
                    "Based on comment (3), which is the most appropriate way to rewrite the topic sentence? [ 17 ]"
                ),
                "ja": "コメント(3)に基づいて，主題文を書き換えるのに最も適当なものはどれか。［17］",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "we can benefit from the harvest",
                    "ja": "私たちは収穫の恩恵を受けることができる",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "we can enjoy visiting the area",
                    "ja": "私たちはその場所を訪れるのを楽しむことができる",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "we can feel closer to nature",
                    "ja": "私たちは自然をより身近に感じることができる",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "we can save shipping costs",
                    "ja": "私たちは輸送費が節約できる",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①。段落はコミュニティ所有による青果の入手しやすさと健康志向の食事につながる内容。"
                    "収穫（harvest）が affordable produce / healthier eating の主題を最も要約する。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["cg_p4_s2", "cg_p4_s3"],
                "instructor_note": {
                    "ja": (
                        "話題文リライトは，段落のSupporting sentencesがすべて説明できる見出しになっているかが判定基準。"
                        "「責任」「自然」「輸送費」など一語に惹かれず，複数文をまたいだ内容（価格・アクセス・健康）を一枚岩で言えるかを見る。"
                    ),
                    "points": [
                        "本段落の具体描写は community ownership → affordable produce → healthier habits と「入手と食生活」の鎖。harvest／収穫がその要約として機能する。",
                        "visit the area は場所訪問にずれ，feel closer to nature は緑化そのものを強調しすぎ。shipping costs は本文が運ぶコストを直接は言わない。",
                        "リライト問題では文法的に続くか（段落がyou／we で統一か）もチェックする癖があると安心。",
                    ],
                },
            },
        },
        {
            "question_id": "問4",
            "answer_number": 18,
            "stem": {
                "en": "Based on comment (4), which is the best replacement? [ 18 ]",
                "ja": "コメント(4)に基づいて，置き換えるのに最も適当なものはどれか。［18］",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "are popular locations for holding events",
                    "ja": "イベント開催地として人気がある",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "can create collaboration among local schools",
                    "ja": "地域の学校間の協力を生み出す",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "have the potential to revitalize unwanted land",
                    "ja": "不用地を活性化する可能性がある",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "help build deeper relationships within the community",
                    "ja": "地域内でより深い人間関係を構築するのに役立つ",
                    "is_correct": True,
                },
            ],
            "answer": "④",
            "explanation": {
                "quoted_ja": (
                    "正解は④。結論の並列は第２段落の交流（世代を超えた知り合い）・第３段落の学び・第４段落の食と"
                    "対応する必要がある。help the elderly だけでは交流の要点を要約できない。④が第２段落の内容に合致。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["cg_p2_s3", "cg_p3_s2", "cg_p4_s2", "cg_p5_s1"],
                "instructor_note": {
                    "ja": (
                        "結論パートの並列はしばしば body の First… Second… Finally… と対応する。"
                        "下線が粗いのは「その段落のキーワードを拾えていない」場合が多く，書き換え先も同じマッピングで探す。"
                    ),
                    "points": [
                        "provide valuable lessons は第３段落（スキル・チームワーク），enrich our diet は第４段落（青果・健康）なので，残りの第一項目は第２段落の「交流・世代」の要約であるべき。",
                        "help the elderly は高齢者にフォーカスしすぎて，世代を超えた interaction／hub の射程を狭める。④が関係性の深化として広く拾える。",
                        "①イベント会場・②学校連携・③土地再生は本文が触れない論点ではじける（典型の誤答パターン）。",
                    ],
                },
            },
        },
    ],
    "vocabulary": {
        "passage": {
            "label_ja": "主な語彙・表現",
            "items": [
                {"en": "in cooperation with ~", "ja": "〜と協力して"},
                {"en": "ensure", "ja": "〜を確実にする"},
                {"en": "potential", "ja": "可能性"},
                {"en": "urban", "ja": "都市の"},
                {"en": "isolation", "ja": "孤立"},
                {"en": "increasingly", "ja": "ますます"},
                {"en": "interaction", "ja": "交流（動詞は interact「交流する」）"},
                {"en": "resident", "ja": "住民"},
                {"en": "serve as ~", "ja": "〜としての役割を果たす；〜として役立つ"},
                {"en": "hub", "ja": "（活動などの）中心地；拠点"},
                {"en": "get to know ~", "ja": "〜と知り合う"},
                {"en": "practical", "ja": "実用的な"},
                {"en": "responsibility", "ja": "責任"},
                {"en": "ownership", "ja": "所有者であること；所有していること"},
                {"en": "nutritious", "ja": "栄養価の高い"},
                {"en": "affordable", "ja": "手頃な価格の"},
                {"en": "produce", "ja": "農産物；生鮮食品"},
                {"en": "enrich", "ja": "〜を豊かにする"},
                {"en": "diet", "ja": "食習慣；食生活"},
                {"en": "問1 ① regardless of ~", "ja": "〜にかかわらず"},
                {"en": "問1 ③ furthermore", "ja": "さらに"},
                {"en": "問1 ④ similarly", "ja": "同様に"},
                {"en": "問2 ① additionally", "ja": "さらに"},
                {"en": "問2 ③ in contrast", "ja": "その一方"},
                {"en": "問3 ① harvest", "ja": "収穫（物）"},
                {"en": "問3 ④ shipping", "ja": "運搬の；輸送の"},
                {"en": "問4 ② collaboration", "ja": "協力"},
                {"en": "問4 ③ revitalize", "ja": "〜を活性化する"},
                {"en": "問4 ③ unwanted", "ja": "要らない；不要な"},
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
    data["sections"] = [s for s in data["sections"] if s.get("section_number") != 4]
    data["sections"].append(section_04)
    data["sections"].sort(key=lambda s: s.get("section_number", 0))
    impl = data.setdefault("exam_info", {}).setdefault("implemented_sections", [])
    if 4 not in impl:
        impl.append(4)
        impl.sort()
    data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Merged section 4 →", data_path)


if __name__ == "__main__":
    main()
