# -*- coding: utf-8 -*-
"""Z会2026第5回 大問7（パーム油）を data.json にマージ。問2用4グラフ画像を matplotlib で生成。"""
import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data.json"
IMG_DIR = Path(__file__).resolve().parent / "images"
OUT_GRAPH = IMG_DIR / "section07_q35_graph_choices.png"


def _years():
    return [1991, 1995, 2000, 2005, 2006, 2010, 2014, 2015, 2018]


def _plot_graph(ax, title_tag, ind, mal, row):
    ys = _years()
    ax.plot(ys, ind, "k-", linewidth=1.8, label="Indonesia")
    ax.plot(ys, mal, "k--", linewidth=1.5, label="Malaysia")
    ax.plot(ys, row, "k:", linewidth=1.5, label="Rest of the world")
    ax.set_title(f"Palm Oil Production — {title_tag}", fontsize=9)
    ax.set_xlim(1990, 2019)
    ax.set_ylim(0, 50)
    ax.set_ylabel("(Millions of Tons)", fontsize=7)
    ax.set_xticks([1991, 1995, 2000, 2005, 2010, 2015, 2018])
    ax.tick_params(labelsize=6)
    ax.grid(True, alpha=0.35)
    ax.legend(loc="upper left", fontsize=5)
    # 解答の①〜④とパネル位置が一目で対応するよう、グラフ領域左上に選択肢番号を重ねる
    ax.text(
        0.02,
        0.98,
        title_tag,
        transform=ax.transAxes,
        fontsize=16,
        fontweight="bold",
        va="top",
        ha="left",
        color="#0a1f44",
        bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor="#0a1f44", linewidth=1.2, alpha=0.92),
    )


def generate_graph_image():
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        # ①などの丸数字が豆腐にならないよう、日本語環境でよくあるゴシックを優先
        plt.rcParams["font.sans-serif"] = [
            "MS Gothic",
            "Yu Gothic",
            "Meiryo",
            "Noto Sans CJK JP",
            "DejaVu Sans",
        ]
        plt.rcParams["axes.unicode_minus"] = False
    except ImportError:
        print("WARN: matplotlib なし。画像は手動で配置してください:", OUT_GRAPH)
        return False

    ys = _years()
    # ② 正解型：インドネシア低出発→2006前後でマレーシアと交差→2018に約40M超
    ind2 = [5, 6, 8, 12, 16, 22, 35, 33, 42]
    mal2 = [8, 9, 11, 14, 16, 19, 20, 20, 21]
    row2 = [3, 3.5, 4, 4.5, 5, 6.5, 8, 8.5, 10]
    # ① 誤答：インドネシアが高く出て落ち込む
    ind1 = [20, 16, 12, 9, 10, 28, 36, 38, 40]
    mal1 = [18, 14, 12, 10, 12, 16, 18, 19, 20]
    row1 = [15, 12, 9, 7, 7, 7, 8, 8, 8]
    # ③ 誤答：マレーシアが長く上でピーク後もインドネシア追い越しが遅い
    ind3 = [4, 5, 7, 9, 11, 18, 30, 36, 42]
    mal3 = [6, 10, 18, 24, 25, 26, 26, 26, 26]
    row3 = [3, 3, 4, 4, 5, 8, 10, 11, 12]
    # ④ 誤答：インドネシアに2014頃のピークと落ち込み
    ind4 = [5, 7, 10, 14, 18, 28, 36, 32, 30]
    mal4 = [8, 10, 12, 15, 17, 20, 22, 26, 29]
    row4 = [3, 4, 4, 5, 6, 7, 8, 9, 10]

    IMG_DIR.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(2, 2, figsize=(9.5, 7.2))
    # 2×2 の位置と選択肢①〜④の対応（上段左→①、上段右→②、下段左→③、下段右→④）
    plots = [
        (axes[0, 0], "①", ind1, mal1, row1),
        (axes[0, 1], "②", ind2, mal2, row2),
        (axes[1, 0], "③", ind3, mal3, row3),
        (axes[1, 1], "④", ind4, mal4, row4),
    ]
    for ax, tag, i, m, r in plots:
        _plot_graph(ax, tag, i, m, r)
    fig.tight_layout()
    fig.savefig(OUT_GRAPH, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print("OK: wrote", OUT_GRAPH)
    return True


def section7():
    return {
        "section_number": 7,
        "title": "第7問",
        "points": 14,
        "points_per_question": 0,
        "description": "長文読解（パーム油・持続可能性・RSPO）",
        "situation": {
            "en": "You are studying about world ecological problems. You are going to read the following article to understand what has happened with palm oil.",
            "ja": "あなたは，世界の環境保護の問題について勉強しています。パーム油に関して何が起こっているのかを理解するために，次の記事を読もうとしています。",
        },
        "passages": [
            {
                "id": "palm_oil_article",
                "framed": True,
                "paragraph_classes": ["para-indent", "para-indent", "para-indent", "para-indent"],
                "paragraphs": [
                    [
                        {
                            "id": "pal_p1_s1",
                            "en": "Palm oil is used as an ingredient in nearly half the products you might buy from a supermarket.",
                            "ja": "パーム油は，あなたがスーパーマーケットで買いそうな製品の半分近くに材料として使われている。",
                        },
                        {
                            "id": "pal_p1_s2",
                            "en": "Not long ago, however, palm oil had a bad reputation.",
                            "ja": "しかし，わりと最近のことまでは，パーム油は評判が悪かった。",
                        },
                        {
                            "id": "pal_p1_s3",
                            "en": "Many tropical forests have been burned down to make space to grow oil palm trees, releasing carbon dioxide into the air and damaging the environment.",
                            "ja": "多くの熱帯林が，油ヤシの木を育てる場所を確保するために焼き払われ，それによって二酸化炭素が大気中に放出され，環境にダメージを与えている。",
                        },
                        {
                            "id": "pal_p1_s4",
                            "en": "Consequently, environmentalists began to consider palm oil production unethical and even encouraged people not to buy products made from it.",
                            "ja": "結果として，環境保護論者はパーム油の生産を非倫理的であると考え始め，人々にパーム油から作られた製品を買わないように働きかけさえした。",
                        },
                        {
                            "id": "pal_p1_s5",
                            "en": "Recently, however, recognizing the importance of palm oil for farmers around the world, they are instead focusing on helping them produce it in a more sustainable way.",
                            "ja": "しかし最近では，世界の農家にとってパーム油が重要であることを認識し，代わりに彼らがより持続可能な方法でパーム油を生産するのを助けることに重点を置いている。",
                        },
                    ],
                    [
                        {
                            "id": "pal_p2_s1",
                            "en": "The popularity of palm oil is due to its many properties and uses.",
                            "ja": "パーム油の人気は，その多くの特性と用途によるものである。",
                        },
                        {
                            "id": "pal_p2_s2",
                            "en": "It is almost solid at room temperature, for example, so it is a useful ingredient for margarine, mayonnaise, and other semi-solid spread foods.",
                            "ja": "例えば，パーム油は室温ではほぼ固体なので，マーガリンやマヨネーズなど，半固体の塗り広げる食品の材料として役に立つ。",
                        },
                        {
                            "id": "pal_p2_s3",
                            "en": "It also helps preserve food by slowing down the effects of spoiling.",
                            "ja": "また，腐敗の進行を遅らせることで食品の保存にも役立つ。",
                        },
                        {
                            "id": "pal_p2_s4",
                            "en": "For producers, palm oil is easier to grow than crops such as soybeans and coconut oil, and it requires fewer chemicals to protect the plants from insects.",
                            "ja": "生産者にとって，パーム油は大豆やココナッツ油などの作物より育てやすく，害虫から植物を守るための化学物質もより少なくてすむ。",
                        },
                    ],
                    [
                        {
                            "id": "pal_p3_s1",
                            "en": "Farmers produced more than 70 million tons of palm oil in 2018, with more than 60 million tons coming from Indonesia and Malaysia alone.",
                            "ja": "農家は2018年に7000万トンを超えるパーム油を生産しており，そのうち6000万トン超がインドネシアとマレーシアだけから来ている。",
                        },
                        {
                            "id": "pal_p3_s2",
                            "en": "Demand has grown steadily from the early 1990s, when thousands of acres of forests were burned to make space for new palm oil plantations, particularly in Indonesia.",
                            "ja": "需要は1990年代初めから着実に増えており，その頃には特にインドネシアで，新しいパーム油プランテーションのための場所を作るために何千エーカーもの森林が焼かれた。",
                        },
                        {
                            "id": "pal_p3_s3",
                            "en": "By 2006, Indonesia had become the world's largest producer, and currently manufactures twice as much palm oil as Malaysia.",
                            "ja": "2006年までにインドネシアは世界最大の生産国となり，現在ではマレーシアの2倍の量のパーム油を生産している。",
                        },
                        {
                            "id": "pal_p3_s4",
                            "en": "As the industry grew, it contributed significantly to global deforestation.",
                            "ja": "産業が成長するにつれ，それは地球規模の森林破壊に大きく寄与した。",
                        },
                        {
                            "id": "pal_p3_s5",
                            "en": "In response, a non-profit group called the Roundtable on Sustainable Palm Oil (RSPO), was set up in 2004 to certify palm oil products that are grown from ethical sources.",
                            "ja": "これに対し，倫理的な供給源から育てられたパーム油製品を認証するために，「持続可能なパーム油のための円卓会議」（RSPO）と呼ばれる非営利団体が2004年に設立された。",
                        },
                        {
                            "id": "pal_p3_s6",
                            "en": "It seeks to reduce the negative effects on the environment and communities.",
                            "ja": "それは環境と地域社会への悪影響を減らそうとしている。",
                        },
                        {
                            "id": "pal_p3_s7",
                            "en": "Their criteria for producers who want to be certified include minimal use of fire to clear land, fair treatment of workers, and proper consultation with local communities about land development.",
                            "ja": "認証を望む生産者に対するその評価基準には，土地を切り開く際の火の使用を必要最小限にすること，労働者への公正な待遇，土地開発について地域社会との適切な協議が含まれる。",
                        },
                        {
                            "id": "pal_p3_s8",
                            "en": "The RSPO reports that an increasing number of producers are committed to such sustainable practices.",
                            "ja": "RSPOは，そのような持続可能な慣行に取り組む生産者の数が増えていると報告している。",
                        },
                        {
                            "id": "pal_p3_s9",
                            "en": "Although certification is not a legal requirement, shoppers who want to support sustainable practices can now look for the RSPO symbol on palm-oil products.",
                            "ja": "認証は法的義務ではないが，持続可能な慣行を支持したい買い物客は今，パーム油製品にRSPOのマークを探すことができる。",
                        },
                    ],
                    [
                        {
                            "id": "pal_p4_s1",
                            "en": "Meanwhile, scientists at an environmental research organization, SMARTRI, are being paid to advise the oil palm industry on sustainable practices.",
                            "ja": "一方，環境調査団体SMARTRIの科学者たちは，持続可能な慣行についてパーム油産業に助言するために報酬を受け取っている。",
                        },
                        {
                            "id": "pal_p4_s2",
                            "en": "Scientists at SMARTRI believe that because palm oil is such an important crop, such partnerships are vital.",
                            "ja": "SMARTRIの科学者たちは，パーム油がこれほど重要な作物であるからこそ，そのようなパートナーシップは不可欠だと考えている。",
                        },
                        {
                            "id": "pal_p4_s3",
                            "en": "They point out that the Indonesian government's new laws to stop unethical practices of the past have not been successful because some forests and communities are still being destroyed by unethical companies.",
                            "ja": "彼らは，過去の非倫理的な慣行を止めるためのインドネシア政府の新しい法律は，非倫理的な企業によって森林や地域社会がいまだ破壊されているため，成功していないと指摘している。",
                        },
                        {
                            "id": "pal_p4_s4",
                            "en": "Critics who distrust the industry, however, suggest that the scientists' research is not independent.",
                            "ja": "しかし産業を信用しない批評家たちは，科学者の研究は独立していないと示唆している。",
                        },
                        {
                            "id": "pal_p4_s5",
                            "en": "They suspect that the companies' intentions are to pay the scientists to improve the industry's reputation while not changing their unethical practices.",
                            "ja": "彼らは，企業の意図は，非倫理的な慣行を変えずに，科学者に報酬を払って産業の評判を高めようとしているのではないかと疑っている。",
                        },
                        {
                            "id": "pal_p4_s6",
                            "en": "Others believe that any efforts to make the production of this important commodity more sustainable are worthwhile.",
                            "ja": "他の人々は，この重要な商品の生産をより持続可能にしようとする努力は，どれも価値があると考えている。",
                        },
                    ],
                ],
            }
        ],
        "questions": [
            {
                "question_id": "問1",
                "answer_number": 34,
                "points": 4,
                "stem": {
                    "en": "According to environmentalists, the production of palm oil [ 34 ].",
                    "ja": "環境保護論者によると，パーム油の生産は［34］。",
                },
                "choices": [
                    {
                        "label": "①",
                        "en": "created issues that are mostly ignored by consumers of palm oil products",
                        "ja": "問題を生み出したが，その大部分はパーム油製品の消費者から無視されている",
                        "is_correct": False,
                    },
                    {
                        "label": "②",
                        "en": "may decrease in time, so it is better to focus on other issues",
                        "ja": "やがて減少するかもしれないので，他の問題に焦点を当てた方がよい",
                        "is_correct": False,
                    },
                    {
                        "label": "③",
                        "en": "was affected by rumors started by other vegetable oil industries",
                        "ja": "他の植物油産業が流したうわさの影響を受けた",
                        "is_correct": False,
                    },
                    {
                        "label": "④",
                        "en": "will continue, so it is better to help make it more sustainable",
                        "ja": "今後も続くだろうから，より持続可能にするのを助ける方がよい",
                        "is_correct": True,
                    },
                ],
                "answer": "④",
                "explanation": {
                    "quoted_ja": "正解は④。第１段落末尾に，農家にとっての重要性を認め，より持続可能な生産を助けることに焦点を移しているとある。",
                    "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子",
                    "evidence_sentences": ["pal_p1_s5"],
                    "instructor_note": {
                        "ja": "they are instead focusing on helping them produce it in a more sustainable way が核。",
                        "points": [],
                    },
                },
            },
            {
                "question_id": "問2",
                "answer_number": 35,
                "points": 4,
                "stem": {
                    "en": (
                        "Out of the following four graphs, which illustrates the historical production of palm oil the best? [ 35 ]\n"
                        "(Layout: top-left panel = ①, top-right = ②, bottom-left = ③, bottom-right = ④ — same as the circled numbers in each panel.)"
                    ),
                    "ja": (
                        "次の４つのグラフのうち，歴史的なパーム油の生産の推移を最もよく表しているのはどれか。［35］\n"
                        "（配置：左上のグラフが①，右上が②，左下が③，右下が④。各グラフ左上の丸数字も同じ対応です。）"
                    ),
                },
                "figure_image": {
                    "src": "data/zkai/2026/round05/images/section07_q35_graph_choices.png",
                    "alt": "Palm oil production graphs ① to ④",
                    "caption_en": "① top left · ② top right · ③ bottom left · ④ bottom right",
                    "caption_ja": "解答の①〜④は、図の左上・右上・左下・右下の各パネルに対応します。",
                },
                "choices": [
                    {"label": "①", "en": "", "ja": "", "is_correct": False},
                    {"label": "②", "en": "", "ja": "", "is_correct": True},
                    {"label": "③", "en": "", "ja": "", "is_correct": False},
                    {"label": "④", "en": "", "ja": "", "is_correct": False},
                ],
                "answer": "②",
                "explanation": {
                    "quoted_ja": "正解は②。第３段落に，2018年の生産量，1990年代初めからの需要増，2006年までにインドネシアが最大産出国で現在マレーシアの2倍，など推移の手がかりがある。",
                    "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子",
                    "evidence_sentences": ["pal_p3_s1", "pal_p3_s2", "pal_p3_s3"],
                    "instructor_note": {
                        "ja": "図は左上が①・右上が②・左下が③・右下が④（各パネル左上の丸数字も同じ）。本文の数値と「交差」「2倍」を軸に照合する。",
                        "points": [
                            "第３段落の 2006 年までにインドネシアが最大，現在マレーシアの2倍，2018年の規模感が②の形と合う。",
                            "①のような高い出発・大きな落ち込みは本文と合わない。",
                            "③はインドネシアがマレーシアを追い越すのが遅すぎる。",
                            "④は2014前後の急ピークと下落が本文の説明と合いにくい。",
                        ],
                    },
                },
            },
            {
                "question_id": "問3",
                "answer_numbers": [36, 37],
                "unordered_slots": [36, 37],
                "points": 3,
                "answer_note": "順不同・両スロット正解で満点",
                "stem": {
                    "en": "According to the article, which two of the following tell us about the current situation in the palm oil industry? (Choose two options. The order does not matter.) [ 36 ] [ 37 ]",
                    "ja": "記事によると，次のうちどの２つがパーム油業界の現在の状況を述べているか。（２つの選択肢を選びなさい。順不同。）［36］［37］",
                },
                "choices_36": [
                    {
                        "label": "①",
                        "en": "Buyers have more options to choose sustainably-grown palm oil.",
                        "ja": "購入者には，持続可能な方法で栽培されたパーム油を選ぶより多くの選択肢がある。",
                        "is_correct": True,
                    },
                    {
                        "label": "②",
                        "en": "Communities near the plantations are being given a share of the profits.",
                        "ja": "プランテーション近くの地域社会には利益の一部が配分されている。",
                        "is_correct": False,
                    },
                    {
                        "label": "③",
                        "en": "Consumers are becoming less willing to use palm oil products.",
                        "ja": "消費者はパーム油製品を使う意欲を失いつつある。",
                        "is_correct": False,
                    },
                    {
                        "label": "④",
                        "en": "Governments have successfully stopped the burning of more forests.",
                        "ja": "政府は，これ以上の森林の焼き払いを食い止めることに成功した。",
                        "is_correct": False,
                    },
                    {
                        "label": "⑤",
                        "en": "Some companies have hired expert advisors to improve their practices.",
                        "ja": "一部の企業は慣行を改善するために専門のアドバイザーを雇っている。",
                        "is_correct": True,
                    },
                ],
                "choices_37": [
                    {
                        "label": "①",
                        "en": "Buyers have more options to choose sustainably-grown palm oil.",
                        "ja": "購入者には，持続可能な方法で栽培されたパーム油を選ぶより多くの選択肢がある。",
                        "is_correct": True,
                    },
                    {
                        "label": "②",
                        "en": "Communities near the plantations are being given a share of the profits.",
                        "ja": "プランテーション近くの地域社会には利益の一部が配分されている。",
                        "is_correct": False,
                    },
                    {
                        "label": "③",
                        "en": "Consumers are becoming less willing to use palm oil products.",
                        "ja": "消費者はパーム油製品を使う意欲を失いつつある。",
                        "is_correct": False,
                    },
                    {
                        "label": "④",
                        "en": "Governments have successfully stopped the burning of more forests.",
                        "ja": "政府は，これ以上の森林の焼き払いを食い止めることに成功した。",
                        "is_correct": False,
                    },
                    {
                        "label": "⑤",
                        "en": "Some companies have hired expert advisors to improve their practices.",
                        "ja": "一部の企業は慣行を改善するために専門のアドバイザーを雇っている。",
                        "is_correct": True,
                    },
                ],
                "answer": {"36": "①", "37": "⑤"},
                "explanation": {
                    "quoted_ja": "正解は①と⑤（順不同）。RSPOマークで持続可能な製品を選べること（第３段落後半），SMARTRIの科学者が産業に助言していること（第４段落冒頭）が根拠。",
                    "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子",
                    "evidence_sentences": ["pal_p3_s9", "pal_p4_s1"],
                    "instructor_note": {
                        "ja": "④は政府の法律が成功していないと否定される。③は現在の方針と矛盾しやすい。",
                        "points": [],
                    },
                },
            },
            {
                "question_id": "問4",
                "answer_number": 38,
                "points": 3,
                "stem": {
                    "en": "The best title for this article is [ 38 ].",
                    "ja": "この記事のタイトルとして最も適切なものは［38］である。",
                },
                "choices": [
                    {
                        "label": "①",
                        "en": "New Approaches to the Palm Oil Problem",
                        "ja": "パーム油の問題への新たなアプローチ",
                        "is_correct": True,
                    },
                    {
                        "label": "②",
                        "en": "Palm Oil is Not the Greenest Type of Oil",
                        "ja": "パーム油は最も環境にやさしい種類の油ではない",
                        "is_correct": False,
                    },
                    {
                        "label": "③",
                        "en": "The Consequences of Our Use of Palm Oil",
                        "ja": "私たちがパーム油を使うことの帰結",
                        "is_correct": False,
                    },
                    {
                        "label": "④",
                        "en": "The Importance of Helping Farmers in Southeast Asia",
                        "ja": "東南アジアの農家を助けることの重要性",
                        "is_correct": False,
                    },
                ],
                "answer": "①",
                "explanation": {
                    "quoted_ja": "正解は①。非倫理的生産への批判から，RSPOやSMARTRIによる持続可能性への取り組みへと焦点が移る流れが「問題への新たなアプローチ」に合う。",
                    "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子",
                    "evidence_sentences": ["pal_p1_s4", "pal_p1_s5", "pal_p3_s5", "pal_p4_s1"],
                    "instructor_note": {
                        "ja": "②は油種の比較，③は使用の帰結の予測，④は農家援助に限定され本文の焦点とずれる。",
                        "points": [],
                    },
                },
            },
        ],
        "vocabulary": {
            "passage": {
                "label_ja": "主な語彙",
                "items": [
                    {"en": "ecological", "ja": "生態学の；環境保護の"},
                    {"en": "palm oil", "ja": "パーム油；ヤシ油"},
                    {"en": "reputation", "ja": "評判"},
                    {"en": "burn down ~", "ja": "～を焼き払う"},
                    {"en": "carbon dioxide", "ja": "二酸化炭素"},
                    {"en": "consequently", "ja": "結果として"},
                    {"en": "environmentalist", "ja": "環境保護論者；環境問題専門家"},
                    {"en": "unethical", "ja": "倫理的でない"},
                    {"en": "sustainable", "ja": "持続可能な"},
                    {"en": "property", "ja": "特性"},
                    {"en": "use", "ja": "利用法"},
                    {"en": "solid", "ja": "固体の"},
                    {"en": "spread food", "ja": "塗り広げる食品"},
                    {"en": "preserve", "ja": "～を保存する"},
                    {"en": "spoil", "ja": "腐敗する"},
                    {"en": "crop", "ja": "農作物"},
                    {"en": "soybean", "ja": "大豆"},
                    {"en": "chemical", "ja": "化学物質"},
                    {"en": "plantation", "ja": "プランテーション；大農園"},
                    {"en": "contribute to ~", "ja": "～の一因となる"},
                    {"en": "significantly", "ja": "著しく；大いに"},
                    {"en": "deforestation", "ja": "森林破壊"},
                    {"en": "set up ~", "ja": "～を設立する"},
                    {"en": "certify", "ja": "～を認証する"},
                    {"en": "ethical source", "ja": "倫理的な供給源"},
                    {"en": "seek to do", "ja": "…しようと努める"},
                    {"en": "reduce", "ja": "～を減らす"},
                    {"en": "criteria", "ja": "評価基準"},
                    {"en": "minimal", "ja": "最小限の"},
                    {"en": "clear land", "ja": "土地を切り開く"},
                    {"en": "fair treatment", "ja": "公正な待遇"},
                    {"en": "sustainable practice", "ja": "持続可能な慣行"},
                    {"en": "vital", "ja": "極めて重要な；不可欠な"},
                    {"en": "critic", "ja": "批判的な人"},
                    {"en": "independent", "ja": "独立した"},
                    {"en": "suspect that ...", "ja": "…ではないかと疑う"},
                    {"en": "intention", "ja": "意図"},
                    {"en": "commodity", "ja": "商品；必需品"},
                    {"en": "worthwhile", "ja": "価値のある；無駄ではない"},
                    {"en": "consumer", "ja": "消費者", "note": "問1 ①"},
                    {"en": "share", "ja": "分配；分け前", "note": "問3 ②"},
                    {"en": "profit", "ja": "利益", "note": "問3 ②"},
                    {"en": "green", "ja": "環境にやさしい", "note": "問4 ②"},
                    {"en": "consequences", "ja": "（しばしば複数形で）結果；帰結", "note": "問4 ③"},
                ],
            }
        },
    }


def main():
    generate_graph_image()
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    data["sections"] = [s for s in data["sections"] if s.get("section_number") != 7]
    data["sections"].append(section7())
    impl = data["exam_info"].setdefault("implemented_sections", [])
    if 7 not in impl:
        impl.append(7)
        impl.sort()
    DATA_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("OK: section 7 merged, implemented_sections:", data["exam_info"]["implemented_sections"])


if __name__ == "__main__":
    main()
