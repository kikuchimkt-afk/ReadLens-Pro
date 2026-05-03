# -*- coding: utf-8 -*-
"""Z会 実戦模試 2026 第3回 第1問 を data.json に書き込む（夜市 Night Market）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

section_01 = {
    "section_number": 1,
    "title": "第1問",
    "points": 6,
    "points_per_question": 2,
    "description": "短文読解（旅行サイトのお知らせ）",
    "situation": {
        "en": (
            "You visited a travel website for international tourists and found this notice "
            "written by a British author about an event in your city."
        ),
        "ja": (
            "あなたは海外旅行者向けの旅行サイトを訪れ，あなたの街で開催されるイベントについて"
            "英国人の著者が書いたこの通知を見つけました。"
        ),
    },
    "passages": [
        {
            "id": "night_market_notice",
            "framed": True,
            "title": {"en": "Night Market", "ja": "夜市"},
            "paragraphs": [
                [
                    {
                        "id": "nm_s1",
                        "en": (
                            "Experience the sights, sounds, and tastes of our city at the Night Market in East Park, "
                            "held once a month during the summer."
                        ),
                        "ja": (
                            "夏の間，東公園で月に一度開かれる夜市で，この街の見どころ，音，味を体験してください。"
                        ),
                    },
                    {
                        "id": "nm_s2",
                        "en": (
                            "Enjoy an evening walk out of the midday heat while you view the fruits and vegetables "
                            "our area has to offer."
                        ),
                        "ja": (
                            "真昼の暑さを逃れて夕暮れの散歩を楽しみながら，この地域が誇る青果をご覧ください。"
                        ),
                    },
                    {
                        "id": "nm_s3",
                        "en": (
                            "You can also see art, clothing, speciality foods, and other beautiful items "
                            "made by local people."
                        ),
                        "ja": (
                            "地元の人々が手がけた美術品，衣類，名物の食品，そのほかすばらしい品々もご覧いただけます。"
                        ),
                    },
                    {
                        "id": "nm_s4",
                        "en": (
                            "With special events arranged by local organisations every night, the Night Market is also "
                            "the perfect place to find out about local hot spots and entertainment."
                        ),
                        "ja": (
                            "毎晩地元の団体が企画する特別イベントもあり，夜市は人気スポットや娯楽を知るのにも最適の場所です。"
                        ),
                    },
                ],
                [
                    {
                        "id": "nm_b1",
                        "en": "Food stands are open every night of the market from 6 p.m. to 10 p.m.",
                        "ja": "夜市が開いている夜は毎晩，屋台は午後6時から午後10時まで営業しています。",
                        "role": "bullet",
                    },
                    {
                        "id": "nm_b2",
                        "en": (
                            "All demonstrations and performances are free of charge and will take place on the stage "
                            "in East Park."
                        ),
                        "ja": (
                            "すべての実演と演技は無料で，東公園のステージで行われます。"
                        ),
                        "role": "bullet",
                    },
                    {
                        "id": "nm_b3",
                        "en": (
                            "No pets of any kind are allowed at the market, even on leads or in carriers."
                        ),
                        "ja": (
                            "夜市にはどのようなペットも持ち込めません。ひもでつながれていても，キャリアに入っていてもです。"
                        ),
                        "role": "bullet",
                    },
                ],
                [
                    {
                        "id": "nm_f1",
                        "en": "For information on directions and parking, please click here.",
                        "ja": "道順と駐車場については，こちらをクリックしてください。",
                    }
                ],
            ],
            "table": {
                "after_paragraph": 1,
                "title": {"en": "Event Schedule", "ja": "イベントスケジュール"},
                "headers": ["Date", "Events"],
                "rows": [
                    {
                        "cells": [
                            "23rd May",
                            (
                                "7 p.m. : Enjoy risotto from Giulia's, a local Italian restaurant\n"
                                "8:30 p.m. : A comedy show performed by local university students"
                            ),
                        ],
                        "cells_ja": [
                            "5月23日",
                            (
                                "午後7時：地元のイタリアンレストラン Giulia's のリゾット\n"
                                "午後8時30分：地元の大学生によるお笑いショー"
                            ),
                        ],
                    },
                    {
                        "cells": [
                            "23rd June",
                            "7 p.m. : A drumming and dance performance by the group Rhythm",
                        ],
                        "cells_ja": [
                            "6月23日",
                            "午後7時：グループ Rhythm による太鼓とダンスの演技",
                        ],
                    },
                    {
                        "cells": [
                            "23rd July",
                            (
                                "7 p.m. : Enjoy sushi from Morita, a local Japanese restaurant\n"
                                "8:30 p.m. : Japanese pop music concert by Minato"
                            ),
                        ],
                        "cells_ja": [
                            "7月23日",
                            (
                                "午後7時：地元の日本食レストラン Morita の寿司\n"
                                "午後8時30分：Minato による J-POP コンサート"
                            ),
                        ],
                    },
                    {
                        "cells": [
                            "23rd August",
                            "7 p.m. : Cooking demonstration by M's Bakery",
                        ],
                        "cells_ja": [
                            "8月23日",
                            "午後7時：M's Bakery による料理実演",
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
                "en": "The purpose of this notice is to let people know about [ 1 ].",
                "ja": "この通知の目的は，人々に［1］ことを知らせることである。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "a way to experience the local culture",
                    "ja": "地域文化を体験するひとつの方法",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "an annual fruit festival at East Park",
                    "ja": "東公園で開かれる年に一度の果物祭り",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "the opening of a new supermarket",
                    "ja": "新しいスーパーマーケットの開店",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "tips for walking safely in the city at night",
                    "ja": "夜の街を安全に歩くためのコツ",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①。通知の第1文に Experience the sights, sounds, and tastes of our city とあり，"
                    "地域の見どころ・音・味を体験する機会として夜市を紹介している。②は果物祭りと決めつけられない。"
                    "③④は本文にない。"
                ),
                "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第3回 解説冊子",
                "evidence_sentences": ["nm_s1"],
                "instructor_note": {
                    "ja": (
                        "purpose（目的）を問う典型。通知の第1文の動詞・目的語（Experience the sights, sounds, and tastes of our city）が，この文書全体の「何のための案内か」の芯になる。"
                        "選択肢はすべて「それっぽいテーマ」を運ぶので，単語の連想（fruit, night, tip など）で決めず，必ずリード文へ立ち返る。"
                    ),
                    "points": [
                        "②：fruit や vegetables は出てくるが，annual fruit festival とは断定できない。East Park / once a month は場所・頻度であって目的そのものではない。",
                        "③：新規店舗のオープンは本文にない。",
                        "④：tip for ~ は「歩行のコツ」に取れるが，この通知の主眼は夜市という文化体験の紹介。テーマのすり替えに注意。",
                        "正解候補を絞ったら，第1文に戻り \"sights, sounds, and tastes\" と選択肢 a way to experience the local culture を照合する。",
                        "見出しが Night Market であっても purpose は「夜市そのもの」ではなく，その背景にある体験の提案であると捉えるとブレにくい。",
                    ],
                },
            },
        },
        {
            "question_id": "問2",
            "answer_number": 2,
            "stem": {
                "en": "On one evening at the Night Market, visitors will [ 2 ].",
                "ja": "夜市が開かれている夜のひとつにおいて，訪問者は［2］だろう。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "enjoy an Italian music show and eat risotto",
                    "ja": "イタリアの音楽ショーを楽しみ，リゾットを食べる",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "enter a dance contest and watch some musical acts",
                    "ja": "ダンスコンテストに参加し，いくつかの音楽番組を見る",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "meet a chef and learn how to play the drums",
                    "ja": "シェフに会い，太鼓の打ち方を学ぶ",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "see a funny performance and try a local restaurant's food",
                    "ja": "お笑いの演技を見て，地元のレストランの料理を試す",
                    "is_correct": True,
                },
            ],
            "answer": "④",
            "explanation": {
                "quoted_ja": (
                    "正解は④。5月23日のスケジュールに risotto from Giulia's（地元イタリアンレストランの料理）と "
                    "comedy show（お笑いショー）があり，④と一致。①は music show ではない。②③はスケジュールにない活動。"
                ),
                "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第3回 解説冊子",
                "instructor_note": {
                    "ja": (
                        "表の「同じ日付の行」だけを根拠にする。別週のイベント（音楽・ダンス等）と混ぜない。"
                        "日本語選択肢は英語より情報が圧縮されているので，料理名・パフォーマンスの種類がその夜の行に明示されているかを照合する。"
                    ),
                    "points": [
                        "5月23日行：comedy show ↔ funny performance，risotto from Giulia's（地元イタリアン）↔ try a local restaurant's food。",
                        "イタリア「音楽」リゾット、ダンスコンテスト、太鼓と言い切られている夜は別日の罠。",
                        "正解を得たら，日本語訳の「お笑い」と「地元店の料理」が原文の comedy / local restaurant にきちんと対応しているか最終確認。",
                        "On one evening は「どこか一夜」なので，表のすべての日をなめる必要はなく，設問が暗に示す日付に注目する（本問は該当行が明示されている前提）。",
                    ],
                },
            },
        },
        {
            "question_id": "問3",
            "answer_number": 3,
            "stem": {
                "en": "If you have a dog and want to go to this event, you will need to [ 3 ].",
                "ja": "犬を飼っていてこのイベントに行きたい場合，あなたは［3］必要がある。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "go between 6 and 8 p.m. only",
                    "ja": "午後6時から8時の間にだけ行く",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "keep away from the stage",
                    "ja": "ステージから離れておく",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "leave your dog at home",
                    "ja": "犬を家に置いておく",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "put your dog on a lead",
                    "ja": "犬をひもにつなぐ",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。箇条書き第3点に No pets of any kind are allowed とあり，"
                    "even on leads or in carriers と補足されているので，犬を連れて行けない＝家に置くしかない。④は本文で否定。"
                ),
                "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第3回 解説冊子",
                "evidence_sentences": ["nm_b3"],
                "instructor_note": {
                    "ja": (
                        "No pets of any kind are allowed の直後 even on leads or in carriers は「連れてすらダメ」という極端な例示。譲歩が利く文ではない。"
                        "条件問題は，ルール文を肯定形・否定形に言い換えたときにどの選択肢だけが必然的になるかまで落とし込む。"
                    ),
                    "points": [
                        "④：ひも（lead）の有無は議論の俎上にすら乗らない。本文は「いかなるペットも不可」。",
                        "①：6–10 p.m. は屋台の営業時間。ペット禁止の条件ではない。",
                        "②：ステージから離れよの根拠はない。",
                        "正解は「連れて行かない＝家に置く」以外の行動に整理しにくい、と考えると③に落ち着く。",
                        "have a dog が惹起する連想（ひもにつなぐ・散歩時間に行く）を本文より優先しない。",
                    ],
                },
            },
        },
    ],
    "vocabulary": {
        "passage": {
            "label_ja": "主な語彙・表現",
            "items": [
                {"en": "midday", "ja": "真昼；正午（⇔ midnight）"},
                {"en": "speciality", "ja": "名物（料理）；特産品（米国英語では specialty）"},
                {"en": "stand", "ja": "売店；露店"},
                {"en": "on a lead", "ja": "（飼い犬などが）ひもでつながれた"},
                {"en": "carrier", "ja": "運ぶための入れ物"},
                {"en": "tip for ~（問1④）", "ja": "〜のコツ；秘訣"},
            ],
        }
    },
}


def main():
    data_path = ROOT / "data.json"
    data = {
        "exam_info": {
            "title": "Z会 共通テスト実戦模試2026年 第3回",
            "publisher": "Z会",
            "year": 2026,
            "round": 3,
            "subject": "英語（リーディング）",
            "time_limit_minutes": 80,
            "total_answer_numbers": 49,
            "implemented_sections": [1],
            "source_pdf_mondai": "第3回_問題.pdf",
            "source_pdf_kaitou": "第3回_解説.pdf",
        },
        "sections": [section_01],
    }
    data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Wrote", data_path)


if __name__ == "__main__":
    main()
