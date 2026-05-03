# -*- coding: utf-8 -*-
"""Z会 実戦模試 2026 第3回 第4問（エッセイ添削・大気汚染 Under One Clean Sky）を data.json にマージする。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUOTED = "Z会『2026年 共通テスト実戦模試 英語リーディング』第3回 解説冊子"

section_04 = {
    "section_number": 4,
    "title": "第4問",
    "points": 12,
    "points_per_question": 3,
    "description": "エッセイ添削（大気汚染・添削コメント）",
    "situation": {
        "en": (
            "In English class you are writing an essay on a social issue you are interested in. "
            "This is your most recent draft. You are now working on revisions based on comments from your teacher."
        ),
        "ja": (
            "英語の授業で，あなたは興味のある社会問題に関するエッセイを書いています。"
            "これはあなたの最新の草稿です。今は先生からのコメントをもとに，推敲に取り組んでいるところです。"
        ),
    },
    "passages": [
        {
            "id": "clean_sky_essay",
            "title": {"en": "Under One Clean Sky", "ja": "一つのきれいな空の下で"},
            "paragraph_classes": ["para-indent", "para-indent", "para-indent", "para-indent", "para-indent"],
            "paragraphs": [
                [
                    {
                        "id": "air_p1_s1",
                        "en": (
                            "I saw a picture of Tokyo in the 1980s in my history class last week. "
                            "I was shocked."
                        ),
                        "ja": "先週の歴史の授業で1980年代の東京の写真を見ました。ショックでした。",
                    },
                    {
                        "id": "air_p1_s2",
                        "en": "The skyline was barely visible because of the air pollution.",
                        "ja": "大気汚染のせいでスカイラインがほとんど見えませんでした。",
                    },
                    {
                        "id": "air_p1_s3",
                        "en": (
                            "A lot has changed since then but I think we need to work harder to solve the problem "
                            "on a global scale. The WHO estimates that almost 7 million people die each year due to "
                            "air pollution! In this essay, I would like to consider what we can do."
                        ),
                        "ja": (
                            "それ以来多くのことが変わりましたが，世界規模でこの問題を解決するために私たちはもっと努力する必要があると思います。"
                            "WHOは，大気汚染が原因で毎年ほぼ700万人が亡くなっていると推定しています！"
                            "このエッセイでは，私たちにできることを考えたいです。"
                        ),
                    },
                ],
                [
                    {
                        "id": "air_p2_s1",
                        "en": (
                            "First, there needs to be a bigger move towards electric cars and buses, since air "
                            "pollution is mainly caused by gasoline-powered cars."
                        ),
                        "ja": (
                            "第一に，大気汚染は主にガソリン車によって起こるので，電気自動車や電気バスへのより大きな転換が必要です。"
                        ),
                    },
                    {
                        "id": "air_p2_s2",
                        "en": "Take a look around and you will see the main reason.",
                        "ja": "周りを見渡せば，その主な理由がわかるでしょう。",
                        "comment_marker": "(1)",
                        "marker_position": "before",
                        "marker_type": "caret",
                    },
                    {
                        "id": "air_p2_s3",
                        "en": (
                            "Because there are not enough charging stations, buying an electric vehicle (EV) is not "
                            "practical for most people."
                        ),
                        "ja": (
                            "充電ステーションが十分にないため，ほとんどの人にとって電気自動車（EV）を購入することは現実的ではありません。"
                        ),
                    },
                    {
                        "id": "air_p2_s4",
                        "en": "I think the government needs to make EVs the cheaper and more convenient option.",
                        "ja": "政府はEVをより安価で便利な選択肢にする必要があると思います。",
                    },
                ],
                [
                    {
                        "id": "air_p3_s1",
                        "en": (
                            "Secondly, Japan needs to follow the lead of other environmentally advanced countries "
                            "and introduce designated areas called LEZs, Low Emission Zones."
                        ),
                        "ja": (
                            "第二に，日本も他の環境先進国に倣って，LEZ（低排出ゾーン）と呼ばれる指定地域を導入する必要があります。"
                        ),
                    },
                    {
                        "id": "air_p3_s2",
                        "en": (
                            "Basically, drivers of vehicles that don't meet the low emission standards have to pay "
                            "money to enter the LEZs."
                        ),
                        "ja": (
                            "基本的に，低排出ガス基準を満たさない車の運転者はLEZに入るためにお金を払わなければなりません。"
                        ),
                    },
                    {
                        "id": "air_p3_s3",
                        "en": (
                            "At present the Japanese policy seems to be to just hope that people buy eco-friendly cars."
                        ),
                        "ja": "現在の日本の政策は，人々がエコカーを購入することを願うことだけのようです。",
                    },
                    {
                        "id": "air_p3_s4",
                        "en": "European cities are taking positive action to encourage people to do more.",
                        "ja": "ヨーロッパの都市は，人々がもっと行動するように，積極的な措置を講じています。",
                        "comment_marker": "(2)",
                        "marker_position": "before",
                        "marker_type": "caret",
                    },
                ],
                [
                    {
                        "id": "air_p4_s1",
                        "en": "Finally, it's time to show that you care!",
                        "ja": "最後に，今こそ，あなたが関心をもっていると示す時です！",
                        "comment_marker": "(3)",
                        "marker_type": "caret",
                        "underline_word": "it's time to show that you care!",
                    },
                    {
                        "id": "air_p4_s2",
                        "en": "We need to plant more trees in city centers.",
                        "ja": "市街地に樹木をより多く植える必要があります。",
                    },
                    {
                        "id": "air_p4_s3",
                        "en": (
                            "As well as helping reduce air pollution by sucking up carbon dioxide, they would also "
                            "provide shade for shoppers on hot summer days."
                        ),
                        "ja": (
                            "二酸化炭素を吸い上げて大気汚染を減らすのに役立つだけでなく，"
                            "暑い夏の日に買い物客に木陰を提供してくれるでしょう。"
                        ),
                    },
                ],
                [
                    {
                        "id": "air_p5_s1",
                        "en": (
                            "In conclusion, although Japan is a lot cleaner than it was in the past, we still must "
                            "play our part as global citizens."
                        ),
                        "ja": (
                            "結論として，日本は過去に比べればかなり汚染がなくなりましたが，"
                            "それでも私たちは地球市民としての役割を果たさなければなりません。"
                        ),
                    },
                    {
                        "id": "air_p5_s2",
                        "en": (
                            "We should promote the use of electric cars, know more about controlling toxic gas, "
                            "and work on further greening our cities."
                        ),
                        "ja": (
                            "電気自動車の普及を促進し，有毒ガスの抑制についてもっと知り，さらに都市の緑化に取り組むべきです。"
                        ),
                        "comment_marker": "(4)",
                        "marker_type": "caret",
                        "underline_word": "know more about",
                    },
                    {
                        "id": "air_p5_s3",
                        "en": "What we do here affects the entire global eco-system.",
                        "ja": "私たちがここで行うことは，地球の生態系全体に影響を及ぼすのです。",
                    },
                ],
            ],
            "margin_comments": [
                {
                    "marker": "(1)",
                    "en": "You are missing something here. Add more information between the two sentences to connect them.",
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
                "title_en": "Overall Comments:",
                "title_ja": "総合的なコメント：",
                "en": (
                    "Overall, it is well-written. It would be perfect with a few minor revisions. "
                    "(I agree with your suggestion of creating LEZs in Japan! 😊)"
                ),
                "ja": (
                    "全体としてよく書けています。あと少し修正すれば完璧でしょう。"
                    "（日本でもLEZをつくるというあなたの提案に同意します！😊）"
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
                    "en": "As of 2023, electric cars were cheaper than gasoline cars.",
                    "ja": "2023年時点で，電気自動車はガソリン自動車より安価だった。",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "As of 2023, most people liked to drive electric cars.",
                    "ja": "2023年時点で，ほとんどの人は電気自動車を運転したがっていた。",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "As of 2023, only 3% of cars in Japan were electric.",
                    "ja": "2023年時点で，日本における電気自動車は3%しかなかった。",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "As of 2023, taxi companies were already using electric cars.",
                    "ja": "2023年時点で，タクシー会社はすでに電気自動車を使っていた。",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。(1)の位置は，より電気自動車への転換が必要だと述べたあと，"
                    "\"Take a look around and you will see the main reason.\" と続く直前である。"
                    "「周りを見れば主な理由がわかる」＝まだガソリン車がほとんどという現状を示す具体情報として，"
                    "日本のEV割合が3%しかないという③が最も自然につながる。①は政府がEVをより安くすべきとあるため矛盾しやすい。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["air_p2_s1", "air_p2_s2"],
                "instructor_note": {
                    "ja": (
                        "文挿入は「前後の論理の隙間」を埋める。次文の the main reason が指す内容を具体化できるかが鍵。"
                        "Take a look around が読者への見立てになっているので，その「見え方」を数字か光景かで示せるかが正誤の分かれ目。"
                    ),
                    "points": [
                        "②④は「好き・タクシー」で主因の可視化として弱い。①は価格関係が本文の government needs to make EVs cheaper と食い違いやすい。",
                        "データ（％）で「まだEVが少ない」を示すと，充電インフラ不足・非現実的という後続とも一本につながる。",
                        "コメント(1) が要求するのは追加情報なので，接続詞だけでなく「エビデンスになる一文」かどうかで選ぶ。",
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
                    "en": "In contrast",
                    "ja": "その一方で（対照的に）",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "In particular",
                    "ja": "特に",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "Nevertheless",
                    "ja": "それにもかかわらず",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "Otherwise",
                    "ja": "そうでなければ",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①。直前は日本の政策が eco-friendly cars を買うよう「願うだけ」の受動的な話で，"
                    "直後は European cities の積極的な行動である。二者は対比なので In contrast が最適。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["air_p3_s3", "air_p3_s4"],
                "instructor_note": {
                    "ja": (
                        "接続詞は「前後の意味関係」を決め打ちする。日本↔欧州の政策スタンスの対照がポイント。"
                        "hope that people buy〜（受動的）と taking positive action（能動的）の語の対比をマーカーにすると In contrast が選びやすい。"
                    ),
                    "points": [
                        "In particular は具体例の絞り込み，Nevertheless は逆接だがここは「対比」が核。",
                        "Otherwise は「そうでないと〜ない」条件めいた用法になりやすく，この並びには馴染みにくい。",
                        "対比なら By contrast / Meanwhile なども同系統。テストでは選択肢語の「対比 vs 追加 vs 逆接」の三分類が早い。",
                    ],
                },
            },
        },
        {
            "question_id": "問3",
            "answer_number": 17,
            "stem": {
                "en": "Based on comment (3), which is the most appropriate way to rewrite the topic sentence? [ 17 ]",
                "ja": "コメント(3)に基づいて，主題文を書き換えるのに最も適当なものはどれか。［17］",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "greener means cleaner",
                    "ja": "緑化は（空気を）より清浄にする",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "let's stop driving cars",
                    "ja": "車の運転をやめよう",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "no more shopping in summer",
                    "ja": "夏の買い物をやめよう",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "save the planet, take the bus",
                    "ja": "地球を守ろう，バスに乗ろう",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①。段落本文は plant more trees と汚染削減・二酸化炭素の話であり，"
                    "主題文は「緑化が清浄化につながる」方向が整合的。②〜④は段落の具体的内容とズレる。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["air_p4_s2", "air_p4_s3"],
                "instructor_note": {
                    "ja": (
                        "リライト問題は段落の主題一致度がすべて。本文の名詞・動詞の束を拾ってパラフレーズ候補を検証する。"
                        "コメント(3) が topic sentence と書いてあるので，見出し調のフレーズではなく「この段落で語っている因果」を一文で言えるかが焦点。"
                    ),
                    "points": [
                        "trees / reduce air pollution / carbon dioxide に直結するのは green と clean の対応。",
                        "バス・運転中止・買い物は別段落の論点に寄りやすい罠。",
                        "it's time to show that you care は感情のスローガンに見えるので，本文の植物・CO2・汚染の語と結びつくまで書き換え候補を絞る。",
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
                    "en": "become more useful to the planet by",
                    "ja": "もっと地球の役に立つようになるために",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "create new vehicles which are suitable for",
                    "ja": "〜に適した新しい車を作ることによって",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "keep up with other environmentally advanced countries in",
                    "ja": "有毒ガスの抑制において他の環境先進国に遅れを取らないようにする",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "make more financial contributions for the purpose of",
                    "ja": "〜のためにさらなる財政貢献をする",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。(4)は結論部の並列のひとつで，第2案のEV，第4案の緑化のあいだに入り，"
                    "第3段落（LEZ・環境先進国との比較・規制）を要約すべき箇所。"
                    "know more about は弱いので，keep up with ... in controlling toxic gas のように「遅れを取らない」方向が本文と一致する。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["air_p3_s1", "air_p5_s2"],
                "instructor_note": {
                    "ja": (
                        "言い換えは「前後の段落役割」。結論の中間項が第3段落の要約になっているかを確認する。"
                        "In conclusion の並列はしばしば First… Secondly… Finally… と対応するので，空所が「第いくつの提案か」を数える。"
                    ),
                    "points": [
                        "promote EV は第2段落，greening は第4段落に対応するイメージで，残るスロットは第3段落（LEZ・欧州比較）。",
                        "①②④は本文の動線（規制・追随・比較）と語彙が合いにくい。",
                        "know more about は「情報を増やす」という弱い動詞なので，規制・追随という具体的政策に差し替えるのがコメント(4) の意図。",
                        "LEZ / emission standards / European cities など第3段落の語を一つでも含む選択肢を優先してもよい。",
                    ],
                },
            },
        },
    ],
    "vocabulary": {
        "passage": {
            "label_ja": "主な語彙・表現",
            "items": [
                {"en": "skyline", "ja": "スカイライン（空を背景とした建物のシルエット）"},
                {"en": "barely", "ja": "ほとんど〜ない"},
                {"en": "visible", "ja": "目に見える"},
                {"en": "global scale", "ja": "世界規模"},
                {"en": "estimate that ...", "ja": "…と推定する"},
                {"en": "move towards ~", "ja": "〜への移行〔変化〕"},
                {"en": "cause", "ja": "〜を引き起こす"},
                {"en": "practical", "ja": "現実的な"},
                {"en": "designated", "ja": "指定された"},
                {"en": "emission", "ja": "排出（量）"},
                {"en": "basically", "ja": "基本的に"},
                {"en": "standard", "ja": "基準"},
                {"en": "policy", "ja": "政策"},
                {"en": "suck up ~", "ja": "〜を吸い上げる"},
                {"en": "carbon dioxide", "ja": "二酸化炭素"},
                {"en": "global citizen", "ja": "地球市民"},
                {"en": "toxic", "ja": "有毒な"},
                {"en": "entire ~", "ja": "〜全体の"},
                {"en": "minor", "ja": "ささいな；ちょっとした"},
                {"en": "as of ~（問1）", "ja": "〜の時点で"},
                {"en": "in contrast（問2①）", "ja": "対照的に；その一方で"},
                {"en": "in particular（問2②）", "ja": "特に"},
                {"en": "nevertheless（問2③）", "ja": "それにもかかわらず"},
                {"en": "keep up with ~（問4③）", "ja": "〜に遅れずについていく"},
                {"en": "contribution（問4④）", "ja": "貢献"},
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
