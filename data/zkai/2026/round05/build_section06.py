# -*- coding: utf-8 -*-
"""Merge Z会2026第5回 大問6 (A Newsworthy Friendship) into round05 data.json."""
import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data.json"


def section6():
    return {
        "section_number": 6,
        "title": "第6問",
        "points": 15,
        "points_per_question": 0,
        "description": "物語文「A Newsworthy Friendship」＋メモ（並べ替え・空欄）",
        "situation": {
            "en": "You are taking part in an English reading club at school. Each student was asked to read a short story in English, prepare notes, and introduce the story to other students. You are preparing your notes now.",
            "ja": "あなたは学校で英語の読書クラブに参加しています。各生徒が英語で書かれた短い物語を読んでメモを作り，その物語を他の生徒に紹介するように言われていました。あなたは今，メモを作っているところです。",
        },
        "passages": [
            {
                "id": "newsworthy_story",
                "framed": True,
                "title": {
                    "en": "<strong>A Newsworthy Friendship</strong>",
                    "ja": "<strong>ニュース級の友情</strong>",
                },
                "block_separators": [1, 7, 8, 11, 16],
                "paragraph_classes": ["para-indent"] * 21,
                "paragraphs": [
                    [
                        {
                            "id": "anf_p1_s1",
                            "en": "Kelsey waved goodbye as she watched her friends Hannah and John get into the car.",
                            "ja": "ケルシーは，友だちのハナとジョンが車に乗り込むのを見ながら，手を振って別れを告げた。",
                        },
                        {
                            "id": "anf_p1_s2",
                            "en": 'As they drove away, Hannah shouted, "We\'ll see you when we\'re home for winter break!"',
                            "ja": "車が走り去りながら，ハナは叫んだ。「冬休みに帰ってきたらまた会おうね！」",
                        },
                    ],
                    [
                        {
                            "id": "anf_p2_s1",
                            "en": "Hannah and John were leaving for their first year of college.",
                            "ja": "ハナとジョンは大学生活１年目に向けて出発した。",
                        },
                        {
                            "id": "anf_p2_s2",
                            "en": "They'd both received scholarships and were excited to live away from home.",
                            "ja": "２人とも奨学金をもらっており，実家を離れて暮らすことにわくわくしていた。",
                        },
                        {
                            "id": "anf_p2_s3",
                            "en": "Kelsey had introduced Hannah to John the previous year, and while she was happy for her friends, part of her wished she'd be joining them.",
                            "ja": "ケルシーは前年にジョンにハナを紹介したのだが，友人たちのことを思うとうれしい反面，心のどこかで自分も彼らと一緒にいたいと思っていた。",
                        },
                        {
                            "id": "anf_p2_s4",
                            "en": "Kelsey would start classes at the college in their hometown soon, but she wasn't sure what she wanted to study.",
                            "ja": "ケルシーはまもなく地元の大学で授業を受けることになっていたが，自分が何を学びたいのかはっきりとはわかっていなかった。",
                        },
                        {
                            "id": "anf_p2_s5",
                            "en": "And, she would continue living in the same house she had lived in for all eighteen years of her life.",
                            "ja": "そして，これまで18年の人生の間ずっと住んできたその家で，彼女は引き続き暮らすことになっていた。",
                        },
                        {
                            "id": "anf_p2_s6",
                            "en": "She began to feel lonely and frustrated.",
                            "ja": "彼女はさみしさと苛立ちを感じ始めていた。",
                        },
                    ],
                    [
                        {
                            "id": "anf_p3_s1",
                            "en": "That evening, Kelsey thought back to the first time she met Hannah when Hannah's family moved into the neighborhood 10 years earlier.",
                            "ja": "その日の晩，ケルシーはハナに初めて会った時のことを思い出していた。10年前に，ハナの一家が近所に引っ越してきたのだった。",
                        },
                        {
                            "id": "anf_p3_s2",
                            "en": "She remembered how she and Hannah enjoyed taking pictures and making videos of themselves.",
                            "ja": "自分とハナが写真を撮ったり，自分たちで動画を作ったりして楽しんでいたことを思い出した。",
                        },
                        {
                            "id": "anf_p3_s3",
                            "en": "Hannah always took better pictures, but Kelsey was always thinking creatively.",
                            "ja": "写真を撮るのはいつもハナの方が上手だった。でもケルシーは，いつも創造的に考えていた。",
                        },
                    ],
                    [
                        {
                            "id": "anf_p4_s1",
                            "en": '"Look at the colorful sky, Hannah! Take a picture," Kelsey said one evening.',
                            "ja": "「あのカラフルな空を見て，ハナ！　撮って」とある夕方，ケルシーは言った。",
                        },
                        {
                            "id": "anf_p4_s2",
                            "en": "Hannah snapped a photo capturing the magical sunset.",
                            "ja": "ハナは魔法のような夕日を捉えた写真を撮った。",
                        },
                        {
                            "id": "anf_p4_s3",
                            "en": "On a high school field trip to a botanical garden, Kelsey encouraged Hannah to take pictures of the unique plants.",
                            "ja": "植物園への高校の校外学習では，ケルシーはハナに珍しい植物の写真を撮るように勧めた。",
                        },
                    ],
                    [
                        {
                            "id": "anf_p5_s1",
                            "en": '"Zoom in on the leaves!" Kelsey instructed. "Look at the exquisite details!"',
                            "ja": "「葉っぱにズームインして！」ケルシーは指示した。「このすばらしい細部を見て！」",
                        },
                        {
                            "id": "anf_p5_s2",
                            "en": "After the trip, the girls admired the photos together.",
                            "ja": "校外学習の後，２人はそれらの写真にほれぼれと見入った。",
                        },
                    ],
                    [
                        {
                            "id": "anf_p6_s1",
                            "en": '"You\'re so skilled behind the camera, Hannah. I think you should upload the photos you take to social media. People love scrolling through beautiful images online, and it\'s an opportunity to display your talent."',
                            "ja": "「あなたは本当にカメラが上手ね，ハナ。撮った写真をソーシャルメディアにアップした方がいいと思う。みんなオンラインできれいな画像をスクロールしながら見るのが大好きだし，あなたの才能を披露するいい機会にもなる。」",
                        },
                    ],
                    [
                        {
                            "id": "anf_p7_s1",
                            "en": '"You really think so?" Hannah asked.',
                            "ja": "「本当にそう思う？」とハナは尋ねた。",
                        },
                        {
                            "id": "anf_p7_s2",
                            "en": '"Absolutely! And you could get better. Look at this!" Kelsey showed Hannah a flyer about the high school photography club recruiting new first-year students.',
                            "ja": "「もちろん！　それに，もっと腕を上げられるかも。これを見て！」ケルシーはハナに，高校の写真部が新入生を募集しているチラシを見せた。",
                        },
                        {
                            "id": "anf_p7_s3",
                            "en": '"You should join!" Kelsey said. "You can learn professional photography with a camera instead of a mobile phone." Hannah smiled with curiosity.',
                            "ja": "「入った方がいいよ！」ケルシーは言った。「携帯電話ではなく，ちゃんとしたカメラでプロの写真の撮り方を学べるよ。」ハナは興味津々で微笑んだ。",
                        },
                    ],
                    [
                        {
                            "id": "anf_p8_s1",
                            "en": "She joined the club the following week and began posting photos regularly on social media.",
                            "ja": "彼女は翌週に入部し，ソーシャルメディアに定期的に写真を投稿し始めた。",
                        },
                        {
                            "id": "anf_p8_s2",
                            "en": "It didn't take long for others to notice Hannah's talent, and soon she was receiving many comments from her followers.",
                            "ja": "人々がハナの才能に気づくのに時間はかからず，すぐに彼女は多くのフォロワーからコメントを受け取るようになった。",
                        },
                    ],
                    [
                        {
                            "id": "anf_p9_s1",
                            "en": "One week after saying goodbye to her friends, Kelsey started classes in her hometown.",
                            "ja": "友人たちと別れてから１週間後，ケルシーは地元で授業を受け始めた。",
                        },
                        {
                            "id": "anf_p9_s2",
                            "en": "None of them were particularly interesting, and she grew dissatisfied with her situation.",
                            "ja": "どの授業もこれといっておもしろいものはなく，彼女は自分の置かれている状況に不満を募らせていった。",
                        },
                        {
                            "id": "anf_p9_s3",
                            "en": "She began wondering if she had made the right decision to attend the local college.",
                            "ja": "彼女は地元の大学に通うという決断が正しかったのか疑問に思い始めた。",
                        },
                        {
                            "id": "anf_p9_s4",
                            "en": "While walking to campus, she often daydreamed about her future.",
                            "ja": "キャンパスまで歩きながら，彼女はよく自分の将来について空想にふけった。",
                        },
                        {
                            "id": "anf_p9_s5",
                            "en": "She contemplated what field of study to pursue, what job she might have, or if she would live in her hometown forever.",
                            "ja": "どんな分野の学問を追い求めようか，どんな仕事に就くだろうか，あるいはこのままずっと地元で暮らすのだろうかと思いを巡らせた。",
                        },
                        {
                            "id": "anf_p9_s6",
                            "en": "But most often, she thought about her friends.",
                            "ja": "だがたいていは，友人たちのことを考えていた。",
                        },
                    ],
                    [
                        {
                            "id": "anf_p10_s1",
                            "en": "Kelsey met John during their first year of high school in essay writing class when the teacher assigned them to review each other's essays.",
                            "ja": "ケルシーは高校１年生の時，エッセイライティングの授業でジョンに出会った。その授業で先生は生徒たちに互いの作文を批評するよう課した。",
                        },
                        {
                            "id": "anf_p10_s2",
                            "en": "Kelsey was impressed by John's work.",
                            "ja": "ケルシーはジョンの作品に感銘を受けた。",
                        },
                        {
                            "id": "anf_p10_s3",
                            "en": '"Your writing is incredibly fluid and descriptive," she told him. "You have a special talent with words."',
                            "ja": "「あなたの文章は驚くほど流麗で描写力に富んでいるわ」と彼女は彼に言った。「あなたには言葉を操る特別な才能がある。」",
                        },
                        {
                            "id": "anf_p10_s4",
                            "en": "John looked surprised.",
                            "ja": "ジョンは驚いた様子だった。",
                        },
                        {
                            "id": "anf_p10_s5",
                            "en": '"You should keep practicing and write a short story for the contest next year," Kelsey continued. "Plus, writing can stimulate your creativity."',
                            "ja": "「練習を続けて，来年のコンテストのために短編小説を書くべきよ」とケルシーは続けた。「それに，書くことはあなたの創造性を刺激することにもなる。」",
                        },
                    ],
                    [
                        {
                            "id": "anf_p11_s1",
                            "en": "John didn't know what to say.",
                            "ja": "ジョンは何と言っていいのかわからなかった。",
                        },
                        {
                            "id": "anf_p11_s2",
                            "en": "While he enjoyed writing, he only did so for class assignments and was shy about sharing with others.",
                            "ja": "確かに書くのは楽しかったが，それはあくまで授業の課題のためにやったものだったし，他人と分かち合うのは照れくさかった。",
                        },
                        {
                            "id": "anf_p11_s3",
                            "en": "He'd also never been told he was talented.",
                            "ja": "彼はこれまで才能があると言われたこともなかった。",
                        },
                        {
                            "id": "anf_p11_s4",
                            "en": "Kelsey made him feel confident, and soon he was writing every day.",
                            "ja": "ケルシーのおかげで彼は自信がつき，すぐに毎日書くようになった。",
                        },
                        {
                            "id": "anf_p11_s5",
                            "en": "He'd write about his feelings, observations, or challenges he was facing.",
                            "ja": "自分の気持ち，観察して気づいたこと，自分が直面している困難について書いた。",
                        },
                        {
                            "id": "anf_p11_s6",
                            "en": "He found the practice beneficial and was grateful for Kelsey's suggestion.",
                            "ja": "彼はその練習が有益であることに気づき，ケルシーが勧めてくれたことに感謝した。",
                        },
                    ],
                    [
                        {
                            "id": "anf_p12_s1",
                            "en": "After nearly a year of daily writing, John submitted his writing to the contest and won first place!",
                            "ja": "ほぼ１年間毎日書き続けたジョンは，作品をコンテストに提出し，１位になった！",
                        },
                    ],
                    [
                        {
                            "id": "anf_p13_s1",
                            "en": "Hannah and John met up a month after college classes had started.",
                            "ja": "ハナとジョンは大学の授業が始まってから１カ月後に会った。",
                        },
                        {
                            "id": "anf_p13_s2",
                            "en": "While walking past a notice board on campus, a poster about the student newspaper caught their eyes.",
                            "ja": "キャンパス内の掲示板のそばを通り過ぎるとき，学生新聞についてのポスターが彼らの目に留まった。",
                        },
                        {
                            "id": "anf_p13_s3",
                            "en": "They went to a meeting where the editor explained the process of planning the newspaper content, designing the layout, and publishing the newspaper.",
                            "ja": "２人は集会に参加した。そこでは編集者が，新聞の掲載内容の企画，レイアウトのデザイン，そして新聞発行の過程を説明した。",
                        },
                        {
                            "id": "anf_p13_s4",
                            "en": "Although they were busy with their class work, Hannah and John agreed that it was an opportunity to develop their skills through experience, so they joined the newspaper.",
                            "ja": "ハナもジョンも授業の課題で忙しかったが，経験を通じて自分たちのスキルを伸ばす機会だということで意見が一致し，新聞部に入部した。",
                        },
                    ],
                    [
                        {
                            "id": "anf_p14_s1",
                            "en": "One October evening while working on their newspaper assignments, they thought about Kelsey.",
                            "ja": "10月のある日の晩，新聞の課題に取り組んでいるとき，２人はケルシーのことを考えた。",
                        },
                        {
                            "id": "anf_p14_s2",
                            "en": "Hannah told John about how Kelsey's convincing suggestion led to her studying photography, and John remembered how Kelsey had appreciated his writing.",
                            "ja": "ハナはジョンに，ケルシーの説得力のある提案が自分の写真の勉強につながった経緯を話し，ジョンはケルシーが彼の文章を高く評価してくれたことを思い出した。",
                        },
                        {
                            "id": "anf_p14_s3",
                            "en": "Suddenly, Hannah felt a bit guilty.",
                            "ja": "突然，ハナは少し後ろめたさを覚えた。",
                        },
                    ],
                    [
                        {
                            "id": "anf_p15_s1",
                            "en": '"You know what, John? I think it\'s time for us to inspire Kelsey. I think she would be an excellent newspaper editor!',
                            "ja": "「ねえ，ジョン。今度は私たちがケルシーを奮い立たせる番だと思う。彼女ならきっとすばらしい新聞の編集者になれると思う！",
                        },
                        {
                            "id": "anf_p15_s2",
                            "en": "She's always been able to notice details, share her opinions, and make suggestions.",
                            "ja": "いつも細かいところまで気がつくし，自分の意見を伝え，提案することもできる。",
                        },
                        {
                            "id": "anf_p15_s3",
                            "en": "She helped me realize my talent and pushed me to improve, but what have I ever done to help her?\"",
                            "ja": "彼女は私に自分の才能を気づかせてくれて，上達するよう後押ししてくれたけど，私が彼女のために何かしたことがあったかな。」",
                        },
                    ],
                    [
                        {
                            "id": "anf_p16_s1",
                            "en": '"You\'re right! She does have all the necessary skills! I wonder why I never thought of giving her any compliments. Are you thinking what I\'m thinking?"',
                            "ja": "「その通りだ！　彼女には必要なスキルが全部そろっている！　なぜ僕は彼女に称賛の言葉をかけたことがなかったんだろう。君も僕と同じことを考えているんだろう？」",
                        },
                    ],
                    [
                        {
                            "id": "anf_p17_s1",
                            "en": "Hannah and John smiled and immediately called their friend.",
                            "ja": "ハナとジョンは微笑み，すぐにその友人に電話した。",
                        },
                    ],
                    [
                        {
                            "id": "anf_p18_s1",
                            "en": "It was winter break, and the three friends were sitting in a café in their hometown chatting about their first fall semester at college.",
                            "ja": "冬休みになり，３人の友だちは地元のカフェの中に座り，大学での最初の秋学期についておしゃべりしていた。",
                        },
                        {
                            "id": "anf_p18_s2",
                            "en": "Hannah and John showed Kelsey a copy of their school newspaper.",
                            "ja": "ハナとジョンはケルシーに自分たちの学校新聞の写しを見せた。",
                        },
                        {
                            "id": "anf_p18_s3",
                            "en": "On the front page was an article written by John with photos taken by Hannah.",
                            "ja": "一面にはジョンが書いた記事とハナが撮った写真が掲載されていた。",
                        },
                        {
                            "id": "anf_p18_s4",
                            "en": "Kelsey smiled as she congratulated her friends.",
                            "ja": "ケルシーは笑みを浮かべて友人たちを祝福した。",
                        },
                    ],
                    [
                        {
                            "id": "anf_p19_s1",
                            "en": '"I also have some news to share," Kelsey exclaimed. "I\'ve decided to major in journalism!',
                            "ja": "「私もニュースがあるの」とケルシーは興奮気味に言った。「ジャーナリズムを専攻することに決めたの！",
                        },
                        {
                            "id": "anf_p19_s2",
                            "en": "You phoned me and asked me to help your newspaper that night, but I'm sorry I can't help you with your newspaper.",
                            "ja": "あの夜電話をくれて，あなたたちの新聞を手伝ってほしいって言ってくれたよね。でもごめん，あなたたちの新聞のお手伝いはできない。",
                        },
                        {
                            "id": "anf_p19_s3",
                            "en": "Instead, your advice made me understand what to do.",
                            "ja": "でも代わりに，あなたたちのアドバイスのおかげで，私が何をすべきかわかったの。",
                        },
                        {
                            "id": "anf_p19_s4",
                            "en": "I decided to check out my school's newspaper.",
                            "ja": "自分の大学の新聞を調べてみることにした。",
                        },
                        {
                            "id": "anf_p19_s5",
                            "en": "Then I met with a school counselor, who told me about the journalism program.",
                            "ja": "それから学校のカウンセラーに会って，ジャーナリズムのプログラムについて教えてもらった。",
                        },
                        {
                            "id": "anf_p19_s6",
                            "en": "I have my first class in mass media next semester, and in the future, I hope to become a professional newspaper editor.\"",
                            "ja": "来学期にはマスメディアの最初の授業があるの。そして将来，プロの新聞編集者になりたいなって。」",
                        },
                    ],
                    [
                        {
                            "id": "anf_p20_s1",
                            "en": '"That\'s amazing!" John exclaimed.',
                            "ja": "「それはすばらしい！」とジョンは叫んだ。",
                        },
                        {
                            "id": "anf_p20_s2",
                            "en": "Hannah nodded in agreement.",
                            "ja": "ハナも同意してうなずいた。",
                        },
                    ],
                    [
                        {
                            "id": "anf_p21_s1",
                            "en": "Kelsey smiled hopefully and thanked her friends.",
                            "ja": "ケルシーは希望に満ちた微笑みを浮かべ，友人たちに感謝した。",
                        },
                        {
                            "id": "anf_p21_s2",
                            "en": "She finally felt like she was moving in the right direction.",
                            "ja": "彼女はついに自分が正しい方向に進み始めているように感じた。",
                        },
                    ],
                ],
            },
            {
                "id": "newsworthy_notes",
                "presentation_outline": {
                    "label_outside_box": {
                        "en": "Your notes:",
                        "ja": "あなたのメモ：",
                    },
                    "title": {
                        "en": "A Newsworthy Friendship",
                        "ja": "ニュース級の友情",
                    },
                    "blocks": [
                        {
                            "type": "story_outline",
                            "heading": {
                                "en": "Story outline",
                                "ja": "物語のあらすじ",
                            },
                            "lead_en": "Hannah's family moves into Kelsey's neighborhood.",
                            "lead_ja": "ハナの一家がケルシーの近所に引っ越してくる。",
                            "sequential_slots": [25, 26, 27, 28],
                            "tail_en": "Kelsey, John, and Hannah meet up during winter break.",
                            "tail_ja": "ケルシー，ジョン，ハナが冬休み中に会う。",
                        },
                        {
                            "type": "section_heading_lines",
                            "heading": {
                                "en": "About Kelsey",
                                "ja": "ケルシーについて",
                            },
                            "bullets": [
                                {
                                    "en": "Met Hannah when she was about [29].",
                                    "ja": "彼女がおよそ［29］の頃に，ハナと出会った。",
                                },
                                {
                                    "en": "How she helped her friends:",
                                    "ja": "彼女が友人をどのように助けたか：",
                                },
                                {
                                    "en": "Encouraged Hannah to [30].",
                                    "ja": "ハナに［30］よう促した。",
                                },
                                {
                                    "en": "Encouraged John to [31].",
                                    "ja": "ジョンに［31］よう促した。",
                                },
                            ],
                        },
                        {
                            "type": "section_heading_lines",
                            "heading": {
                                "en": "Key moments in the story",
                                "ja": "物語におけるカギとなる瞬間",
                            },
                            "bullets": [
                                {
                                    "en": "Hannah and John realize that [32].",
                                    "ja": "ハナとジョンは［32］ことに気づいた。",
                                },
                                {
                                    "en": "Kelsey feels grateful towards her friends because [33].",
                                    "ja": "ケルシーは友人たちに感謝している。なぜなら［33］からである。",
                                },
                            ],
                        },
                    ],
                },
            },
        ],
        "questions": [
            {
                "question_id": "問1",
                "question_type": "ordering",
                "points": 3,
                "answer_numbers": [25, 26, 27, 28],
                "stem": {
                    "en": "Choose four out of the five options (① ~ ⑤) and rearrange them in the order they happened. [ 25 ] → [ 26 ] → [ 27 ] → [ 28 ]",
                    "ja": "次の①〜⑤のうちから４つを選び，それらが起こった順に並べ替えなさい。［25］→［26］→［27］→［28］",
                },
                "choices": [
                    {
                        "label": "①",
                        "en": "Hannah and John join the school newspaper.",
                        "ja": "ハナとジョンが学校の新聞部に入る。",
                        "is_correct": True,
                    },
                    {
                        "label": "②",
                        "en": "Hannah signs up for the photography club.",
                        "ja": "ハナが写真部に入部する。",
                        "is_correct": True,
                    },
                    {
                        "label": "③",
                        "en": "John wins a writing contest.",
                        "ja": "ジョンが作文コンテストで優勝する。",
                        "is_correct": True,
                    },
                    {
                        "label": "④",
                        "en": "Kelsey becomes the editor of a newspaper.",
                        "ja": "ケルシーが新聞の編集者になる。",
                        "is_correct": False,
                    },
                    {
                        "label": "⑤",
                        "en": "Kelsey starts college classes in her hometown.",
                        "ja": "ケルシーが地元で大学の授業を受け始める。",
                        "is_correct": True,
                    },
                ],
                "answer": "②→③→⑤→①",
                "answer_sequence": ["②", "③", "⑤", "①"],
                "explanation": {
                    "quoted_ja": "正解の順序は②→③→⑤→①。写真部入部（高１の回想）→ほぼ１年後のコンテスト優勝→友人と別れた１週間後の地元大学開始→大学開始１カ月後の新聞部入部の時系列。④は本文にない誤答肢。",
                    "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子",
                    "evidence_sentences": [
                        "anf_p7_s3",
                        "anf_p12_s1",
                        "anf_p9_s1",
                        "anf_p13_s1",
                    ],
                    "instructor_note": {
                        "ja": "５つから４つ選ぶ並べ替え。回想パートの写真部→ジョンのコンテスト→「１週間後」の地元大学→「１カ月後」の新聞部の順に固定する。",
                        "points": [
                            "④はケルシーが編集者になったという記述はなく除外。",
                            "②は first-year students を募集する写真部の場面に対応。",
                        ],
                    },
                },
            },
            {
                "question_id": "問2",
                "answer_number": 29,
                "points": 3,
                "stem": {
                    "en": "Choose the best option for [ 29 ].",
                    "ja": "［29］に最も適当な選択肢を選びなさい。",
                },
                "choices": [
                    {
                        "label": "①",
                        "en": "5 years old",
                        "ja": "5歳",
                        "is_correct": False,
                    },
                    {
                        "label": "②",
                        "en": "8 years old",
                        "ja": "8歳",
                        "is_correct": True,
                    },
                    {
                        "label": "③",
                        "en": "10 years old",
                        "ja": "10歳",
                        "is_correct": False,
                    },
                    {
                        "label": "④",
                        "en": "18 years old",
                        "ja": "18歳",
                        "is_correct": False,
                    },
                ],
                "answer": "②",
                "explanation": {
                    "quoted_ja": "正解は②。現在18年同じ家にいて，10年前にハナと出会ったので，出会いのときは8歳。",
                    "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子",
                    "evidence_sentences": ["anf_p2_s5", "anf_p3_s1"],
                    "instructor_note": {
                        "ja": "年齢計算。all eighteen years と 10 years earlier を組み合わせる。",
                        "points": [],
                    },
                },
            },
            {
                "question_id": "問3",
                "answer_numbers": [30, 31],
                "points": 3,
                "stem": {
                    "en": "Choose the best options for [ 30 ] and [ 31 ].",
                    "ja": "［30］と［31］に最も適当な選択肢を選びなさい。",
                },
                "answer": {"30": "③", "31": "④"},
                "choices_30": [
                    {
                        "label": "①",
                        "en": "apply for a college scholarship",
                        "ja": "大学の奨学金を申し込む",
                        "is_correct": False,
                    },
                    {
                        "label": "②",
                        "en": "buy a new professional camera",
                        "ja": "新しいプロ用カメラを買う",
                        "is_correct": False,
                    },
                    {
                        "label": "③",
                        "en": "post photos online for others to enjoy",
                        "ja": "他の人が楽しめるよう写真をオンラインに投稿する",
                        "is_correct": True,
                    },
                    {
                        "label": "④",
                        "en": "start writing more regularly",
                        "ja": "もっと定期的に書くことを始める",
                        "is_correct": False,
                    },
                    {
                        "label": "⑤",
                        "en": "take college classes in their hometown",
                        "ja": "地元で大学の授業を受ける",
                        "is_correct": False,
                    },
                ],
                "choices_31": [
                    {
                        "label": "①",
                        "en": "apply for a college scholarship",
                        "ja": "大学の奨学金を申し込む",
                        "is_correct": False,
                    },
                    {
                        "label": "②",
                        "en": "buy a new professional camera",
                        "ja": "新しいプロ用カメラを買う",
                        "is_correct": False,
                    },
                    {
                        "label": "③",
                        "en": "post photos online for others to enjoy",
                        "ja": "他の人が楽しめるよう写真をオンラインに投稿する",
                        "is_correct": False,
                    },
                    {
                        "label": "④",
                        "en": "start writing more regularly",
                        "ja": "もっと定期的に書くことを始める",
                        "is_correct": True,
                    },
                    {
                        "label": "⑤",
                        "en": "take college classes in their hometown",
                        "ja": "地元で大学の授業を受ける",
                        "is_correct": False,
                    },
                ],
                "explanation": {
                    "quoted_ja": "正解は［30］③，［31］④。ハナにはソーシャルメディアへのアップロードを勧め，ジョンには練習を続けコンテスト用の短編を書くよう勧めている。",
                    "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子",
                    "evidence_sentences": ["anf_p6_s1", "anf_p10_s5"],
                    "instructor_note": {
                        "ja": "空欄ごとに勧めの内容が異なる。ハナ＝upload／ジョン＝keep practicing … contest。",
                        "points": [],
                    },
                },
            },
            {
                "question_id": "問4",
                "answer_number": 32,
                "points": 3,
                "stem": {
                    "en": "Choose the best option for [ 32 ].",
                    "ja": "［32］に最も適当な選択肢を選びなさい。",
                },
                "choices": [
                    {
                        "label": "①",
                        "en": "attending college was not the best decision",
                        "ja": "大学進学は最善の決断ではなかった",
                        "is_correct": False,
                    },
                    {
                        "label": "②",
                        "en": "receiving feedback is not always beneficial",
                        "ja": "フィードバックをもらうことが常に有益とは限らない",
                        "is_correct": False,
                    },
                    {
                        "label": "③",
                        "en": "they don't have time for the newspaper",
                        "ja": "新聞の仕事をする時間がない",
                        "is_correct": False,
                    },
                    {
                        "label": "④",
                        "en": "they haven't been supportive of their friend",
                        "ja": "自分たちは友人であるケルシーを支えてこなかった",
                        "is_correct": True,
                    },
                ],
                "answer": "④",
                "explanation": {
                    "quoted_ja": "正解は④。ハナは罪悪感を覚え，ケルシーを励ます番だと語り，自分が何をしてあげたかと問う流れは「友人への返報が足りなかった」に合致する。",
                    "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子",
                    "evidence_sentences": ["anf_p14_s3", "anf_p15_s1", "anf_p15_s3"],
                    "instructor_note": {
                        "ja": "guilty と inspire Kelsey / what have I ever done が手がかり。",
                        "points": [],
                    },
                },
            },
            {
                "question_id": "問5",
                "answer_number": 33,
                "points": 3,
                "stem": {
                    "en": "Choose the best option for [ 33 ].",
                    "ja": "［33］に最も適当な選択肢を選びなさい。",
                },
                "choices": [
                    {
                        "label": "①",
                        "en": "they didn't criticize her opinions",
                        "ja": "彼らが彼女の意見を批判しなかった",
                        "is_correct": False,
                    },
                    {
                        "label": "②",
                        "en": "they helped her identify a career path",
                        "ja": "彼らが彼女の進路を見いだす手助けをしてくれた",
                        "is_correct": True,
                    },
                    {
                        "label": "③",
                        "en": "they introduced her to new people",
                        "ja": "彼らが彼女を新しい人たちに紹介してくれた",
                        "is_correct": False,
                    },
                    {
                        "label": "④",
                        "en": "they wrote a newspaper article about her",
                        "ja": "彼らが彼女についての新聞記事を書いてくれた",
                        "is_correct": False,
                    },
                ],
                "answer": "②",
                "explanation": {
                    "quoted_ja": "正解は②。電話とアドバイスをきっかけにジャーナリズム専攻と進路を決めたとケルシーが語る。",
                    "quoted_source": "Z会『2026年 共通テスト実戦模試 英語リーディング』第5回 解説冊子",
                    "evidence_sentences": ["anf_p19_s2", "anf_p19_s3", "anf_p19_s5"],
                    "instructor_note": {
                        "ja": "your advice made me understand what to do と journalism program が根拠。",
                        "points": [],
                    },
                },
            },
        ],
        "vocabulary": {
            "passage": {
                "label_ja": "主な語彙",
                "items": [
                    {"en": "newsworthy", "ja": "ニュースにする価値のある，報道価値のある"},
                    {"en": "wave goodbye", "ja": "さようならと手を振る"},
                    {"en": "scholarship", "ja": "奨学金"},
                    {"en": "feel frustrated", "ja": "イライラする，欲求不満を感じる"},
                    {"en": "think back to ~", "ja": "〜を思い返す"},
                    {"en": "snap a photo", "ja": "スナップ写真を撮る"},
                    {"en": "capture", "ja": "〜を（写真等に）うまく捉える"},
                    {"en": "magical", "ja": "魔法のような"},
                    {"en": "field trip", "ja": "校外学習，遠足"},
                    {"en": "botanical garden", "ja": "植物園"},
                    {"en": "encourage ~ to do", "ja": "〜に…するよう促す，励ます"},
                    {"en": "zoom in on ~", "ja": "〜にズームインする，拡大する"},
                    {"en": "instruct", "ja": "指示する"},
                    {"en": "exquisite", "ja": "非常に美しい，精妙な"},
                    {"en": "admire", "ja": "〜を感心して眺める，見とれる"},
                    {"en": "skilled", "ja": "腕の良い，上手な"},
                    {"en": "behind the camera", "ja": "カメラマンとして"},
                    {"en": "display", "ja": "〜を披露する"},
                    {"en": "flyer", "ja": "チラシ"},
                    {"en": "recruit", "ja": "〜を募集する"},
                    {"en": "daydream", "ja": "空想にふける"},
                    {"en": "contemplate", "ja": "〜について熟考する"},
                    {"en": "pursue", "ja": "〜を追求する，追い求める"},
                    {"en": "assign ~ to do", "ja": "〜に…するように指示する，課題を出す"},
                    {"en": "review", "ja": "〜を批評する"},
                    {"en": "fluid", "ja": "流暢な，流麗な"},
                    {"en": "descriptive", "ja": "描写力に富んだ"},
                    {"en": "stimulate", "ja": "〜を刺激する"},
                    {"en": "challenge", "ja": "困難，難題"},
                    {"en": "face", "ja": "〜に直面する"},
                    {"en": "suggestion", "ja": "提案"},
                    {"en": "submit A to B", "ja": "AをBに提出する"},
                    {"en": "walk past ~", "ja": "〜のそばを通り過ぎる"},
                    {"en": "notice board", "ja": "掲示板"},
                    {"en": "catch one's eye", "ja": "〜の目を引く"},
                    {"en": "editor", "ja": "（新聞・雑誌などの）編集長；編集者"},
                    {"en": "convincing", "ja": "説得力のある"},
                    {"en": "you know what", "ja": "《話を切り出す時に》ねえ，あのさ"},
                    {"en": "inspire", "ja": "〜を奮い立たせる"},
                    {"en": "push ~ to do", "ja": "〜に…するように強く促す"},
                    {"en": "compliment", "ja": "褒め言葉"},
                    {"en": "semester", "ja": "学期"},
                    {"en": "front page", "ja": "（新聞の）一面"},
                    {"en": "congratulate", "ja": "〜を祝う"},
                    {"en": "exclaim", "ja": "叫ぶ"},
                    {"en": "major in ~", "ja": "〜を専攻する"},
                    {"en": "check out ~", "ja": "〜を調べる"},
                    {"en": "nod in agreement", "ja": "同意してうなずく"},
                    {"en": "sign up for ~", "ja": "〜に入会する，届け出を出す", "note": "問1 ②"},
                ],
            }
        },
    }


def main():
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    if any(s.get("section_number") == 6 for s in data["sections"]):
        # Replace existing section 6
        data["sections"] = [s for s in data["sections"] if s.get("section_number") != 6]
    data["sections"].append(section6())
    impl = data["exam_info"].setdefault("implemented_sections", [])
    if 6 not in impl:
        impl.append(6)
        impl.sort()
    DATA_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("OK: section 6 written, implemented_sections:", data["exam_info"]["implemented_sections"])


if __name__ == "__main__":
    main()
