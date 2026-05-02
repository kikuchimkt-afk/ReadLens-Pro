# -*- coding: utf-8 -*-
"""駿台2026 第5回 第7問セクションを生成し data.json にマージする。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

P1 = [
    ("v_p1_s1", "When you think of viruses, you probably think of disease.", "ウイルスと言えば，あなたはおそらく病気を思い浮かべるだろう。"),
    ("v_p1_s2", "After all, viruses are responsible for many of the illnesses that regularly affect humans.", "何といっても，ウイルスは頻繁に人間を襲う病気の多くの原因なのだ。"),
    ("v_p1_s3", "Influenza, the common cold, COVID-19, and countless other diseases are caused by viruses that specifically infect humans.", "インフルエンザや一般的な風邪，COVID-19やそのほか数えきれない病気が，特にヒトに伝染するウイルスによって引き起こされている。"),
    ("v_p1_s4", "For that reason, many people believe that all viruses are bad and must be avoided at all costs.", "そのため多くの人が，すべてのウイルスは悪いもので何としても避けなくてはならないものだと信じている。"),
    ("v_p1_s5", "However, that is not strictly true.", "しかし，それは厳密に言うと正しくない。"),
    ("v_p1_s6", "There are many viruses that live inside us that are not responsible for disease at all.", "私たちの体内にあって病気の原因にはまったくならないウイルスもたくさんある。"),
    ("v_p1_s7", "In fact, the opposite is true, because many viruses that live inside our digestive systems actually keep us healthy by killing harmful bacteria.", "実際，本当はその正反対なのである。なぜなら私たちの消化器系の中に住んでいる多くのウイルスは，有害な細菌を殺すことによって，実際には私たちの健康を保っていてくれるのだから。"),
    ("v_p1_s8", 'Those viruses are called "bacteriophages," and they do not harm human cells at all.', "そういうウイルスは「バクテリオファージ［殺菌ウイルス］」と呼ばれ，ヒトの細胞を害することは全くない。"),
    ("v_p1_s9", "Moreover, scientists have also been researching other types of viruses that can kill cancer cells.", "さらに科学者たちは，がん細胞を殺せる他の種類のウイルスもずっと研究し続けている。"),
    ("v_p1_s10", "These cancer-killing viruses have already been used to treat skin cancer in patients, and it is hoped that more treatment of this kind will be developed in the future.", "これらの抗がんウイルスはすでに患者の皮膚がんを治療するために使われており，将来はこのような種類の治療がもっと開発されることが期待されているのだ。"),
]

P2 = [
    ("v_p2_s1", 'The interesting thing about viruses is that they are not really "alive."', "ウイルスについて興味深いことは，それらが本当は「生きて」などいないということだ。"),
    ("v_p2_s2", "They are not made out of cells, and they cannot make energy or reproduce by themselves.", "ウイルスは細胞でできているのではなく，エネルギーを作り出すことも自己増殖することもできない。"),
    ("v_p2_s3", "In simple terms, they are just a small piece of genetic material, such as DNA, surrounded by a protein case.", "簡単な言葉で言うと，それらはタンパク質の外被に囲まれた，DNAのような遺伝物質の小さなかけらにすぎない。"),
    ("v_p2_s4", "Because viruses are very simple structures, they are very small.", "ウイルスは非常に単純な構造をしているので，非常に小さい。"),
    ("v_p2_s5", "In fact, most viruses are 100-times smaller than a human cell.", "実際ほとんどのウイルスはヒトの細胞の100分の1の小ささだ。"),
    ("v_p2_s6", "They are so small that they cannot be seen under a standard microscope.", "非常に小さいので通常の顕微鏡では見ることができない。"),
    ("v_p2_s7", "However, it's a virus's size and structure that allows it to bind to the outside of a host cell, insert its genetic instructions, then use the host cell's machinery to make copies of itself.", "しかし，ウイルスが宿主になる細胞の外側に付着してその遺伝子の指示を注入し，それから自分のコピーを作り出すために宿主細胞の機構を利用することができるのは，その小ささと構造のおかげなのだ。"),
    ("v_p2_s8", "The attack on a cell by a virus in this way usually results in the death of the host cell.", "このようにしてウイルスが細胞を攻撃すると，その結果，たいてい宿主細胞は死んでしまう。"),
]

P3 = [
    ("v_p3_s1", "It is a virus's ability to kill a host cell that has allowed researchers to develop cancer treatments using viruses.", "研究者たちがウイルスを使ったがん治療を開発できたのは，宿主細胞を殺してしまうというウイルスの能力のおかげだ。"),
    ("v_p3_s2", "In 2015, the first virus treatment for cancer was approved by the US government for use on patients.", "2015年に初めて，ウイルスを使用したがん治療を患者に実施してよいという合衆国政府からの認可が得られた。"),
    ("v_p3_s3", "Scientists used a herpes virus, which usually causes mouth sores in humans.", "科学者たちは，たいていヒトの口腔に炎症を作り出す原因となるヘルペスウイルスを使った。"),
    ("v_p3_s4", "They modified the outer protein case of the virus so that it ignored healthy cells and attached itself to the outside of cancer cells.", "彼らはウイルスのタンパク質の外被を変異させ，ウイルスが健康な細胞を無視し，がん細胞の外側に取り付くようにした。"),
    ("v_p3_s5", "They also modified the genetic material of the virus so that it produced molecules called antigens that would attract human immune cells to the site of the cancer.", "またウイルスの遺伝子物質をも変異させ，ウイルスが抗原［アンチゲン］と呼ばれる分子を生産するようにした。抗原はヒトの免疫細胞をがんの患部へと引き寄せるのである。"),
    ("v_p3_s6", "Doctors could then inject these modified viruses into the site of the cancer every two weeks.", "すると医師たちはこれらの変異したウイルスをがんの患部に2週間ごとに注入できる。"),
    ("v_p3_s7", "The viruses would use the cancer cells to reproduce, killing the host cells in the process.", "それらのウイルスは増殖するためにがん細胞を利用し，そしてその過程で宿主細胞を殺してしまうのである。"),
    ("v_p3_s8", "The body's immune system would also attack the cancer cells itself.", "人体の免疫システムもまた，自分自身でがん細胞を攻撃する。"),
    ("v_p3_s9", "In this way, large skin cancer tumors have been destroyed.", "このようにして，大きな皮膚がんの腫瘍が破壊されてしまう。"),
]

P4 = [
    ("v_p4_s1", "There are many benefits of this treatment compared to standard medicine.", "この治療法には普通の薬と比べて多くの良い点がある。"),
    ("v_p4_s2", "First, there are fewer bad side effects because the virus only attacks cancer cells and leaves healthy cells alone.", "第1に，ウイルスはがん細胞を攻撃するだけで健康な細胞には手を付けないので，悪い副作用が少ない。"),
    ("v_p4_s3", "It is also a good way to treat skin tumors that cannot be removed by surgery.", "またそれは，外科手術では取り除けない皮膚腫瘍を治療するのにもよい方法だ。"),
    ("v_p4_s4", "In addition, the viruses are injected directly into the tumor, so the treatment is targeted by location.", "さらに，ウイルスは腫瘍に直接注入されるので，治療は患部に的を絞って行われる。"),
    ("v_p4_s5", "This treatment is also easier for patients because it involves short visits to a doctor instead of long stays in hospital.", "この治療法は病院に長く入院するのでなく，短時間通院すればよいので，患者にとっても楽だ。"),
    ("v_p4_s6", "On the other hand, there may be mild side effects such as fever and tiredness.", "他方，熱や疲労感といった軽い副作用がある可能性がある。"),
    ("v_p4_s7", "In addition, this treatment cannot be used on patients with weak immune systems.", "さらに，この治療法は免疫システムの弱い患者には使えない。"),
]

P5 = [
    ("v_p5_s1", "Currently, scientists are testing a similar treatment for patients with an eye disease that causes vision to gradually decline.", "現在科学者たちは，視力が徐々に弱まっていく眼病の患者たちに同様の治療法を試みている。"),
    ("v_p5_s2", "Scientists have altered the genetic information in a virus so that it can deliver treatment to the eyes of patients with this disease to stop the vision loss.", "科学者たちはこの病気の患者の視力が失われるのを阻止するため，目に治療を届けられるように，ウイルスの中の遺伝子情報を変化させた。"),
    ("v_p5_s3", "This treatment has been successful on laboratory mice, and it is hoped that it can be used in humans in the near future.", "実験室のネズミについてはこの治療は成功しており，近い将来人間にも実施できると期待されている。"),
    ("v_p5_s4", "However, one of the biggest challenges associated with this type of therapy is preventing the body's own immune system from identifying and killing the virus before it can deliver its important package to the cells that need it.", "しかし，このタイプの治療法に伴う最大の難問の1つは，ウイルスがその重要な内包物を，それを必要としている細胞に届けないうちに，人体自身の免疫システムがそのウイルスを見分けて殺してしまうのを防ぐことだ。"),
]

P6 = [
    ("v_p6_s1", "In summary, viruses can be used for good.", "要約すると，ウイルスは善用できる。"),
    ("v_p6_s2", "They can be used to fight cancer and deliver important genes to the site of genetic disease.", "がんと闘い，遺伝子病の患部に重要な遺伝子を届けるために利用できる。"),
    ("v_p6_s3", "In the future, many other human diseases may be cured by specially adapted viruses.", "将来は，その他の多くの人間の病気が，特別に改作されたウイルスによって治せるかもしれない。"),
]


def para(rows):
    return [{"id": i, "en": e, "ja": j} for i, e, j in rows]


section_07 = {
    "section_number": 7,
    "title": "第7問",
    "points": 16,
    "description": "長文読解（生物学・発表スライド）",
    "situation": {
        "intro_sentences": [
            {
                "id": "sit_r5_q7_s1",
                "en": "You are in a student group preparing for a university biology presentation.",
                "ja": "あなたは大学の生物学の発表の準備をしている学生グループの一員です。",
            },
            {
                "id": "sit_r5_q7_s2",
                "en": "You are using the following passage to create your part of the presentation on useful viruses.",
                "ja": "役に立つウイルスについての発表の，自分の担当部分を作るために次の一節を利用しています。",
            },
        ]
    },
    "passages": [
        {
            "id": "virus_article",
            "paragraphs": [para(P1), para(P2), para(P3), para(P4), para(P5), para(P6)],
        },
        {
            "id": "virus_slides",
            "title": {"en": "Your presentation slides:", "ja": "あなたの発表用のスライド："},
            "presentation_image": "images/q07_presentation_slides.png",
        },
    ],
    "questions": [
        {
            "question_id": "問1",
            "answer_number": 32,
            "points": 3,
            "stem": {
                "sentences": [
                    {
                        "id": "q7_q1_st",
                        "en": "Which of the following should you <u>not</u> include for [32]?",
                        "ja": "[32] に入れるべき<u>でない</u>のは次のうちどれか。",
                    }
                ]
            },
            "choices": [
                {
                    "label": "①",
                    "en": "Help human cells reproduce quickly",
                    "ja": "ヒトの細胞の速やかな増殖を助ける",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "Most viruses are one-hundredth the size of a human cell",
                    "ja": "ほとんどのウイルスはヒトの細胞の100分の1の大きさである",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "No reproduction without a host",
                    "ja": "宿主細胞がなければ増殖できない",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "Reproduction usually kills the host cell",
                    "ja": "増殖するとたいてい宿主細胞を殺してしまう",
                    "is_correct": False,
                },
                {
                    "label": "⑤",
                    "en": "Simple genetic material in a protein case",
                    "ja": "たんぱく質の外被に包まれた単純な遺伝子物質",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": "正解は①。ウイルスについての基本的な情報は第2段落に書かれている。本文の内容と一致しないものを選ぶことに注意する。②は第5文，③は第2文および第7文，⑤は第3文，④は最終文と一致する。①はウイルスの特徴として本文に書かれていない。",
                "quoted_source": "駿台『2026年駿台実戦問題集 英語リーディング』第5回 解説冊子",
                "evidence_sentences": ["v_p2_s2", "v_p2_s3", "v_p2_s5", "v_p2_s7", "v_p2_s8"],
                "instructor_note": {
                    "ja": "NOT 問題は「本文にない／言い換えが成立しない」選択肢を選ぶ。①はヒト細胞を助けるという記述はどこにもない。",
                    "points": [
                        "②: 100分の1の大きさ（第5文）",
                        "③④: 宿主細胞・増殖・死（第2・7・最終文）",
                    ],
                },
            },
        },
        {
            "question_id": "問2",
            "answer_numbers": [33, 34],
            "unordered_slots": [33, 34],
            "points": 4,
            "stem": {
                "sentences": [
                    {
                        "id": "q7_q2_st_a",
                        "en": 'For the Benefits of This Treatment slide, select two aspects of this treatment that are beneficial to the patient. (The order does not matter.)',
                        "ja": "スライドの「この治療法のよい点」に，この治療法の患者にとって利益となる側面を2つ選んで入れなさい（順番は問わない）。",
                    }
                ]
            },
            "choices_33": [
                {
                    "label": "①",
                    "en": "By using modified herpes viruses, the patient also becomes immune to future herpes infections.",
                    "ja": "変異ヘルペスウイルスを使うことで，患者は将来ヘルペスに感染しない免疫も獲得できる。",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "It is not so hard on the patient because it only requires short visits to a doctor.",
                    "ja": "医師のところに短時間通院するだけでよいので患者の負担が少ない。",
                    "is_correct": True,
                },
                {
                    "label": "③",
                    "en": "It is usually used to make the removal of tumors by surgery much easier and faster.",
                    "ja": "外科手術で腫瘍を取り除くことをずっと楽で速くするために使われることが普通である。",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "The modified herpes viruses are adapted to attack only cancer cells, so healthy cells do not die.",
                    "ja": "変異ヘルペスウイルスはがん細胞だけを攻撃するように改作されているので，健康な細胞は死なない。",
                    "is_correct": True,
                },
                {
                    "label": "⑤",
                    "en": "This treatment causes no side effects, unlike cancer medicine which causes fever.",
                    "ja": "発熱を伴うがんの治療薬とは違い，この治療法には副作用がない。",
                    "is_correct": False,
                },
            ],
            "choices_34": [
                {
                    "label": "①",
                    "en": "By using modified herpes viruses, the patient also becomes immune to future herpes infections.",
                    "ja": "変異ヘルペスウイルスを使うことで，患者は将来ヘルペスに感染しない免疫も獲得できる。",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "It is not so hard on the patient because it only requires short visits to a doctor.",
                    "ja": "医師のところに短時間通院するだけでよいので患者の負担が少ない。",
                    "is_correct": True,
                },
                {
                    "label": "③",
                    "en": "It is usually used to make the removal of tumors by surgery much easier and faster.",
                    "ja": "外科手術で腫瘍を取り除くことをずっと楽で速くするために使われることが普通である。",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "The modified herpes viruses are adapted to attack only cancer cells, so healthy cells do not die.",
                    "ja": "変異ヘルペスウイルスはがん細胞だけを攻撃するように改作されているので，健康な細胞は死なない。",
                    "is_correct": True,
                },
                {
                    "label": "⑤",
                    "en": "This treatment causes no side effects, unlike cancer medicine which causes fever.",
                    "ja": "発熱を伴うがんの治療薬とは違い，この治療法には副作用がない。",
                    "is_correct": False,
                },
            ],
            "answer": {"33": "②", "34": "④"},
            "answer_note": "順不同・両スロット正解で満点",
            "explanation": {
                "quoted_ja": "正解は②と④（順不同）。ウイルスを使った治療法の特徴については第4段落に書かれている。第2文に「がん細胞を攻撃するだけで健康な細胞には手を付けないので，悪い副作用が少ない」とあり④と一致する。第5文に「短時間通院すればよいので，患者にとっても楽だ」とあり②と一致する。①の記述はない。③は外科手術では取り除けない腫瘍向けと書いてあり矛盾する。第6文は軽い副作用の可能性があるとあり⑤と矛盾する。",
                "quoted_source": "駿台『2026年駿台実戦問題集 英語リーディング』第5回 解説冊子",
                "evidence_sentences": ["v_p4_s2", "v_p4_s5", "v_p4_s3", "v_p4_s6"],
                "instructor_note": {
                    "ja": "メリットは第4段落の fewer side effects / short visits の2点が核。",
                    "points": ["④: only cancer cells", "②: short visits vs hospital stay"],
                },
            },
        },
        {
            "question_id": "問3",
            "answer_number": 35,
            "points": 3,
            "stem": {
                "sentences": [
                    {
                        "id": "q7_q3_st",
                        "en": "Complete the missing labels on the illustration for the How the Treatment Works slide [35].",
                        "ja": "スライド「どのように治療法は働くのか」の図に付けるラベルを完成させよ［35］。",
                    }
                ]
            },
            "choices": [
                {
                    "label": "①",
                    "en": "(A) antigens, (B) immune cell, (C) modified virus",
                    "ja": "(A) 抗原，(B) 免疫細胞，(C) 変異したウイルス",
                    "is_correct": False,
                },
                {
                    "label": "②",
                    "en": "(A) antigens, (B) modified virus, (C) immune cell",
                    "ja": "(A) 抗原，(B) 変異したウイルス，(C) 免疫細胞",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "(A) immune cell, (B) modified virus, (C) antigens",
                    "ja": "(A) 免疫細胞，(B) 変異したウイルス，(C) 抗原",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "(A) modified virus, (B) antigens, (C) immune cell",
                    "ja": "(A) 変異したウイルス，(B) 抗原，(C) 免疫細胞",
                    "is_correct": True,
                },
                {
                    "label": "⑤",
                    "en": "(A) modified virus, (B) immune cell, (C) antigens",
                    "ja": "(A) 変異したウイルス，(B) 免疫細胞，(C) 抗原",
                    "is_correct": False,
                },
            ],
            "answer": "④",
            "explanation": {
                "quoted_ja": "正解は④。第3段落第4文で外被を変異させがん細胞に取り付くのが変異ウイルスなので(A)は modified virus。第5文で抗原が免疫細胞を引き寄せるので(B)は antigens，(C)は immune cells。",
                "quoted_source": "駿台『2026年駿台実戦問題集 英語リーディング』第5回 解説冊子",
                "evidence_sentences": ["v_p3_s4", "v_p3_s5", "v_p3_s7"],
                "instructor_note": {
                    "ja": "注射される粒＝ウイルス，細胞内・破片まわり＝抗原→免疫細胞の流れを図と照合する。",
                    "points": [
                        "(A) 注入物＝modified virus（第4文の attach to cancer）。",
                        "(B)(C) antigen が immune cells を引き寄せる（第5文）。",
                        "細胞破片フェーズでは抗原が免疫応答の目印になるイメージ。",
                    ],
                },
            },
        },
        {
            "question_id": "問4",
            "answer_number": 36,
            "points": 3,
            "stem": {
                "sentences": [
                    {
                        "id": "q7_q4_st",
                        "en": "Which is the best statement for the final slide? [36]",
                        "ja": "最後のスライドに最適な記述はどれか［36］。",
                    }
                ]
            },
            "choices": [
                {
                    "label": "①",
                    "en": "Although many viruses cause disease, some are actually beneficial to humans. Furthermore, some viruses can be adapted so that they target and kill unhealthy cells.",
                    "ja": "多くのウイルスが病気を引き起こすが，実は人間に恩恵をもたらすものもある。さらに，不健康な細胞に的を絞って殺すことができるように一部のウイルスを変異させることができる。",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "In the future, our knowledge of viruses will help us cure diseases such as cancer. However, until this technology develops, viruses are dangerous to humans.",
                    "ja": "将来，ウイルスに関する私たちの知識ががんのような病気を治すのに役立つだろう。しかし，この科学技術が発達するまでは，ウイルスは人間にとって危険なものである。",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "The number of viruses that cure diseases is greater than the number that cause them, so their negative reputation is no longer deserved.",
                    "ja": "病気を治すウイルスの方が病気を引き起こすウイルスよりも数が多い。だからウイルスに対する否定的な評価はもはやふさわしくない。",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "Viruses that cause disease and illness have sometimes evolved to cure diseases such as cancer in humans.",
                    "ja": "病気を引き起こすウイルスは，時にはがんのようなヒトの病気を治すように進化したことがある。",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": "正解は①。第1段落第7文の消化器系の善玉ウイルスと，第3段落のがん細胞狙いの改作という2線が①にまとまる。②は既に皮膚がん治療に使われている記述と矛盾。③は数の比較の記述なし。④は科学者が改作したのであり自然進化ではない。",
                "quoted_source": "駿台『2026年駿台実戦問題集 英語リーディング』第5回 解説冊子",
                "evidence_sentences": ["v_p1_s7", "v_p3_s4", "v_p1_s10"],
                "instructor_note": {
                    "ja": "結論は「害もあるが益もあり／改作して治療」が軸。進化(evolved)に誘惑されない。",
                    "points": [
                        "beneficial: 消化器の善玉ウイルス（第1段落）。",
                        "adapted: 科学者が modify／研究者開発（第3段落）。",
                        "②の dangerous until は本文の既に治療使用中と矛盾。",
                    ],
                },
            },
        },
        {
            "question_id": "問5",
            "answer_number": 37,
            "points": 3,
            "stem": {
                "sentences": [
                    {
                        "id": "q7_q5_st",
                        "en": "Why is the body's own immune system a barrier to the effectiveness of virus-based treatments? [37]",
                        "ja": "人体自身の免疫システムがウイルスを使った治療法の効果にとって障害になるのはなぜか［37］。",
                    }
                ]
            },
            "choices": [
                {
                    "label": "①",
                    "en": "The body's immune system may find the virus and kill it before it can treat the disease.",
                    "ja": "人体の免疫システムは，ウイルスが病気を治療する前にそれを見つけて殺してしまう可能性がある。",
                    "is_correct": True,
                },
                {
                    "label": "②",
                    "en": "The human immune system is not good at reacting to viruses that enter the body.",
                    "ja": "ヒトの免疫システムは体内に侵入してくるウイルスにうまく反応できない。",
                    "is_correct": False,
                },
                {
                    "label": "③",
                    "en": "Viruses cannot be recognized by the human immune system so the treatment is useless.",
                    "ja": "ヒトの免疫システムはウイルスを認識できないので，その治療は役に立たない。",
                    "is_correct": False,
                },
                {
                    "label": "④",
                    "en": "Viruses may cause the body's immune system to kill healthy cells instead of cancer cells.",
                    "ja": "ウイルスが原因で，人体の免疫システムが，がん細胞でなく健康な細胞を殺してしまう。",
                    "is_correct": False,
                },
            ],
            "answer": "①",
            "explanation": {
                "quoted_ja": "正解は①。第5段落最終文が，免疫系がウイルスを識別して殺すことを防ぐのが難題だと述べる。③は認識できないと書いてあり本文と矛盾。",
                "quoted_source": "駿台『2026年駿台実戦問題集 英語リーディング』第5回 解説冊子",
                "evidence_sentences": ["v_p5_s4"],
                "instructor_note": {
                    "ja": "先にウイルスが排除されると遺伝子配送が届かない、というパラドックス。",
                    "points": [
                        "deliver its important package が鍵（標的細胞への荷渡し）。",
                        "identifying and killing the virus = ① の paraphrase。",
                        "③は immune が認識できないと書いてあるので本文と正反対。",
                    ],
                },
            },
        },
    ],
    "vocabulary": {
        "lead_text": {
            "label_ja": "リード文",
            "items": [
                {"en": "biology", "pos": "名", "ja": "生物学"},
                {"en": "presentation", "pos": "名", "ja": "発表"},
                {"en": "useful", "pos": "形", "ja": "役に立つ"},
            ],
        },
        "p1": {
            "label_ja": '第1段落（When you think ... で始まる）',
            "items": [
                {"en": "after all", "ja": "そもそも；何しろ"},
                {"en": "be responsible for ...", "ja": "…の原因である"},
                {"en": "regularly", "pos": "副", "ja": "いつも；決まって"},
                {"en": "affect", "pos": "動", "ja": "〈病気などが〉…を襲う；…に影響を及ぼす"},
                {"en": "countless", "pos": "形", "ja": "無数の；数えきれない"},
                {"en": "at all costs", "ja": "どんな犠牲を払っても；ぜひとも"},
                {"en": "strictly", "pos": "副", "ja": "厳密に言うと"},
                {"en": "digestive", "pos": "形", "ja": "消化（器）の"},
                {"en": "harmful", "pos": "形", "ja": "有害な"},
                {"en": "bacteriophage", "pos": "名", "ja": "バクテリオファージ；殺菌ウイルス"},
            ],
        },
        "p2": {
            "label_ja": '第2段落（The interesting thing ... で始まる）',
            "items": [
                {"en": "be made out of ...", "ja": "…から作られて"},
                {"en": "reproduce", "pos": "動", "ja": "再生する；増殖［繁殖］する"},
                {"en": "genetic", "pos": "形", "ja": "遺伝子の"},
                {"en": "protein case", "ja": "タンパク質の外被"},
                {"en": "standard microscope", "ja": "通常の顕微鏡"},
                {"en": "bind to ...", "ja": "…と化学結合する"},
                {"en": "host cell", "ja": "宿主細胞"},
                {"en": "machinery", "pos": "名", "ja": "機構；仕組み"},
                {"en": "results in ...", "ja": "…という結果になる"},
            ],
        },
        "p3": {
            "label_ja": '第3段落（It is a virus\'s ability ... で始まる）',
            "items": [
                {"en": "approve", "pos": "動", "ja": "…を認可する"},
                {"en": "modify", "pos": "動", "ja": "…を修正する；変形する"},
                {"en": "antigen", "pos": "名", "ja": "抗原（免疫系にさまざまな免疫応答を引き起こす物質）"},
                {"en": "immune", "pos": "形", "ja": "免疫の"},
                {"en": "every two weeks", "ja": "2週間ごとに"},
                {"en": "ignore", "pos": "動", "ja": "…を無視する"},
            ],
        },
        "p4": {
            "label_ja": '第4段落（There are many benefits ... で始まる）',
            "items": [
                {"en": "benefit", "pos": "名", "ja": "恩恵；利益；良い点"},
                {"en": "side effect", "ja": "副作用"},
                {"en": "leave ... alone", "ja": "…に手をつけずにおく；…に被害を与えない"},
                {"en": "surgery", "pos": "名", "ja": "外科手術"},
                {"en": "targeted by location", "ja": "患部に的を絞って（治療する）"},
                {"en": "tiredness", "pos": "名", "ja": "疲労（感）"},
            ],
        },
        "p5": {
            "label_ja": '第5段落（Currently, scientists ... で始まる）',
            "items": [
                {"en": "gradually", "pos": "副", "ja": "徐々に；次第に"},
                {"en": "alter", "pos": "動", "ja": "…を変える"},
                {"en": "associated with ...", "ja": "…に伴う"},
                {"en": "prevent ... from -ing", "ja": "…が…するのを防ぐ"},
                {"en": "identify", "pos": "動", "ja": "…を見分ける；認識する"},
                {"en": "therapy", "pos": "名", "ja": "療法"},
            ],
        },
        "p6": {
            "label_ja": '最終段落（In summary ... で始まる）',
            "items": [
                {"en": "in summary", "ja": "要約すると"},
                {"en": "gene", "pos": "名", "ja": "遺伝子"},
                {"en": "adapt", "pos": "動", "ja": "…を改作する；変える"},
                {"en": "cure", "pos": "動", "ja": "…を治す"},
            ],
        },
        "questions_and_choices": {
            "items": [
                {"en": "one-hundredth", "ja": "100分の1の（大きさ）"},
                {"en": "modified virus", "ja": "変異［改作］されたウイルス"},
                {"en": "barrier", "ja": "障害；壁"},
            ],
        },
    },
}


def main():
    data_path = ROOT / "data.json"
    with open(data_path, encoding="utf-8") as f:
        data = json.load(f)
    # 既存の第7問があれば差し替え（語彙構造の修正など再実行用）
    data["sections"] = [s for s in data["sections"] if s.get("section_number") != 7]
    data["exam_info"]["implemented_sections"] = [1, 2, 3, 4, 5, 6, 7]
    data["sections"].append(section_07)
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Merged section 7 into", data_path)


if __name__ == "__main__":
    main()
