# -*- coding: utf-8 -*-
"""Z会 実戦模試 2026 第4回 第3問（科学博物館のブログ・ケイ）を data.json にマージする。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUOTED = "Z会『2026年 共通テスト実戦模試 英語リーディング』第4回 解説冊子"

section_03 = {
    "section_number": 3,
    "title": "第3問",
    "points": 9,
    "points_per_question": 3,
    "description": "ブログ読解（科学博物館の校外学習）",
    "situation": {
        "en": (
            "You are getting ready for a school trip to the science museum with your classmates next week. "
            "You are reading an online blog post written by a high school student, Kei, who recently went there on a field trip."
        ),
        "ja": (
            "あなたは，来週のクラスメートとの科学博物館への修学旅行の準備をしています。"
            "あなたは高校生のケイが書いたオンラインブログ記事を読んでいます。彼女は学校の校外学習で最近そこに行きました。"
        ),
    },
    "passages": [
        {
            "id": "kei_science_museum_blog",
            "framed": True,
            "title": {
                "en": "One Day at the Science Museum",
                "ja": "科学博物館での１日",
            },
            "paragraphs": [
                [
                    {
                        "id": "kei_p1_s1",
                        "en": (
                            "Last month, my classmates and I went on an exciting field trip to a large science museum "
                            "in the neighboring city."
                        ),
                        "ja": "先月，クラスメートと隣の市にある大きな科学博物館へワクワクする校外学習に行った。",
                    },
                    {
                        "id": "kei_p1_s2",
                        "en": "I had been looking forward to it all week, and finally, the day arrived!",
                        "ja": "一週間ずっと楽しみにしていて，ついにその日がやって来た。",
                    },
                    {
                        "id": "kei_p1_s3",
                        "en": (
                            "As our class entered the massive building, the teachers encouraged us to explore "
                            "where our interests led us."
                        ),
                        "ja": "巨大な建物にクラスが入ると，先生たちは自分たちの興味の赴くままに見て回るよう勧めてくれた。",
                    },
                ],
                [
                    {
                        "id": "kei_p2_s1",
                        "en": "Our first stop was the interactive physics exhibit.",
                        "ja": "最初に立ち寄ったのは体験型の物理学のコーナーだった。",
                    },
                    {
                        "id": "kei_p2_s2",
                        "en": "There were hands-on displays about how motion and energy work.",
                        "ja": "運動とエネルギーがどのように働くかについて，実際に触って学べる展示があった。",
                    },
                    {
                        "id": "kei_p2_s3",
                        "en": (
                            "I had the chance to create mini-tornadoes in a tube and even tried some interactive exhibits "
                            "with magnets."
                        ),
                        "ja": "筒の中でミニ竜巻を作ったり，磁石を使った体験型の展示にも挑戦した。",
                    },
                    {
                        "id": "kei_p2_s4",
                        "en": (
                            "They used metallic pieces and tiny marbles to demonstrate how magnets stick together or separate."
                        ),
                        "ja": "金属片や小さなビー玉を使って，磁石がくっついたり離れたりする様子を実演していた。",
                    },
                    {
                        "id": "kei_p2_s5",
                        "en": (
                            "The best part was definitely that we could touch and manipulate so many things, "
                            "which made it a lot more exciting than an ordinary science class."
                        ),
                        "ja": (
                            "いちばんよかったのは，たくさんのものに触って操作できたことで，"
                            "普通の理科の授業よりずっとワクワクした。"
                        ),
                    },
                ],
                [
                    {
                        "id": "kei_p3_s1",
                        "en": "Next, we all gathered in a large auditorium for the live science show.",
                        "ja": "次に，全員で大きな講堂に集まり，実演のサイエンスショーを見た。",
                    },
                    {
                        "id": "kei_p3_s2",
                        "en": "This one really impressed me and my friends alike.",
                        "ja": "このショーは私も友人たちも本当に感動した。",
                    },
                    {
                        "id": "kei_p3_s3",
                        "en": (
                            "The presenters showed us some incredible experiments, like freezing flowers with liquid nitrogen "
                            "and then shattering them like glass."
                        ),
                        "ja": (
                            "実演者は液体窒素で花を凍らせてガラスのように粉々にしたりするすごい実験をいくつか見せてくれた。"
                        ),
                    },
                    {
                        "id": "kei_p3_s4",
                        "en": (
                            "They also used electricity to create bright flashes of light and loud sounds "
                            "that made us all jump in our seats."
                        ),
                        "ja": (
                            "また電気を使って明るい閃光と，私たち全員が席で飛び上がるほど大きな音を立てた。"
                        ),
                    },
                    {
                        "id": "kei_p3_s5",
                        "en": "It felt more like something out of a magic show than a museum performance.",
                        "ja": "博物館の実演というよりマジックショーのようだった。",
                    },
                ],
                [
                    {
                        "id": "kei_p4_s1",
                        "en": "For some reason, the last exhibit I saw stuck in my mind.",
                        "ja": "どういうわけか，最後に見た展示が私の印象に残った。",
                    },
                    {
                        "id": "kei_p4_s2",
                        "en": (
                            "It involved rubbing your hands together over a net and you somehow couldn't feel it."
                        ),
                        "ja": "手をこすり合わせると，どういうわけで感じられないネットのようなものに触っている展示だった。",
                    },
                    {
                        "id": "kei_p4_s3",
                        "en": "It felt like touching a very soft surface.",
                        "ja": "とても柔らかいものに触っているような感覚だった。",
                    },
                    {
                        "id": "kei_p4_s4",
                        "en": (
                            "It got me thinking a lot about how the human body sends signals to the brain when we touch things."
                        ),
                        "ja": "物に触れたときに人体が脳にどのように信号を送るかについて，とても考えさせられた。",
                    },
                    {
                        "id": "kei_p4_s5",
                        "en": "By the end of the day, my friends and I were all exhausted.",
                        "ja": "その日の終わりには，友人たちも私もみんなくたくただった。",
                    },
                    {
                        "id": "kei_p4_s6",
                        "en": (
                            "Not only had we been on our feet most of the day, but we had taken in so many new experiences."
                        ),
                        "ja": (
                            "一日のほとんどを立ちっぱなしで過ごしただけでなく，"
                            "これでもかというほど新しい体験を詰め込んだからだ。"
                        ),
                    },
                ],
            ],
            "images": [
                {
                    "paragraph_index": 0,
                    "src": "images/science_museum_building.png",
                    "position": "float-right",
                    "alt": "Large science museum building with dome",
                    "max_width": 220,
                }
            ],
        },
        {
            "id": "kei_science_museum_coda",
            "framed": True,
            "paragraphs": [
                [
                    {
                        "id": "kei_coda_s1",
                        "en": (
                            "In the end, I realized that there's so much to discover about the world around us and our bodies too."
                        ),
                        "ja": (
                            "結局，私たちの周りの世界や，私たち自身の体についても，まだまだ発見することがたくさんあると気づいた。"
                        ),
                    },
                    {
                        "id": "kei_coda_s2",
                        "en": "I hope we get a chance to visit the science museum again next year!",
                        "ja": "来年もまたこの科学博物館に来られるといいなと思う。",
                    },
                ]
            ],
        },
    ],
    "questions": [
        {
            "question_id": "問1",
            "question_type": "ordering",
            "answer_numbers": [8, 9, 10, 11],
            "stem": {
                "en": (
                    "Kei's blog post also included student comments (① ~ ④) describing the events in the museum trip. "
                    "Put the comments in the order in which the events happened. [ 8 ] → [ 9 ] → [ 10 ] → [ 11 ]"
                ),
                "ja": (
                    "ケイのブログ記事には，博物館の校外学習のできごとを描写する学生のコメント（①〜④）も載っていた。"
                    "できごとが起こった順にコメントを並べよ。［8］→［9］→［10］→［11］"
                ),
            },
            "choices": [
                {
                    "label": "①",
                    "en": (
                        "At one exhibit, we could rub our hands together over a net that we could not feel. "
                        "That one really shocked my friends!"
                    ),
                    "ja": (
                        "ある展示では，感じられないネットの上で手をこすり合わせることができた。"
                        "その展示は友人たちを本当に驚かせた！"
                    ),
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": (
                        "I can't believe how tired we were when it was all over! We were on the move almost all day."
                    ),
                    "ja": "全部終わったときどれだけ疲れていたか信じられない！ほとんど一日中動き回っていた。",
                    "is_correct": True,
                },
                {
                    "label": "③",
                    "en": (
                        "I was really shocked when they froze the plants. The part with the liquid nitrogen was so cool!"
                    ),
                    "ja": "植物を凍らせたときは本当にびっくりした。液体窒素のところはすごくかっこよかった！",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": (
                        "The area with the magnets really grabbed my attention. I felt like I could finally understand "
                        "what the teacher had explained to us in class last week."
                    ),
                    "ja": (
                        "磁石のコーナーがいちばん目を引いた。先週先生が授業で説明してくれたことが，ようやくわかった気がした。"
                    ),
                    "is_correct": True,
                },
            ],
            "answer": "④→③→①→②",
            "answer_sequence": ["④", "③", "①", "②"],
            "explanation": {
                "quoted_ja": (
                    "正解の順序は④→③→①→②。④は第2段落の磁石の体験，③は第3段落の液体窒素の実演，"
                    "①は第4段落のネットの展示，②は第4段落後半の疲労の感想に対応する。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["kei_p2_s3", "kei_p3_s3", "kei_p4_s2", "kei_p4_s5"],
                "instructor_note": {
                    "ja": (
                        "見学ルートは段落の先頭（Our first stop / Next / last exhibit）と，コメント中の固有名詞・話題語を対応させる。"
                        "疲労や感情のコメントは時系列の末尾に置きがちなので，②を機械的に先頭にしない。"
                    ),
                    "points": [
                        "最初の見学は物理学コーナー＝磁石・竜巻（④が最優先しやすい）。",
                        "次は講堂のショー＝液体窒素（③）。",
                        "「最後に見た」展示＝ネット（①）。",
                        "一日の終わりの疲れ（②）は最後。",
                        "liquid nitrogen と magnets を同一展示にしない（段落が別）。",
                    ],
                },
            },
        },
        {
            "question_id": "問2",
            "answer_number": 12,
            "stem": {
                "sentences": [
                    {
                        "id": "kei_q2_stem",
                        "en": "During his stay at the museum, Kei did <strong><u>not</u></strong> experience [ 12 ].",
                        "ja": "博物館滞在中に，ケイは<strong><u>しなかった</u></strong>のは［12］である。",
                    }
                ]
            },
            "choices": [
                {
                    "label": "①",
                    "en": "bright flashes of light",
                    "ja": "明るい閃光",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "flowers breaking apart",
                    "ja": "粉々になる花",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "frozen magnets",
                    "ja": "凍った磁石",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "surprising loud sounds",
                    "ja": "驚くような大きな音",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。磁石の実験はあるが「凍った磁石」の記述はない。"
                    "閃光・大きな音・花を凍らせて砕く様子は第3段落にある。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["kei_p3_s3", "kei_p3_s4", "kei_p2_s3"],
                "instructor_note": {
                    "ja": (
                        "NOT experience は「本文にある出来事の否定」ではなく，選択肢の語の組み合わせが本文と整合するかを見る。"
                        "動詞の対象（何を凍らせたか）と名詞（磁石か花か）を分解して照合する。"
                    ),
                    "points": [
                        "凍結・粉々は液体窒素の実演で花に及んでおり，磁石は別展示。frozen magnets は成立しない組み合わせ。",
                        "magnets と liquid nitrogen を混同しない。",
                        "①④は electricity の文，②は freezing flowers と対応。",
                    ],
                },
            },
        },
        {
            "question_id": "問3",
            "answer_number": 13,
            "stem": {
                "en": "At the end of the day, Kei was curious about [ 13 ].",
                "ja": "その日の最後に，ケイは［13］に関心を持った。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "magic tricks",
                    "ja": "手品",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "the next trip",
                    "ja": "次回の校外学習",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "the world around us",
                    "ja": "自分たち人間の周りの世界",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "tornado formation",
                    "ja": "竜巻の構造",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。最終段落（In the end...）に there's so much to discover about the world around us とある。"
                    "②は再来訪の希望であり「次の校外学習への関心」とは言い切れない。①は比喩表現の magic show に惑わされない。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["kei_coda_s1"],
                "instructor_note": {
                    "ja": (
                        "At the end of the day は「締めのまとめ段落」の触发語。"
                        "ショーの刺激や途中の展示ではなく，結びの段落（In the end...）で気づきを述べるブロックを対象にする。"
                    ),
                    "points": [
                        "world around us は選択肢③とほぼ直結。",
                        "tornado は第2段落の話で，設問の「最後の関心」とはズレる。",
                        "②の next trip は再来訪の希望であって「その日の終わりに抱いた関心」とは別レイヤー。",
                        "magic tricks は比喩の magic show に引っ張られない。",
                    ],
                },
            },
        },
    ],
    "vocabulary": {
        "passage": {
            "label_ja": "主な語彙・表現",
            "items": [
                {"en": "massive", "ja": "巨大な"},
                {"en": "interactive", "ja": "双方向の，対話的な；参加・体験型の展示"},
                {"en": "exhibit", "ja": "展示"},
                {"en": "hands-on", "ja": "体験型の，実際に操作できる"},
                {"en": "motion", "ja": "運動"},
                {"en": "tornado", "ja": "竜巻"},
                {"en": "demonstrate", "ja": "〜を示す，〜を実演する"},
                {"en": "manipulate", "ja": "〜を操作する"},
                {"en": "gather", "ja": "集まる"},
                {"en": "auditorium", "ja": "講堂，ホール"},
                {"en": "impress", "ja": "〜を感動させる"},
                {"en": "presenter", "ja": "実演者"},
                {"en": "liquid nitrogen", "ja": "液体窒素"},
                {"en": "flash", "ja": "（光などの）閃光"},
                {"en": "stick in one's mind", "ja": "〜の印象に残る"},
                {"en": "rub", "ja": "（手など）をこすり合わせる"},
                {"en": "signal", "ja": "信号"},
                {"en": "grab one's attention（問1④）", "ja": "〜の注意を引く"},
                {"en": "break apart（問2②）", "ja": "粉々になる"},
                {"en": "formation（問3④）", "ja": "構造"},
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
