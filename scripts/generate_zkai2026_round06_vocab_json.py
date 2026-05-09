# -*- coding: utf-8 -*-
"""Z会実戦模試2026第6回の語彙フラッシュカード用 JSON を生成する（例文は手作業）。

第1〜4問は data.json の vocabulary に準拠。第5問語彙は data.json 未収録のため解説冊子（語句表）を正とする。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/zkai/2026/round06/vocabulary_explanations_only_all_sections.json"

# (section_number, flashcard_order, term_en, term_ja, example_en, example_ja, source)
ROWS = [
    # === 第1問 国際フードフェスティバル（ウェブお知らせ）===
    (1, 0, "diverse", "〈形〉多様な", "The festival celebrates our town's diverse cultures through shared meals.", "その祭りは共食を通して町の多様な文化を祝う。", "zkai2026_round06_section1_passage"),
    (1, 1, "demonstration", "〈名〉実演", "Chefs schedule cooking demonstrations every afternoon in the hall.", "シェフたちは会議室で毎午後、料理の実演を予定している。", "zkai2026_round06_section1_passage"),
    (1, 2, "recipe exchange", "〈名〉レシピ交換", "Visitors swap cards at the recipe exchange near the information desk.", "案内所近くのレシピ交換で来場者はカードを交換する。", "zkai2026_round06_section1_passage"),
    (1, 3, "coupon", "〈名〉クーポン", "The admission ticket doubles as a 500-yen coupon at food stalls.", "入場券は屋台で使える500円クーポン兼用だ。", "zkai2026_round06_section1_passage"),
    (1, 4, "stall", "〈名〉露店；売店", "Craft vendors set up stalls beside the outdoor stage.", "クラフト出店者が野外ステージ脇に露店を出す。", "zkai2026_round06_section1_passage"),
    (1, 5, "food stall", "〈名〉フードスタンド", "Arrive early if you want shorter lines at each food stall.", "各フードスタンドの列を短くしたいなら早めに来なさい。", "zkai2026_round06_section1_passage"),
    (1, 6, "admission", "〈名〉入場料", "Admission is five hundred yen for ages thirteen and up.", "13歳以上の入場料は500円である。", "zkai2026_round06_section1_passage"),
    (1, 7, "~ and up", "〈表現〉～以上（年齢など）", "The coupon applies to visitors age thirteen and up only.", "クーポンは13歳以上の来場者にのみ適用される。", "zkai2026_round06_section1_passage"),
    (1, 8, "city hall", "〈名〉市庁舎", "All concerts and talks take place inside the city hall.", "コンサートと講演はすべて市庁舎で行われる。", "zkai2026_round06_section1_passage"),
    (1, 9, "gospel", "〈名〉ゴスペル", "A gospel choir closes Saturday night on the main stage.", "ゴスペルクワイアが土曜夜のメインステージを締める。", "zkai2026_round06_section1_passage"),
    # === 第2問 就活・記事要約 Get Experience, Get Ahead ===
    (2, 0, "real-world", "〈形〉実社会の", "Employers now weigh real-world experience alongside grades.", "雇用主は成績と並んで実社会の経験を重んじる。", "zkai2026_round06_section2_passage"),
    (2, 1, "CV = Curriculum Vitae", "〈名〉履歴書（英式。美式は résumé）", "She rewrote her CV to highlight volunteer leadership roles.", "彼女はボランティアのリーダー経験を強調するようCVを書き直した。", "zkai2026_round06_section2_passage"),
    (2, 2, "qualification", "〈名〉資格", "An extra teaching qualification helped one student stand out.", "追加の教職資格が一人の学生を目立たせた。", "zkai2026_round06_section2_passage"),
    (2, 3, "demonstrate", "〈動〉〜を示す", "Volunteer work demonstrates both leadership and social responsibility.", "ボランティアはリーダーシップと社会責任の両方を示す。", "zkai2026_round06_section2_passage"),
    (2, 4, "licence", "〈名〉免許（証）；許可（英式。美式は license）", "He earned a tour-guide licence during his final year.", "彼は最終学年にツアーガイドの免許を取った。", "zkai2026_round06_section2_passage"),
    (2, 5, "tech firm", "〈名〉IT企業（technology firm）", "Coding classes led to a job offer from a major tech firm.", "プログラミング講座が大手IT企業からの内定につながった。", "zkai2026_round06_section2_passage"),
    (2, 6, "internship", "〈名〉実務研修；インターンシップ", "Her law-office internship lasted three busy months.", "法律事務所のインターンは忙しい3か月続いた。", "zkai2026_round06_section2_passage"),
    (2, 7, "economically-challenged", "〈形〉経済的に困窮している", "Unpaid internships are not realistic for economically-challenged students.", "無給のインターンは経済的に苦しい学生には現実的でない。", "zkai2026_round06_section2_passage"),
    (2, 8, "unpaid", "〈形〉無給の", "Many unpaid internships still build valuable teamwork skills.", "多くの無給インターンでも貴重な協働スキルが身につく。", "zkai2026_round06_section2_passage"),
    (2, 9, "tuition", "〈名〉授業料", "A part-time job can help cover tuition and living costs.", "アルバイトは授業料と生活費の一部を支えうる。", "zkai2026_round06_section2_passage"),
    (2, 10, "strategy", "〈名〉戦略", "Students should pick the strategy that matches their career goals.", "学生は自分の進路目標に合った戦略を選ぶべきだ。", "zkai2026_round06_section2_passage"),
]

# 第3問 自然鑑賞キャンプ（本文）
ROWS += [
    (3, 0, "breeze", "〈名〉微風", "We felt a cool ocean breeze as soon as we stepped off the bus.", "バスを降りるとすぐ涼しい海風を感じた。", "zkai2026_round06_section3_passage"),
    (3, 1, "ancient", "〈形〉古代の；古い", "An ancient forest trail wound toward the shoreline cliffs.", "古代林の小道が海岸の崖へと続いていた。", "zkai2026_round06_section3_passage"),
    (3, 2, "put up ~", "〈表現〉〜（テント）を張る", "We put up our tents before the sun dipped below the ridge.", "太陽が尾根に沈む前にテントを張った。", "zkai2026_round06_section3_passage"),
    (3, 3, "reflect", "〈動〉〜を反射する", "Moonlight began to reflect on the quiet tidal pools.", "月明かりが静かな潮だまりに反射し始めた。", "zkai2026_round06_section3_passage"),
    (3, 4, "layer", "〈名〉層", "Fog formed a thin layer over the grass at sunrise.", "日の出に草の上に薄い霧の層ができた。", "zkai2026_round06_section3_passage"),
    (3, 5, "break ~ open", "〈表現〉〜を割って開ける", "Instructor Yuki showed how to break a coconut open without tools.", "ユキ講師は道具なしでココナッツを割って開ける方法を見せた。", "zkai2026_round06_section3_passage"),
    (3, 6, "flesh", "〈名〉（果物の）果肉", "The sweet flesh tasted better than any supermarket fruit.", "甘い果肉はどのスーパーの果物よりおいしかった。", "zkai2026_round06_section3_passage"),
    (3, 7, "head back", "〈表現〉戻る", "We headed back to camp when thunder rumbled offshore.", "沖で雷鳴がしたのでキャンプ地へ戻った。", "zkai2026_round06_section3_passage"),
]
ROWS += [
    (3, 8, "shelter（問1②）", "〈名〉住居；身を守る場所", "Choice ② described leaves as shelter from heavy rain.", "選択肢②は葉を大雨からの身を守る場所として描いた。", "zkai2026_round06_section3_questions"),
    (3, 9, "creature（問1③）", "〈名〉生物", "Option ③ mentioned shy forest creatures Tony never saw.", "選択肢③はトニーが見なかった臆病な森の生物に言及した。", "zkai2026_round06_section3_questions"),
    (3, 10, "organism（問2③）", "〈名〉（特に小さな）生物；生命体", "The correct item named soil organisms that recycle nutrients.", "正解は養分を循環させる土の微生物に言及していた。", "zkai2026_round06_section3_questions"),
]

# 第4問 目の健康エッセイ（本文）
ROWS += [
    (4, 0, "screen time", "〈名〉（パソコン・スマートフォンなどの）画面を眺めて過ごす時間；スクリーンタイム", "Too much screen time can worsen children's vision.", "画面を眺める時間が長すぎると子どもの視力を悪化させうる。", "zkai2026_round06_section4_passage"),
    (4, 1, "vision", "〈名〉視力；視覚", "Outdoor breaks may protect vision more than extra classes do.", "外遊びの休憩は増補の授業より視力を守りうる。", "zkai2026_round06_section4_passage"),
    (4, 2, "take a step for ~", "〈表現〉〜のために措置を講じる", "Schools should take a step for eye health before exams peak.", "試験本番の前に学校は目の健康のための措置を講じるべきだ。", "zkai2026_round06_section4_passage"),
    (4, 3, "focus on ~", "〈表現〉〜に焦点を合わせる", "The third paragraph focuses on the twenty-twenty-twenty rule.", "第3段落は20-20-20のルールに焦点を合わせる。", "zkai2026_round06_section4_passage"),
    (4, 4, "strain", "〈名〉（目などの）緊張；負担", "Short pauses ease eye strain during long study sessions.", "長い勉強の合間の短い休憩が眼の疲れを和らげる。", "zkai2026_round06_section4_passage"),
    (4, 5, "sunscreen", "〈名〉日焼け止め剤", "Sunscreen shields skin just as sunglasses shield the eyes.", "日焼け止めが肌を守るようにサングラスが目を守る。", "zkai2026_round06_section4_passage"),
    (4, 6, "look into the distance", "〈表現〉遠くを見る", "Every twenty minutes look into the distance for twenty seconds.", "20分ごとに20秒間、遠くを見なさい。", "zkai2026_round06_section4_passage"),
]
ROWS += [
    (4, 7, "improvement（問3④）", "〈名〉改善；改良", "Choice ④ promised cosmetic improvements instead of eye science.", "選択肢④は眼科学より化粧品の改良を約束した。", "zkai2026_round06_section4_questions"),
]

# 第5問 学習スタイル・研修（語句表／data.json 未収録）
ROWS += [
    (5, 0, "educational psychologist", "〈名〉教育心理学者", "An educational psychologist explained how memory differs by learner.", "教育心理学者が学習者ごとの記憶の違いを説明した。", "zkai2026_round06_section5_passage"),
    (5, 1, "business manager", "〈名〉経営者", "The business manager asked HR for clearer training metrics.", "経営者は人事に研修の指標を明確にしてほしいと頼んだ。", "zkai2026_round06_section5_passage"),
    (5, 2, "auditory", "〈形〉聴覚の", "Auditory learners remember talks better if they record them.", "聴覚型の学習者は話を録音したほうが覚えやすい。", "zkai2026_round06_section5_passage"),
    (5, 3, "kinesthetic", "〈形〉運動感覚の", "Kinesthetic students grasp ideas faster when they move or build models.", "運動感覚型の生徒は体を動かしたり模型を作ると理解が早い。", "zkai2026_round06_section5_passage"),
    (5, 4, "pictogram", "〈名〉絵文字", "Safety pictograms near the machinery need no words.", "機械のそばの安全標識のピクトグラムはことばがなくても通じる。", "zkai2026_round06_section5_passage"),
    (5, 5, "diagram", "〈名〉図表", "She redrew the wiring diagram until every wire matched reality.", "彼女は実物に合うまで配線の図表を描き直した。", "zkai2026_round06_section5_passage"),
    (5, 6, "recall", "〈動〉〜を思い出す", "Can you recall the three cues the trainer stressed?", "講師が強調した3つの手がかりを思い出せますか。", "zkai2026_round06_section5_passage"),
    (5, 7, "content", "〈名〉コンテンツ，内容", "Video content helps only if captions match the spoken lines.", "字幕が発話と一致して初めて動画の内容は役立つ。", "zkai2026_round06_section5_passage"),
    (5, 8, "summarize", "〈動〉〜を要約する", "Summarize each chapter in one sentence before next week.", "来週までに各章を一文で要約しなさい。", "zkai2026_round06_section5_passage"),
    (5, 9, "strategy", "〈名〉戦略", "Their onboarding strategy mixes online modules and floor shadowing.", "新人研修の戦略はオンラインモジュールと現場同行を混ぜる。", "zkai2026_round06_section5_passage"),
    (5, 10, "enhance", "〈動〉〜を向上させる", "Short quizzes can enhance retention without adding lecture hours.", "短い小テストは講義時間を増やさず定着を向上させうる。", "zkai2026_round06_section5_passage"),
    (5, 11, "hands-on", "〈形〉現場での，実地の", "New hires need hands-on practice on the assembly line.", "新入社員は組立ラインでの実地の練習が要る。", "zkai2026_round06_section5_passage"),
    (5, 12, "engage in ~", "〈表現〉〜に関わる", "Trainers engage learners in role-play before the real calls start.", "講師は本番の電話の前にロールプレイへ学習者を巻き込む。", "zkai2026_round06_section5_passage"),
    (5, 13, "material", "〈名〉素材", "The recycled material met strength tests for airplane panels.", "再生材は機体パネルに耐える強度試験を満たした。", "zkai2026_round06_section5_passage"),
    (5, 14, "acknowledge", "〈動〉〜を認める", "Managers must acknowledge mistakes before proposing fixes.", "管理者は修正案を出す前に過ちを認めねばならない。", "zkai2026_round06_section5_passage"),
    (5, 15, "demonstration", "〈名〉実演", "The safety demonstration used a cutaway motor everyone could see.", "安全の実演では誰もが見える断面モーターを使った。", "zkai2026_round06_section5_passage"),
    (5, 16, "in person", "〈副〉自分で，直接に", "Apply in person if the portal keeps rejecting your ID scan.", "IDスキャンが弾かれるなら直接窓口へ出向きなさい。", "zkai2026_round06_section5_passage"),
    (5, 17, "informational", "〈形〉情報を得られる", "The booth is informational only; it does not sell products.", "そのブースは情報提供のみで商品は売らない。", "zkai2026_round06_section5_passage"),
    (5, 18, "drawing", "〈名〉図面", "Check the drawing for bolt size before you order spares.", "予備部品を注文する前に図面のボルト寸法を確かめなさい。", "zkai2026_round06_section5_passage"),
    (5, 19, "machinery", "〈名〉（集合的に）機械（設備）", "Guards around heavy machinery must stay locked during power-up.", "大型機械周りのガードは立ち上げ中は施錠したままにする。", "zkai2026_round06_section5_passage"),
    (5, 20, "handle", "〈動〉〜に手を触れて扱う，操作する", "Trainees may not handle live wires until they pass the quiz.", "小テストに合格するまで研修生は活線に触れてはならない。", "zkai2026_round06_section5_passage"),
]
ROWS += [
    (5, 21, "co-worker（問1④）", "〈名〉同僚，仕事仲間", "Choice ④ used co-worker in a sense that did not match the stem.", "選択肢④は設問文と合わない意味で co-worker を使っていた。", "zkai2026_round06_section5_questions"),
]

# 第6問 物語（語句表／data.json 未収録）
ROWS += [
    (6, 0, "reunion", "〈名〉再会（の集い）", "The alumni reunion filled the gym with laughter and name tags.", "同窓会の再会の集いは体育館に笑い声と名札で満ちた。", "zkai2026_round06_section6_passage"),
    (6, 1, "starting line", "〈名〉スタートライン", "Runners toe the starting line until the gun cracks.", "選手たちは発砲までスタートラインに足をそろえる。", "zkai2026_round06_section6_passage"),
    (6, 2, "a sea of ~", "〈名表現〉非常にたくさんの～", "A sea of umbrellas swayed outside the concert hall.", "コンサートホール外では傘が非常にたくさん揺れた。", "zkai2026_round06_section6_passage"),
    (6, 3, "flyer", "〈名〉チラシ", "She grabbed a flyer taped to the community board.", "彼女は掲示板に貼られたチラシを手に取った。", "zkai2026_round06_section6_passage"),
    (6, 4, "bond", "〈自〉信頼関係を結ぶ；〈名〉きずな", "Long talks helped them bond during the winter retreat.", "冬の合宿で長い話が二人のきずなを深めた。", "zkai2026_round06_section6_passage"),
    (6, 5, "halfway through", "〈副〉途中で", "Halfway through the speech, thunder drowned the mic.", "スピーチの途中で雷がマイクの声をかき消した。", "zkai2026_round06_section6_passage"),
    (6, 6, "medical", "〈形〉医療の", "Volunteers offered medical checks beside the finish tents.", "ボランティアがフィニッシュテント脇で医療チェックを行った。", "zkai2026_round06_section6_passage"),
    (6, 7, "cross the finish line", "〈表現〉ゴールインする，完走する", "She cried when her grandmother crossed the finish line.", "祖母がゴールテープを切ったとき彼女は泣いた。", "zkai2026_round06_section6_passage"),
    (6, 8, "refuse to do", "〈表現〉…することを断る，拒む", "He refused to quit even when his knees shook.", "膝が震えても彼は棄権することを拒んだ。", "zkai2026_round06_section6_passage"),
    (6, 9, "race", "〈自〉（脈拍・胸などが）どきどきする，速く打つ", "Her pulse began to race as the anthem swelled.", "国歌が高まるにつれ脈がどきどきし始めた。", "zkai2026_round06_section6_passage"),
    (6, 10, "fire", "〈自〉（銃・砲が）発射される", "No starter pistol may fire until every lane is set.", "全レーンが整うまでスターターピストルは発射されない。", "zkai2026_round06_section6_passage"),
    (6, 11, "in rhythm with ~", "〈表現〉～とリズムが合って", "Their footsteps fell in rhythm with the drum major's baton.", "足音はドラムメジャーのバトンとリズムが合った。", "zkai2026_round06_section6_passage"),
    (6, 12, "be close to doing", "〈表現〉今にも…しそうである", "She was close to tears when the medal arrived.", "メダルが渡るとき彼女は今にも涙がこぼれそうだった。", "zkai2026_round06_section6_passage"),
    (6, 13, "near", "〈他〉～に近づく", "He neared the podium but paused to breathe.", "彼は演壇に近づいたが立ち止まって呼吸した。", "zkai2026_round06_section6_passage"),
    (6, 14, "drive", "〈動〉～を駆り立てる", "Pride drove her to train every dawn that month.", "誇りが彼女をその月は毎朝の訓練へ駆り立てた。", "zkai2026_round06_section6_passage"),
    (6, 15, "muscle", "〈名〉筋肉", "Ice packs soothed the sore muscle after the relay.", "リレーのあとアイスパックが痛む筋肉を和らげた。", "zkai2026_round06_section6_passage"),
    (6, 16, "ache", "〈動〉痛む", "Her shoulders ached from clapping for every finisher.", "すべての完走者に拍手するあまり肩が痛んだ。", "zkai2026_round06_section6_passage"),
    (6, 17, "struggle", "〈名〉苦労，難題", "Finishing the course was a struggle after the injury.", "故障のあとでコースを完走するのは難題だった。", "zkai2026_round06_section6_passage"),
    (6, 18, "rush", "〈名〉勢いよく流れること", "She felt a rush of relief when buses returned on time.", "バスが定刻で戻ったとき安堵がどっと流れた。", "zkai2026_round06_section6_passage"),
    (6, 19, "breathe", "〈動〉呼吸する", "Stop beside the cone and breathe through your nose.", "コーンの横で立ち止まり鼻で呼吸しなさい。", "zkai2026_round06_section6_passage"),
    (6, 20, "as ... as ever", "〈表現〉相変わらず…", "Granddad was as cheerful as ever despite the rain.", "祖父は雨にもかかわらず相変わらず陽気だった。", "zkai2026_round06_section6_passage"),
    (6, 21, "remark that ...", "〈表現〉…と言う，述べる", "The coach remarked that pacing mattered more than pride.", "コーチはペース配分が誇りより大事だと述べた。", "zkai2026_round06_section6_passage"),
    (6, 22, "wipe away a tear", "〈表現〉涙をふく", "Her sister wiped away a tear as the anthem played.", "国歌が流れるとき姉は涙をふいた。", "zkai2026_round06_section6_passage"),
    (6, 23, "catch up", "〈表現〉（久しく会わなかった人と）話をする；（新しい情報，近況などを）聞く", "We caught up over tea about jobs and toddlers.", "お茶を飲みながら仕事や幼児の近況を聞き合った。", "zkai2026_round06_section6_passage"),
    (6, 24, "eagerly", "〈副〉熱心に", "Fans eagerly scanned the results posted on the wall.", "ファンは壁に貼られた結果を熱心に見た。", "zkai2026_round06_section6_passage"),
    (6, 25, "await", "〈動〉～を待つ", "A warm breakfast awaited them in the tent city.", "テント村には温かい朝食が彼らを待っていた。", "zkai2026_round06_section6_passage"),
]
ROWS += [
    (6, 26, "inspire（問1②）", "〈動〉～を鼓舞する", "Choice ② paired inspire with a mentor cliché missing from the text.", "選択肢②は本文にないメンターの型言句に inspire を結びつけた。", "zkai2026_round06_section6_questions"),
]

# 第7問 サンゴ礁・環境（語句表／data.json 未収録）
ROWS += [
    (7, 0, "coral", "〈名〉サンゴ", "Bleached coral looks like pale rock underwater.", "白化したサンゴは水中で淡い岩のように見える。", "zkai2026_round06_section7_passage"),
    (7, 1, "reef", "〈名〉礁（水面に表れていない岩）", "The ship avoided a hidden reef near the buoy.", "船はブイ近くの水面下の礁を避けた。", "zkai2026_round06_section7_passage"),
    (7, 2, "trigger", "〈動〉〜を引き起こす", "Warmer seas can trigger mass bleaching events.", "海水温の上昇が大量白化を引き起こしうる。", "zkai2026_round06_section7_passage"),
    (7, 3, "geographical", "〈形〉地理的な", "A geographical survey mapped every shallow shelf.", "地理的調査が浅い棚礁をすべて地図化した。", "zkai2026_round06_section7_passage"),
    (7, 4, "threaten", "〈動〉〜を脅かす", "Polluted runoff threatens larvae before they settle.", "汚染された地表水が付着前の幼生を脅かす。", "zkai2026_round06_section7_passage"),
    (7, 5, "ecosystem", "〈名〉生態系", "One collapsed ecosystem can echo along the food web.", "一つの生態系の崩壊は食物連鎖に波及する。", "zkai2026_round06_section7_passage"),
    (7, 6, "seashore", "〈名〉海岸", "Tourists crowded the seashore but the reef stayed closed.", "観光客は海岸に殺到したがサンゴ域は閉鎖されたままだった。", "zkai2026_round06_section7_passage"),
    (7, 7, "address", "〈動〉〜に対処する", "Engineers addressed erosion with living barriers.", "技術者は生物によるバリアで浸食に対処した。", "zkai2026_round06_section7_passage"),
    (7, 8, "attach (*oneself*) to ~", "〈表現〉〜に付着する〔くっつく〕", "Larvae attach themselves to clean rock before growing.", "幼生は成長する前にきれいな岩に付着する。", "zkai2026_round06_section7_passage"),
    (7, 9, "reproduce", "〈動〉繁殖する", "Once algae dominate, corals struggle to reproduce.", "藻が優占するとサンゴは繁殖しにくくなる。", "zkai2026_round06_section7_passage"),
    (7, 10, "erosion", "〈名〉浸食", "Wave erosion reshaped the soft limestone cliffs.", "波の浸食が軟らかい石灰岩の崖を形作り直した。", "zkai2026_round06_section7_passage"),
    (7, 11, "wear away ~", "〈表現〉〜をすり減らす", "Tides slowly wear away the older seawall blocks.", "潮が古い防潮ブロックをじわじわすり減らす。", "zkai2026_round06_section7_passage"),
    (7, 12, "soil", "〈名〉土壌", "Storm water washed soil straight into the bay.", "雨水が土壌をそのまま湾へ流し込んだ。", "zkai2026_round06_section7_passage"),
    (7, 13, "as much as ~", "〈表現〉〜（ほど）も", "They removed almost as much as the dredgers had dumped.", "彼らは浚渫船が捨てた量ほどもほぼ撤去した。", "zkai2026_round06_section7_passage"),
    (7, 14, "seawall", "〈名〉護岸堤，防潮堤", "The cracked seawall failed when swells exceeded forecasts.", "予報を超えるうねりでひび割れた護岸堤は耐えられなかった。", "zkai2026_round06_section7_passage"),
    (7, 15, "steel", "〈形〉鋼鉄の", "Steel frames brace the museum against storm surges.", "鋼鉄の骨組みが博物館を高潮から守る。", "zkai2026_round06_section7_passage"),
    (7, 16, "cage", "〈名〉檻", "Volunteers lifted fish cages off delicate polyps.", "ボランティアは繊弱なポリプから魚の檻を持ち上げた。", "zkai2026_round06_section7_passage"),
    (7, 17, "incredibly", "〈副〉信じられないことに", "Incredibly, sponges colonized the old anchors first.", "信じられないことだがスポンジがまず旧い錨に定着した。", "zkai2026_round06_section7_passage"),
    (7, 18, "erode", "〈動〉浸食される", "Without mangroves the bank erodes within one monsoon.", "マングローブがなければ土手は一つの雨季で浸食される。", "zkai2026_round06_section7_passage"),
    (7, 19, "the Mediterranean Sea", "〈名〉地中海", "Posidonia meadows ring parts of the Mediterranean Sea.", "海神草の草原が地中海の一部を取り囲む。", "zkai2026_round06_section7_passage"),
    (7, 20, "population", "〈名〉個体数", "The population of reef fish fell after the heat spike.", "熱波のあと礁で魚の個体数が減った。", "zkai2026_round06_section7_passage"),
    (7, 21, "last", "〈動〉維持〔持続〕する", "The calm lasted only until the cold front landed.", "小康は寒冷前線が来るまでしか続かなかった。", "zkai2026_round06_section7_passage"),
    (7, 22, "over time", "〈副〉長期にわたって；やがて", "Over time, replanted corals regained their color.", "やがて移植したサンゴは色を取り戻した。", "zkai2026_round06_section7_passage"),
    (7, 23, "incorrectly", "〈副〉間違って", "Maps incorrectly marked the channel as deep water.", "海図は水路を誤って深水として示していた。", "zkai2026_round06_section7_passage"),
    (7, 24, "approve", "〈動〉〜を承認する", "The harbor board refused to approve more breakwater quarrying.", "港務局は防潮堤の採石追加を承認しなかった。", "zkai2026_round06_section7_passage"),
    (7, 25, "hold ~ together", "〈表現〉〜を一体化させる", "Calcium skeletons hold the colony together.", "石灰質の骨格が群体を一体化させる。", "zkai2026_round06_section7_passage"),
    (7, 26, "break down", "〈表現〉分解する", "Bacteria break down dead matter on the sandy bottom.", "細菌が砂底のデトリタスを分解する。", "zkai2026_round06_section7_passage"),
    (7, 27, "end up doing", "〈表現〉結局…することになる", "We end up doing night dives whenever the moon is bright.", "月が明るい夜は結局ナイトダイブに行くことになる。", "zkai2026_round06_section7_passage"),
    (7, 28, "ceramics", "〈名〉陶磁器", "Broken ceramics littered the tide line after the storm.", "嵐のあと干潮線に砕けた陶磁器が散らばった。", "zkai2026_round06_section7_passage"),
    (7, 29, "the Indian Ocean", "〈名〉インド洋", "Warm Indian Ocean currents reach this atoll in March.", "インド洋の暖流が3月にこの環礁へ届く。", "zkai2026_round06_section7_passage"),
    (7, 30, "innovative", "〈形〉革新的な", "Their innovative reef tiles seeded faster growth.", "彼らの革新的な礁タイルがより速い成長を促した。", "zkai2026_round06_section7_passage"),
    (7, 31, "implement", "〈動〉〜を実行する", "Park rangers implement the closure weekly during spawning.", "公園のレンジャーは産卵期に毎週閉鎖を実行する。", "zkai2026_round06_section7_passage"),
]
ROWS += [
    (7, 32, "adapt to ~（問4④）", "〈表現〉〜に適応する", "Choice ④ misused adapt to for a habitat the essay never cited.", "選択肢④は本文にない生息地に adapt to を当てはめた。", "zkai2026_round06_section7_questions"),
    (7, 33, "the next time ...（問5③）", "〈表現〉次に…する時は", "Option ③ shifted the timeline with the next time we dredge.", "選択肢③は次に浚渫するときはで時系列をずらした。", "zkai2026_round06_section7_questions"),
    (7, 34, "count on ~（問5④）", "〈表現〉〜を頼る", "④ suggested tourists could count on calm seas every noon.", "選択肢④は毎正午に穏やかな海と頼れると示唆した。", "zkai2026_round06_section7_questions"),
    (7, 35, "note that ...（問5⑤）", "〈表現〉…ことに注目する", "The stem asked you to note that funding lagged repairs.", "設問は資金が修復に追いつかないことに注目するよう求めた。", "zkai2026_round06_section7_questions"),
]

# 第8問 自動運転・意見読解（語句表／data.json 未収録）
ROWS += [
    (8, 0, "legal", "〈形〉法律の，法定の", "Strict legal tests delay every new driver-assist feature.", "厳しい法定試験が新しい運転支援機能ごとに遅らせる。", "zkai2026_round06_section8_passage"),
    (8, 1, "viewpoint", "〈名〉見解，観点", "The editorial mixed four viewpoints on road data sharing.", "社説は道路データ共有について四つの観点を混ぜた。", "zkai2026_round06_section8_passage"),
    (8, 2, "outline", "〈名〉概要", "Your outline should preview each counterargument fairly.", "概要は反論も公平に予告すべきだ。", "zkai2026_round06_section8_passage"),
    (8, 3, "additional", "〈形〉追加の", "City hall posted additional maps of trial service zones.", "市役所は試行運行圏の追加の地図を掲示した。", "zkai2026_round06_section8_passage"),
    (8, 4, "source", "〈名〉出典，情報源，資料", "Check the source before you cite crash statistics online.", "引用前にネットの事故統計の出典を確かめなさい。", "zkai2026_round06_section8_passage"),
    (8, 5, "safety", "〈名〉安全性", "Safety agencies argue software updates beat roadside banners.", "安全当局はソフト更新が看板より効くと主張する。", "zkai2026_round06_section8_passage"),
    (8, 6, "responsibility", "〈名〉責任", "Shared responsibility blurred when two systems steer at once.", "二つのシステムが同時に操舵すると責任がぼやける。", "zkai2026_round06_section8_passage"),
    (8, 7, "get around", "〈表現〉あちこち移動する", "Seniors get around more if subsidized robotaxis return.", "補助付きロボタクが再開すれば高齢者はあちこち動きやすい。", "zkai2026_round06_section8_passage"),
    (8, 8, "be tempted to do", "〈表現〉…したくなる", "Drivers are tempted to nap whenever the cabin goes silent.", "車内が静かになるといつも運転席で眠くなる。", "zkai2026_round06_section8_passage"),
    (8, 9, "risky", "〈形〉危険な", "Over-the-air patches feel risky on mountain switchbacks.", "山道のヘアピンでOTA更新は危険に感じる。", "zkai2026_round06_section8_passage"),
    (8, 10, "economy", "〈名〉経済", "The gig economy reshaped how teens earn driving data credits.", "ギグ経済は若者が運転データのクレジットを得る形を変えた。", "zkai2026_round06_section8_passage"),
    (8, 11, "freedom", "〈名〉自由", "Advocates tie freedom of movement to open routing APIs.", "支援者は移動の自由を公開ルーティングAPIに結びつける。", "zkai2026_round06_section8_passage"),
    (8, 12, "undergo", "〈動〉〜を経験する", "Every module must undergo redundancy tests each winter.", "各モジュールは毎冬冗長試験を経験しなければならない。", "zkai2026_round06_section8_passage"),
    (8, 13, "noticeable", "〈形〉顕著な", "A noticeable lag appeared after the cloud handshake failed.", "クラウド握手失敗のあと顕著な遅れが出た。", "zkai2026_round06_section8_passage"),
    (8, 14, "risk assessment", "〈名〉危険性の評価", "Their risk assessment ignored cyclists hugging the curb.", "彼らの危険性の評価は縁石に寄る自転車を無視していた。", "zkai2026_round06_section8_passage"),
    (8, 15, "have an impact on ~", "〈表現〉〜に影響を与える", "Weather hardly has an impact on lidar the way fog does on cameras.", "天候はカメラのような霧ほどライダーに影響を与えにくい。", "zkai2026_round06_section8_passage"),
    (8, 16, "wealthy", "〈形〉裕福な", "Only wealthy cities piloted convoys with platinum sensors.", "裕福な都市だけが最高級センサーの隊列走行を試した。", "zkai2026_round06_section8_passage"),
    (8, 17, "go against ~", "〈表現〉〜に反する", "Selling raw footage may go against privacy guidelines.", "生映像を売ることはプライバシー指針に反しうる。", "zkai2026_round06_section8_passage"),
    (8, 18, "division", "〈名〉分断", "Public hearings exposed the rural-urban division on subsidies.", "公聴会は補助金をめぐる都市と地方の分断を露わにした。", "zkai2026_round06_section8_passage"),
    (8, 19, "destructive", "〈形〉破壊的な", "One destructive rumor stalled the merger vote overnight.", "一つの破壊的うわさが一夜で合併投票を滞らせた。", "zkai2026_round06_section8_passage"),
    (8, 20, "fault", "〈名〉責任，欠点", "Insurers disputed fault when both logs looked incomplete.", "双方のログが欠けると保険会社は過失を争った。", "zkai2026_round06_section8_passage"),
    (8, 21, "behavior", "〈名〉態度，行動", "Telemetric behavior scoring spooked privacy advocates.", "遠隔計測の行動スコアはプライバシー擁護派を驚かせた。", "zkai2026_round06_section8_passage"),
    (8, 22, "parental", "〈形〉保護者の", "Parental consent gates every teen ride-share download here.", "ここでは保護者の同意が若者のライドシェアDLを規制する。", "zkai2026_round06_section8_passage"),
    (8, 23, "observe", "〈動〉〜を観察する", "Analysts observe rush-hour merges to tune the merge model.", "分析者は合流モデルを調整するためラッシュ時の合流を観察する。", "zkai2026_round06_section8_passage"),
]
ROWS += [
    (8, 24, "be related to ~（問1②）", "〈表現〉〜に関係する", "Choice ② claimed fines were related to mileage, not risk.", "選択肢②は罰金が危険ではなく走行距離に関係すると主張した。", "zkai2026_round06_section8_questions"),
    (8, 25, "effective（問1③）", "〈形〉効果的な", "③ praised the ad as effective though it cited no numbers.", "③は数字を掲げていないのに広告を効果的だとほめた。", "zkai2026_round06_section8_questions"),
    (8, 26, "mature（問1③）", "〈動〉成長する", "Another ③ option said the market must mature before rollout.", "別の③は市場がデプロイ前に成熟しなければと述べた。", "zkai2026_round06_section8_questions"),
    (8, 27, "technological skill（問2②）", "〈名〉科学技術を扱う力", "② linked technological skill to hardware swaps, not ethics.", "②は科学技術を扱う力を倫理ではなく部品交換に結びつけた。", "zkai2026_round06_section8_questions"),
    (8, 28, "safety feature（問2③）", "〈名〉安全機能", "③ overstated a safety feature the brochure never listed.", "③はパンフにない安全機能を誇張した。", "zkai2026_round06_section8_questions"),
    (8, 29, "statistics（問3[43]①）", "〈名〉統計（データ）", "① leaned on outdated statistics about pedestrian deaths.", "①は歩行者死亡の古い統計に頼った。", "zkai2026_round06_section8_questions"),
    (8, 30, "evidence（問3[43]①）", "〈名〉証拠", "Duplicate ① paired weak evidence with a bold headline.", "重複する①は弱い証拠を大胆な見出しと結びつけた。", "zkai2026_round06_section8_questions"),
    (8, 31, "process（問3[43]②）", "〈名〉過程", "② skipped the approval process outlined in Source B.", "②は資料Bの承認過程を飛ばした。", "zkai2026_round06_section8_questions"),
    (8, 32, "lose focus（問3[43]③）", "〈表現〉集中力を失う", "③ warned drivers lose focus when alarms pulse constantly.", "③は警報が連続だと運転者が集中力を失うと警告した。", "zkai2026_round06_section8_questions"),
    (8, 33, "appropriate（問4）", "〈形〉適切な", "The reviewer asked for a more appropriate tone in Step 2.", "査読者はステップ2の語気をより適切に求めた。", "zkai2026_round06_section8_questions"),
    (8, 34, "expense（問4①）", "〈名〉費用", "① hid the long-run expense of fleet upgrades.", "①は車両更新の長期的費用を隠した。", "zkai2026_round06_section8_questions"),
    (8, 35, "result in ~（問4②）", "〈表現〉（結果的に）〜につながる", "One ② claimed deregulation would result in chaos.", "一方の②は規制緩和が混乱につながると述べた。", "zkai2026_round06_section8_questions"),
    (8, 36, "be capable of ~（問4②）", "〈表現〉〜の能力がある", "The other ② said AI was capable of moral reasoning.", "もう一方の②はAIが道徳推論の能力があるとした。", "zkai2026_round06_section8_questions"),
    (8, 37, "drug addiction（問5①）", "〈名〉薬物中毒", "① drew a loose analogy to drug addiction and screen time.", "①はスクリーンタイムと薬物中毒をゆるく類推した。", "zkai2026_round06_section8_questions"),
    (8, 38, "ignore（問5②）", "〈動〉〜を無視する", "② urged cities not to ignore nighttime freight routes.", "②は都市に夜間貨物ルートを無視するなと訴えた。", "zkai2026_round06_section8_questions"),
    (8, 39, "additionally（問5③）", "〈副〉その上，さらに", "One ③ opener used additionally without adding new data.", "③の一つは新データなしに additionally で始めた。", "zkai2026_round06_section8_questions"),
    (8, 40, "indicate that ...（問5③）", "〈表現〉…ということを示す", "Another ③ failed to indicate that the chart was indexed.", "別の③は図表が指数化されていることを示さなかった。", "zkai2026_round06_section8_questions"),
    (8, 41, "demonstrate（問5④）", "〈動〉〜を示す", "④ did demonstrate bias but mislabeled the axis.", "④は偏りは示したが軸のラベルを誤った。", "zkai2026_round06_section8_questions"),
]


def build():
    entries = []
    for sec, order, te, tj, ex_en, ex_ja, src in ROWS:
        entries.append(
            {
                "term_en": te,
                "term_ja": tj,
                "example_en": ex_en,
                "example_ja": ex_ja,
                "flashcard_order": order,
                "occurrences": [
                    {
                        "section_number": sec,
                        "question_id": "vocabulary",
                        "answer_number": None,
                        "source": src,
                    }
                ],
            }
        )
    counts = {}
    for sec, *_ in ROWS:
        counts[sec] = counts.get(sec, 0) + 1
    n3p = sum(1 for r in ROWS if r[0] == 3 and r[6] == "zkai2026_round06_section3_passage")
    n3q = sum(1 for r in ROWS if r[0] == 3 and r[6] == "zkai2026_round06_section3_questions")
    n4p = sum(1 for r in ROWS if r[0] == 4 and r[6] == "zkai2026_round06_section4_passage")
    n4q = sum(1 for r in ROWS if r[0] == 4 and r[6] == "zkai2026_round06_section4_questions")
    n5p = sum(1 for r in ROWS if r[0] == 5 and r[6] == "zkai2026_round06_section5_passage")
    n5q = sum(1 for r in ROWS if r[0] == 5 and r[6] == "zkai2026_round06_section5_questions")
    n6p = sum(1 for r in ROWS if r[0] == 6 and r[6] == "zkai2026_round06_section6_passage")
    n6q = sum(1 for r in ROWS if r[0] == 6 and r[6] == "zkai2026_round06_section6_questions")
    n7p = sum(1 for r in ROWS if r[0] == 7 and r[6] == "zkai2026_round06_section7_passage")
    n7q = sum(1 for r in ROWS if r[0] == 7 and r[6] == "zkai2026_round06_section7_questions")
    n8p = sum(1 for r in ROWS if r[0] == 8 and r[6] == "zkai2026_round06_section8_passage")
    n8q = sum(1 for r in ROWS if r[0] == 8 and r[6] == "zkai2026_round06_section8_questions")
    meta = {
        "exam": "Z会 共通テスト実戦模試 2026年 第6回",
        "source": (
            "data/zkai/2026/round06/data.json（第1〜4問 vocabulary）／"
            "第5〜8問は解説冊子語句表に準拠（data 未収録・scripts/generate_zkai2026_round06_vocab_json.py）"
        ),
        "sections_in_data": [1, 2, 3, 4, 5, 6, 7, 8],
        "section1_passage_vocab": {"label": "第1問 語句（国際フードフェスティバル）", "count": counts.get(1, 0)},
        "section2_passage_vocab": {"label": "第2問 語句（就活・記事要約）", "count": counts.get(2, 0)},
        "section3_passage_vocab": {"label": "第3問 語句・本文（自然鑑賞キャンプ）", "count": n3p},
        "section3_questions_vocab": {"label": "第3問 設問語句", "count": n3q},
        "section4_passage_vocab": {"label": "第4問 語句・本文（目の健康）", "count": n4p},
        "section4_questions_vocab": {"label": "第4問 設問語句", "count": n4q},
        "section5_passage_vocab": {"label": "第5問 語句・本文（学習スタイル・研修）", "count": n5p},
        "section5_questions_vocab": {"label": "第5問 設問語句", "count": n5q},
        "section6_passage_vocab": {"label": "第6問 語句・本文（物語）", "count": n6p},
        "section6_questions_vocab": {"label": "第6問 設問語句", "count": n6q},
        "section7_passage_vocab": {"label": "第7問 語句・本文（サンゴ礁・環境）", "count": n7p},
        "section7_questions_vocab": {"label": "第7問 設問語句", "count": n7q},
        "section8_passage_vocab": {"label": "第8問 語句・本文（意見・自動運転レポート）", "count": n8p},
        "section8_questions_vocab": {"label": "第8問 設問語句", "count": n8q},
    }
    return {"meta": meta, "entries": entries}


def main():
    data = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({len(data['entries'])} entries)")


if __name__ == "__main__":
    main()
