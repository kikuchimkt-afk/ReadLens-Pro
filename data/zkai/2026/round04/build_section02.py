# -*- coding: utf-8 -*-
"""Z会 実戦模試 2026 第4回 第2問（AIと医療のポッドキャスト要約）を data.json にマージする。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUOTED = "Z会『2026年 共通テスト実戦模試 英語リーディング』第4回 解説冊子"

section_02 = {
    "section_number": 2,
    "title": "第2問",
    "points": 8,
    "points_per_question": 2,
    "description": "長文読解（AIと医療のポッドキャスト要約）",
    "situation": {
        "en": (
            "You need to prepare for a technology class on the future benefits of AI. "
            "You are reading this summary of a recent British podcast on the topic."
        ),
        "ja": (
            "あなたは人工知能の将来の恩恵について技術の授業の準備をする必要があります。"
            "あなたはその話題についての最近のイギリスのポッドキャストのこの要約を読んでいます。"
        ),
    },
    "passages": [
        {
            "id": "ai_healthcare_podcast_summary",
            "framed": True,
            "title": {
                "en": "<strong>Health World Podcast</strong> — Summary",
                "ja": "<strong>『ヘルス・ワールド・ポッドキャスト』</strong> — 要約",
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
                        "id": "aih_p1_s1",
                        "en": (
                            "On today's Health World Podcast, three technology experts discussed how AI is transforming "
                            "healthcare."
                        ),
                        "ja": (
                            "本日の『ヘルス・ワールド・ポッドキャスト』では，３人のテクノロジー専門家が，"
                            "AIが医療をどのように変えつつあるかを論じた。"
                        ),
                    },
                    {
                        "id": "aih_p1_s2",
                        "en": (
                            "There was general agreement that AI will help doctors to diagnose and treat disease faster "
                            "and earlier due to AI's strength in analysing vast quantities of data at speed."
                        ),
                        "ja": (
                            "AIは膨大なデータを高速に分析する強みがあるため，医師の診断や治療をより速く，より早期に"
                            "支援するという点では，概ね一致した見解があった。"
                        ),
                    },
                ],
                [
                    {
                        "id": "aih_p2_s1",
                        "en": (
                            "Two of the experts supported the independent action of AI in providing medicines and "
                            "treatment, especially in poorer parts of the world where there are not enough doctors."
                        ),
                        "ja": (
                            "専門家のうち２人は，医師が十分にいない世界の貧しい地域などでは，"
                            "AIが薬や治療を独力で提供することを支持した。"
                        ),
                    },
                    {
                        "id": "aih_p2_s2",
                        "en": (
                            "The disagreement arose over whether doctors should always be part of the decision process."
                        ),
                        "ja": "意見の対立が生じたのは，意思決定に医師が常に関与すべきかどうかについてだった。",
                    },
                    {
                        "id": "aih_p2_s3",
                        "en": (
                            "One of the speakers felt strongly that some decisions need an understanding of humans and "
                            "their emotions which AI does not have."
                        ),
                        "ja": (
                            "話者の一人は，意思決定にはAIにはない人間や感情への理解が必要な場合があると"
                            "強く感じていた。"
                        ),
                    },
                ],
                [
                    {
                        "id": "aih_p3_s1",
                        "en": (
                            "All felt that doctors would have more time to spend with patients as AI can take care of "
                            "paperwork and administration."
                        ),
                        "ja": (
                            "誰もが，AIが書類仕事や事務を担えるため，医師は患者と過ごす時間をより多く持てるだろうと"
                            "考えた。"
                        ),
                    },
                    {
                        "id": "aih_p3_s2",
                        "en": (
                            "Medical research would also benefit as AI can run tests and check data more efficiently than "
                            "regular computer programs, but they agreed that research should go through a final human "
                            "check before it is released."
                        ),
                        "ja": (
                            "医学研究も恩恵を受けるだろう。AIは通常のコンピュータ・プログラムより効率よく"
                            "試験を走らせデータを確認できるが，成果を公表する前には最終的な人間による確認を"
                            "経るべきだという点では一致した。"
                        ),
                    },
                ],
                [
                    {
                        "id": "aih_p4_s1",
                        "en": "AI's reputation for using biased algorithms poses a problem.",
                        "ja": "偏ったアルゴリズムを使うというAIの評判は問題を呈する。",
                    },
                    {
                        "id": "aih_p4_s2",
                        "en": (
                            "The news often features reports of AI using a poor balance of data that is different from "
                            "real-world data."
                        ),
                        "ja": (
                            "ニュースでは，現実世界のデータとはバランスの取れないデータをAIが用いたという報道が"
                            "よく取り上げられる。"
                        ),
                    },
                    {
                        "id": "aih_p4_s3",
                        "en": "This could lead to poor medical decisions.",
                        "ja": "それは不適切な医療判断につながりかねない。",
                    },
                    {
                        "id": "aih_p4_s4",
                        "en": (
                            "Two of the speakers felt that government regulations and laws would take care of this "
                            "problem, but one felt that this could always be an issue with AI and that more regulations "
                            "need to be developed if AI is going to be used on patients."
                        ),
                        "ja": (
                            "話者のうち２人は政府の規制と法律がこの問題に対処すると考えたが，"
                            "もう一人はAIには常にこの問題がつきまとい，患者にAIを使うならさらなる規制の整備が"
                            "必要だと感じた。"
                        ),
                    },
                    {
                        "id": "aih_p4_s5",
                        "en": (
                            "He felt that we weren't yet ready for large-scale AI in the medical world."
                        ),
                        "ja": "彼は，医療の世界でAIを大規模に導入する準備はまだできていないと感じていた。",
                    },
                ],
                [
                    {
                        "id": "aih_p5_s1",
                        "en": (
                            "Finally, there were disagreements regarding timing and what percentage of decisions we can "
                            "leave up to AI."
                        ),
                        "ja": (
                            "最後に，導入の時期や，どの程度の判断をAIに委ねてよいかについても意見の相違があった。"
                        ),
                    },
                    {
                        "id": "aih_p5_s2",
                        "en": (
                            "However, all felt that if politicians, doctors and technology experts work together, AI "
                            "can have a positive effect on the future of healthcare."
                        ),
                        "ja": (
                            "しかし，政治家と医師とテクノロジー専門家が協力すれば，AIは医療の未来に"
                            "良い影響を与えうると誰もが考えた。"
                        ),
                    },
                ],
            ],
            "images": [
                {
                    "paragraph_index": 0,
                    "src": "images/ai_healthcare_doctor.png",
                    "position": "float-right",
                    "alt": "Doctor with digital healthcare interface",
                    "max_width": 220,
                }
            ],
        }
    ],
    "questions": [
        {
            "question_id": "問1",
            "answer_number": 4,
            "stem": {
                "en": "Which of the following did all of the speakers agree on? [ 4 ]",
                "ja": "話者全員が一致したのは次のうちどれか。［4］",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "AI can demonstrate its ability to find out data that is hard to obtain",
                    "ja": "AIは入手が難しいデータを見つけ出す能力を示しうる",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "AI will be more useful in the future when it develops human emotions",
                    "ja": "AIが人間の感情を獲得すれば将来さらに有用になる",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "Poorer parts of the world could use AI alone when there were no doctors",
                    "ja": "医師がいない地域ではAIだけで対応できる",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "The use of AI would make earlier and speedier treatment available",
                    "ja": "AIの利用によりより早期で迅速な治療が可能になる",
                    "is_correct": True,
                },
            ],
            "answer": "④",
            "explanation": {
                "quoted_ja": (
                    "正解は④。第１段落後半に，AIはデータ分析が速いため診断や治療をより速くより早期に助けると"
                    "general agreement とある。③は専門家２人の見解であり全員一致ではない。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["aih_p1_s2"],
                "instructor_note": {
                    "ja": (
                        "all of the speakers / general agreement / two of the experts など，人数・範囲を決める副詞・表現に色を付けて読む。"
                        "「一致したのは誰全員か／一部か」を問う設問で，部分一致の内容を正解にしない。"
                    ),
                    "points": [
                        "第１段落の general agreement は診断・治療の early / faster とデータ分析の速さに結びついている。④がその要約。",
                        "②は感情を持つAIという本文にない未来像。①は根拠が曖昧。",
                        "③のように聞こえる内容は，あくまで two of the experts supported ... の文にあり，全員一致ではない。",
                    ],
                },
            },
        },
        {
            "question_id": "問2",
            "answer_number": 5,
            "stem": {
                "en": "AI use will most likely [ 5 ].",
                "ja": "AIの利用は最もありそうなこととして［5］である。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "allow doctors to see more patients, or to spend more time with each patient",
                    "ja": "医師がより多くの患者を診るか，一人あたりにより多くの時間をかけられるようにする",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "be available on a large scale for medical care in the near future",
                    "ja": "近い将来，医療に大規模に導入される",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "give doctors a deeper understanding of patients and their problems",
                    "ja": "医師により深い患者理解を与える",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "provide access to cheaper healthcare for people who need to see a doctor",
                    "ja": "診療を必要とする人により安い医療へのアクセスを提供する",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①。第３段落冒頭に，書類や事務をAIが担えば医師は患者ともっと時間を過ごせると"
                    "All felt とある。②は第４段落で large-scale AI にまだ準備ができていないという否定的意見がある。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["aih_p3_s1", "aih_p4_s5"],
                "instructor_note": {
                    "ja": (
                        "most likely は本文で複数話者が繰り返し触れた「実務上の帰結」を選ぶことが多い。"
                        "paperwork を誰が担うか，患者時間がどう増えるかを一文で言い切っている段落を探す。"
                    ),
                    "points": [
                        "All felt で接続される節は「医師が患者ともっと時間を過ごせる／AIが事務を処理」と長所の核。①がこれを選択肢化したもの。",
                        "②は後半で large-scale に慎重な話者がおり「目前に普及」とは読みにくい。",
                        "③は感情理解は AI にないという別ブロックの話。④は費用について本文が断定していない。",
                    ],
                },
            },
        },
        {
            "question_id": "問3",
            "answer_number": 6,
            "stem": {
                "en": "One expert's opinion is that [ 6 ].",
                "ja": "専門家の一人の意見として［6］である。",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "AI is not yet ready to work independently without human assistance",
                    "ja": "AIはまだ人の支援なしに独力で働ける段階にはない",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "AI would not ever be useful because it uses unfair algorithms",
                    "ja": "不公平なアルゴリズムを使うためAIは決して有用にならない",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "medical research needs to be done by AI after the human check is finished",
                    "ja": "医学研究は人間の確認のあとにAIが行う必要がある",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "positive AI research results must always be reviewed by doctors",
                    "ja": "AIの有望な研究結果は常に医師が查読しなければならない",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": (
                    "正解は①。第４段落末に，大規模な医療AIの導入にはまだ準備ができていないと感じた（一人の）"
                    "話者がいる。④の研究の人間確認は合意事項であって一人の専門意見ではない。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["aih_p4_s5"],
                "instructor_note": {
                    "ja": (
                        "One expert / One of the speakers / He felt の直後だけを切り取り，「合意」と「個人の警告」を混ぜない。"
                        "後半でまだ準備ができていない系のトーンがどの話者に紐づくかを確認する。"
                    ),
                    "points": [
                        "large-scale AI ... not yet ready は規制論とは別に，一人の強い懸念として提示されている。①がこれを抽象化。",
                        "②は useful を絶対否定しており本文トーンより過激。③④は「合意で決まった手順」を一人の意見と取り違えやすい。",
                    ],
                },
            },
        },
        {
            "question_id": "問4",
            "answer_number": 7,
            "stem": {
                "en": "Which of the following points is mentioned in the podcast? [ 7 ]",
                "ja": "次のうち，ポッドキャストで述べられている点はどれか。［7］",
            },
            "choices": [
                {
                    "label": "①",
                    "en": "AI's help in administration; cutting down consultation hours",
                    "ja": "事務へのAIの助力；診察時間の短縮",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "Doctors learning more about technology to improve care",
                    "ja": "医師がケア向上のために技術を学ぶこと",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "Many experts cooperating to produce successful medical AI",
                    "ja": "成功する医療AIを生むための多くの専門家の協力",
                    "is_correct": True,
                },
                {
                    "label": "④",
                    "en": "Paperwork being done by doctors to avoid bias and mistakes",
                    "ja": "偏りや誤りを避けるため医師が書類仕事をすること",
                    "is_correct": False,
                },
            ],
            "answer": "③",
            "explanation": {
                "quoted_ja": (
                    "正解は③。最終段落に，政治家・医師・テクノロジー専門家が協力すればとある。"
                    "①の診察時間短縮は本文にない。④はAIが事務を担うという記述と矛盾する。"
                ),
                "quoted_source": QUOTED,
                "evidence_sentences": ["aih_p5_s2"],
                "instructor_note": {
                    "ja": (
                        "mentioned 問題は「本文に単語として現れるか」より，議論の焦点として触れられているかで判定する。"
                        "複数のステークホルダが並ぶ文は頻出パターンなので，politicians / doctors / experts に注目。"
                    ),
                    "points": [
                        "最終段落の協働は③の many experts cooperating に対応しやすい（業界横断の協調という読み）。",
                        "①は administration はあるが consultation hours の短縮とは結びつけていない「合成エラー」になりやすい。",
                        "④は AI が paperwork と書いてあり医師が書類という逆。②は医師の技術学習として本文に線がない。",
                    ],
                },
            },
        },
    ],
    "vocabulary": {
        "passage": {
            "label_ja": "主な語彙・表現",
            "items": [
                {"en": "transform", "ja": "〜を変える"},
                {"en": "diagnose", "ja": "診断する"},
                {"en": "vast quantities of", "ja": "莫大な量の"},
                {"en": "independent", "ja": "独自の；自立した"},
                {"en": "paperwork", "ja": "書類仕事"},
                {"en": "administration", "ja": "事務，運営"},
                {"en": "biased", "ja": "偏った"},
                {"en": "regulation", "ja": "規制"},
                {"en": "healthcare", "ja": "医療；保健"},
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
