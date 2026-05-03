# -*- coding: utf-8 -*-
"""Z会 実戦模試 2026 第3回 第3問（ミオのオープンキャンパス・ブログ）を data.json にマージする。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUOTED = "Z会『2026年 共通テスト実戦模試 英語リーディング』第3回 解説冊子"

section_03 = {
    "section_number": 3,
    "title": "第3問",
    "points": 9,
    "points_per_question": 3,
    "description": "ブログ読解（オープンキャンパス）",
    "situation": {
        "en": (
            "You are a senior high school student researching university life. You are reading an online blog post "
            "by another senior high school student, Mio, who recently attended an open campus event at an "
            "international university in Tokyo."
        ),
        "ja": (
            "あなたは大学生活について調べている高校生である。東京の国際大学で最近開催されたオープンキャンパスに参加した"
            "別の高校生ミオのオンラインブログを読んでいる。"
        ),
    },
    "passages": [
        {
            "id": "mio_open_day_blog",
            "framed": True,
            "title": {
                "en": "Discovering My Future at a University Open Day",
                "ja": "大学のオープンキャンパスで未来を発見して",
            },
            "paragraphs": [
                [
                    {
                        "id": "mio_p1_s1",
                        "en": "Last Saturday, I attended an open day at a university in Tokyo.",
                        "ja": "先週の土曜日，私は東京のある大学のオープンキャンパスに参加した。",
                    },
                    {
                        "id": "mio_p1_s2",
                        "en": (
                            "I had always dreamed of attending such a school, but I wasn't sure what to expect."
                        ),
                        "ja": "ずっとそのような学校に通うことを夢見ていたが，実際がどうなのかはわからなかった。",
                    },
                    {
                        "id": "mio_p1_s3",
                        "en": (
                            "I decided I had to see the school for myself to know if it was right for me."
                        ),
                        "ja": "自分に合うかどうか確かめるには，自分の目で学校を見なければならないと決めた。",
                    },
                ],
                [
                    {
                        "id": "mio_p2_s1",
                        "en": "The day started with a guided tour of the campus.",
                        "ja": "その日はガイド付きのキャンパスツアーから始まった。",
                    },
                    {
                        "id": "mio_p2_s2",
                        "en": (
                            "The library, one of the largest I had ever seen, was filled with busy students."
                        ),
                        "ja": "今まで見た中でも最大級の図書館には，忙しそうな学生でいっぱいだった。",
                    },
                    {
                        "id": "mio_p2_s3",
                        "en": (
                            "Some were deeply focused, but others took the time to smile and wave when they saw our group."
                        ),
                        "ja": (
                            "深く集中している人もいれば，私たちのグループを見て微笑み，手を振ってくれる人もいた。"
                        ),
                    },
                    {
                        "id": "mio_p2_s4",
                        "en": (
                            "I also visited the laboratories, where I saw some awesome equipment provided by the "
                            "university for experiments."
                        ),
                        "ja": (
                            "また研究室も見学し，大学が実験のために用意しているすばらしい機材も目にした。"
                        ),
                    },
                    {
                        "id": "mio_p2_s5",
                        "en": (
                            "Our guide explained how these facilities were available to students for both classwork "
                            "and independent study projects."
                        ),
                        "ja": (
                            "ガイドは，これらの施設が授業の課題と自主研究プロジェクトの両方に，学生が利用できると説明してくれた。"
                        ),
                    },
                ],
                [
                    {
                        "id": "mio_p3_s1",
                        "en": "Next, we moved on to the dorms.",
                        "ja": "次に，私たちは寮へ向かった。",
                    },
                    {
                        "id": "mio_p3_s2",
                        "en": (
                            "They were huge, with long hallways and hundreds of rooms shared by students from Japan "
                            "and other countries."
                        ),
                        "ja": (
                            "とても大きく，長い廊下と何百もの部屋があり，日本や他の国からの学生がシェアしていた。"
                        ),
                    },
                    {
                        "id": "mio_p3_s3",
                        "en": (
                            "What impressed me the most was the activity center, with its billiards tables, "
                            "table tennis, video games, snacks, and lots of books too."
                        ),
                        "ja": (
                            "いちばん印象に残ったのは，ビリヤード台，卓球台，ビデオゲーム，おやつ，それに本もたくさんある"
                            "アクティビティセンターだった。"
                        ),
                    },
                    {
                        "id": "mio_p3_s4",
                        "en": (
                            "It was great to see students had a place to relax with their friends after classes."
                        ),
                        "ja": "授業のあと友だちとくつろげる場所があるのを見てすばらしいと思った。",
                    },
                ],
                [
                    {
                        "id": "mio_p4_s1",
                        "en": (
                            "After the tour, I had the chance to speak with some current students and professors."
                        ),
                        "ja": "ツアーのあと，在学生や教授とも話す機会があった。",
                    },
                    {
                        "id": "mio_p4_s2",
                        "en": (
                            "One student told me about her struggles during her freshman year."
                        ),
                        "ja": "ある学生は，大学1年生のときの苦労について話してくれた。",
                    },
                    {
                        "id": "mio_p4_s3",
                        "en": (
                            "However, she said that she got through it thanks to the university's great support system."
                        ),
                        "ja": "しかし，大学のすぐれたサポートのおかげで乗り越えられたと言っていた。",
                    },
                    {
                        "id": "mio_p4_s4",
                        "en": (
                            "One professor talked about the importance of building relationships with others."
                        ),
                        "ja": "ある教授は，他者との関係を築くことの大切さについて話してくれた。",
                    },
                    {
                        "id": "mio_p4_s5",
                        "en": (
                            "Talking to both of them made me realize that university is not just about studying — "
                            "it's also about growing as a person."
                        ),
                        "ja": (
                            "二人と話して，大学は勉強するだけの場所ではなく，人として成長する場所でもあると気づいた。"
                        ),
                    },
                ],
                [
                    {
                        "id": "mio_p5_s1",
                        "en": (
                            "By the end of the day, I felt much more confident that I had found the university where "
                            "I wanted to spend the next four years."
                        ),
                        "ja": (
                            "その日の終わりには，この先4年を過ごしたいと思える大学を見つけたという自信が大いに高まった。"
                        ),
                    },
                    {
                        "id": "mio_p5_s2",
                        "en": (
                            "I left the campus feeling inspired to study as hard as I could for the rest of my senior "
                            "year of high school."
                        ),
                        "ja": (
                            "キャンパスを後にするとき，高校生活の残りはできる限り一生懸命勉強しようという気持ちになった。"
                        ),
                    },
                ],
            ],
            "images": [
                {
                    "paragraph_index": 1,
                    "src": "images/mio_library.png",
                    "position": "float-right",
                    "alt": "Students in the university library",
                    "max_width": 220,
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
                    "Mio's blog post also included students' comments (①~④) describing the events during the open day. "
                    "Put the comments in the order in which the events happened. [ 9 ] → [ 10 ] → [ 11 ] → [ 12 ]"
                ),
                "ja": (
                    "ミオのブログ記事には，オープンキャンパス中の出来事を描写する学生のコメント（①〜④）も載っていた。"
                    "出来事が起きた順にコメントを並べよ。［9］→［10］→［11］→［12］"
                ),
            },
            "choices": [
                {
                    "label": "①",
                    "en": (
                        "I had never thought about how much college changes us. The people around us have a big impact "
                        "on our lives."
                    ),
                    "ja": "大学が自分たちをどれだけ変えるか，考えたことがなかった。周りの人々は自分の人生に大きな影響を与える。",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": (
                        "I started thinking about my future projects! That's way more exciting than my regular homework."
                    ),
                    "ja": "将来のプロジェクトについて考え始めた。いつもの宿題よりずっとわくわくする。",
                    "is_correct": True,
                },
                {
                    "label": "③",
                    "en": (
                        "I was touched by the students concentrating on their studies, surrounded by many books."
                    ),
                    "ja": "多くの本に囲まれ，学業に集中する学生たちに心を打たれた。",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": (
                        "It's also important to be able to have a good time and hang around after a hard day of studying."
                    ),
                    "ja": (
                        "一日一生懸命勉強したあと，楽しく過ごしたりのんびりしたりできることも大切だ。"
                    ),
                    "is_correct": True,
                },
            ],
            "answer": "③②④①",
            "answer_sequence": ["③", "②", "④", "①"],
            "explanation": {
                "quoted_ja": (
                    "正解の順序は ③→②→④→①。③は第2段落の図書館，②は同段落後半の研究室・facilities / independent study projects，"
                    "④は第3段落のアクティビティセンター，①は第4段落の教授・学生との対話・気づきに対応する。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": [
                    "mio_p2_s2",
                    "mio_p2_s5",
                    "mio_p3_s3",
                    "mio_p4_s5",
                ],
                "instructor_note": {
                    "ja": (
                        "ブログの叙述順＝時系列に沿って，各コメントがどの場面の感想かを突き合わせる。"
                        "迷ったら，コメントに出る名詞（books, lab, table tennis, professors）を本文で検索し，出現段落の前後を読み返す。"
                    ),
                    "points": [
                        "③は library … busy students / deeply focused と対応。最初の見学パート。",
                        "②は laboratories・classwork / independent study projects という「これからの課題・研究」の連想に近い。",
                        "④は activity center・relax with friends と対応。寮エリアの見学のあと。",
                        "①は最終段落に近い抽象度（人との関係・成長）。対話シーンのあとの総括に相当。",
                        "コメントの語彙（books, projects, hang around, college changes us）を本文の固有名詞・場所と結びつける練習をすると安定する。",
                        "「施設名が出る順」と「感情の高まり（具体→抽象）」の二筋で検証すると，①を最後に置く理屈が掴みやすい。",
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
                        "id": "mio_q2_stem",
                        "en": (
                            "During the open day, Mio did <strong><u>not</u></strong> [ 13 ]."
                        ),
                        "ja": "オープンキャンパス当日，ミオは<strong><u>しなかった</u></strong>のは［13］である。",
                    }
                ]
            },
            "choices": [
                {
                    "label": "①",
                    "en": "play table tennis",
                    "ja": "卓球をした",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "speak to a professor",
                    "ja": "教授と話した",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "talk to a student",
                    "ja": "在学生と話した",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "visit a laboratory",
                    "ja": "研究室を訪れた",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①。第3段落に卓球台があることは書いてあるが，ミオ本人が打ったとは書かれていない。"
                    "④は第2段落の laboratories，③②は第4段落の students / professors でそれぞれ触れている。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["mio_p3_s3", "mio_p2_s4", "mio_p4_s1"],
                "instructor_note": {
                    "ja": (
                        "NOT 問題＝「書いてあるか」ではなく「主人公がしたと断言できるか」。設備の存在と行為は別。"
                        "Mio / I が主語の文だけを追うと，見学と体験の区別がつきやすい。"
                    ),
                    "points": [
                        "table tennis は activity center の設備の列挙の一部。見学して感動したが，プレーしたとは読めない。",
                        "speak with … professors / current students は第4段落で明示。",
                        "visited the laboratories は第2段落で I also visited。",
                        "設問の not が太字なのは，肯定系の選択肢を選びやすい罠だと知らせる記号。",
                        "同型の NOT 設問は「動詞の体（継続・完了）」に騙されない。例：see a table と play table tennis。",
                    ],
                },
            },
        },
        {
            "question_id": "問3",
            "answer_number": 14,
            "stem": {
                "en": "At the end of the open day, Mio likely learned the university [ 14 ].",
                "ja": "オープンキャンパスの終わりまでに，ミオはその大学が自分に［14］とおそらく理解した。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "lacks good support",
                    "ja": "十分な支援がない",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "offers many sports",
                    "ja": "多くのスポーツを提供している",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "separates different students",
                    "ja": "異なる学生を隔てている",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "suited her well",
                    "ja": "よく合っている",
                    "is_correct": True,
                },
            ],
            "answer": "④",
            "explanation": {
                "quoted_ja": (
                    "正解は④。第1段落で whether it was right for me と動機づけし，最終段落で "
                    "I felt much more confident that I had found the university where I wanted to spend the next four years "
                    "とあり，「自分に合う大学だ」という認識に至っている。①は great support system で否定。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["mio_p1_s3", "mio_p5_s1", "mio_p4_s3"],
                "instructor_note": {
                    "ja": (
                        "infer 系は「直後の心情・評価語」を優先し，選択肢はパラフレーズ（right for me → suit）として読む。"
                        "At the end of the day は「一日の体験の積み重ねのあと」なので，冒頭の不安（whether … right for me）との対比で読む。"
                    ),
                    "points": [
                        "support に関して本文は肯定的なので①は排除。スポーツの網羅的説明（②）はなし。",
                        "寮で各国の学生がシェアしている記述と③は矛盾。",
                        "learned の後ろに続く補語として，感情的まとめ（confident / found … wanted）と整合するのは suit。",
                        "likely は断定ではなく推論なので，選択肢に must / only のような絶対語がなくても④でよい。",
                    ],
                },
            },
        },
    ],
    "vocabulary": {
        "passage": {
            "label_ja": "主な語彙・表現",
            "items": [
                {"en": "campus", "ja": "キャンパス；（大学などの）構内"},
                {"en": "focused", "ja": "集中した；専念した"},
                {"en": "dorm (= dormitory)", "ja": "寮"},
                {"en": "impress", "ja": "〜に強い印象を与える；感銘を与える"},
                {"en": "current", "ja": "現在の；（地位などに）ある"},
                {"en": "struggle", "ja": "苦闘；難局"},
                {"en": "freshman", "ja": "（大学の）1年生"},
                {"en": "feel inspired to do", "ja": "…しようという気になる"},
                {"en": "senior year", "ja": "（高校・大学などの）最終学年"},
                {"en": "impact（問1①）", "ja": "影響"},
                {"en": "hang around（問1④）", "ja": "ぶらぶらする；のんびり過ごす"},
                {"en": "suit（問3④）", "ja": "（人・目的などに）合う；向いている"},
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
