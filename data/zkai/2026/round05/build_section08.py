# -*- coding: utf-8 -*-
"""Z会2026第5回 大問8（動物実験・エッセイ構成）を data.json にマージ。Step2（問3）は [41][42] 順不同＋[43] の全正解で得点。"""
import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data.json"
IMG_DIR = Path(__file__).resolve().parent / "images"
OUT_GRAPH = IMG_DIR / "section08_source_b_graph.png"


def generate_graph_image():
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("WARN: matplotlib なし。画像は手動で配置してください:", OUT_GRAPH)
        return False

    years = list(range(2002, 2023))
    # 解説方針：2002→2022 でイヌ・サルは概ね約半減。ウマは後半上昇ピーク、ネコは早期にほぼゼロ。
    horses = [
        8000, 8100, 8200, 8200, 8300, 8350, 8400, 8500, 8600, 8700, 8800, 9000, 9500, 10200,
        10800, 11200, 11100, 11000, 10900, 10500, 8200,
    ]
    dogs = [
        8000, 7950, 7800, 7200, 6500, 6000, 5500, 5000, 4800, 4600, 4500, 4400, 4200, 4100,
        4000, 4100, 4200, 4150, 4100, 4050, 4100,
    ]
    monkeys = [
        4000, 4200, 4100, 4500, 4300, 4000, 3800, 3500, 3200, 2800, 2500, 2800, 3200, 3500,
        3400, 3200, 3000, 2800, 2600, 2400, 2200,
    ]
    cats = [
        1500, 1200, 900, 600, 400, 200, 100, 80, 60, 50, 40, 40, 35, 30, 30, 25, 25, 20, 20, 15, 10,
    ]

    IMG_DIR.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    ax.plot(years, horses, "k:", linewidth=1.8, label="Horses")
    ax.plot(years, dogs, "k-.", linewidth=1.6, label="Dogs")
    ax.plot(years, monkeys, "k--", linewidth=1.6, label="Monkeys")
    ax.plot(years, cats, "k-", linewidth=2.0, label="Cats")
    ax.set_title("Number of Animals Used in Medical Research", fontsize=11)
    ax.set_xlabel("Year", fontsize=9)
    ax.set_ylabel("Number of animals", fontsize=9)
    ax.set_xticks(years[::2])
    ax.set_ylim(0, 12000)
    ax.grid(True, alpha=0.35)
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT_GRAPH, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print("OK: wrote", OUT_GRAPH)
    return True


def section_08():
    return {
        "section_number": 8,
        "title": "第8問",
        "points": 18,
        "points_per_question": 0,
        "description": "レポート構成（動物実験）：意見読解・立場・情報源活用",
        "situation": {
            "en": (
                "You are working on an essay about whether medical companies should test their products on animals. "
                "You will follow the steps below:"
            ),
            "ja": (
                "あなたは，医療企業が自社製品を動物実験すべきかどうかについてのエッセイに取り組んでいます。"
                "あなたは以下のステップに従います。"
            ),
            "steps": [
                {
                    "en": "Step 1: Read and understand various viewpoints on animal testing.",
                    "ja": "ステップ1：動物実験に関するさまざまな観点を読み，理解する。",
                },
                {
                    "en": "Step 2: Take a position on medical testing on animals.",
                    "ja": "ステップ2：動物で医療実験をすることに対する自分の立場を決める。",
                },
                {
                    "en": "Step 3: Create an outline for an essay using additional sources.",
                    "ja": "ステップ3：追加の資料を用いてエッセイの概要を作成する。",
                },
            ],
        },
        "passages": [
            {
                "id": "step1_animal_views",
                "title": {
                    "en": "[Step 1] Read various sources",
                    "ja": "［ステップ1］さまざまな資料を読む",
                },
                "layout": "speaker_boxes",
                "paragraphs": [
                    [
                        {"id": "at8_a_h", "en": "Author A (Hospital patient)", "ja": "筆者A（入院患者）"},
                        {
                            "id": "at8_a_s1",
                            "en": (
                                "I am recovering from a very dangerous disease. I heard that the medicine the doctors gave me to save my life "
                                "was developed through animal testing. I am deeply thankful for the medicine, but it troubles me to think that "
                                "it was developed through the suffering of innocent animals."
                            ),
                            "ja": (
                                "私はとても危険な病気から回復しつつあります。私の命を救うために医師が与えた薬が，動物実験を通して開発されたものだと聞きました。"
                                "私はその薬に深く感謝していますが，その薬が罪のない動物たちの苦痛を通して開発されたものだと思うと悩みます。"
                            ),
                        },
                        {
                            "id": "at8_a_s2",
                            "en": (
                                "I have heard that often animal testing is chosen because it is less expensive than other methods, "
                                "such as those using state-of-the-art technology. I believe that animal testing should be replaced by other methods."
                            ),
                            "ja": (
                                "最先端技術を使ったものなどの他の方法よりも安価であるため，動物実験がしばしば選択されると聞いたことがあります。"
                                "動物実験は他の方法に置き換えられるべきだと思います。"
                            ),
                        },
                    ],
                    [
                        {"id": "at8_b_h", "en": "Author B (Animal rights expert)", "ja": "筆者B（動物の権利に関する専門家）"},
                        {
                            "id": "at8_b_s1",
                            "en": (
                                "Some people argue that animal testing is acceptable because animals also benefit from medicine created for humans. "
                                "I think that is a poor argument. We only use medicine to save animals that are of use to humans, "
                                "such as companion animals or farm animals, not wild animals."
                            ),
                            "ja": (
                                "動物も人間のために作られた薬の恩恵を受けているのだから動物実験は容認されると主張する人がいます。"
                                "それは稚拙な主張だと思います。私たちが薬を使うのは，コンパニオンアニマル（ペット）や家畜など，"
                                "人間にとって有用な動物を救うためだけで，野生動物のためではありません。"
                            ),
                        },
                        {
                            "id": "at8_b_s2",
                            "en": (
                                "Furthermore, the procedures are often cruel. For example, the animals are given diseases and then tested "
                                "to see if the drugs or treatment work for the target diseases. I think that it is immoral."
                            ),
                            "ja": (
                                "さらに，その手段はしばしば残酷です。例えば，動物を病気に感染させ，それから薬や治療法が対象となる病気に効くかどうかを検査します。"
                                "道義に反すると思います。"
                            ),
                        },
                    ],
                    [
                        {"id": "at8_c_h", "en": "Author C (Doctor)", "ja": "筆者C（医師）"},
                        {
                            "id": "at8_c_s1",
                            "en": (
                                "If it were not for animal testing, drugs and treatments would be too dangerous to recommend to my patients "
                                "and so many people would die — many of them very young."
                            ),
                            "ja": (
                                "もし動物実験がなかったら，薬や治療法が危険すぎて患者に勧められず，"
                                "あまりに多くの人が，その中の多くはとても若くして，死んでしまうでしょう。"
                            ),
                        },
                        {
                            "id": "at8_c_s2",
                            "en": (
                                "Of course, I feel sad about the death and suffering of the animals, but a huge number of people are saved "
                                "thanks to the whole procedure involved in developing medicine, which includes animal testing. "
                                "In my opinion, that would compensate for the sacrifice. Also, much of the research for human medicine "
                                "is also useful in making animal medicine."
                            ),
                            "ja": (
                                "もちろん，動物の死や苦痛は悲しいことだと思いますが，膨大な数の人々が救われているのは，"
                                "医薬品開発に伴うすべての手順のおかげであり，その中には動物実験も含まれます。"
                                "私の意見では，このことは犠牲を埋め合わせるものになっていると思います。"
                                "また，人間の薬を対象とする研究の多くは，動物の薬を作るのにも役立っています。"
                            ),
                        },
                    ],
                    [
                        {"id": "at8_d_h", "en": "Author D (High school student)", "ja": "筆者D（高校生）"},
                        {
                            "id": "at8_d_s1",
                            "en": (
                                "My class discussed this topic at school in one of our biology lessons and I feel strongly against using animals "
                                "in medical experiments. When it comes to testing new drugs or treatments, healthy animals are chosen as subjects "
                                "and infected with disease. This is ethically wrong, I think."
                            ),
                            "ja": (
                                "私のクラスは学校の生物の授業でこの話題について話し合い，私は医療実験に動物を使うことに強く反対しています。"
                                "新しい薬や治療法を試す場合に，健康な動物が被験動物として選ばれ，病気に感染させられます。"
                                "これは倫理的に間違っていると思います。"
                            ),
                        },
                        {
                            "id": "at8_d_s2",
                            "en": (
                                "Our teacher told us that there are alternative methods for testing medicine. These include testing on human cells "
                                "in test tubes, or predicting results using computer software rather than live animals. "
                                "I hope that these methods will be more widely adopted."
                            ),
                            "ja": (
                                "先生は，医薬品の試験には代替の方法があると教えてくれました。"
                                "試験管に入れた人間の細胞で実験したり，生きた動物ではなくコンピュータソフトを使って結果を予測したりする方法が含まれます。"
                                "このような方法がもっと広く採用されることを願っています。"
                            ),
                        },
                    ],
                    [
                        {"id": "at8_e_h", "en": "Author E (Scientist)", "ja": "筆者E（科学者）"},
                        {
                            "id": "at8_e_s1",
                            "en": (
                                "At my laboratory, we test medicines and treatments on animals every day. We test them on small animals like rats, "
                                "but we also test them on dogs and chimpanzees. Sadly, many of the animals suffer a lot. "
                                "I feel terrible when I see this every day."
                            ),
                            "ja": (
                                "私の研究室では，毎日動物を使って薬や治療法を試験しています。"
                                "ラットのような小動物で検査しますが，犬やチンパンジーでも検査しています。"
                                "悲しいことに，多くの動物がとても苦しんでいます。このような状況を毎日見て，私はつらい気持ちになります。"
                            ),
                        },
                        {
                            "id": "at8_e_s2",
                            "en": (
                                "However, I wish people would understand that we are following very strict rules to keep the animals in decent "
                                "conditions and that there are few really good alternatives. Actually, very few animals die and suffer in testing "
                                "compared with the number of human lives we will save."
                            ),
                            "ja": (
                                "しかし，私たちが動物を適切な環境に置くために非常に厳しい規則に従っていること，"
                                "そして本当に良い代替手段がほとんどないことを理解してほしいと思います。"
                                "実際，私たちが救おうとする人間の命の数に比べれば，検査で死んだり苦しんだりする動物はごくわずかです。"
                            ),
                        },
                    ],
                ],
                "inline_solve_markers": [
                    {
                        "after_paragraph": 4,
                        "question_ids": ["問1", "問2"],
                        "answer_numbers": [39, 40],
                    },
                    {
                        "after_paragraph": 4,
                        "marker_type": "navigate",
                        "action_ja": "解答が終わったら本文に戻り、Step 3 の概要と設問欄（Step 2）に進みます。",
                    },
                ],
            },
            {
                "id": "step3_outline",
                "title": {
                    "en": "[Step 3] Create an outline using Sources A and B",
                    "ja": "［ステップ3］資料AとBを用いて概要を作成する",
                },
                "subtitle": {
                    "id": "at8_step3_outline_label",
                    "en": "Outline of your essay:",
                    "ja": "あなたのエッセイの概要：",
                },
                "layout": "essay_outline_box",
                "paragraphs": [
                    [
                        {
                            "id": "at8_eo_title",
                            "en": "Testing medicines on animals is an acceptable practice",
                            "ja": "動物を使っての医薬品の実験は容認されるべき行為である",
                            "role": "outline_title",
                        }
                    ],
                    [
                        {
                            "id": "at8_eo_in_h",
                            "en": "Introduction",
                            "ja": "導入",
                            "role": "outline_subheader",
                        }
                    ],
                    [
                        {
                            "id": "at8_eo_in1",
                            "en": (
                                "Testing medicines on animals has made it possible to produce many medicines. "
                                "We should not stop researchers from using this important tool."
                            ),
                            "ja": (
                                "動物を使っての医薬品の実験のおかげで，多くの薬を製造することが可能になっている。"
                                "研究者がこの重要な手段を使うのを妨げてはならない。"
                            ),
                        }
                    ],
                    [
                        {
                            "id": "at8_eo_bd_h",
                            "en": "Body",
                            "ja": "本論",
                            "role": "outline_subheader",
                        }
                    ],
                    [
                        {
                            "id": "at8_eo_r1",
                            "en": "Reason 1: [From Step 2]",
                            "ja": "理由1：［ステップ2より］",
                            "role": "outline_line",
                        }
                    ],
                    [
                        {
                            "id": "at8_eo_r2",
                            "en": "Reason 2: [Based on Source A] ([44])",
                            "ja": "理由2：［資料Aに基づいて］（[44]）",
                            "role": "outline_line",
                        }
                    ],
                    [
                        {
                            "id": "at8_eo_r3",
                            "en": "Reason 3: [Based on evidence ([45]) from Source B]",
                            "ja": "理由3：［資料Bからの論拠（[45]）に基づいて］",
                            "role": "outline_line",
                        }
                    ],
                    [
                        {
                            "id": "at8_eo_co_h",
                            "en": "Conclusion",
                            "ja": "結論",
                            "role": "outline_subheader",
                        }
                    ],
                    [
                        {
                            "id": "at8_eo_co1",
                            "en": "Testing medicine on animals is the right thing to do.",
                            "ja": "動物を使っての医薬品の実験は正しい行為である。",
                        }
                    ],
                ],
                "inline_solve_markers": [
                    {
                        "after_paragraph": 8,
                        "question_ids": ["問3"],
                        "answer_numbers": [41, 42, 43],
                    },
                    {
                        "after_paragraph": 8,
                        "marker_type": "navigate",
                        "action_ja": "解答が終わったら本文に戻り、資料Aを読みます。",
                    },
                ],
            },
            {
                "id": "source_a",
                "title": {"en": "Source A", "ja": "資料A"},
                "paragraphs": [
                    [
                        {
                            "id": "at8_sa_p1_s1",
                            "en": (
                                "Animal testing is often debated because of its cost in terms of animal lives. It is an emotional issue for most people. "
                                "However, it's crucial to understand the strict rules that govern animal testing, aimed at ensuring humane treatment."
                            ),
                            "ja": (
                                "動物実験は，動物の命という代償のためにしばしば議論の対象となる。ほとんどの人にとって感情的な問題である。"
                                "しかし，思いやりのある扱いを保証することを目的とした動物実験を統制する厳格な規則を理解することは極めて重要である。"
                            ),
                        },
                        {
                            "id": "at8_sa_p1_s2",
                            "en": (
                                "Institutions conducting animal research are required to follow strict laws, which require testers to get approval "
                                "for their research from special committees. Such committees are usually made up of experts in veterinary science, "
                                "ethics, and research."
                            ),
                            "ja": (
                                "動物研究を行う機関は厳しい法律に従うことが求められており，試験者は特別な委員会から研究の承認を得る必要がある。"
                                "そのような委員会は通常，獣医学，倫理学，研究の各分野の専門家で構成されている。"
                            ),
                        },
                        {
                            "id": "at8_sa_p1_s3",
                            "en": (
                                "They carefully check the proposed studies to ensure they are necessary and that every possible measure is taken "
                                "to minimize animal suffering. Furthermore, researchers must follow comprehensive guidelines focusing on animal welfare."
                            ),
                            "ja": (
                                "委員会は，提案された研究が必要であること，また動物の苦痛を最小限にするためのあらゆる手段が講じられていることを確認するために，"
                                "慎重に調べる。さらに，研究者は動物の福祉に焦点を当てた包括的な指針に従わなければならない。"
                            ),
                        },
                    ],
                    [
                        {
                            "id": "at8_sa_p2_s1",
                            "en": (
                                "These include providing proper care, reducing the number of animals used, and refining procedures to reduce emotional stress. "
                                "Regular inspections ensure these standards are maintained. While the loss of animal life in research is a sad reality, "
                                "these regulations and observation systems help raise the level of ethical responsibility in scientific exploration."
                            ),
                            "ja": (
                                "これには適切な世話の提供，使用する動物数の削減，感情的ストレスを減らす手順の改良などが含まれる。"
                                "定期的な検査によって，これらの基準が維持されていることが保証される。"
                                "研究における動物の命の喪失は悲しい現実であるが，これらの規則と監視の仕組みは，科学的探求における倫理的責任の水準を高めるのに役立っている。"
                            ),
                        },
                    ],
                ],
                "inline_solve_markers": [
                    {
                        "after_paragraph": 1,
                        "question_ids": ["問4"],
                        "answer_numbers": [44],
                    },
                    {
                        "after_paragraph": 1,
                        "marker_type": "navigate",
                        "action_ja": "解答が終わったら本文に戻り、資料Bを読みます。",
                    },
                ],
            },
            {
                "id": "source_b",
                "title": {"en": "Source B", "ja": "資料B"},
                "paragraphs": [
                    [
                        {
                            "id": "at8_sb_s1",
                            "en": (
                                "The organizations that use animals in their medical research in the UK must record the number of experiments "
                                "they do on live animals every year. The graph below shows how many horses, dogs, cats, and monkeys are used in medical research."
                            ),
                            "ja": (
                                "イギリスで医学研究に動物を使用する機関は，毎年生きた動物に対して行った実験の回数を記録しなければならない。"
                                "下のグラフは，医学研究に使用されるウマ，イヌ，ネコ，サルの数を示している。"
                            ),
                        },
                    ],
                ],
                "graph_image": {
                    "src": "images/section08_source_b_graph.png",
                    "after_paragraph": 1,
                    "alt": "Number of Animals Used in Medical Research",
                },
                "inline_solve_markers": [
                    {
                        "after_paragraph": 0,
                        "question_ids": ["問5"],
                        "answer_numbers": [45],
                    },
                ],
            },
        ],
        "questions": [
            {
                "question_id": "問1",
                "answer_number": 39,
                "points": 3,
                "step": 1,
                "question_text": {
                    "en": "Both Authors B and D mention that [39].",
                    "ja": "筆者BとDはともに [39] と言及している。",
                },
                "choices": [
                    {
                        "label": "①",
                        "en": "human medicines should be tested on humans because animals are not similar enough",
                        "ja": "動物は人間に十分似ていないので，人間用の薬は人間を対象に試験すべきだ",
                        "is_correct": False,
                    },
                    {
                        "label": "②",
                        "en": "nowadays we can verify the safety of new medicines without using animal testing",
                        "ja": "今日では動物実験を使わずに新薬の安全性を確認できる",
                        "is_correct": False,
                    },
                    {
                        "label": "③",
                        "en": "pets and farm animals also benefit from the medical research relying on animal testing",
                        "ja": "ペットや家畜も，動物実験に依存する医学研究の恩恵を受けている",
                        "is_correct": False,
                    },
                    {
                        "label": "④",
                        "en": "the animals used in medical testing are intentionally made sick by the researchers",
                        "ja": "医学試験に使われる動物は，研究者によって意図的に病気にされる",
                        "is_correct": True,
                    },
                ],
                "answer": "④",
                "explanation": {
                    "quoted_ja": (
                        "正解は④。筆者Bは the animals are given diseases and then tested と述べ，"
                        "筆者Dは healthy animals … infected with disease と述べており，いずれも「研究のために意図的に病気にされる」点で一致する。"
                    ),
                    "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子",
                    "evidence_sentences": ["at8_b_s2", "at8_d_s1"],
                    "instructor_note": {
                        "ja": "「両者が言及していること」は，キーワードの丸暗記より，BとDの段落で“同じ出来事”として語られているかで探す。",
                        "points": [
                            "②の代替手段はDの先生の話であり，Bは触れていない。",
                            "③のペット・家畜の恩恵はBが反論している論点で，Dの主張ともズレる。",
                            "①の「人間で試せ」は両者とも述べていない。",
                            "given diseases / infected with disease と intentionally の対応を確認する。",
                        ],
                    },
                },
            },
            {
                "question_id": "問2",
                "answer_number": 40,
                "points": 3,
                "step": 1,
                "question_text": {
                    "en": "Author A implies that [40].",
                    "ja": "筆者Aは [40] と暗示している。",
                },
                "choices": [
                    {
                        "label": "①",
                        "en": "he appreciates the chance to live that animals have given him",
                        "ja": "動物たちによって与えられた生きる機会に感謝している",
                        "is_correct": True,
                    },
                    {
                        "label": "②",
                        "en": "he will dedicate his life to saving animals after he recovers",
                        "ja": "回復したら動物を救うことに一生を捧げるつもりだ",
                        "is_correct": False,
                    },
                    {
                        "label": "③",
                        "en": "only medicine that is tested on animals can save the lives of humans",
                        "ja": "動物実験された薬だけが人間の命を救える",
                        "is_correct": False,
                    },
                    {
                        "label": "④",
                        "en": "people should not have negative images of animal testing anymore",
                        "ja": "もはや人々は動物実験に対する否定的イメージを持つべきではない",
                        "is_correct": False,
                    },
                ],
                "answer": "①",
                "explanation": {
                    "quoted_ja": (
                        "正解は①。筆者Aは薬に deeply thankful と明言しており，"
                        "動物の苦痛への悩みはあるが「命を救ってもらった感謝」が暗示の中心。②〜④は本文のトーンと合わない。"
                    ),
                    "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子",
                    "evidence_sentences": ["at8_a_s1"],
                    "instructor_note": {
                        "ja": "imply は「書いてあること」より「読み手が引き出せる態度・感情」を問う。感謝と葛藤の主従に注目する。",
                        "points": [
                            "deeply thankful と appreciate the chance to live が同じ感謝の軸で結べる。",
                            "③の only は断定が強すぎ，筆者は代替を支持しており「動物実験だけが救う」とは言い切っていない。",
                            "④は否定的イメージを捨てよという方向で，本文の troubled と逆になる誘答。",
                            "②は本文に根拠のない未来の決意なので除外しやすい。",
                        ],
                    },
                },
            },
            {
                "question_id": "問3",
                "step": 2,
                "points": 6,
                "points_note": "［41］〜［43］はすべて正解で得点。［41］［42］は順不同。",
                "pre_header": {
                    "en": "[Step 2] Take a position",
                    "ja": "［ステップ2］立場を決める",
                },
                "answer_numbers": [41, 42, 43],
                "unordered_slots": [41, 42],
                "stem": {
                    "en": (
                        "Now that you understand the various viewpoints, you have taken a position on medical testing on animals, "
                        "and have written it out as below. Choose the best options to complete [41] — [43]. "
                        "(You must have all of [41] — [43] correct to get points.)"
                    ),
                    "ja": (
                        "さまざまな観点を理解したうえで，動物実験について自分の立場を決め，以下のように書いた。"
                        "［41］から［43］を完成させるのに最も適当な選択肢を選びなさい。"
                        "（得点するためには［41］から［43］のすべてに正解する必要がある。）"
                    ),
                },
                "position_box": {
                    "en": (
                        "Your position: Testing medicine on animals is the right thing to do.\n"
                        "  • Authors [41] and [42] support your position.\n"
                        "  • The main argument of the two authors: [43]"
                    ),
                    "ja": (
                        "あなたの立場：動物を使っての医薬品の実験は正しい行為である。\n"
                        "  • 筆者 [41] と [42] はあなたの立場を支持する。\n"
                        "  • この2人の筆者の主な論拠： [43]"
                    ),
                },
                "choices_41": [
                    {"label": "①", "en": "A", "ja": "A", "is_correct": False},
                    {"label": "②", "en": "B", "ja": "B", "is_correct": False},
                    {"label": "③", "en": "C", "ja": "C", "is_correct": True},
                    {"label": "④", "en": "D", "ja": "D", "is_correct": False},
                    {"label": "⑤", "en": "E", "ja": "E", "is_correct": True},
                ],
                "choices_42": [
                    {"label": "①", "en": "A", "ja": "A", "is_correct": False},
                    {"label": "②", "en": "B", "ja": "B", "is_correct": False},
                    {"label": "③", "en": "C", "ja": "C", "is_correct": True},
                    {"label": "④", "en": "D", "ja": "D", "is_correct": False},
                    {"label": "⑤", "en": "E", "ja": "E", "is_correct": True},
                ],
                "choices_43": [
                    {
                        "label": "①",
                        "en": "Animals should only be used to find cures for diseases that affect people with healthy lifestyles.",
                        "ja": "動物は，健康的な生活習慣を持つ人に影響を及ぼす病気の治療法を見つけるためにのみ使われるべきだ。",
                        "is_correct": False,
                    },
                    {
                        "label": "②",
                        "en": (
                            "It is better to test medicines on small animals like rats because they may feel less pain than bigger animals."
                        ),
                        "ja": "大きな動物よりも感じる痛みが少ないかもしれないので，ラットのような小さな動物で医薬品の検査をする方がよい。",
                        "is_correct": False,
                    },
                    {
                        "label": "③",
                        "en": "The number of lives that will be saved by animal testing is large enough to make testing acceptable.",
                        "ja": "動物実験によって救われる人命の数は，実験を容認するのに十分なくらい多い。",
                        "is_correct": True,
                    },
                    {
                        "label": "④",
                        "en": (
                            "The number of medicines that can be made through animal testing is higher than if we only tested on humans."
                        ),
                        "ja": "動物実験を通して作ることができる薬の数は，人間だけで実験した場合よりも多い。",
                        "is_correct": False,
                    },
                ],
                "answer": {"41": "③", "42": "⑤", "43": "③"},
                "answer_note": "［41］と［42］には C（③）と E（⑤）が順不同で入る。",
                "explanation": {
                    "quoted_ja": (
                        "正解は［41］③／［42］⑤（順不同），［43］③。"
                        "「動物を使っての医薬品の実験は正しい行為」と明確に支持するのは医師のCと研究室のE。"
                        "［43］は両者に共通する「救われる人命の規模と動物の犠牲・苦痛の対比」が③に相当する。"
                    ),
                    "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子",
                    "evidence_sentences": ["at8_c_s1", "at8_c_s2", "at8_e_s2"],
                    "instructor_note": {
                        "ja": "大問8の配点の山はここ。立場が問題文で固定されているので「賛成の声」を拾う作業に切り替える練習をさせると安定する。",
                        "points": [
                            "［41］［42］は C と E の順不同。同じ筆者を二枠に入れることは論理上ありえないので，A/B/D を早めに消す。",
                            "［43］は「二人の主な論拠」＝両段落に共通する“人命のスケールと犠牲のトレードオフ”が書かれているかで絞る。",
                            "④は薬の“種類の数”で，C の compensate / E の few … compared とは軸がずれやすい。",
                            "得点は［41］〜［43］の全正解が条件なので，43 だけ当たっても満点にならない点を事前に伝えるとミスが減る。",
                        ],
                    },
                },
            },
            {
                "question_id": "問4",
                "answer_number": 44,
                "points": 3,
                "step": 3,
                "question_text": {
                    "en": "Based on Source A, which of the following is the most appropriate for Reason 2? [44]",
                    "ja": "資料Aに基づき，理由2として最も適当なものは次のうちどれか。［44］",
                },
                "choices": [
                    {
                        "label": "①",
                        "en": "Experts in veterinary science are advising researchers to use animals to find new medicines for humans.",
                        "ja": "獣医学の専門家は，人間の新薬を見つけるために研究者に動物の使用を勧めている",
                        "is_correct": False,
                    },
                    {
                        "label": "②",
                        "en": "The government is encouraging animal testing by publishing guidelines for researchers to use.",
                        "ja": "政府は研究者が使う指針を公表することで動物実験を奨励している",
                        "is_correct": False,
                    },
                    {
                        "label": "③",
                        "en": "The laws surrounding the use of animals for medical research are likely to become stricter in the future.",
                        "ja": "医学研究における動物の使用をめぐる法律は，将来より厳しくなる可能性が高い",
                        "is_correct": False,
                    },
                    {
                        "label": "④",
                        "en": (
                            "While it is unfortunate that some animals must die for research, there are rules in place to reduce their pain."
                        ),
                        "ja": "研究のために動物が死ななければならないのは不幸だが，その苦痛を減らす規則が施行されている",
                        "is_correct": True,
                    },
                ],
                "answer": "④",
                "explanation": {
                    "quoted_ja": (
                        "正解は④。資料Aは厳格な規則・委員会・苦痛の最小化・点検を主線とし，"
                        "最終文で動物の命の喪失は悲しい現実と認めつつ規制の意義に触れる。①②③は本文の主張とずれる。"
                    ),
                    "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子",
                    "evidence_sentences": ["at8_sa_p1_s1", "at8_sa_p1_s3", "at8_sa_p2_s1"],
                    "instructor_note": {
                        "ja": "アウトライン上の Reason 2 は「規制・倫理の枠組み」を一言で要約するタイプ。専門家の役割を“勧める内容”まで膨らませない。",
                        "points": [
                            "①は委員会に獣医学者がいる事実の先取りで，「動物を使えと助言している」まで読むと過剰。",
                            "②の encourage は guidelines の趣旨（遵守・福祉）とニュアンスが逆向きになりやすい。",
                            "③の将来より厳格は本文に根拠がなく，時制の飛躍になりがち。",
                            "④は sad reality と rules / minimize suffering の往復を一枚に圧縮した選択肢。",
                        ],
                    },
                },
            },
            {
                "question_id": "問5",
                "answer_number": 45,
                "points": 3,
                "step": 3,
                "question_text": {
                    "en": (
                        'For Reason 3, you have decided to write, "Researchers are using more caution in choosing whether or not to test '
                        'medicines on certain animals." Based on Source B, which option best supports this statement? [45]'
                    ),
                    "ja": (
                        "理由3として，あなたは『研究者は特定の動物で医薬品を試験するかどうかの選択に，より慎重になっている。』と書くことにした。"
                        "資料Bに基づき，この意見を最もよくサポートする選択肢はどれか。［45］"
                    ),
                },
                "choices": [
                    {
                        "label": "①",
                        "en": (
                            "About half as many dogs and monkeys were used in research in 2022 compared with 20 years before. "
                            "This shows a growing concern for the welfare of these animals."
                        ),
                        "ja": (
                            "2022年には，20年前に比べて約半数のイヌとサルが研究に使用された。"
                            "これは，これらの動物の福祉に対する関心が高まっていることを示している。"
                        ),
                        "is_correct": True,
                    },
                    {
                        "label": "②",
                        "en": (
                            "Medical research using monkeys has dropped at nearly twice the rate of research involving dogs. "
                            "This suggests that our relationship with dogs is being considered."
                        ),
                        "ja": (
                            "サルを使った医学研究は，イヌを使った研究の約2倍の割合で減少している。"
                            "これは人間とイヌとの関係が考慮されていることを示唆している。"
                        ),
                        "is_correct": False,
                    },
                    {
                        "label": "③",
                        "en": (
                            "The number of cats and horses used for medical testing has remained fairly constant. "
                            "These animals must have proven valuable to medical science."
                        ),
                        "ja": (
                            "医学実験に使われるネコとウマの数は，ほぼ一定に保たれている。"
                            "これらの動物は医学にとって価値があったに違いない。"
                        ),
                        "is_correct": False,
                    },
                    {
                        "label": "④",
                        "en": (
                            "The use of dogs and monkeys sharply decreased during the period 2012-2022. "
                            "More and more researchers have come to respond to the demand for animal welfare."
                        ),
                        "ja": (
                            "2012年から2022年の期間に，イヌとサルの使用は急激に減少した。"
                            "動物愛護の要請に応える研究者がますます増えてきた。"
                        ),
                        "is_correct": False,
                    },
                ],
                "answer": "①",
                "explanation": {
                    "quoted_ja": (
                        "正解は①。グラフ上で2002年と2022年を比べるとイヌ・サルはおおむね半減しており，"
                        "特定動物の使用を抑える慎重さと福祉への関心を最もよく裏づける。②は減少率の比較が誤答，③はネコ・ウマの推移が一定ではない，④は2012–22の急落と言い切れない。"
                    ),
                    "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子",
                    "evidence_sentences": ["at8_sb_s1"],
                    "instructor_note": {
                        "ja": "設問で与えられた英文の主語（Researchers … certain animals）に合わせ，イヌとサルに視点を固定して読むと迷いが減る。",
                        "points": [
                            "区間の“急激さ”より，2002 と 2022 の二点を結ぶイメージで①の約半分を確認する。",
                            "②は「約2倍」など比率の言い切りが数字の読み取りで崩れやすい典型誤答。",
                            "③はネコとウマが「ほぼ一定」と言いにくい形の年があると落とせる。",
                            "④は期間を 2012–2022 に狭めると，線の下り方が必ずしも sharply と言えない年が混ざりやすい。",
                        ],
                    },
                },
            },
        ],
        "vocabulary": {
            "passage": {
                "label_ja": "主な語句・表現",
                "items": [
                    {"en": "viewpoint", "ja": "見解；観点"},
                    {"en": "outline", "ja": "概要"},
                    {"en": "additional", "ja": "追加の"},
                    {"en": "source", "ja": "（研究・調査の）資料；出典"},
                    {"en": "suffering", "ja": "苦痛"},
                    {"en": "innocent", "ja": "罪のない；無実の"},
                    {"en": "state-of-the-art", "ja": "最先端の"},
                    {"en": "companion animal", "ja": "コンパニオンアニマル（ペット）"},
                    {"en": "immoral", "ja": "道徳に反する"},
                    {"en": "compensate for ~", "ja": "〜を補う"},
                    {"en": "sacrifice", "ja": "犠牲"},
                    {"en": "subject", "ja": "被験者；実験動物"},
                    {"en": "alternative", "ja": "代替の；（名詞で）代替手段"},
                    {"en": "decent", "ja": "適切な"},
                    {"en": "humane", "ja": "思いやりのある；（不必要な）苦痛を与えない"},
                    {"en": "committee", "ja": "委員会"},
                    {"en": "minimize", "ja": "〜を最小限にする"},
                    {"en": "welfare", "ja": "福祉"},
                    {"en": "regulation", "ja": "規則"},
                ],
            },
            "questions_and_choices": {
                "items": [
                    {"en": "verify（問1②）", "ja": "〜を検証する"},
                    {"en": "intentionally（問1④）", "ja": "意図的に"},
                    {"en": "imply（問2）", "ja": "〜を暗示する"},
                    {"en": "dedicate A to B（問2②）", "ja": "AをBに捧げる"},
                    {"en": "cure（問3［43］①）", "ja": "治療法"},
                    {"en": "unfortunate（問4④）", "ja": "不幸な"},
                    {"en": "in place（問4④）", "ja": "施行されて"},
                    {"en": "use caution（問5）", "ja": "注意する"},
                    {"en": "concern（問5①）", "ja": "関心；懸念"},
                    {"en": "constant（問5③）", "ja": "一定の"},
                ],
            },
        },
    }


def main():
    generate_graph_image()
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    data["sections"] = [s for s in data["sections"] if s.get("section_number") != 8]
    data["sections"].append(section_08())
    data["sections"].sort(key=lambda s: s.get("section_number", 0))
    impl = data["exam_info"].setdefault("implemented_sections", [])
    if 8 not in impl:
        impl.append(8)
        impl.sort()
    DATA_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("OK: section 8 merged, implemented_sections:", data["exam_info"]["implemented_sections"])


if __name__ == "__main__":
    main()
