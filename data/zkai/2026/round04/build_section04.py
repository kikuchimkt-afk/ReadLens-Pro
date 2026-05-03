# -*- coding: utf-8 -*-
"""Z会 実戦模試 2026 第4回 第4問（エッセイ推敲・学校改善の提案）を data.json にマージする。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUOTED = "Z会『2026年 共通テスト実戦模試 英語リーディング』第4回 解説冊子"

section_04 = {
    "section_number": 4,
    "title": "第4問",
    "points": 12,
    "points_per_question": 3,
    "description": "エッセイ添削（授業改善の提案・先生コメント）",
    "situation": {
        "en": (
            "In your English class, you are writing an essay about the suggestions to improve this school. "
            "This is your most recent draft. You are now working on revisions after reading your teacher's advice."
        ),
        "ja": (
            "英語の授業で，あなたはこの学校を良くするための提案についてエッセイを書いています。"
            "これはあなたの最新の草稿です。今は先生からの助言を読んだあと，推敲に取り組んでいるところです。"
        ),
    },
    "passages": [
        {
            "id": "improve_classes_essay",
            "title": {
                "en": "How to Improve Classes for Future Students",
                "ja": "未来の生徒のために授業をいかに改善するか",
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
                        "id": "imp_p1_s1",
                        "en": (
                            "I think our school is well run and offers a safe and healthy learning environment "
                            "where most students are happy."
                        ),
                        "ja": (
                            "私たちの学校は適切に運営されており，安全で健全な学習環境を提供し，"
                            "そこで学ぶ大半の生徒が満足していると思う。"
                        ),
                    },
                    {
                        "id": "imp_p1_s2",
                        "en": (
                            "Even so, I believe learning would be more effective if some changes were made "
                            "to classes and lesson structure."
                        ),
                        "ja": (
                            "とはいえ，クラスや授業の構成にいくつかの変化が加えられれば，"
                            "学習は今以上に効果的になるだろう。"
                        ),
                    },
                ],
                [
                    {
                        "id": "imp_p2_s1",
                        "en": "First, I would like the school to offer more individual learning plans.",
                        "ja": "まず，学校には，もっと個々人に合った学習計画を提供してほしい。",
                    },
                    {
                        "id": "imp_p2_s2",
                        "en": (
                            "For example, several students go to cram schools after school for the sole purpose "
                            "of preparing for university entrance exams."
                        ),
                        "ja": (
                            "例えば，大学受験の準備だけを目的として放課後に塾へ通う生徒もいる。"
                        ),
                    },
                    {
                        "id": "imp_p2_s3",
                        "en": (
                            "If there were intensive classes to meet individual needs here at school, "
                            "it would benefit all students."
                        ),
                        "ja": (
                            "もし学校でも個々のニーズに応える集中的な授業があれば，すべての生徒に役立つだろう。"
                        ),
                        "comment_marker": "(1)",
                        "marker_type": "caret",
                    },
                ],
                [
                    {
                        "id": "imp_p3_s1",
                        "en": "Second, we should be able to learn in classes for ourselves.",
                        "ja": "第二に，私たちは「自分たちのための」授業の中で学べるべきだ。",
                        "comment_marker": "(2)",
                        "underline_word": "for ourselves",
                    },
                    {
                        "id": "imp_p3_s2",
                        "en": "Currently, we have classes based on ability only for math.",
                        "ja": "現在，習熟度別クラスがあるのは数学だけだ。",
                    },
                    {
                        "id": "imp_p3_s3",
                        "en": (
                            "However, if we could have discussions or do group work with students of around the same level, "
                            "maybe in English, social studies and Japanese, we would feel more confident to speak up "
                            "and be active in class."
                        ),
                        "ja": (
                            "しかし，英語や社会，国語でも，おおよそ同じレベルの生徒同士で話し合ったりグループ活動ができれば，"
                            "発言したり授業に積極的に参加したりする自信がもっと持てるだろう。"
                        ),
                    },
                ],
                [
                    {
                        "id": "imp_p4_s1",
                        "en": "My final point is that assignments should be tailored to suit the ability of the individual.",
                        "ja": "最後に，課題はそれぞれの能力に合わせて調整されるべきだ。",
                    },
                    {
                        "id": "imp_p4_s2",
                        "en": (
                            "In other words, I want teachers to plan lessons with easier or more difficult content, "
                            "depending on individual academic achievement."
                        ),
                        "ja": (
                            "言い換えれば，教師には個人の学力に応じて，よりやさしい内容かより難しい内容かを計画してほしい。"
                        ),
                    },
                    {
                        "id": "imp_p4_s3",
                        "en": (
                            "Everybody could feel more progress and motivation if the tasks were not too easy or too difficult."
                        ),
                        "ja": (
                            "課題が簡単すぎず難しすぎなければ，誰もがもっと成長実感と意欲を持てるだろう。"
                        ),
                        "comment_marker": "(3)",
                        "marker_type": "caret",
                    },
                ],
                [
                    {
                        "id": "imp_p5_s1",
                        "en": "Our school is already a good school in terms of academic level.",
                        "ja": "学力という点では，私たちの学校はすでにすぐれた学校だ。",
                    },
                    {
                        "id": "imp_p5_s2",
                        "en": "However, we are all individuals with strong points and weak points.",
                        "ja": "しかし，私たち一人ひとりには長所も短所もある。",
                    },
                    {
                        "id": "imp_p5_s3",
                        "en": (
                            "I feel that if there were more optional classes and students were more equal, "
                            "it would be a more efficient and positive experience for all students."
                        ),
                        "ja": (
                            "選択制の授業がもっと増え，生徒同士がより対等であれば，"
                            "すべての生徒にとってより効率的で前向きな経験になると感じる。"
                        ),
                        "comment_marker": "(4)",
                        "underline_word": "students were more equal",
                    },
                ],
            ],
            "margin_comments": [
                {
                    "marker": "(1)",
                    "en": "You need more explanation. Add something here to clarify what you mean.",
                    "ja": "説明がもっと必要です。あなたの言いたいことをはっきりさせるために，ここに何か加えなさい。",
                },
                {
                    "marker": "(2)",
                    "en": "It is not clear what you mean. Write a better expression here.",
                    "ja": "何を言いたいのかがはっきりしません。より適切な表現を書きなさい。",
                },
                {
                    "marker": "(3)",
                    "en": "Add a connecting expression here.",
                    "ja": "ここに接続の表現を加えなさい。",
                },
                {
                    "marker": "(4)",
                    "en": "The underlined part doesn't summarize your point well. Change it.",
                    "ja": "下線部はあなたの主張を十分に要約していません。変更しなさい。",
                },
            ],
            "teacher_comment": {
                "title_en": "Overall comments:",
                "title_ja": "総合的なコメント：",
                "en": (
                    "You have some very interesting ideas. I like that you have thought clearly and carefully "
                    "about how to improve life for all students."
                ),
                "ja": (
                    "とても興味深い考えがいくつもあります。"
                    "すべての生徒の生活をどう改善するかについて，はっきりと慎重に考えていることが気に入りました。"
                ),
            },
        }
    ],
    "questions": [
        {
            "question_id": "問1",
            "answer_number": 14,
            "stem": {
                "en": "Based on comment (1), which is the best sentence to add? [ 14 ]",
                "ja": "コメント(1)に基づいて，付け加えるのに最も適当な文はどれか。［14］",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "Meanwhile, other students are having a hard time with self-study.",
                    "ja": "その一方，自学自習に苦労している生徒もいる。",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "On the contrary, there are students of poor level here.",
                    "ja": "反対に，ここにはレベルの低い生徒もいる。",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "On the other hand, teachers are not helping average students.",
                    "ja": "他方，先生たちは平均的な生徒の助けになっていない。",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "Yet learning can be more effective through self-study.",
                    "ja": "それでも，自学自習によって学習はより効果的になるだろう。",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①。(1)は塾へ行く生徒の具体例のあと，個別ニーズに応える集中クラスの提案につなげる位置。"
                    "受験以外のニーズや自学の苦手さを示す①が，後続の if there were intensive classes への橋渡しとして妥当。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["imp_p2_s2", "imp_p2_s3"],
                "instructor_note": {
                    "ja": (
                        "コメント(1) が求めるのは「塾に行く具体例」と「学校側で intensive に用意すべきクラス」の間の論理的ギャップを埋める一文。"
                        "受験一本の生徒だけが救われるのではなく，多様なニーズがあることをさりげなく差し込めるかが鍵。"
                    ),
                    "points": [
                        "①は自学や塾以外の学び方に苦手さ・ニーズを示し，後続の if there were intensive classes here と矛盾しない橋渡しになる。",
                        "②③は教師や平均の生徒への評価が前面に出てエッセイのトーンを壊しやすい。④は自学効果を断定しすぎて後文の学校側提案とずれる。",
                        "「塾の話の直後」に置くと読みやすい位置だが，Grammatically に前後の文とつながる主語・接続にも目を通す。",
                    ],
                },
            },
        },
        {
            "question_id": "問2",
            "answer_number": 15,
            "stem": {
                "en": "Based on comment (2), which would be a clearer expression? [ 15 ]",
                "ja": "コメント(2)に基づいて，より明瞭な表現はどれか。［15］",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "that are made for each of us",
                    "ja": "自分たち一人一人のために作られた",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "where we can study on our own",
                    "ja": "自分たちで勉強できる",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "with fewer students",
                    "ja": "もっと生徒の少ない",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "with students suited to our academic level",
                    "ja": "自分の学力レベルと合った生徒たちから成る",
                    "is_correct": True,
                },
            ],
            "answer": "④",
            "explanation": {
                "quoted_ja": (
                    "正解は④。classes for ourselves が曖昧で，段落の主旨は数学以外でも習熟度に応じたクラスを求めること。"
                    "④が ability-based classes の言い換えとして最も近い。①は次段落の個別課題と混同しやすい。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["imp_p3_s1", "imp_p3_s2", "imp_p3_s3"],
                "instructor_note": {
                    "ja": (
                        "classes for ourselves が抽象的なので，後続段落が語る「習熟度・レベル・グループ」を一言で言い換える。"
                        "『自分たちのため』を『自分に合った仲間と』へ具体化できる選択肢を探す。"
                    ),
                    "points": [
                        "④は around the same level / ability-based の流れと整合し，数学以外の教科にも一般化できる。",
                        "②は study on our own で自学に寄り，段落が狙う分层・班会とは別方向。",
                        "③は人数のみで本文が述べていない縮小。①は次段落の個別課題 tailor と語がぶつかりやすい。",
                    ],
                },
            },
        },
        {
            "question_id": "問3",
            "answer_number": 16,
            "stem": {
                "en": "Based on comment (3), which would be the best expression to use? [ 16 ]",
                "ja": "コメント(3)に基づいて，用いるのに最も適当な表現はどれか。［16］",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "For a start",
                    "ja": "手始めに",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "Furthermore",
                    "ja": "さらに",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "In this way",
                    "ja": "このようにして",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "On the other hand",
                    "ja": "他方",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。前句で個人の学力に応じた授業内容を述べたうえで，"
                    "その結果・方法として課題の難易が適切なら動機づけが高まると続ける。"
                    "In this way が「そうしたやり方なら」の接続として自然。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["imp_p4_s2", "imp_p4_s3"],
                "instructor_note": {
                    "ja": (
                        "コメント(3) は「前の政策提案と，その結果としての効果」の関係を示す接続が欲しい場面。"
                        "前文が手段なら In this way / As a result 系，単なる追加なら Furthermore になるかを切り分ける。"
                    ),
                    "points": [
                        "前句は個人の学力に応じた授業内容，後句はそうした設計が動機づけに与える影響。手段→帰結のつながりで③が自然。",
                        "Furthermore は「もう一つ別の提案」を足すニュアンスが強く，同じ段落内の因果の締めとしてはやや浮く。",
                        "On the other hand は対立段落が続くときに限定。For a start は列挙の冒頭向けでここでは弱い。",
                    ],
                },
            },
        },
        {
            "question_id": "問4",
            "answer_number": 17,
            "stem": {
                "en": "Based on comment (4), which is the best replacement? [ 17 ]",
                "ja": "コメント(4)に基づいて，置き換えるのに最も適当なものはどれか。［17］",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "students were allowed to choose classes",
                    "ja": "生徒がクラスを選べた",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "students were given the same assignments",
                    "ja": "生徒に一律の課題が課された",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "students were helped in difficult classes",
                    "ja": "生徒が難しい授業で助けを得られた",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "students were taught according to their level",
                    "ja": "生徒が自分のレベルに応じて授業を受けられた",
                    "is_correct": True,
                },
            ],
            "answer": "④",
            "explanation": {
                "quoted_ja": (
                    "正解は④。締めの段落で optional classes と並列の内容は，個別ニーズ・習熟度別・課題調整という前文の要約であるべき。"
                    "students were more equal は主旨をまとめきれない。④がレベルに応じた授業という趣旨に合致。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["imp_p2_s1", "imp_p3_s3", "imp_p4_s1", "imp_p5_s3"],
                "instructor_note": {
                    "ja": (
                        "結論の並列は optional classes と more equal が担う「平等・個別最適」の軸をまとめ直す語が必要。"
                        "equal をそのまま英語で言い換えるより，前文で繰り返した ability / level / tailored を再注入できるか。"
                    ),
                    "points": [
                        "④は taught according to their level で，個別学習計画・習熟度別クラス・課題の tailor と一本線で結べる。",
                        "②は same assignments で本文の主旨と正反対。①③はエッセイが立てていない実証なので排除しやすい。",
                        "more equal だけでは「何が平等か」が抽象的で，設問はより具体的な言い換えを求めていると心得る。",
                    ],
                },
            },
        },
    ],
    "vocabulary": {
        "passage": {
            "label_ja": "主な語彙・表現",
            "items": [
                {"en": "run", "ja": "〜を運営する"},
                {"en": "structure", "ja": "構成；仕組み"},
                {"en": "individual", "ja": "個人の；各自の；個人"},
                {"en": "cram school", "ja": "塾，予備校"},
                {"en": "for the sole purpose of ~", "ja": "もっぱら〜を目的として"},
                {"en": "intensive", "ja": "集中的な；徹底的な"},
                {"en": "meet one's needs", "ja": "〜のニーズを満たす"},
                {"en": "benefit", "ja": "〜の役に立つ；〜に利する"},
                {"en": "speak up", "ja": "発言する"},
                {"en": "assignment", "ja": "課題；宿題"},
                {"en": "tailor", "ja": "〜を（要求・必要などに）合わせて作る"},
                {"en": "suit", "ja": "〜に合う，〜に適合する"},
                {"en": "depending on ~", "ja": "〜次第で；〜に応じて"},
                {"en": "academic", "ja": "学問の；教育に関する"},
                {"en": "in terms of ~", "ja": "〜に関して言えば"},
                {"en": "optional", "ja": "選択制の"},
                {"en": "have a hard time with ~（問1①）", "ja": "〜で苦労する"},
                {"en": "average（問1③）", "ja": "普通の；平均的な"},
                {"en": "according to ~（問4④）", "ja": "〜に応じて；〜にしたがって"},
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
