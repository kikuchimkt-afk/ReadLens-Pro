# -*- coding: utf-8 -*-
"""Z会 実戦模試 2026 第5回 第1問（地元フードフェス・お知らせ）を data.json に書き込む。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUOTED = "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子"

section_01 = {
    "section_number": 1,
    "title": "第1問",
    "points": 6,
    "points_per_question": 2,
    "description": "短文読解（町の英語サイト・フードフェス募集）",
    "situation": {
        "en": "You visited your town's English website written by a British person and found this notice.",
        "ja": "あなたは英国人が書いた，自分の住む町の英語版ウェブサイトを見て，このお知らせを見つけました。",
    },
    "passages": [
        {
            "id": "food_festival_notice",
            "framed": True,
            "title": {
                "en": "<strong><u>Call for Chefs and Volunteers: Local Food Festival</u></strong>",
                "ja": "シェフとボランティアを募集：地元のフードフェスティバル",
            },
            "paragraph_classes": [
                "para-indent",
                "para-indent",
                "para-indent",
            ],
            "paragraphs": [
                [
                    {
                        "id": "ff_p1_s1",
                        "en": "What is your favourite local dish?",
                        "ja": "あなたのお気に入りの郷土料理は何ですか。",
                    },
                    {
                        "id": "ff_p1_s2",
                        "en": "We are planning a food festival with a cooking competition.",
                        "ja": "私たちは料理のコンテスト付きのフードフェスティバルを企画しています。",
                    },
                    {
                        "id": "ff_p1_s3",
                        "en": "We are looking for local participants who have confidence in their cooking ability.",
                        "ja": "料理への自信がある地元の参加者を募集しています。",
                    },
                    {
                        "id": "ff_p1_s4",
                        "en": "Trials for the competition will be held on the 15th of June.",
                        "ja": "コンテストの予選は6月15日に行われます。",
                    },
                    {
                        "id": "ff_p1_s5",
                        "en": (
                            "Finalists will cook their dishes to be judged in a live competition at the festival "
                            "on the 4th of August."
                        ),
                        "ja": (
                            "決勝進出者は8月4日のフェスティバルで実演のコンテストに料理を作り，審査を受けることになります。"
                        ),
                    },
                    {
                        "id": "ff_p1_s6",
                        "en": (
                            "Everyone coming to the festival will be able to taste the dishes and vote for their favourite dishes."
                        ),
                        "ja": (
                            "フェスティバルに来た人は誰でも料理を味わい，お気に入りの料理に投票することができます。"
                        ),
                    },
                    {
                        "id": "ff_p1_s7",
                        "en": "The winner will be announced at the evening party.",
                        "ja": "優勝者は夕方のパーティーで発表されます。",
                    },
                ],
                [
                    {
                        "id": "ff_p2_s1",
                        "en": (
                            "We are also looking for volunteers to help set up tables and chairs, move cooking equipment, "
                            "and count the votes for the competition."
                        ),
                        "ja": (
                            "また，テーブルと椅子の設置，調理器具の移動，コンテストの票の集計を手伝ってくれるボランティアも募集しています。"
                        ),
                    }
                ],
                [
                    {
                        "id": "ff_p3_s1",
                        "en": (
                            "Click <u>here</u> to download detailed information and requirements for chefs and volunteers "
                            "at the festival."
                        ),
                        "ja": (
                            "フェスティバルにおけるシェフとボランティアの詳細情報と応募条件は<u>こちら</u>からダウンロードしてください。"
                        ),
                    },
                    {
                        "id": "ff_p3_s2",
                        "en": "If you have any questions, please call 0XX-85XX-11XX.",
                        "ja": "質問がある場合は，0XX-85XX-11XXまでお電話ください。",
                    },
                ],
            ],
            "table": {
                "after_paragraph": 2,
                "title": {
                    "en": "Schedule",
                    "ja": "スケジュール",
                },
                "headers": ["Date", "Events"],
                "rows": [
                    {
                        "cells": [
                            "20th ~ 21st May",
                            "Registration day at the community centre 10 a.m. - 3 p.m.",
                        ],
                        "cells_ja": [
                            "5月20日〜21日",
                            "地域センターでの登録日　午前10時〜午後3時",
                        ],
                    },
                    {
                        "cells": ["15th June", "Competition Trials"],
                        "cells_ja": ["6月15日", "コンテスト予選"],
                    },
                    {
                        "cells": ["30th June", "Announcement of finalists"],
                        "cells_ja": ["6月30日", "決勝進出者の発表"],
                    },
                    {
                        "cells": ["3rd August", "Volunteers set up the festival"],
                        "cells_ja": ["8月3日", "ボランティアによる設営"],
                    },
                    {
                        "cells": [
                            "4th August",
                            "Food Festival Day 11 a.m. - 4 p.m.\nEvening Party for participants and awarding of prizes",
                        ],
                        "cells_ja": [
                            "8月4日",
                            "フードフェスティバル当日　午前11時〜午後4時\n参加者向け夕方のパーティーと表彰",
                        ],
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
                "en": "The purpose of this notice is to find people from the local town to [ 1 ].",
                "ja": "このお知らせの目的は，地元の町の人々のうち，［1］人を見つけることである。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "donate food to a school",
                    "ja": "学校に食料を寄付する",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "take cooking lessons",
                    "ja": "料理の講習を受ける",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "take part in an event",
                    "ja": "催し物に参加する",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "volunteer for a charity",
                    "ja": "慈善のためにボランティアをする",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。タイトルと本文がシェフ・参加者・ボランティアを募り，料理コンテストやフェスティバルという催しへの参加を求めている。"
                    "①②④は本文の募集目的と合わない。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["ff_p1_s2", "ff_p1_s3", "ff_p2_s1"],
                "instructor_note": {
                    "ja": (
                        "本文全体が「フードフェスとコンテストに関わってほしい」という募集であることに立ち返る。"
                        "purpose（このお知らせの目的）は，見出しの Call for〜 と第１〜２段落の looking for の対象をひとまとめにして捉える。"
                    ),
                    "points": [
                        "シェフ募集・一般参加者・ボランティアの三本柱があり，いずれも催し（コンテスト／当日運営）にかかわる採用である。",
                        "④ volunteer は「慈善団体のため」限定ではなく，フェス運営の手伝いも含む語として広く使われるため，本文のボランティア項目だけを見て charity と決めつけると落とし穴。",
                        "①寄付・②料理教室は本文の中心（料理を披露する催し）とズレやすい。正解の take part in an event は企画全体を包む言い方として妥当。",
                    ],
                },
            },
        },
        {
            "question_id": "問2",
            "answer_number": 2,
            "stem": {
                "en": "During the festival all of the attendees will be able to [ 2 ].",
                "ja": "フェスティバルの間は，参加者全員が［2］ことができるだろう。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "award prizes to each other",
                    "ja": "互いに賞を与える",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "cook food at the event",
                    "ja": "催し物で料理を作る",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "learn how to make healthy food",
                    "ja": "健康的な食べ物の作り方を習う",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "vote for their favourite recipe",
                    "ja": "気に入ったレシピに投票する",
                    "is_correct": True,
                },
            ],
            "answer": "④",
            "explanation": {
                "quoted_ja": (
                    "正解は④。第1段落に Everyone coming to the festival will be able to taste the dishes and vote for "
                    "their favourite dishes とある。attendees は coming to the festival に対応，recipe は dishes の言い換えとして読める。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["ff_p1_s6"],
                "instructor_note": {
                    "ja": (
                        "設問の During the festival / all of the attendees は，特に来場者全員に当てはまる行動を聞いている。"
                        "本文で「来た人は誰でも（Everyone coming）」と明言された文に当たりを付ける。"
                    ),
                    "points": [
                        "vote for their favourite (dishes) は taste the dishes と同じ Everyone 節にぶら下がり，来場者全員の権利として一貫している。",
                        "② cook at the event は最終的に審査を受けるのは finalists なので，一般来場者の全員に当てはまると言い切れない。",
                        "①授与は主催・審査側，③健康食品の作り方は本文に根拠がない。",
                    ],
                },
            },
        },
        {
            "question_id": "問3",
            "answer_number": 3,
            "stem": {
                "en": "People who want to take part in the cooking competition must [ 3 ].",
                "ja": "料理コンテストに参加したい人は，［3］しなくてはならない。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "attend a cooking trial",
                    "ja": "料理の予選に参加する",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "click the link to register",
                    "ja": "登録するためにリンクをクリックする",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "cook more than one dish",
                    "ja": "2品以上の料理を作る",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "help set up tables and chairs",
                    "ja": "テーブルと椅子を並べるのを手伝う",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①。本文はコンテスト予選を6月15日に行うとあり，スケジュール表にも Competition Trials とある。"
                    "リンクは詳細ダウンロード用で登録そのものとは限らない。④はボランティアの役割。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["ff_p1_s4"],
                "instructor_note": {
                    "ja": (
                        "must は「参加条件として必須の手続き・行動」を問う。コンテスト参加希望者向けの必須工程を，本文とスケジュール表の両方で確認する。"
                    ),
                    "points": [
                        "本文の Trials for the competition と表の Competition Trials を突き合わせ，予選日（6月15日）に立ち会う＝参加の前提条件と読む。",
                        "Click here は詳細ダウンロード用で，登録そのものの手続きを直接指すとは限らない。must の根拠として弱い。",
                        "④はボランティア向け，③は本文にない課題数の制限。",
                    ],
                },
            },
        },
    ],
    "vocabulary": {
        "passage": {
            "label_ja": "主な語彙・表現",
            "items": [
                {"en": "call for ~", "ja": "〜の要請；〜のお願い"},
                {"en": "local dish", "ja": "郷土料理"},
                {"en": "participant", "ja": "参加者"},
                {"en": "confidence", "ja": "自信"},
                {"en": "live", "ja": "生の；実演の"},
                {"en": "vote", "ja": "投票する；票"},
                {"en": "award", "ja": "〜（賞など）を与える"},
                {"en": "prize", "ja": "賞；賞品；賞金"},
                {"en": "donate（問1①）", "ja": "〜を寄付する"},
                {"en": "attendee（問2）", "ja": "出席者；参加者"},
            ],
        }
    },
}


def main():
    data_path = ROOT / "data.json"
    base = {
        "exam_info": {
            "title": "Z会 共通テスト実戦模試2026年 第5回",
            "publisher": "Z会",
            "year": 2026,
            "round": 5,
            "subject": "英語（リーディング）",
            "time_limit_minutes": 80,
            "total_answer_numbers": 49,
            "implemented_sections": [],
            "source_pdf_mondai": "第5回_問題.pdf",
            "source_pdf_kaitou": "第5回_解説.pdf",
        },
        "sections": [],
    }
    if data_path.exists():
        base = json.loads(data_path.read_text(encoding="utf-8"))
    base["sections"] = [s for s in base["sections"] if s.get("section_number") != 1]
    base["sections"].append(section_01)
    base["sections"].sort(key=lambda s: s.get("section_number", 0))
    impl = base.setdefault("exam_info", {}).setdefault("implemented_sections", [])
    if 1 not in impl:
        impl.append(1)
        impl.sort()
    data_path.write_text(json.dumps(base, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Merged section 1 →", data_path)


if __name__ == "__main__":
    main()
