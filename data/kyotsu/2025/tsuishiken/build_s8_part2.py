# -*- coding: utf-8 -*-
# Part2: Questions for Tsuishiken Section 8
def get_questions():
    return [
        {"question_id":"問1","answer_number":38,
         "stem":{"en":"Which of the following best summarizes Indira\u2019s opinion? [38]","ja":"次の中でIndiraの意見の要約として最も適切なものはどれか。[38]"},
         "choices":[
             {"label":"\u2460","en":"Humans and animals should have different rights.","ja":"人間と動物は異なる権利を持つべきだ。","is_correct":False},
             {"label":"\u2461","en":"Mistreatment of animals is a serious problem.","ja":"動物に対する虐待は重大な問題だ。","is_correct":True},
             {"label":"\u2462","en":"Observation is key to understanding animal suffering.","ja":"観察が動物の苦しみを理解するために重要だ。","is_correct":False},
             {"label":"\u2463","en":"Prisons are necessary to keep society safe.","ja":"監獄は社会を安全にしておくために必要だ。","is_correct":False}
         ],
         "answer":"\u2461",
         "explanation":{
             "quoted_ja":"正解は\u2461。Indiraは，第1文（Zoos are prisons ...）で「動物園は動物にとって監獄だ」とした上で，チータの身になって考えるよう訴えて（第2・3文），第4文（We would not expose ...）と第5文（Why do so many people ...）で「私たちは人間をそんな残酷な目にあわせたりはしないでしょう。なぜとても多くの人が動物をこんなふうに扱っても構わないと思っているのでしょうか？」と結んでいる。最後の文は修辞疑問文で，「動物をこんなふうに扱っても構わないと思っている理由などない」と言っているのとほぼ同じなので，Indiraは動物園があることによって人間が動物を残酷な目にあわせていることを批判していることから，下線部の「残酷な目（cruel treatment）」または同じ意味の「虐待（mistreatment）」を含む\u2461が正解となる。",
             "quoted_source":"共通テスト 2025年度 追試験 英語（リーディング） 問題・解説",
             "evidence_sentences":["s8t_s12","s8t_s15","s8t_s16"],
             "instructor_note":{
                 "ja":"Indiraの意見全体を通じた主張を正確に要約する問題です。修辞疑問文（rhetorical question）の読み取りがポイントです。",
                 "points":[
                     "s8t_s12 の Zoos are prisons for animals が核心的な主張。動物園＝監獄という比喩を読み取る。",
                     "s8t_s15 の We would not expose any persons to such cruel treatment が cruel treatment（残酷な扱い）＝ mistreatment（虐待）に対応。",
                     "s8t_s16 の Why do so many people ... は修辞疑問文。『そう思っている理由はない』という否定的な主張を表す。",
                     "①の罠: different rights は述べていない。Indiraは動物と人間を同等に扱うべきと主張している。",
                     "③の罠: observation（観察）は Indira の論点ではない。Imagine being ... は共感を促す手法。",
                     "④の罠: prisons は動物園の比喩であり，社会の安全のための監獄の必要性は述べていない。"
                 ]
             }
         }},
        {"question_id":"問2","answer_number":39,
         "stem":{"en":"Both David and Yo mention that zoos [39].","ja":"DavidとYoはどちらも，動物園は[39]と述べている。"},
         "choices":[
             {"label":"\u2460","en":"are often located in large cities","ja":"大都市にあることが多い","is_correct":False},
             {"label":"\u2461","en":"can be the source of infectious diseases","ja":"伝染病の発生源になりうる","is_correct":False},
             {"label":"\u2462","en":"can potentially cause harm to people","ja":"潜在的に人間に害をもたらしうる","is_correct":True},
             {"label":"\u2463","en":"work toward protecting the environment","ja":"環境を保護する方向で働いている","is_correct":False}
         ],
         "answer":"\u2462",
         "explanation":{
             "quoted_ja":"正解は\u2462。Davidは，トビリシ動物園の例を挙げて（第3文：In the country of ...），動物園の動物が人間を襲撃する危険性を訴えている。Yoは，動物園の動物が人間にウイルスを移す危険性を懸念している（第2文：While so-called \u201cvirus jumping\u201d ...）。したがって両者に共通する点は，\u2462のように動物園は「潜在的に人間に害（harm）をもたらしうる」ということである。\u2460はDavidのみ，\u2461はYoのみが述べていることなので，いずれも正解にはなれない。\u2463のようなことはどちらも述べていない。",
             "quoted_source":"共通テスト 2025年度 追試験 英語（リーディング） 問題・解説",
             "evidence_sentences":["s8t_s9","s8t_s25"],
             "instructor_note":{
                 "ja":"2人の意見に共通する点を見つける問題です。DavidとYoそれぞれの主張から共通のテーマ（動物園の危険性）を抽出しましょう。",
                 "points":[
                     "David: s8t_s9 の escaped ... posing a danger to local citizens → 動物の脱走による物理的な害。",
                     "Yo: s8t_s25 の zoos too must be considered as a potential source of such events → ウイルス感染による害。",
                     "③: 両者に共通するのは can potentially cause harm to people（潜在的に人間に害をもたらしうる）。harm が包括的な表現。",
                     "①の罠: located in large cities は David のみの言及（s8t_s7）。Yo は場所に触れていない。",
                     "②の罠: infectious diseases は Yo のみの話題。David は物理的危険を述べている。",
                     "④の罠: 環境保護については David も Yo も述べていない。"
                 ]
             }
         }},
        {"question_id":"問3","answer_number":40,
         "answer_numbers":[40,41,42],"unordered_slots":[40,41],
         "stem":{"en":"Now that you have understood the various opinions, you have taken a position on zoos and written some notes below. Choose the best options to complete [40]\u2013[42]. (You must have all of [40]\u2013[42] correct to get points.)","ja":"あなたはさまざまな意見を理解したので，動物園に関する見解を固めて，下にいくつかのメモを書いた。[40]\u2013[42]を埋めるのに最適な選択肢を選びなさい。（[40]\u2013[42]のすべてに正解した場合のみ得点を与える。）"},
         "position_box":{"en":"POSITION: We should support and actively maintain zoos.\n\u2022 [40] and [41] opinions support this the most.\n\u2022 An argument common to these two people is that [42].","ja":"見解：私たちは動物園を支援して積極的に維持すべきだ。\n・[40]意見と[41]意見がこれを最も支持している。\n・この2人に共通する主張は，[42]ということである。"},
         "choices_40":[
             {"label":"\u2460","en":"Aya\u2019s","ja":"Ayaの","is_correct":True},
             {"label":"\u2461","en":"David\u2019s","ja":"Davidの","is_correct":False},
             {"label":"\u2462","en":"Indira\u2019s","ja":"Indiraの","is_correct":False},
             {"label":"\u2463","en":"Kenyatta\u2019s","ja":"Kenyattaの","is_correct":True},
             {"label":"\u2464","en":"Yo\u2019s","ja":"Yoの","is_correct":False}
         ],
         "choices_41":[
             {"label":"\u2460","en":"Aya\u2019s","ja":"Ayaの","is_correct":True},
             {"label":"\u2461","en":"David\u2019s","ja":"Davidの","is_correct":False},
             {"label":"\u2462","en":"Indira\u2019s","ja":"Indiraの","is_correct":False},
             {"label":"\u2463","en":"Kenyatta\u2019s","ja":"Kenyattaの","is_correct":True},
             {"label":"\u2464","en":"Yo\u2019s","ja":"Yoの","is_correct":False}
         ],
         "choices_42":[
             {"label":"\u2460","en":"a country\u2019s culture is reflected in its zoos","ja":"国の文化がその国の動物園に反映されている","is_correct":False},
             {"label":"\u2461","en":"animal welfare is the priority when running a zoo","ja":"動物の幸福が動物園を運営する際の優先事項だ","is_correct":False},
             {"label":"\u2462","en":"sharing knowledge is an important function of a zoo","ja":"知識の共有が動物園の重要な機能の1つだ","is_correct":True},
             {"label":"\u2463","en":"zoos provide useful data on local economies","ja":"動物園は地域経済に関する有用なデータを提供する","is_correct":False}
         ],
         "answer":{"40":"\u2460","41":"\u2463","42":"\u2462"},
         "answer_note":"[40]と[41]は順不同。[40]\u2013[42]すべて正解で得点",
         "explanation":{
             "quoted_ja":"正解は[40]\u2460・[41]\u2463，[42]\u2462。[40]と[41]には，「私たちは動物園を支援して積極的に維持すべきだ」という見解と基本的に同じ趣旨の意見を述べている人物の意見を選ぶ。選択肢の5人のうち，DavidとIndiraとYoは動物園について否定的な見解を抱いている（問1・2の解説参照）ので，この3人は正解にはなれない。残るAyaとKenyattaは，動物園について肯定的な見解を抱いていることから，\u2460と\u2463が正解となる。[42]の選択肢：正解は\u2462。AyaとKenyattaに共通する主張を選ぶ。Ayaの意見の最終文（Other benefits provided ...）に「動物園が提供できるその他の利点には，大学との共同研究や，学校との連携による児童教育（collaborating with universities on research, or with schools on children\u2019s education）などがあります」とあり，Kenyattaの意見の最終文（This can also help ...）に「これはまた，動物学上の情報のやり取り（the mutual flow of zoological information）を促進するのにも役立ち，これによって世界全体のつながりがより良くなるのです」とある。\u2462の中の「知識の共有（sharing knowledge）」は，2つの下線部の共通点を表現していると考えられることから，\u2462が正解となる。",
             "quoted_source":"共通テスト 2025年度 追試験 英語（リーディング） 問題・解説",
             "evidence_sentences":["s8t_s5","s8t_s22"],
             "instructor_note":{
                 "ja":"見解に最も合う意見の持ち主2名と，その2名の共通主張を選ぶ問題です。まず各人物のスタンス（賛成/反対）を整理しましょう。",
                 "points":[
                     "5人のスタンス整理: Aya=賛成，David=反対，Indira=反対，Kenyatta=賛成，Yo=反対。",
                     "[40][41]: 『動物園を支援すべき』という見解に合うのは Aya と Kenyatta のみ → ①④。",
                     "[42]: Aya の s8t_s5 collaborating with universities on research, or with schools on children's education と Kenyatta の s8t_s22 promote the mutual flow of zoological information を共通化すると sharing knowledge。",
                     "③以外の選択肢の罠: ①は Kenyatta のみ，②は両者とも述べていない，④は Aya のみ。"
                 ]
             }
         }},
        {"question_id":"問4","answer_number":43,
         "stem":{"en":"Based on Source A, which of the following is the most appropriate for REASON 2? [43]","ja":"資料Aに基づけば，次の中で理由2として最も適切なものはどれか。[43]"},
         "choices":[
             {"label":"\u2460","en":"Due to zoos working in on-site environments, some rare birds have reappeared in the wild.","ja":"動物園のオンサイト環境での働きにより，一部の希少な鳥が野生に再び姿を現した。","is_correct":False},
             {"label":"\u2461","en":"Funding research on Red List animals is a path that has been pursued by many zoos.","ja":"レッドリストに載っている動物の調査への資金提供は，多くの動物園がたどってきた道だ。","is_correct":False},
             {"label":"\u2462","en":"Thanks to zoos, recorded observations of some endangered species seem to be on the rise.","ja":"動物園のおかげで，一部の絶滅危惧種の観察記録が増えつつあるようだ。","is_correct":True},
             {"label":"\u2463","en":"Zoos have been protecting and saving the lives of a broad range of abandoned animals.","ja":"動物園はさまざまな捨てられた動物の命を守り救ってきた。","is_correct":False}
         ],
         "answer":"\u2462",
         "explanation":{
             "quoted_ja":"正解は\u2462。資料Aでは，絶滅危惧種の保護に動物園が積極的な役割を果たすことが期待されていると述べられており，日本の動物園のオフサイト保存による成功例などが紹介された後，最終文（Although they once ...）では，トキなどの絶滅危惧種について「これらはかつて自然界から姿を消したが，動物園の努力によってその数が増えてきている（their numbers have been growing）」と述べられている。選択肢\u2462の中の「観察記録（recorded observations）」という表現は資料Aの中では用いられていないものの，下線部分は絶滅危惧種の観察記録が存在して，それが増加していることを示唆しているので，\u2462の「動物園のおかげで，一部の絶滅危惧種の観察記録が増えつつあるようだ」という指摘は誤りではないことから，これが正解となる。",
             "quoted_source":"共通テスト 2025年度 追試験 英語（リーディング） 問題・解説",
             "evidence_sentences":["s8t_s45","s8t_s46","s8t_s47"],
             "instructor_note":{
                 "ja":"資料Aの内容に基づいてエッセイの理由2を選ぶ問題です。資料Aの主旨（動物園による種の保存の成果）を正確に読み取りましょう。",
                 "points":[
                     "③: s8t_s47 の their numbers have been growing が recorded observations ... on the rise に対応。recorded observations は直接的な表現ではないが，個体数の増加は観察記録の増加を示唆する。",
                     "①の罠: on-site environments は本文では on-site conservation と off-site conservation の2方式を挙げており，日本の動物園が積極的なのは off-site conservation。on-site を選ぶと逆。",
                     "②の罠: Funding research は資料Aで述べられていない。動物園の役割は保護と繁殖（protect and breed）。",
                     "④の罠: abandoned animals（捨てられた動物）は資料Aの話題ではない。endangered animals（絶滅危惧種）と混同させる罠。"
                 ]
             }
         }},
        {"question_id":"問5","answer_number":44,
         "stem":{"en":"For REASON 3, you have decided to write <em>Zoos have animals that children want to see</em>. Based on Source B, which option best supports this statement? [44]","ja":"理由3として，あなたは「動物園には子どもたちが見たがる動物がいる」と書くことにした。資料Bに基づけば，この言葉を支持する選択肢として最も適切なものはどれか。[44]"},
         "choices":[
             {"label":"\u2460","en":"According to the table, pandas, lions, and elephants are the three most popular zoo animals. The fact that each of them was liked by more than half the kids clearly reveals their popularity.","ja":"表によると，パンダ，ライオン，ゾウの3種は，最も人気のある動物園の動物である。これらのそれぞれが半数を超える子どもたちに好まれたという事実は，明らかにこれらの人気を示している。","is_correct":False},
             {"label":"\u2461","en":"Although the top two animals commonly live among humans, in Japan, more than two thirds of the top 10 animals can only be seen in zoos. This suggests that zoos are special places for young children.","ja":"上位2種の動物は，普通人間と一緒に暮らしているが，日本では上位10種の3分の2を超える動物が，動物園でしか見られない。これは動物園が幼い子どもたちにとって特別な場所であることを示唆している。","is_correct":True},
             {"label":"\u2462","en":"Cats, dogs, and rabbits get a lot of likes from children and can be seen outside zoos. While the number of people keeping pets is reportedly decreasing, their popularity among children is increasing.","ja":"猫，犬，ウサギは子どもたちに好かれることが多く，動物園の外で見ることができる。ペットを飼っている人の数は減っていると報告されているが，子どもたちの間では人気が高まっている。","is_correct":False},
             {"label":"\u2463","en":"While more than 50% of children answered that they liked either cats or dogs, the other top 10 animals are found only in zoos. This means that zoos provide a unique opportunity for kids to see a variety of animals they prefer.","ja":"50パーセントを超える子どもたちが猫か犬のどちらかを好きだと答えたが，上位10種の中でそれ以外の動物は動物園でしか見られない。これは，子どもがより好むさまざまな動物を見る独特の機会を動物園が与えていることを意味する。","is_correct":False}
         ],
         "answer":"\u2461",
         "explanation":{
             "quoted_ja":"正解は\u2461。資料Bの表を参照することにより，\u2461の中の「上位2種の動物（the top two animals）」は，普通人間と一緒に暮らしている」という部分は，下線部が猫と犬のことだとわかるので，常識から考えて正しいとわかる。また「日本では上位10種の3分の2を超える動物が，動物園でしか見られない」という部分も，表の中の「動物園（Zoo）」の欄にチェックマークが7つ付いていることからも正しいとわかる。そして「これは動物園が幼い子どもたちにとって特別な場所であることを示唆している」も特に誤りを含む主張ではないことから，\u2461が正解となる。",
             "quoted_source":"共通テスト 2025年度 追試験 英語（リーディング） 問題・解説",
             "evidence_sentences":["s8t_s48","s8t_s49","s8t_s50","s8t_s51"],
             "instructor_note":{
                 "ja":"資料Bの表データを正確に読み取り，『動物園には子どもが見たがる動物がいる』という主張を裏付ける根拠を選ぶ問題です。",
                 "points":[
                     "②: 上位2種（cat, dog）は動物園外で見られるが，残り8種中7種（panda以下）は動物園でしか見られない → 7/10 > 2/3 → 正しい。動物園が特別な場所であることの根拠として適切。",
                     "①の罠: panda(157), lion(143), elephant(130) → 300人中の半数(150)を超えるのは panda のみ。lion(143) と elephant(130) は半数未満。each of them was liked by more than half は誤り。",
                     "③の罠: ペットを飼う人の数が減っている / 子どもの間で人気が高まっている，という情報は資料Bに存在しない。",
                     "④の罠: 表で rabbit(6位) は Zoo にチェックなし → cat, dog 以外の top 10 が全て動物園にいるわけではない。the other top 10 animals are found only in zoos は誤り。"
                 ]
             }
         }}
    ]
