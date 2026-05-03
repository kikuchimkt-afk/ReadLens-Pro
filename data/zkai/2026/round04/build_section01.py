# -*- coding: utf-8 -*-
"""Z会 実戦模試 2026 第4回 第1問 を data.json に書き込む（交換留学生選考のお知らせ）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

QUOTED = "Z会『2026年 共通テスト実戦模試 英語リーディング』第4回 解説冊子"

section_01 = {
    "section_number": 1,
    "title": "第1問",
    "points": 6,
    "points_per_question": 2,
    "description": "短文読解（大学サイト・交換留学選考のお知らせ）",
    "situation": {
        "en": "You visited your university's website and found an interesting notice.",
        "ja": "あなたは自分の通う大学のウェブサイトを訪れ，興味深いお知らせを見つけました。",
    },
    "passages": [
        {
            "id": "exchange_notice",
            "framed": True,
            "title": {
                "en": "Selection of Exchange Students to Go to Canada",
                "ja": "カナダへ行く交換留学生の選考",
            },
            "paragraph_classes": ["para-indent", "para-indent", "para-indent", "para-indent"],
            "paragraphs": [
                [
                    {
                        "id": "ca_intro_s1",
                        "en": (
                            "Our university will send three exchange students to our sister school in Vancouver, "
                            "Canada in August 2026. The schedule for selecting them is as follows."
                        ),
                        "ja": (
                            "本学は2026年8月，カナダのバンクーバーにある姉妹校に3人の交換留学生を派遣する予定です。"
                            "交換留学生の選考スケジュールは以下のとおりです。"
                        ),
                    }
                ],
                {
                    "list_style": "star",
                    "items": [
                        {
                            "id": "ca_nb1",
                            "en": (
                                "You may hand in the application after the Orientation in September."
                            ),
                            "ja": "9月のオリエンテーション後でも応募用紙の提出は可能です。",
                        },
                        {
                            "id": "ca_nb2",
                            "en": (
                                "The interview examination can only be taken by those who pass the written examination."
                            ),
                            "ja": "面接試験は筆記試験を通過した人のみが受けられます。",
                        },
                        {
                            "id": "ca_nb3",
                            "en": (
                                "The final orientation is for the students selected for the program."
                            ),
                            "ja": "最後のオリエンテーションはプログラムに選出された学生が対象です。",
                        },
                    ],
                },
                [
                    {
                        "id": "ca_main_s1",
                        "en": (
                            "Three students will be selected based on their current academic performance, "
                            "their scores on a written English examination, and an interview examination in English."
                        ),
                        "ja": (
                            "3人の学生が現在の学業成績，英語筆記試験の得点，英語面接試験に基づいて選出されます。"
                        ),
                    },
                    {
                        "id": "ca_main_s2",
                        "en": (
                            "Our sister school also runs the same program for students from around the world."
                        ),
                        "ja": "本学の姉妹校はまた，世界中の学生を対象に同じプログラムを行っています。",
                    },
                    {
                        "id": "ca_main_s3",
                        "en": (
                            "Going to our sister school will be a great chance to practice English and make a lot of "
                            "friends from various countries."
                        ),
                        "ja": (
                            "姉妹校に行くことは，英語を練習し，さまざまな国から来た友だちをたくさん作るすばらしい機会となるでしょう。"
                        ),
                    },
                ],
                [
                    {
                        "id": "ca_main_s4",
                        "en": (
                            "We are sure that you will learn many new things. If you have any questions, "
                            "please feel free to ask us. We are looking forward to receiving your applications."
                        ),
                        "ja": (
                            "あなたたちが多くの新しいことを学ぶと確信しています。"
                            "何か質問がありましたら，遠慮なく私たちに聞いてください。"
                            "あなたたちの応募をお待ちしております。"
                        ),
                    },
                    {
                        "id": "ca_main_s5",
                        "en": "To contact us, please click <u>here</u>.",
                        "ja": "私たちに連絡するには<u>こちら</u>をクリックしてください。",
                    },
                ],
            ],
            "table": {
                "after_paragraph": 1,
                "title": {
                    "en": "2025-2026 Exchange Student Selection Schedule",
                    "ja": "2025-2026年 交換留学生選考スケジュール",
                },
                "headers": ["Date", "Events"],
                "rows": [
                    {
                        "cells": ["July 12", "Study Abroad Information Session"],
                        "cells_ja": ["7月12日", "海外留学説明会"],
                    },
                    {
                        "cells": ["September 1", "Orientation for Applicants"],
                        "cells_ja": ["9月1日", "希望者対象オリエンテーション"],
                    },
                    {
                        "cells": ["October 20", "Written English Examination"],
                        "cells_ja": ["10月20日", "英語筆記試験"],
                    },
                    {
                        "cells": ["November 5", "Interview Examination in English"],
                        "cells_ja": ["11月5日", "英語面接試験"],
                    },
                    {
                        "cells": ["March 16", "Orientation for Exchange Students"],
                        "cells_ja": ["3月16日", "交換留学生対象オリエンテーション"],
                    },
                ],
            },
        }
    ],
    "questions": [
        {
            "question_id": "問1",
            "answer_number": 1,
            "stem": {
                "en": "The purpose of this notice is to [ 1 ].",
                "ja": "このお知らせの目的は［1］ことである。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "improve the students' English skills",
                    "ja": "学生の英語のスキルを向上させる",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "inform the students about a schedule change",
                    "ja": "学生にスケジュールの変更について知らせる",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "introduce the sister school to the students",
                    "ja": "姉妹校を学生に紹介する",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "show how to choose students for the program",
                    "ja": "プログラムに参加する学生の選考方法を示す",
                    "is_correct": True,
                },
            ],
            "answer": "④",
            "explanation": {
                "quoted_ja": (
                    "正解は④。タイトルが「カナダへ行く交換留学生の選考」であり，本文は選考スケジュールと選考の過程を示している。"
                    "英語力向上や姉妹校紹介は本文に触れる程度であり，このお知らせ全体の目的としては④が最も適切。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["ca_intro_s1"],
                "instructor_note": {
                    "ja": (
                        "お知らせ全体の purpose は，見出し・リード・スケジュールが一体となって「何を読者にさせたいか」を示す。"
                        "個別の一文（姉妹校の説明など）に引きずられず，募集・選考という機能でまとめられるかを見る。"
                    ),
                    "points": [
                        "selection schedule / applicants / written examination / interview が並ぶ体裁は「選考の仕組み」の説明であることを示す。",
                        "②は変更告知ではなく初出スケジュール。①③は手段・背景レベルで主目的ではない。",
                        "姉妹校紹介や英語学習に触れる文はあるが，スケジュール＋選考基準の塊が本文の主役なので，「留学の魅力」系の①③より「選び方の提示」④が purpose に合う。",
                    ],
                },
            },
        },
        {
            "question_id": "問2",
            "answer_number": 2,
            "stem": {
                "en": "Before going to Canada, the students must [ 2 ].",
                "ja": "カナダへ留学に行く前に，学生たちには［2］ことが求められる。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "get good grades in their classes",
                    "ja": "授業でいい成績を取る",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "have an interview in Japanese and English",
                    "ja": "日本語と英語の面接を受ける",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "study other languages and cultures",
                    "ja": "他の言語と文化を勉強する",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "take a lot of English written tests",
                    "ja": "多くの英語筆記試験を受ける",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①。Three students will be selected based on their current academic performance より，渡航前の条件として"
                    "学業成績が選考要素に含まれる。面接は英語のみ（Japanese は本文なし）。筆記は複数回とは書かれていない。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["ca_main_s1"],
                "instructor_note": {
                    "ja": (
                        "must は「渡航に際して満たすべき条件／選考で問われる要件」と読む。"
                        "本文は Three students will be selected based on ... で選考基準を列挙しているので，その語を選択肢にマッピングする。"
                    ),
                    "points": [
                        "academic performance が①に直結。②は言語がずれる。④は a written examination が一度の選考である。",
                        "オリエンテーションは①の選択肢にも似せられるが，設問は「留学に行く前に必ず〜」と選考要件に寄っており，成績要件が本文で明示されている。",
                        "③の他言語・文化はプログラムの魅力には触れても，must の直接対象としては本文が支持しない。",
                    ],
                },
            },
        },
        {
            "question_id": "問3",
            "answer_number": 3,
            "stem": {
                "en": (
                    "The study abroad program will be a valuable opportunity because the students will [ 3 ]."
                ),
                "ja": (
                    "その留学プログラムは貴重な機会となるだろう。なぜなら，学生たちは［3］ことになるからである。"
                ),
            },
            "choices": [
                {
                    "label": "①",
                    "en": "get important information in the orientation",
                    "ja": "オリエンテーションで重要な情報を得る",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "improve how they express themselves",
                    "ja": "自己表現の仕方を向上させる",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "meet students from other foreign schools",
                    "ja": "他の海外の学校から来た学生に会う",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "stay in Canada for free",
                    "ja": "無料でカナダに滞在する",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。a great chance to practice English and make a lot of friends from various countries が根拠。"
                    "友だちは各国からの学生＝他校・外国の学生に会う機会と読める。無料滞在・自己表現改善は本文にない。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["ca_main_s3"],
                "instructor_note": {
                    "ja": (
                        "because 問題は「貴重な機会」の理由を，プログラム説明のベネフィットから一言で拾うタイプ。"
                        "friends / countries / practice English など並列にある語を切り離さず，設問の空所に入る名詞句として自然なものを選ぶ。"
                    ),
                    "points": [
                        "friends from various countries を foreign schools / countries のイメージにマッピング。",
                        "practice English は②に似せるが，設問は「機会の価値」の理由として③がベストマッチしやすい。",
                        "①オリエンテーションは手続きの話で「機会の本質」より一段手前。④無料滞在は本文が約束していない。",
                    ],
                },
            },
        },
    ],
    "vocabulary": {
        "passage": {
            "label_ja": "主な語彙・表現",
            "items": [
                {"en": "as follows", "ja": "次のとおり"},
                {"en": "applicant", "ja": "応募者"},
                {"en": "interview", "ja": "面接"},
                {"en": "hand in ~", "ja": "〜を提出する"},
                {"en": "application", "ja": "応募書類；申込用紙"},
                {"en": "based on ~", "ja": "〜に基づいて"},
                {"en": "academic performance", "ja": "学業成績"},
                {"en": "run（プログラムを）", "ja": "〜を実施する"},
            ],
        }
    },
}


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    data_path = ROOT / "data.json"
    data = {
        "exam_info": {
            "title": "Z会 共通テスト実戦模試2026年 第4回",
            "publisher": "Z会",
            "year": 2026,
            "round": 4,
            "subject": "英語（リーディング）",
            "time_limit_minutes": 80,
            "total_answer_numbers": 49,
            "implemented_sections": [1],
            "source_pdf_mondai": "第4回_問題.pdf",
            "source_pdf_kaitou": "第4回_解説.pdf",
        },
        "sections": [section_01],
    }
    data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Wrote", data_path)


if __name__ == "__main__":
    main()
