# -*- coding: utf-8 -*-
"""Z会実戦模試2026第2回の語彙フラッシュカード用 JSON を生成する（data.json 準拠・例文は手作業）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/zkai/2026/round02/vocabulary_explanations_only_all_sections.json"

# (section_number, flashcard_order, term_en, term_ja, example_en, example_ja, source)
ROWS = [
    # === 第1問 パンフレット（町の本棚）===
    (1, 0, "access", "〈動〉〜に接近する；〜を利用できる", "Pick a place that readers can access without a key.", "鍵なしで利用者が手の届く場所を選びましょう。", "zkai2026_round02_section1_passage"),
    (1, 1, "option", "〈名〉選択肢", "A shelf in a park or near home are both good options.", "公園や自宅近くの棚は、どちらもよい選択肢です。", "zkai2026_round02_section1_passage"),
    (1, 2, "contribute", "〈動〉〜を寄付する", "You can contribute novels you have already enjoyed.", "すでに楽しんだ小説を寄付してもよいでしょう。", "zkai2026_round02_section1_passage"),
    (1, 3, "welcoming", "〈形〉（人を）歓迎する", "Paint the little library so it looks welcoming in winter.", "冬でも親しみやすく見えるように小さな図書棚を塗りましょう。", "zkai2026_round02_section1_passage"),
    (1, 4, "install", "〈動〉〜を取り付ける", "Install a light inside so people can browse after sunset.", "日没後に本を選べるよう、中に灯りを取り付けましょう。", "zkai2026_round02_section1_passage"),
    (1, 5, "automatically", "〈副〉自動的に", "Some boxes open automatically when you wave your hand.", "手をかざすと自動的に開く箱もあります。", "zkai2026_round02_section1_passage"),
    (1, 6, "notepad", "〈名〉メモ帳", "Keep a notepad inside for visitors to leave kind messages.", "来場者が短いメモを残せるよう、中にメモ帳を置きましょう。", "zkai2026_round02_section1_passage"),
    # === 第2問 記事（オンライン試験）===
    (2, 0, "flexibility", "〈名〉柔軟性，融通性", "Teachers praised the flexibility of taking exams from home.", "教師たちは在宅受験の柔軟性を高く評価した。", "zkai2026_round02_section2_passage"),
    (2, 1, "institution", "〈名〉機構，組織", "Each institution saves money by printing fewer paper tests.", "各機関は紙の試験を少なく印刷することで経費を抑える。", "zkai2026_round02_section2_passage"),
    (2, 2, "mark", "〈動〉採点する", "Fewer staff members are needed to mark papers by hand.", "手で答案を採点する人数は少なくて済む。", "zkai2026_round02_section2_passage"),
    (2, 3, "grade", "〈動〉採点する；成績を付ける", "Automated systems can grade multiple-choice items faster.", "自動採点は選択式問題の成績付けを速くできる。", "zkai2026_round02_section2_passage"),
    (2, 4, "cheat", "〈動〉カンニングをする", "Cameras aim to reduce the chance that students will cheat.", "カメラは受験者がカンニングする可能性を減らす目的がある。", "zkai2026_round02_section2_passage"),
    (2, 5, "reliable", "〈形〉信頼できる", "Anti-cheat software can make online results more reliable.", "不正防止ソフトはオンラインの結果をより信頼できるものにしうる。", "zkai2026_round02_section2_passage"),
    (2, 6, "certificate", "〈名〉証明書，免許状", "The article never said digital certificates would get cheaper.", "記事は電子証明書の料金が下がるとは述べていない。", "zkai2026_round02_section2_passage"),
    # === 第3問 物語（FILM SCHOOL）===
    (3, 0, "unforgettable", "〈形〉忘れられない", "Alex shouted, \"Let's make something unforgettable!\"", "アレックスは「忘れられないものを作ろう！」と叫んだ。", "zkai2026_round02_section3_passage"),
    (3, 1, "split ~ into ...", "〈表現〉〜を…に分ける", "We were split into groups of four on week one.", "私たちは第1週に4人ずつのグループに分けられた。", "zkai2026_round02_section3_passage"),
    (3, 2, "direct", "〈動〉（映画・劇などの）監督をする", "Alex volunteered to direct our rushed short film.", "アレックスは急ぎの短編を監督すると志願した。", "zkai2026_round02_section3_passage"),
    (3, 3, "operate", "〈動〉〜を操作する", "Helen could operate the camera but not the boom mic.", "ヘレンはカメラは操作できたが、マイクの竿は扱えなかった。", "zkai2026_round02_section3_passage"),
    (3, 4, "editor", "〈名〉編集者", "Colin became the editor and also played the lead role.", "コリンは編集者になり、主演もこなした。", "zkai2026_round02_section3_passage"),
    (3, 5, "script", "〈名〉台本", "Because I love writing, I handled the script.", "書くことが好きなので、私が台本を担当した。", "zkai2026_round02_section3_passage"),
    (3, 6, "proudly", "〈副〉誇らしげに", "I proudly handed Alex my draft the very next morning.", "私は翌朝、誇らしげに原稿をアレックスに渡した。", "zkai2026_round02_section3_passage"),
    (3, 7, "edit", "〈動〉〜を編集する", "Colin found the footage almost impossible to edit smoothly.", "コリンはその映像をスムーズに編集するのはほぼ不可能だと感じた。", "zkai2026_round02_section3_passage"),
    (3, 8, "hysterically", "〈副〉ヒステリックに，ものすごく", "At the screening everyone except the professor laughed hysterically.", "上映会では教授以外が大笑いした。", "zkai2026_round02_section3_passage"),
    (3, 9, "thankfully", "〈副〉ありがたいことに", "Thankfully, every other group's film failed just as badly.", "ありがたいことに、他のグループの作品も同様にひどかった。", "zkai2026_round02_section3_passage"),
    (3, 10, "strangely", "〈副〉不思議なことに", "Strangely, I felt excited even after the embarrassing screening.", "不思議なことに、恥ずかしい上映のあともわくわくした。", "zkai2026_round02_section3_passage"),
    (3, 11, "afterward", "〈副〉その後で", "Afterward I could not wait to study real filmmakers' methods.", "その後、本物の映画作家の手法を学ぶのが待ちきれなかった。", "zkai2026_round02_section3_passage"),
    (3, 12, "filmmaker", "〈名〉映画制作者，映画監督", "I wondered how master filmmakers overcame the same messes.", "大映画作家が同じような混乱をどう乗り越えたのか知りたかった。", "zkai2026_round02_section3_passage"),
    (3, 13, "admire", "〈動〉〜に敬服する", "I admire directors who finish strong stories on tiny budgets.", "わずかな予算で力強い物語を完成させる監督に敬服する。", "zkai2026_round02_section3_passage"),
    (3, 14, "overcome", "〈動〉（困難・問題など）を克服する", "Great artists overcome technical limits with patience.", "偉大な芸術家は忍耐で技術的限界を克服する。", "zkai2026_round02_section3_passage"),
    (3, 15, "eager", "〈形〉熱心な", "The choices call the writer eager after the final class.", "選択肢は、最後の授業のあとの筆者を熱心だと表す。", "zkai2026_round02_section3_passage"),
]

# 第4問 本文
ROWS += [
    (4, 0, "must-see", "〈形〉必見の；ぜひ見るべき", "Kyoto stayed on every tourist's must-see list that spring.", "その春も京都は旅行者の「必見」リストの上位にあった。", "zkai2026_round02_section4_passage"),
    (4, 1, "highlight", "〈動〉〜を浮き彫りにする〔強調する〕", "This essay will highlight both problems and practical fixes.", "このエッセイは問題と現実的な対策の両方を強調する。", "zkai2026_round02_section4_passage"),
    (4, 2, "crowding", "〈名〉混雑", "First the writer names crowding on local buses.", "筆者はまず市内バスでの混雑を挙げる。", "zkai2026_round02_section4_passage"),
    (4, 3, "deal with ~", "〈表現〉〜に対処する", "Officials have discussed how to deal with packed buses.", "当局は混雑したバスへどう対処するか議論してきた。", "zkai2026_round02_section4_passage"),
    (4, 4, "a number of ~", "〈表現〉いくつかの〜", "A number of pricing ideas were debated for foreign riders.", "外国人都賃の案がいくつも議論された。", "zkai2026_round02_section4_passage"),
    (4, 5, "charge", "〈動〉〜（＝料金・値段）を請求する", "Higher fares for visitors charge tourists extra for rush-hour routes.", "観光客に割增高い運賃を請求する案もあった。", "zkai2026_round02_section4_passage"),
    (4, 6, "practical", "〈形〉現実的な；実際的な", "The student prefers practical fixes like double-decker buses.", "生徒は2階建てバスのような現実的な解決策を好む。", "zkai2026_round02_section4_passage"),
    (4, 7, "introduce", "〈動〉〜を導入する", "Kyoto could introduce London-style buses to carry more riders.", "京都はロンドン式バスを導入して輸送力を増やせる。", "zkai2026_round02_section4_passage"),
    (4, 8, "double-decker bus", "〈名〉2階建てバス", "A double-decker could move twice as many sightseers per trip.", "2階建てバスは一回で観光客を倍近く運べる。", "zkai2026_round02_section4_passage"),
    (4, 9, "complain about ~", "〈表現〉〜について不平〔文句〕を言う", "Visitors complain about the lack of street trash cans.", "訪問者は街頭のゴミ箱の少なさに文句を言う。", "zkai2026_round02_section4_passage"),
    (4, 10, "trash can", "〈名〉（大型の）ゴミ箱", "QR codes on each trash can could signal when bins are full.", "各ゴミ箱のQRコードが満杯を知らせられる。", "zkai2026_round02_section4_passage"),
    (4, 11, "dispose of ~", "〈表現〉〜を捨てる〔廃棄する〕", "We need more spots where guests can dispose of wrappers.", "包装紙を捨てられる場所をもっと増やす必要がある。", "zkai2026_round02_section4_passage"),
    (4, 12, "scan", "〈動〉〜をスキャンする", "Tourists scan a code to report bins that need emptying.", "観光客がコードをスキャンして空にする必要を通知する。", "zkai2026_round02_section4_passage"),
    (4, 13, "need doing", "〈表現〉…される必要がある", "If a bin needs emptying, staff receive an alert at once.", "ゴミ箱を空にする必要があるとすぐ職員に知らせが行く。", "zkai2026_round02_section4_passage"),
    (4, 14, "empty", "〈動〉〜を空にする", "Night crews empty the cans before dawn on busy weekends.", "混雑週末は夜勤が明け方前に缶を空にする。", "zkai2026_round02_section4_passage"),
    (4, 15, "outside regular collection hours", "〈副・表現〉通常の収集時間外に", "Alerts matter outside regular collection hours in summer.", "夏は定時収集の時間外に知らせが特に役立つ。", "zkai2026_round02_section4_passage"),
    (4, 16, "take measures", "〈表現〉手段を講じる；対策を取る", "The prefecture takes measures to spread visitors to the coast.", "府は海沿いへ観光客を分散させる対策を講じている。", "zkai2026_round02_section4_passage"),
    (4, 17, "encourage ~ to do", "〈表現〉〜に…するよう促す", "Planners encourage locals to open small farm stays.", "計画者は地元に小さな農家滞在を開くよう促す。", "zkai2026_round02_section4_passage"),
    (4, 18, "scenery", "〈名〉景色；景観", "Travelers enjoy scenery and daily life away from the core ward.", "中心部から離れ景色と暮らしの両方を楽しめる。", "zkai2026_round02_section4_passage"),
    (4, 19, "high-capacity", "〈形〉収容人数の多い", "Let's add high-capacity transportation and cleaner streets.", "収容力の大きい交通と清潔な街路を増やそう。", "zkai2026_round02_section4_passage"),
    (4, 20, "transportation", "〈名〉交通手段", "Better transportation spreads crowds beyond the old city.", "より良い交通は混雑を旧市街の外へ広げる。", "zkai2026_round02_section4_passage"),
]
# 第4問 設問語句
ROWS += [
    (4, 21, "after all", "〈副〉結局のところ", "Choice ① used after all, but it did not fit the gap.", "選択肢①は「結局のところ」を使っていたが、空欄には合わなかった。", "zkai2026_round02_section4_questions"),
    (4, 22, "available", "〈形〉利用できる；（ホテルの部屋などが）空いている", "The passage never said hotel rooms stayed available all season.", "ホテルに空室がずっとあるとは本文は言っていない。", "zkai2026_round02_section4_questions"),
    (4, 23, "act as ~", "〈表現〉〜の役割を務める", "Option ① paired act as with representatives incorrectly.", "選択肢①はact asとrepresentativesを不適切に結びつけた。", "zkai2026_round02_section4_questions"),
    (4, 24, "representative", "〈名〉代表（者）", "The distractor mentioned city representatives, not the essay.", "迷選択肢は街の代表について述べていたが本文とは無関係だ。", "zkai2026_round02_section4_questions"),
    (4, 25, "concentration", "〈名〉（人・物の）集中", "Correct choice spoke of easing concentration downtown.", "正解は市街地への人の集中を緩和することに言及する。", "zkai2026_round02_section4_questions"),
    (4, 26, "city center", "〈名〉街の中心；市街地", "Crowds in the city center sparked the writer's proposals.", "市街地の混雑が筆者の提案を促した。", "zkai2026_round02_section4_questions"),
    (4, 27, "entertain", "〈動〉〜を楽ませる", "Entertain locals was not the campaign's stated goal.", "地元民を楽しませることがキャンペーンの主目的ではなかった。", "zkai2026_round02_section4_questions"),
]
# === 第5問 メール（新入生オリエンテーション案内）===
ROWS += [
    (5, 0, "orientation", "〈名〉オリエンテーション", "The orientation helps freshmen feel ready for September classes.", "オリエンテーションは新入生が9月の授業に備える助けになる。", "zkai2026_round02_section5_vocab"),
    (5, 1, "coordinator", "〈名〉コーディネーター", "Please email the student coordinator if your plans change.", "予定が変わったら学生コーディネーターにメールしてください。", "zkai2026_round02_section5_vocab"),
    (5, 2, "aim to do", "〈表現〉〜することを目指す", "We aim to make the campus tour both fun and informative.", "キャンパスツアーを楽しく、かつ有益なものにしたい。", "zkai2026_round02_section5_vocab"),
    (5, 3, "comfortable", "〈形〉快適な、リラックスした", "Wear shoes that keep you comfortable on long walks.", "長距離を歩いても快適な靴を履いてください。", "zkai2026_round02_section5_vocab"),
    (5, 4, "confirm", "〈動〉〜を確認する", "Could you confirm whether the auditorium is free at noon?", "正午に講堂が空いているか確認していただけますか。", "zkai2026_round02_section5_vocab"),
    (5, 5, "available", "〈形〉利用できる", "Let us know if no projector is available that morning.", "当日プロジェクターが使えない場合は知らせてください。", "zkai2026_round02_section5_vocab"),
    (5, 6, "arrange", "〈動〉〜を配置する、手配する", "We still need to arrange seats for guests near the stage.", "まだ客席を舞台近くに配置する必要がある。", "zkai2026_round02_section5_vocab"),
    (5, 7, "get used to", "〈表現〉〜に慣れる", "Icebreakers help new students get used to speaking up.", "アイスブレイクは新入生が発言に慣れる助けになる。", "zkai2026_round02_section5_vocab"),
    (5, 8, "appreciate", "〈動〉〜に感謝する", "I appreciate your quick reply about the tech center.", "テクノロジーセンターについての早い返信に感謝します。", "zkai2026_round02_section5_vocab"),
    (5, 9, "drop out", "〈表現〉（参加を）やめる、脱落する", "Tell us if a guide must drop out of the walking tour.", "歩きのツアーからガイドが抜けねばならない場合は連絡を。", "zkai2026_round02_section5_vocab"),
    (5, 10, "unavailable", "〈形〉都合がつかない、手が空いていない", "Two volunteers were unavailable on the rehearsal day.", "リハ当日はボランティア2人が都合がつかなかった。", "zkai2026_round02_section5_vocab"),
    (5, 11, "in common", "〈副〉共通して", "The hosts in common share maps and emergency numbers.", "司会者同士は地図と緊急連絡先を共通で持っている。", "zkai2026_round02_section5_vocab"),
    (5, 12, "resource", "〈名〉リソース、資料", "Printable resources will sit on the welcome desk.", "印刷できる資料はウェルカムデスクに置く。", "zkai2026_round02_section5_vocab"),
    (5, 13, "seating arrangement", "〈名〉座席配置", "The seating arrangement keeps chaperones near the exits.", "座席配置は引率が出口近くになるようになっている。", "zkai2026_round02_section5_vocab"),
    (5, 14, "audience", "〈名〉聴衆", "A short skit wakes up the audience before the talk.", "短いスキットが講演の前に聴衆を目覚めさせる。", "zkai2026_round02_section5_vocab"),
    (5, 15, "atmosphere", "〈名〉雰囲気", "Soft music keeps the atmosphere relaxed in the hall.", "ホールでは穏やかな音楽が雰囲気を和らげる。", "zkai2026_round02_section5_vocab"),
]
# === 第6問 物語 A Critic's Journey ===
ROWS += [
    (6, 0, "soapbox", "〈名〉演説台（転じて，自分の意見を主張する場）", "His blog became a soapbox for sharp film reviews.", "彼のブログは鋭い映画評の演説台のようになった。", "zkai2026_round02_section6_passage"),
    (6, 1, "witty", "〈形〉機知に富んだ", "Fans loved her witty jokes about Hollywood clichés.", "ファンはハリウッドのお決まりを茶化す機知に富んだ冗談を愛した。", "zkai2026_round02_section6_passage"),
    (6, 2, "dormitory", "〈名〉寮", "She met her roommate on the first night in the dormitory.", "彼女は寮の初日の夜にルームメイトに会った。", "zkai2026_round02_section6_passage"),
    (6, 3, "inspiration", "〈名〉ひらめき，インスピレーション", "A midnight film gave her the inspiration for a new column.", "深夜の上映が新しい連載のひらめきを与えた。", "zkai2026_round02_section6_passage"),
    (6, 4, "shrug", "〈動〉肩をすくめる", "He shrugged when critics praised his harsh tone.", "批評家が厳しい調子をほめても彼は肩をすくめた。", "zkai2026_round02_section6_passage"),
    (6, 5, "internship", "〈名〉インターンシップ，研修", "The internship taught him how sets really operate.", "インターンシップで現場の実情を学んだ。", "zkai2026_round02_section6_passage"),
    (6, 6, "take off", "〈動〉（事業・キャリアなどが）軌道に乗る", "Her podcast took off after one viral interview.", "バズったインタビュー一つでポッドキャストが軌道に乗った。", "zkai2026_round02_section6_passage"),
    (6, 7, "critique", "〈名〉批評", "Studios feared his critique but still quoted it on posters.", "スタジオは彼の批評を恐れつつポスターに引用した。", "zkai2026_round02_section6_passage"),
    (6, 8, "scold", "〈動〉〜を叱る", "The editor had to scold him for missing deadlines.", "締切を守れない彼を編集者は叱らねばならなかった。", "zkai2026_round02_section6_passage"),
    (6, 9, "insight", "〈名〉洞察，見識", "Readers praised the insight in his final essay on noir.", "読者はノワール論の最終エッセイの洞察を称賛した。", "zkai2026_round02_section6_passage"),
    (6, 10, "consultant", "〈名〉コンサルタント，顧問", "Studios hired him as a consultant, not as lead director.", "スタジオは彼を主演監督ではなく顧問として雇った。", "zkai2026_round02_section6_passage"),
    (6, 11, "perspective", "〈名〉視点，見方", "Travel gave her a fresh perspective on silent movies.", "旅は無声映画を見る新しい視点を与えた。", "zkai2026_round02_section6_passage"),
    (6, 12, "contribution", "〈名〉貢献", "Teachers cited his contribution to classroom film clubs.", "教師たちは映画サークルへの彼の貢献を挙げた。", "zkai2026_round02_section6_passage"),
    (6, 13, "enthusiastic", "〈形〉熱心な，熱意のある", "Despite low pay he remained enthusiastic on set.", "低給でも現場では熱意を失わなかった。", "zkai2026_round02_section6_passage"),
    (6, 14, "dilemma", "〈名〉ジレンマ，板挟み", "The video call exposed the dilemma between art and income.", "ビデオ通話が芸術と収入の板挟みを浮き彫りにした。", "zkai2026_round02_section6_passage"),
    (6, 15, "at one's expense", "〈表現〉〜を犠牲にして；〜をネタにして", "Comedians joked at his expense during the roast.", "特別番組で彼がネタにされる冗談が飛んだ。", "zkai2026_round02_section6_passage"),
    (6, 16, "tear apart", "〈表現〉〜を厳しく批判する；〜をばらばらにする", "Reviewers tear apart sequels that recycle old plots.", "レビュアーは古い筋を再利用する続編を厳しく批判する。", "zkai2026_round02_section6_passage"),
    (6, 17, "confess", "〈動〉〜を打ち明ける，告白する", "He confessed the job left him anxious every Friday.", "金曜ごとに不安になったことを打ち明けた。", "zkai2026_round02_section6_passage"),
    (6, 18, "accomplishment", "〈名〉達成，業績", "Finishing the series was an accomplishment he treasured.", "そのシリーズを完走したことが誇りの業績だった。", "zkai2026_round02_section6_passage"),
    (6, 19, "gratitude", "〈名〉感謝（の気持ち）", "She closed the speech with gratitude toward mentors.", "スピーチは恩師への感謝で締めくくった。", "zkai2026_round02_section6_passage"),
    (6, 20, "constructive", "〈形〉建設的な", "Even harsh notes can be constructive if timed well.", "厳しい指摘もタイミングよければ建設的になりうる。", "zkai2026_round02_section6_passage"),
]
# === 第7問 資料（伝統医学）===
ROWS += [
    (7, 0, "traditional medicine", "〈名〉伝統医学", "Traditional medicine still draws millions of curious patients.", "伝統医学は好奇心の強い患者を今も引きつける。", "zkai2026_round02_section7_passage"),
    (7, 1, "wellness", "〈名〉ウェルネス、健康", "Spas blend wellness marketing with old herbal recipes.", "スパはウェルネス宣伝と古い草薬を混ぜる。", "zkai2026_round02_section7_passage"),
    (7, 2, "evidence-based", "〈形〉証拠に基づいた", "Doctors prefer evidence-based guides for chronic pain.", "医師は慢性的な痛みには根拠のあるガイドを好む。", "zkai2026_round02_section7_passage"),
    (7, 3, "spiritual", "〈形〉精神的な、霊的な", "Some seekers want spiritual comfort as much as relief.", "求める人によっては鎮痛と同じくらい心の支えが欲しい。", "zkai2026_round02_section7_passage"),
    (7, 4, "originate", "〈動〉発祥する、起源を持つ", "Many remedies originate in villages along the trade routes.", "多くの民間療法は交易路沿いの村に起源を持つ。", "zkai2026_round02_section7_passage"),
    (7, 5, "resistance", "〈名〉抵抗（力）", "Germs may grow resistance if herbs are misused.", "薬草の乱用は細菌の耐性を助長しうる。", "zkai2026_round02_section7_passage"),
    (7, 6, "symptom", "〈名〉症状", "Track each symptom before you change any supplement.", "サプリを変える前に症状ひとつひとつを記録しなさい。", "zkai2026_round02_section7_passage"),
    (7, 7, "cognitive function", "〈名〉認知機能", "The trial measured cognitive function after six months.", "試験は6か月後の認知機能を測った。", "zkai2026_round02_section7_passage"),
    (7, 8, "regulate", "〈動〉〜を調節する", "Certain plants help regulate sleep cycles gently.", "ある植物は穏やかに睡眠リズムを調節する助けになる。", "zkai2026_round02_section7_passage"),
    (7, 9, "clinical trial", "〈名〉臨床試験", "A clinical trial compared the herbal mix with placebo.", "臨床試験は漢方をプラセボと比較した。", "zkai2026_round02_section7_passage"),
    (7, 10, "chronic", "〈形〉慢性の", "Chronic fatigue needs longer follow-up than acute flu.", "慢性の疲労は急性の感冒より長い経過観察が要る。", "zkai2026_round02_section7_passage"),
    (7, 11, "methotrexate", "〈名〉メトトレキサート（薬剤名）", "Methotrexate interacts badly with some herbal teas.", "メトトレキサートは一部のハーブティーと悪く相互作用する。", "zkai2026_round02_section7_passage"),
    (7, 12, "commitment", "〈名〉コミットメント、専念", "True healing demands commitment from both healer and patient.", "真の癒しには治療者と患者両方の専念が要る。", "zkai2026_round02_section7_passage"),
    (7, 13, "potential risk", "〈名〉潜在的なリスク", "Labels must list potential risk beside promised benefits.", "表示には利点の隣に潜在リスクも書かねばならない。", "zkai2026_round02_section7_passage"),
    (7, 14, "toxic", "〈形〉有毒な", "Toxic metals showed up in poorly sourced powders.", "出所不明の粉末から有毒金属が出た。", "zkai2026_round02_section7_passage"),
    (7, 15, "screening", "〈名〉スクリーニング、ふるい分け", "Routine screening caught high mercury before kidney harm.", "定期スクリーニングが腎障害の前に水銀の高値をつかんだ。", "zkai2026_round02_section7_passage"),
    (7, 16, "mercury", "〈名〉水銀", "Long use of some creams raised mercury in blood tests.", "あるクリームの長期使用が血液検査で水銀を上げた。", "zkai2026_round02_section7_passage"),
    (7, 17, "consult", "〈動〉〜に相談する", "Always consult your physician before stopping prescriptions.", "処方を止める前は必ず医師に相談しなさい。", "zkai2026_round02_section7_passage"),
    (7, 18, "alternative", "〈名〉代替手段、選択肢", "Yoga became a popular alternative when pills failed.", "薬が効かないときヨガが人気の代替策になった。", "zkai2026_round02_section7_passage"),
]
# === 第8問 レポート（AIと社会）===
ROWS += [
    (8, 0, "viewpoint", "〈名〉見解、視点", "The report contrasts every viewpoint on workplace AI.", "レポートは職場のAIに関するあらゆる見解を対比する。", "zkai2026_round02_section8_passage"),
    (8, 1, "impact", "〈名〉影響", "We must weigh AI's impact on wages and morale.", "賃金と士気へのAIの影響を比較衡量しなければならない。", "zkai2026_round02_section8_passage"),
    (8, 2, "role-playing", "〈名〉ロールプレイング", "Role-playing tasks train staff before live deployment.", "ロールプレイの課題が本番前の訓練になる。", "zkai2026_round02_section8_passage"),
    (8, 3, "recommend", "〈動〉〜を推薦する", "Experts recommend clear rules before wide AI rollout.", "専門家は本格的導入前に明確な規則を推薦する。", "zkai2026_round02_section8_passage"),
    (8, 4, "take over", "〈表現〉〜を乗っ取る、引き継ぐ", "Fear that bots will take over jobs spreads on social media.", "ボットが仕事を奪う恐れがSNSで拡散する。", "zkai2026_round02_section8_passage"),
    (8, 5, "restrict", "〈動〉〜を制限する", "Some unions want laws that restrict automated hiring.", "一部組合は自動採用を制限する法を求めている。", "zkai2026_round02_section8_passage"),
    (8, 6, "grab one's attention", "〈表現〉（人）の注意を引く", "A bold chart grabs the reader's attention on page one.", "一枚目の大胆な図が読者の注意を引く。", "zkai2026_round02_section8_passage"),
    (8, 7, "handy", "〈形〉便利な", "Handy mobile tools still need human judgment.", "便利なモバイルツールも人間の判断を要する。", "zkai2026_round02_section8_passage"),
    (8, 8, "keep track of", "〈表現〉〜を記録する、追跡する", "Apps keep track of energy use in smart homes.", "アプリがスマートホームのエネルギー使用を追跡する。", "zkai2026_round02_section8_passage"),
    (8, 9, "meaningful", "〈形〉意味のある", "Students want meaningful careers alongside faster tech.", "学生は高速な技術と並立する意味のある職を求める。", "zkai2026_round02_section8_passage"),
    (8, 10, "intense debate", "〈名〉激しい議論", "An intense debate surrounded the facial-scan pilot.", "顔認証パイロットをめぐり激しい議論が起きた。", "zkai2026_round02_section8_passage"),
    (8, 11, "advancement", "〈名〉進歩、向上", "Rapid advancement surprises even cautious engineers.", "急速な進歩は用心深い技術者さえ驚かせる。", "zkai2026_round02_section8_passage"),
    (8, 12, "unemployment", "〈名〉失業", "Forecasters link AI to unemployment in retail sectors.", "予測者は小売部門の失業とAIを結びつける。", "zkai2026_round02_section8_passage"),
    (8, 13, "adapt to", "〈表現〉〜に適応する", "Workers must adapt to tools that learn every week.", "労働者は毎週学習するツールに適応しなければならない。", "zkai2026_round02_section8_passage"),
    (8, 14, "pace", "〈名〉ペース、速度", "The pace of upgrades overwhelms small school boards.", "アップデートのペースが小さな教育委員会を圧倒する。", "zkai2026_round02_section8_passage"),
    (8, 15, "dilemma", "〈名〉ジレンマ、板挟み", "Managers face a dilemma between cost cuts and ethics.", "管理者はコスト削減と倫理の板挟みに直面する。", "zkai2026_round02_section8_passage"),
    (8, 16, "enhance", "〈動〉〜を向上させる、高める", "AI can enhance diagnostics when doctors stay in charge.", "医師が最終判断するときAIは診断を高めうる。", "zkai2026_round02_section8_passage"),
    (8, 17, "opportunity", "〈名〉機会", "Start-ups see opportunity in bilingual chatbots.", "スタートアップは二言語チャットボットに機会を見る。", "zkai2026_round02_section8_passage"),
    (8, 18, "argument", "〈名〉主張、議論", "His argument cites surveys from three continents.", "彼の主張は三つの大陸の調査を引用する。", "zkai2026_round02_section8_passage"),
    (8, 19, "virtual assistant", "〈名〉仮想アシスタント", "A virtual assistant schedules meetings across time zones.", "仮想アシスタントがタイムゾーンをまたぐ会議を入れる。", "zkai2026_round02_section8_passage"),
    (8, 20, "voice recognition", "〈名〉音声認識", "Voice recognition still struggles in noisy classrooms.", "音声認識は騒がしい教室ではまだ苦戦する。", "zkai2026_round02_section8_passage"),
    (8, 21, "efficiency", "〈名〉効率", "Efficiency gains must not erase transparency.", "効率の向上が透明性を奪ってはならない。", "zkai2026_round02_section8_passage"),
    (8, 22, "public opinion", "〈名〉世論", "Public opinion shifts slowly after each data breach.", "データ漏洩のたびに世論はゆっくり動く。", "zkai2026_round02_section8_passage"),
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
    n4p = sum(1 for r in ROWS if r[0] == 4 and r[6] == "zkai2026_round02_section4_passage")
    n4q = sum(1 for r in ROWS if r[0] == 4 and r[6] == "zkai2026_round02_section4_questions")
    meta = {
        "exam": "Z会 共通テスト実戦模試 2026年 第2回",
        "source": "data/zkai/2026/round02/data.json（各問 vocabulary 準拠・例文は手作業・scripts/generate_zkai2026_round02_vocab_json.py）",
        "sections_in_data": [1, 2, 3, 4, 5, 6, 7, 8],
        "section1_passage_vocab": {"label": "第1問 語句（町の本棚）", "count": counts.get(1, 0)},
        "section2_passage_vocab": {"label": "第2問 語句（オンライン試験）", "count": counts.get(2, 0)},
        "section3_passage_vocab": {"label": "第3問 語句（FILM SCHOOL）", "count": counts.get(3, 0)},
        "section4_passage_vocab": {"label": "第4問 語句・本文（京都オーバーツーリズム）", "count": n4p},
        "section4_questions_vocab": {"label": "第4問 設問語句", "count": n4q},
        "section5_passage_vocab": {"label": "第5問 語句（オリエンテーション・メール）", "count": counts.get(5, 0)},
        "section6_passage_vocab": {"label": "第6問 語句（A Critic's Journey）", "count": counts.get(6, 0)},
        "section7_passage_vocab": {"label": "第7問 語句（伝統医学）", "count": counts.get(7, 0)},
        "section8_passage_vocab": {"label": "第8問 語句（AIと社会）", "count": counts.get(8, 0)},
    }
    return {"meta": meta, "entries": entries}


def main():
    data = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({len(data['entries'])} entries)")


if __name__ == "__main__":
    main()
