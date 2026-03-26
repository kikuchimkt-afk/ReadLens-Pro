import json
import re

en_text = """
Cake, candy, soft drinks—most of us love sweet things. In fact, young people say "Sweet!" to mean something is "good" in English. When we think of sweetness, we imagine ordinary white sugar from sugar cane or sugar beet plants. Scientific discoveries, however, have changed the world of sweeteners. We can now extract sugars from many other plants. The most obvious example is corn. Corn is abundant, inexpensive, and easy to process. High fructose corn syrup (HFCS) is about 1.2 times sweeter than regular sugar, but quite high in calories. Taking science one step further, over the past 70 years scientists have developed a wide variety of artificial sweeteners.
A recent US National Health and Nutrition Examination Survey concluded that 14.6% of the average American's energy intake is from "added sugar," which refers to sugar that is not derived from whole foods. A banana, for example, is a whole food, while a cookie contains added sugar. More than half of added sugar calories are from sweetened drinks and desserts. Lots of added sugar can have negative effects on our bodies, including excessive weight gain and other health problems. For this reason, many choose low-calorie substitutes for drinks, snacks, and desserts.
Natural alternatives to white sugar include brown sugar, honey, and maple syrup, but they also tend to be high in calories. Consequently, alternative "low-calorie sweeteners" (LCSs), mostly artificial chemical combinations, have become popular. The most common LCSs today are aspartame, Ace-K, stevia, and sucralose. Not all LCSs are artificial—stevia comes from plant leaves.
Alternative sweeteners can be hard to use in cooking because some cannot be heated and most are far sweeter than white sugar. Aspartame and Ace-K are 200 times sweeter than sugar. Stevia is 300 times sweeter, and sucralose has twice the sweetness of stevia. Some new sweeteners are even more intense. A Japanese company recently developed "Advantame," which is 20,000 times sweeter than sugar. Only a tiny amount of this substance is required to sweeten something.
When choosing sweeteners, it is important to consider health issues. Making desserts with lots of white sugar, for example, results in high-calorie dishes that could lead to weight gain. There are those who prefer LCSs for this very reason. Apart from calories, however, some research links consuming artificial LCSs with various other health concerns. Some LCSs contain strong chemicals suspected of causing cancer, while others have been shown to affect memory and brain development, so they can be dangerous, especially for young children, pregnant women, and the elderly. There are a few relatively natural alternative sweeteners, like xylitol and sorbitol, which are low in calories. Unfortunately, these move through the body extremely slowly, so consuming large amounts can cause stomach trouble.
When people want something sweet, even with all the information, it is difficult for them to decide whether to stick to common higher calorie sweeteners like sugar or to use LCSs. Many varieties of gum and candy today contain one or more artificial sweeteners; nonetheless, some people who would not put artificial sweeteners in hot drinks may still buy such items. Individuals need to weigh the options and then choose the sweeteners that best suit their needs and circumstances.
"""

ja_text = """
ケーキ，キャンディー，清涼飲料水――我々のほとんどは甘い物が大好きだ。事実，英語では若者が何かが「良い」ということを言うのに，「スイート！」と言う。我々が甘さについて考えるとき，サトウキビやテンサイから作られる普通の白砂糖を想像する。しかしながら，科学的発見が甘味料の世界を一変させてしまった。今や多くのほかの植物から砂糖を抽出することが可能だ。最も分かりやすい例はトウモロコシである。トウモロコシは豊富で，安く，加工が簡単だ。高果糖コーンシロップ（HFCS）は普通の砂糖より1.2倍ほど甘く，非常に高カロリーである。科学をさらに一歩深めることで，この70年間にわたって，科学者はさまざまな人工甘味料を開発してきた。
最近の米国国民健康栄養調査は，平均的なアメリカ人のエネルギー摂取量の14.6%が「添加糖」，つまり自然食品に由来しない糖によるものであると結論づけた。たとえば，バナナは自然食品だが，一方クッキーには添加糖が入っている。添加糖のカロリーの半分以上は甘い飲み物やデザートからきている。大量の添加糖は肥満や他の健康問題を含む悪影響を我々の体に及ぼす。この理由のため，多くの人々は飲み物，お菓子，デザートに低カロリーの代替品を選んでいるのだ。
白砂糖の天然の代替品には黒砂糖，はちみつ，メープルシロップがあるが，それらもまたカロリーが高い傾向にある。その結果，他の「低カロリー甘味料」（LCSs）が，それらはほとんどが人工化学合成物質であるが，人気を集めてきた。今日の最も一般的なLCSsはアスパルテーム，Ace-K（アセスルファムカリウム），ステビア，スクラロースである。すべてのLCSsが人工物というわけではない――ステビアは植物の葉由来である。
代替甘味料は，加熱できないものがあり，またはとんどが白砂糖よりもずっと甘いので，料理に使うことが難しいかもしれない。アスパルテームとAce-Kは砂糖の200倍甘い。ステビアは砂糖の300倍甘く，スクラロースはステビアの2倍甘い。新しい甘味料の中にはもっと強烈なものもある。ある日本の企業は最近「アドバンテーム」を開発したが，それは砂糖の2万倍の甘さなのだ。何かを甘くするのにこの物質はごくわずかしか必要ではないのである。
甘味料を選ぶときには，健康問題を考慮することが大切だ。たとえば，大量の白砂糖を使用してデザートを作れば，結果として体重増加につながるかもしれない高カロリー料理ができてしまう。まさにこの理由のためにLCSsを好む人々がいるのだ。しかしカロリーは別として，人工LCSsの摂取をさまざまな他の健康不安に関連づける調査もある。発がん性を疑わせる強い化学物質を含むものや，記憶力や脳の発達に影響を与えることを示すLCSsもあるので，それらは特に幼い子ども，妊娠中の女性，お年寄りには危険かもしれないのだ。キシリトールやソルビトールなど，低カロリーで比較的自然の代替甘味料も多少ある。残念ながら，これらは体を通り抜けるのが極めて遅いため，大量に摂取すると胃の不調を起こす可能性がある。
甘い物が欲しいとき，たとえすべての情報を持っていたとしても，砂糖のような一般的な高カロリー甘味料にこだわるか，LCSsを使用するかを決めるのは困難である。今日，多くの種類のガムやキャンディーには1つ以上の人工甘味料が含まれている。それにもかかわらず，人工甘味料を温かい飲み物に決して入れない人でも，そのような商品を購入しているかもしれない。各人がそれらの甘味料を比較検討し，自分のニーズと状況にかなった甘味料を選択する必要があるのだ。
"""

en_paras = [p.strip() for p in en_text.strip().split('\n') if p.strip()]
ja_paras = [p.strip() for p in ja_text.strip().split('\n') if p.strip()]

paragraphs_out = []
sid = 1

for i, (ep, jp) in enumerate(zip(en_paras, ja_paras)):
    # Rough split by . and ! and ?
    es = [s.strip() + '.' for s in ep.replace('!', '!.').replace('?', '?.').split('. ') if s.strip()]
    if es and es[-1].endswith('..'): es[-1] = es[-1][:-1]
    
    js = jp.replace('。', '。\n').replace('！', '！\n').replace('？', '？\n').split('\n')
    js = [s.strip() for s in js if s.strip()]
    
    # Very manual fix for Paragraph alignments if needed
    if len(es) != len(js):
        print(f"Warning: Para {i} mismatch. EN: {len(es)}, JA: {len(js)}")
        # Simple fix: merge last ones
        if len(es) < len(js):
            js = js[:len(es)-1] + [" ".join(js[len(es)-1:])]
        else:
            es = es[:len(js)-1] + [" ".join(es[len(js)-1:])]
            
    p_out = []
    for eng, jpn in zip(es, js):
        p_out.append({
            "id": f"6b_s{sid}",
            "en": eng,
            "ja": jpn
        })
        sid += 1
    paragraphs_out.append(p_out)

# Now, we manually construct the section structure
sec6b = {
    "section_number": "6B",
    "title": "第6問 B",
    "points": 12,
    "pdf_pages": [32, 33, 34, 35],
    "passage_images": [
        "images/mondai_p32.png",
        "images/mondai_p33.png"
    ],
    "explanation_images": [
        "images/kaitou_p20.png",
        "images/kaitou_p21.png",
        "images/kaitou_p22.png"
    ],
    "situation": {
        "en": "You are studying nutrition in health class. You are going to read the following passage from a textbook to learn more about various sweeteners.",
        "ja": "あなたは保健の授業で栄養について勉強しています。さまざまな甘味料についてもっと学ぶため，教科書から次の文章を読む予定です。"
    },
    "passages": [
        {
            "id": "textbook",
            "title": {
                "en": "Sweeteners",
                "ja": "甘味料"
            },
            "paragraphs": paragraphs_out
        }
    ],
    "questions": [
        {
            "question_id": "問1",
            "answer_number": 43,
            "stem": {
                "en": "You learn that modern science has changed the world of sweeteners by [ 43 ]",
                "ja": "「あなたは現代科学が [ 43 ] によって甘味料の世界を一変させてしまったことを学んだ。」"
            },
            "choices": [
                {
                    "label": "①",
                    "en": "discovering new, sweeter white sugar types",
                    "ja": "より甘い新種の白砂糖を発見したこと",
                    "is_correct": False
                },
                {
                    "label": "②",
                    "en": "measuring the energy intake of Americans",
                    "ja": "アメリカ人のエネルギー摂取量を測定すること",
                    "is_correct": False
                },
                {
                    "label": "③",
                    "en": "providing a variety of new options",
                    "ja": "さまざまな新しい選択肢を提供すること",
                    "is_correct": True
                },
                {
                    "label": "④",
                    "en": "using many newly-developed plants from the environment",
                    "ja": "自然環境から新たに開発されたたくさんの植物を使用すること",
                    "is_correct": False
                }
            ],
            "answer": "③",
            "explanation": {
                "ja": "設問は，第1段落第4文の Scientific discoveries ... have changed the world of sweeteners. (科学的発見が甘味料の世界を一変させてしまった。) の言い換えなので，「科学的発見」は何かを探す。まずは第1段落第5文に，We can now extract sugars from many other plants. (今や多くのほかの植物から砂糖を抽出することが可能だ。) とあるように，「サトウキビやテンサイから作る白砂糖以外にも，トウモロコシのような他の植物から甘味料が作れるようになったこと」が1つである。次に，第1段落最終文に，Taking science one step further, over the past 70 years scientists have developed a wide variety of artificial sweeteners. (科学をさらに一歩深めることで，この70年間にわたって，科学者はさまざまな人工甘味料を開発してきた。) とあるように，「人工甘味料を開発したこと」である。したがって，従来の白砂糖以外のこれらの新しい甘味料を「さまざまな新しい選択肢の提供」と言い換えている③が正解。",
                "evidence_sentences": ["6b_s5", "6b_s9"]
            }
        },
        {
            "question_id": "問2",
            "answer_number": 44,
            "stem": {
                "en": "You are summarizing the information you have just studied. How should the table be finished? [ 44 ]",
                "ja": "「あなたは今勉強したことを要約している。どのように表を完成させるべきか。」"
            },
            "graph_image": "images/mondai_p34_graph.png",
            "choices": [
                {
                    "label": "①",
                    "en": "(A) Stevia, (B) Sucralose, (C) Ace-K, Aspartame, (D) HFCS",
                    "ja": "(A) ステビア, (B) スクラロース, (C) Ace-K, アスパルテーム, (D) HFCS",
                    "is_correct": False
                },
                {
                    "label": "②",
                    "en": "(A) Stevia, (B) Sucralose, (C) HFCS, (D) Ace-K, Aspartame",
                    "ja": "(A) ステビア, (B) スクラロース, (C) HFCS, (D) Ace-K, アスパルテーム",
                    "is_correct": False
                },
                {
                    "label": "③",
                    "en": "(A) Sucralose, (B) Stevia, (C) Ace-K, Aspartame, (D) HFCS",
                    "ja": "(A) スクラロース, (B) ステビア, (C) Ace-K, アスパルテーム, (D) HFCS",
                    "is_correct": True
                },
                {
                    "label": "④",
                    "en": "(A) Sucralose, (B) Stevia, (C) HFCS, (D) Ace-K, Aspartame",
                    "ja": "(A) スクラロース, (B) ステビア, (C) HFCS, (D) Ace-K, アスパルテーム",
                    "is_correct": False
                }
            ],
            "answer": "③",
            "explanation": {
                "ja": "甘味料を甘いものから順に並べる問題。各甘味についての記述は以下の通り。\n・HFCS: 第1段落第8文: High fructose corn syrup (HFCS) is about 1.2 times sweeter than regular sugar (高果糖コーンシロップ（HFCS）は普通の砂糖より1.2倍ほど甘い)\n・Ace-K, アスパルテーム: 第4段落第2文: Aspartame and Ace-K are 200 times sweeter than sugar. (アスパルテームとAce-Kは砂糖の200倍甘い。)\n・ステビア: 第4段落第3文: Stevia is 300 times sweeter (than sugar) (ステビアは（砂糖の）300倍甘い)\n・スクラロース: 第4段落第3文: sucralose has twice the sweetness of stevia (スクラロースはステピアの2倍甘い)\nしたがって，甘い順に，スクラロース→ステビア→Ace-K, アスパルテーム→HFCSとなるので，③が正解。",
                "evidence_sentences": ["6b_s8", "6b_s21", "6b_s22"]
            }
        },
        {
            "question_id": "問3",
            "answer_number": "45, 46",
            "stem": {
                "en": "According to the article you read, which of the following are true? (Choose two options. The order does not matter.) [ 45 ] ・ [ 46 ]",
                "ja": "「あなたが読んだ記事によると，次のうち正しいのはどれか。」（2つの選択肢を選びなさい。順不同。）"
            },
            "choices": [
                {
                    "label": "①",
                    "en": "Alternative sweeteners have been proven to cause weight gain.",
                    "ja": "代替甘味料は体重増加を引き起こすことが証明されている。",
                    "is_correct": False
                },
                {
                    "label": "②",
                    "en": "Americans get 14.6% of their energy from alternative sweeteners.",
                    "ja": "アメリカ人は代替甘味料から14.6%のエネルギーを得ている。",
                    "is_correct": False
                },
                {
                    "label": "③",
                    "en": "It is possible to get alternative sweeteners from plants.",
                    "ja": "植物から代替甘味料を得ることは可能だ。",
                    "is_correct": True
                },
                {
                    "label": "④",
                    "en": "Most artificial sweeteners are easy to cook with.",
                    "ja": "大部分の人工甘味料は料理に使うことが簡単だ。",
                    "is_correct": False
                },
                {
                    "label": "⑤",
                    "en": "Sweeteners like xylitol and sorbitol are not digested quickly.",
                    "ja": "キシリトールやソルビトールのような甘味料は素早く消化されない。",
                    "is_correct": True
                }
            ],
            "answer": "③, ⑤",
            "explanation": {
                "ja": "第3段落最終文，Not all LCSs are artificial - stevia comes from plant leaves. (すべてのLCSsが人工物というわけではない――ステビアは植物の葉由来である。) から，植物から代替甘味料が得られることがわかるので，③は正解。第5段落第7文では，キシリトールやソルビトールなどの代替甘味料について，these move through the body extremely slowly, so consuming large amounts can cause stomach trouble (これらは体を通り抜けるのが極めて遅いため，大量に摂取すると胃の不調を起こす可能性がある) とあるので，これを are not digested quickly (素早く消化されない) と言い換えた⑤も正解。",
                "evidence_sentences": ["6b_s19", "6b_s32"]
            }
        },
        {
            "question_id": "問4",
            "answer_number": 47,
            "stem": {
                "en": "To describe the author's position, which of the following is most appropriate? [ 47 ]",
                "ja": "「筆者の立場を述べるにあたり，次のうち最も適切なものはどれか。」"
            },
            "choices": [
                {
                    "label": "①",
                    "en": "The author argues against the use of artificial sweeteners in drinks and desserts.",
                    "ja": "筆者は飲み物やデザートに人工甘味料を使用することに反対だ。",
                    "is_correct": False
                },
                {
                    "label": "②",
                    "en": "The author believes artificial sweeteners have successfully replaced traditional ones.",
                    "ja": "筆者は人工甘味料が従来の甘味料に取って代わることに成功したと信じている。",
                    "is_correct": False
                },
                {
                    "label": "③",
                    "en": "The author states that it is important to invent much sweeter products for future use.",
                    "ja": "筆者は将来的な使用のためにもっと甘い製品を開発することが重要だと述べている。",
                    "is_correct": False
                },
                {
                    "label": "④",
                    "en": "The author suggests people focus on choosing sweeteners that make sense for them.",
                    "ja": "筆者は，自分が納得する甘味料を選ぶことに焦点を当てるよう提案している。",
                    "is_correct": True
                }
            ],
            "answer": "④",
            "explanation": {
                "ja": "筆者は本文最終文で，Individuals need to weigh the options and then choose the sweeteners that best suit their needs and circumstances. (各人がそれらの甘味料を比較検討し，自分のニーズと状況にかなったものを選択する必要があるのだ。) と，全体の結論として自分の意見を述べている。これを言い換えた④が正解。第5段落第1〜5文で，筆者は人工甘味料であるLCSsの利点と懸念点の両方を挙げている。利点は，白砂糖に比べて低カロリーであること。懸念点は，がんや記憶力や脳の発達に影響を与える可能性があることだ。一方的な立場に偏っていないことから，①や②は不適当。③について，本文ではより甘い製品の開発が重要だとは述べられていないので，不適当。",
                "evidence_sentences": ["6b_s36"]
            }
        }
    ]
}

with open(r"g:\マイドライブ\ReadLens Pro\data\kakomon\2021_1\sec6b.json", "w", encoding="utf-8") as f:
    json.dump(sec6b, f, ensure_ascii=False, indent=2)

print("Generated sec6b.json")
