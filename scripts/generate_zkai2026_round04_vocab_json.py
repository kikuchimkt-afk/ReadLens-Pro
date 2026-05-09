# -*- coding: utf-8 -*-
"""Z会実戦模試2026第4回の語彙フラッシュカード用 JSON を生成する（data.json 準拠・例文は手作業）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/zkai/2026/round04/vocabulary_explanations_only_all_sections.json"

# (section_number, flashcard_order, term_en, term_ja, example_en, example_ja, source)
ROWS = [
    # === 第1問 大学サイト・交換留学選考 ===
    (1, 0, "as follows", "〈副〉次のとおり", "The selection schedule is described as follows on this page.", "選考の日程はこのページに次のとおり示されている。", "zkai2026_round04_section1_passage"),
    (1, 1, "applicant", "〈名〉応募者", "Each applicant must attend a short interview in March.", "応募者は全員、3月に短い面接を受けなければならない。", "zkai2026_round04_section1_passage"),
    (1, 2, "interview", "〈名〉面接", "The interview focuses on motivation rather than memorized facts.", "面接は暗記の事実より動機を見る。", "zkai2026_round04_section1_passage"),
    (1, 3, "hand in ~", "〈表現〉〜を提出する", "You must hand in the application form by the due date.", "申込用紙は締切までに提出しなければならない。", "zkai2026_round04_section1_passage"),
    (1, 4, "application", "〈名〉応募書類；申込用紙", "Incomplete applications will not be accepted.", "未記入の応募書類は受理されない。", "zkai2026_round04_section1_passage"),
    (1, 5, "based on ~", "〈前〉〜に基づいて", "Finalists are chosen based on academic performance and essays.", "最終候補は学業成績とエッセイに基づいて選ばれる。", "zkai2026_round04_section1_passage"),
    (1, 6, "academic performance", "〈名〉学業成績", "Your academic performance should appear on the official transcript.", "学業成績は成績証明書に載っているべきだ。", "zkai2026_round04_section1_passage"),
    (1, 7, "run（プログラムを）", "〈動〉〜を実施する", "The office will run an orientation before students fly abroad.", "事務室は留学前にオリエンテーションを実施する。", "zkai2026_round04_section1_passage"),
    # === 第2問 AI と医療のポッドキャスト要約 ===
    (2, 0, "transform", "〈動〉〜を変える", "Experts debated how AI is transforming healthcare delivery.", "専門家たちはAIが医療提供をどう変えるかを論じた。", "zkai2026_round04_section2_passage"),
    (2, 1, "diagnose", "〈動〉診断する", "New tools can diagnose some conditions from routine scans.", "新しい道具が定期検査から一部の病態を診断しうる。", "zkai2026_round04_section2_passage"),
    (2, 2, "vast quantities of", "〈名表現〉莫大な量の", "Algorithms digest vast quantities of imaging data overnight.", "アルゴリズムは一夜に莫大な画像データを処理する。", "zkai2026_round04_section2_passage"),
    (2, 3, "independent", "〈形〉独自の；自立した", "Several independent studies reached similar cautious conclusions.", "いくつかの独立研究が同様に慎重な結論に達した。", "zkai2026_round04_section2_passage"),
    (2, 4, "paperwork", "〈名〉書類仕事", "Doctors hoped AI would reduce repetitive paperwork in clinics.", "医師はAIが診療所の反復的な書類仕事を減らすことを期待した。", "zkai2026_round04_section2_passage"),
    (2, 5, "administration", "〈名〉事務，運営", "Hospital administration must approve any major software rollout.", "病院運営側が大規模ソフト導入を承認しなければならない。", "zkai2026_round04_section2_passage"),
    (2, 6, "biased", "〈形〉偏った", "A biased training set can mislabel rare conditions.", "偏った学習データは稀な病態を誤分類しうる。", "zkai2026_round04_section2_passage"),
    (2, 7, "regulation", "〈名〉規制", "Strict regulation may slow how fast models reach patients.", "厳しい規制はモデルが患者に届く速さを遅らせうる。", "zkai2026_round04_section2_passage"),
    (2, 8, "healthcare", "〈名〉医療；保健", "Public healthcare systems test AI tools under heavy scrutiny.", "公的医疗制度はAIツールを厳しい監視下で試す。", "zkai2026_round04_section2_passage"),
]

# 第3問 科学博物館（本文）
ROWS += [
    (3, 0, "massive", "〈形〉巨大な", "The museum's massive dome welcomed thousands of school groups.", "博物館の巨大なドームが何千もの校外学習団を迎えた。", "zkai2026_round04_section3_passage"),
    (3, 1, "interactive", "〈形〉双方向の，対話的な；参加・体験型の展示", "Interactive maps let visitors replay ancient earthquake waves.", "体験型の地図で訪問者は古代の地震波を追いかけられる。", "zkai2026_round04_section3_passage"),
    (3, 2, "exhibit", "〈名〉展示", "Each exhibit in the climate hall had its own narrator button.", "気候ホールの展示ごとに解説ボタンがあった。", "zkai2026_round04_section3_passage"),
    (3, 3, "hands-on", "〈形〉体験型の，実際に操作できる", "Hands-on labs turned skeptical teens into curious physicists.", "体験型のラボが懐疑的なティーンを好奇心の強い物理徒に変えた。", "zkai2026_round04_section3_passage"),
    (3, 4, "motion", "〈名〉運動", "Sensors tracked the roller coaster car's violent motion.", "センサーがジェットコースター車両の激しい運動を追った。", "zkai2026_round04_section3_passage"),
    (3, 5, "tornado", "〈名〉竜巻", "A swirling tornado model filled the central cylinder.", "渦巻く竜巻模型が中央の筒を満たした。", "zkai2026_round04_section3_passage"),
    (3, 6, "demonstrate", "〈動〉〜を示す，〜を実演する", "Staff demonstrate liquid nitrogen experiments every hour.", "職員が毎時液体窒素の実演をする。", "zkai2026_round04_section3_passage"),
    (3, 7, "manipulate", "〈動〉〜を操作する", "Visitors manipulate levers to change wind speed in the tunnel.", "訪問者はトンネル内の風速を変えるレバーを操作する。", "zkai2026_round04_section3_passage"),
    (3, 8, "gather", "〈動〉集まる", "Crowds gather early for the science magic show.", "科学マジックショーに客は早めに集まる。", "zkai2026_round04_section3_passage"),
    (3, 9, "auditorium", "〈名〉講堂，ホール", "The chemistry show filled every seat in the auditorium.", "化学ショーは講堂の座席をすべて埋めた。", "zkai2026_round04_section3_passage"),
    (3, 10, "impress", "〈動〉〜を感動させる", "The hologram did not impress students who preferred live flames.", "生の炎を好む学生にはホログラムは感動を与えなかった。", "zkai2026_round04_section3_passage"),
    (3, 11, "presenter", "〈名〉実演者", "The presenter joked while pouring smoking foam into a beaker.", "実演者はビーカーに煙の出る泡を注ぎながら冗談を言った。", "zkai2026_round04_section3_passage"),
    (3, 12, "liquid nitrogen", "〈名〉液体窒素", "Liquid nitrogen froze a rose brittle enough to shatter.", "液体窒素はバラを粉々に砕けるほど脆く凍らせた。", "zkai2026_round04_section3_passage"),
    (3, 13, "flash", "〈名〉（光などの）閃光", "A bright flash blinded the camera for half a second.", "強い閃光がカメラを半秒見えなくした。", "zkai2026_round04_section3_passage"),
    (3, 14, "stick in one's mind", "〈表現〉〜の印象に残る", "One statistic about plastic waste stuck in everyone's mind.", "プラスチック廃棄物に関する一つの数字が皆の心に残った。", "zkai2026_round04_section3_passage"),
    (3, 15, "rub", "〈動〉（手など）をこすり合わせる", "She rubbed her gloves before touching the static ball.", "静電気の球に触る前に手袋をこすった。", "zkai2026_round04_section3_passage"),
    (3, 16, "signal", "〈名〉信号", "A red signal warned when the turbine spun too fast.", "タービンが速く回りすぎると赤い信号が警告した。", "zkai2026_round04_section3_passage"),
]
# 第3問 設問
ROWS += [
    (3, 17, "grab one's attention（問1④）", "〈表現〉〜の注意を引く", "The flashy poster fails to grab the reader's attention to safety rules.", "派手なポスターは安全規則へ読者の注意を向けさせにくい。", "zkai2026_round04_section3_questions"),
    (3, 18, "break apart（問2②）", "〈表現〉粉々になる", "Ice bridges may break apart when the temperature swings wildly.", "気温が激しく変わると氷の橋は粉々になりうる。", "zkai2026_round04_section3_questions"),
    (3, 19, "formation（問3④）", "〈名〉構造", "Cloud formation depends on humidity and rising warm air.", "雲の構造は湿度と上昇する暖気に左右される。", "zkai2026_round04_section3_questions"),
]

# 第4問 塾・個別学習のエッセイ（本文）
ROWS += [
    (4, 0, "run", "〈動〉〜を運営する", "She runs a small cram school that focuses on writing.", "彼女は作文に重点を置く小さな塾を運営している。", "zkai2026_round04_section4_passage"),
    (4, 1, "structure", "〈名〉構成；仕組み", "The essay compares the structure of public and private classes.", "そのエッセイは公立と私立のクラスの仕組みを比較する。", "zkai2026_round04_section4_passage"),
    (4, 2, "individual", "〈形・名〉個人の；各自の；個人", "Each student follows an individual study plan online.", "各生徒はオンラインで各自の学習計画に従う。", "zkai2026_round04_section4_passage"),
    (4, 3, "cram school", "〈名〉塾，予備校", "Many teenagers commute to a cram school after club practice.", "多くのティーンは部活のあと塾に通う。", "zkai2026_round04_section4_passage"),
    (4, 4, "for the sole purpose of ~", "〈表現〉もっぱら〜を目的として", "He enrolled for the sole purpose of passing one entrance exam.", "彼は一つの入学試験に受かることだけを目的に入学した。", "zkai2026_round04_section4_passage"),
    (4, 5, "intensive", "〈形〉集中的な；徹底的な", "The intensive course meets every weekend in July.", "集中的なコースは7月の週末ごとに開催される。", "zkai2026_round04_section4_passage"),
    (4, 6, "meet one's needs", "〈表現〉〜のニーズを満たす", "Tutors adapt drills to meet each learner's needs.", "講師は学習者ごとのニーズを満たすようにドリルを変える。", "zkai2026_round04_section4_passage"),
    (4, 7, "benefit", "〈動〉〜の役に立つ；〜に利する", "Peer tutoring can benefit shy students who fear asking teachers.", "同級生のチュータリングは教師に聞くのが怖い内向的な生徒の役に立つ。", "zkai2026_round04_section4_passage"),
    (4, 8, "speak up", "〈表現〉発言する", "Teachers encourage everyone to speak up during debates.", "教師は討論ですべてに発言するよう促す。", "zkai2026_round04_section4_passage"),
    (4, 9, "assignment", "〈名〉課題；宿題", "Weekly assignments mix essays with data interpretation.", "週の課題はエッセイとデータ読解を混ぜる。", "zkai2026_round04_section4_passage"),
    (4, 10, "tailor", "〈動〉〜を（要求・必要などに）合わせて作る", "Apps tailor quizzes to the mistakes you repeat most.", "アプリは繰り返す誤答に合わせて小テストを作る。", "zkai2026_round04_section4_passage"),
    (4, 11, "suit", "〈動〉〜に合う，〜に適合する", "Not every pace suits students who need frequent breaks.", "休憩をしばしば要する生徒にはどのペースも合うとは限らない。", "zkai2026_round04_section4_passage"),
    (4, 12, "depending on ~", "〈表現〉〜次第で；〜に応じて", "Fees change depending on which electives you add.", "選択科目によって料金が変わる。", "zkai2026_round04_section4_passage"),
    (4, 13, "academic", "〈形〉学問の；教育に関する", "Her academic adviser suggested fewer cram nights.", "学業面の指導教員が塾の夜ふかしを減らすよう勧めた。", "zkai2026_round04_section4_passage"),
    (4, 14, "in terms of ~", "〈表現〉〜に関して言えば", "In terms of cost, online tutoring beat driving across town.", "費用の点ではオンライン指導が遠方まで車を出すより得だった。", "zkai2026_round04_section4_passage"),
    (4, 15, "optional", "〈形〉選択制の", "Optional coding camps run every August afternoon.", "任意のプログラミング合宿は毎年8月の午後に開く。", "zkai2026_round04_section4_passage"),
]
ROWS += [
    (4, 16, "have a hard time with ~（問1①）", "〈表現〉〜で苦労する", "Students with dyslexia have a hard time with timed cloze tests.", "失読症の生徒は制限時間の穴埋めに苦労しがちだ。", "zkai2026_round04_section4_questions"),
    (4, 17, "average（問1③）", "〈形〉普通の；平均的な", "The essay targets average teens, not only top scorers.", "そのエッセイは最高点者だけでなく普通のティーンを対象にする。", "zkai2026_round04_section4_questions"),
    (4, 18, "according to ~（問4④）", "〈表現〉〜に応じて；〜にしたがって", "Plans shift according to each prefecture's budget rules.", "計画は都道府県の予算規則に応じて変わる。", "zkai2026_round04_section4_questions"),
]

# 第5問 ティーンの睡眠（本文）
ROWS += [
    (5, 0, "neural connection", "〈名〉神経結合", "Sleep strengthens neural connections that support memory.", "睡眠は記憶を支える神経結合を強める。", "zkai2026_round04_section5_passage"),
    (5, 1, "strengthen", "〈動〉〜を強くする", "Reading before bed may strengthen vocabulary more than cramming.", "就寝前の読書は詰め込みより語彙を強化しうる。", "zkai2026_round04_section5_passage"),
    (5, 2, "transfer", "〈動〉〜を移動させる", "Brains transfer facts from short-term caches while we dream.", "脳は夢を見ている間に事実を短期のキャッシュから移す。", "zkai2026_round04_section5_passage"),
    (5, 3, "short-term memory", "〈名〉短期記憶", "Short-term memory buckles after only five hours of sleep.", "5時間睡眠だけでは短期記憶は不安定になる。", "zkai2026_round04_section5_passage"),
    (5, 4, "long-term memory", "〈名〉長期記憶", "Long-term memory needs repeated nights of adequate rest.", "長期記憶には十分な休息の繰り返し夜が要る。", "zkai2026_round04_section5_passage"),
    (5, 5, "insufficient", "〈形〉不十分な；不足している", "Insufficient sleep blurs emotional regulation all day.", "睡眠が不足すると一日じゅう感情のコントロールがぼやける。", "zkai2026_round04_section5_passage"),
    (5, 6, "consistently", "〈副〉一貫して", "Teens who consistently nap still need deep night sleep.", "昼寝をするティーンも夜の深い眠りは一貫して要る。", "zkai2026_round04_section5_passage"),
    (5, 7, "respectively", "〈副〉それぞれ；各々", "Boys and girls reported 6.2 and 6.5 hours, respectively.", "男子と女子はそれぞれ6.2時間と6.5時間と答えた。", "zkai2026_round04_section5_passage"),
    (5, 8, "improper", "〈形〉間違った；不適切な", "Improper bedtime scrolling steals melatonin hours.", "就寝前の不適切なスマホ眺めがメラトニンの時間を奪う。", "zkai2026_round04_section5_passage"),
    (5, 9, "extracurricular activity", "〈名〉課外活動", "Sports and bands are extracurricular activities that cut sleep.", "運動部と吹奏楽は睡眠を削る課外活動だ。", "zkai2026_round04_section5_passage"),
    (5, 10, "social media", "〈名〉ソーシャルメディア（インターネット上のSNS，ブログなど）", "Social media pings keep brains alert far past midnight.", "SNSの通知が脳を真夜中ずっと覚醒させる。", "zkai2026_round04_section5_passage"),
    (5, 11, "negative consequence", "〈名〉負の結果；よくない結果", "Grumpy mornings are one negative consequence of chronic debt.", "慢性的な寝不足のよくない結果の一つが不機嫌な朝だ。", "zkai2026_round04_section5_passage"),
    (5, 12, "behavioral", "〈形〉行動に関する", "Counselors track behavioral changes linked to fatigue.", "カウンセラーは疲労に結びついた行動の変化を追う。", "zkai2026_round04_section5_passage"),
    (5, 13, "psychological", "〈形〉心の；精神的な", "Psychological stress rises when exams overlap with part-time jobs.", "試験とアルバイトが重なると精神的ストレスが上がる。", "zkai2026_round04_section5_passage"),
    (5, 14, "aggressive", "〈形〉攻撃的な", "Sleep-deprived mice grow more aggressive in mazes.", "寝不足のネズミは迷路でより攻撃的になる。", "zkai2026_round04_section5_passage"),
    (5, 15, "consistent", "〈形〉一貫した；着実な", "Only consistent bedtimes anchor circadian rhythms.", "一貫した就寝時刻だけが概日リズムを固定する。", "zkai2026_round04_section5_passage"),
]
ROWS += [
    (5, 16, "問4 ① biologically", "〈副〉生物学的に", "Choice ① argued the shift was biologically inevitable for teens.", "選択肢①はその変化がティーンには生物学的に避けられないと主張した。", "zkai2026_round04_section5_questions"),
    (5, 17, "問4 ③ insufficiently", "〈副〉不十分に", "Option ③ said schools slept insufficiently rather than lazily.", "選択肢③は学校が怠けているのではなく不十分に眠っていると述べた。", "zkai2026_round04_section5_questions"),
]

# 第6問 Grandmother's Secret Recipes
ROWS += [
    (6, 0, "flour", "〈名〉小麦粉", "Sift the flour twice before you fold in the butter.", "バターを混ぜる前に小麦粉を二度ふるいにかけなさい。", "zkai2026_round04_section6_passage"),
    (6, 1, "stir", "〈動〉〜をかき混ぜる", "Grandmother used chopsticks to stir the broth clockwise.", "おばあちゃんは箸でスープを時計回りにかき混ぜた。", "zkai2026_round04_section6_passage"),
    (6, 2, "filling", "〈名〉（パイなどの）中身・具", "The sweet bean filling leaked through a tiny crack.", "甘いあんの具が小さなひびから漏れた。", "zkai2026_round04_section6_passage"),
    (6, 3, "nervously", "〈副〉神経質に", "He tasted the sauce nervously before anyone else.", "彼は誰より先にソースを神経質に味見した。", "zkai2026_round04_section6_passage"),
    (6, 4, "sibling", "〈名〉きょうだい", "Every sibling received a notebook of different recipes.", "きょうだい一人ひとりが違うレシピのノートを受け取った。", "zkai2026_round04_section6_passage"),
    (6, 5, "frequent", "〈副〉しばしば", "Frequent Sunday dinners kept the cousins close.", "しばしばの日曜の夕食がいとこ同士を近づけた。", "zkai2026_round04_section6_passage"),
    (6, 6, "gathering", "〈名〉集まり", "The annual gathering smelled of garlic and laughter.", "年に一度の集まりにニンニクの香りと笑い声が満ちた。", "zkai2026_round04_section6_passage"),
    (6, 7, "be involved in ~", "〈表現〉〜に打ち込んでいる", "Mom was involved in community meals every winter.", "母は毎冬、地域の食事会に打ち込んでいた。", "zkai2026_round04_section6_passage"),
    (6, 8, "drift apart", "〈表現〉だんだんと疎遠になる", "Cousins drift apart once colleges scatter them overseas.", "いとこは大学で各国に散るとだんだん疎遠になる。", "zkai2026_round04_section6_passage"),
    (6, 9, "pass away", "〈表現〉亡くなる（婉曲）", "After grandmother passed away, the kitchen felt hollow.", "おばあちゃんが亡くなってから台所が虚しく感じた。", "zkai2026_round04_section6_passage"),
    (6, 10, "funeral", "〈名〉葬儀", "At the funeral everyone mentioned her dumplings first.", "葬儀では誰もがまず彼女の餃子の話をした。", "zkai2026_round04_section6_passage"),
    (6, 11, "sort through ~", "〈表現〉〜を仕分けして整理する", "We had to sort through moth-eaten boxes in the attic.", "屋根裏で虫食いの箱を仕分け整理しなければならなかった。", "zkai2026_round04_section6_passage"),
    (6, 12, "flood back", "〈表現〉〔記憶が〕よみがえる", "The cinnamon smell made memories flood back instantly.", "シナモンの匂いで思い出が一瞬によみがえった。", "zkai2026_round04_section6_passage"),
    (6, 13, "stain", "〈名〉しみ", "A soy stain marked the page stained with oil too.", "醤油のしみが油で汚れたページにもついた。", "zkai2026_round04_section6_passage"),
    (6, 14, "reconnect", "〈動〉再びつながる", "Video calls helped cousins reconnect across time zones.", "ビデオ通話がタイムゾーンを越えていとこを再びつないだ。", "zkai2026_round04_section6_passage"),
    (6, 15, "regret", "〈名〉後悔", "Her only regret was not writing measurements down earlier.", "彼女の唯一の後悔は量をもっと早く書き留めていなかったことだ。", "zkai2026_round04_section6_passage"),
    (6, 16, "assure ~ (that ...)", "〈動〉〜に…と保証して安心させる", "She assured us that forgiveness sat in every simmering pot.", "彼女は許しがどの鍋にもあると私たちに安心させた。", "zkai2026_round04_section6_passage"),
    (6, 17, "guilty", "〈形〉罪悪感がある", "He felt guilty hiding the last jar of jam.", "彼は最後のジャムの瓶を隠していて罪悪感があった。", "zkai2026_round04_section6_passage"),
    (6, 18, "tap", "〈動〉（指で）軽く打つ", "She tapped the scale until the needle settled.", "針が止まるまで彼女は秤を指で軽く叩いた。", "zkai2026_round04_section6_passage"),
    (6, 19, "whisper", "〈動〉ささやく", "Aunt May whispered the secret ratio of sugar to salt.", "メイおばさんは砂糖と塩の秘密の比率をささやいた。", "zkai2026_round04_section6_passage"),
    (6, 20, "squeeze", "〈動〉〜を強く握る", "He squeezed her hand when the timer buzzed.", "タイマーが鳴ったとき彼は彼女の手を強く握った。", "zkai2026_round04_section6_passage"),
    (6, 21, "make it a habit to do", "〈表現〉…することを習慣にする", "Make it a habit to taste before you adjust the spices.", "味を整える前に味見することを習慣にしなさい。", "zkai2026_round04_section6_passage"),
]

# 第7問 カーボンオフセット（本文）
ROWS += [
    (7, 0, "indirectly", "〈副〉間接的に", "Flying indirectly funds tree-planting if you buy offsets.", "オフセットを買えば飛行は間接的に植林に金が流れる。", "zkai2026_round04_section7_passage"),
    (7, 1, "carbon dioxide", "〈名〉二酸化炭素", "Mangrove mud traps carbon dioxide better than lawns.", "マングローブの泥は芝生より二酸化炭素を留める。", "zkai2026_round04_section7_passage"),
    (7, 2, "balance out ~", "〈表現〉〜を相殺する〔つり合わせる〕", "Credits balance out emissions from a long-haul flight.", "クレジットが長距離便の排出を相殺する。", "zkai2026_round04_section7_passage"),
    (7, 3, "figure out ~", "〈表現〉〜を計算する", "Apps figure out how many tons your road trip emitted.", "アプリがドライブで何トン出したか計算する。", "zkai2026_round04_section7_passage"),
    (7, 4, "trap", "〈動〉〜を閉じ込める", "Salt marsh roots trap organic muck for centuries.", "塩沼の根が有機的な泥を何世紀も閉じ込める。", "zkai2026_round04_section7_passage"),
    (7, 5, "layer", "〈名〉層", "A thin algae layer signals rising salinity.", "薄い藻の層は塩分上昇を示す。", "zkai2026_round04_section7_passage"),
    (7, 6, "mud", "〈名〉泥", "Boots sank into mud that stored ancient carbon.", "長靴は古い炭素を蓄えた泥に沈んだ。", "zkai2026_round04_section7_passage"),
    (7, 7, "invest in ~", "〈表現〉〜に投資する", "Cities invest in blue carbon after storm surges.", "都市は高潮のあとブルーカーボンに投資する。", "zkai2026_round04_section7_passage"),
    (7, 8, "enhance", "〈動〉〜を強化する", "Restoration projects enhance biodiversity and storage.", "復元事業は生物多様性と蓄積の両方を強化する。", "zkai2026_round04_section7_passage"),
    (7, 9, "depend on ~", "〈表現〉〜に依存する", "Carbon markets depend on verified satellite data.", "カーボン市場は検証済みの衛星データに依存する。", "zkai2026_round04_section7_passage"),
    (7, 10, "concerning", "〈前〉〜に関する", "New rules concerning double counting worry exporters.", "二重計上に関する新規則が輸出業者を不安にする。", "zkai2026_round04_section7_passage"),
    (7, 11, "pretend to do", "〈表現〉…するふりをする", "Polluters cannot pretend to plant trees they never funded.", "汚染者は金を出していない樹を植えたふりはできない。", "zkai2026_round04_section7_passage"),
    (7, 12, "trick O into doing", "〈表現〉Oをだまして…させる", "Scam sites trick users into buying fake certificates.", "詐欺サイトは利用者をだまして偽証明書を買わせる。", "zkai2026_round04_section7_passage"),
    (7, 13, "designate A as B", "〈表現〉AをBとして指定する", "The treaty designates certain wetlands as carbon banks.", "条約は特定の湿地を炭素の貯蔵庫として指定する。", "zkai2026_round04_section7_passage"),
    (7, 14, "cancel out ~", "〈表現〉〜を相殺する", "Renewable power alone cannot cancel out decades of coal.", "再生エネだけでは何十年の石炭を相殺できない。", "zkai2026_round04_section7_passage"),
]
ROWS += [
    (7, 15, "wildlife", "〈名〉野生生物", "Choice ④ links offsets to wildlife rather than urban trees.", "選択肢④はオフセットを街路樹ではなく野生生物に結びつける。", "zkai2026_round04_section7_questions"),
    (7, 16, "cheat", "〈動〉いかさまをする", "Option ③ warned buyers that some brokers cheat on audits.", "選択肢③は仲介者が監査でいかさまをする場合があると警告した。", "zkai2026_round04_section7_questions"),
    (7, 17, "pose", "〈動〉〜をもたらす", "Cheap credits may pose reputational risk for airlines.", "安いクレジットは航空会社に評判のリスクをもたらしうる。", "zkai2026_round04_section7_questions"),
    (7, 18, "ban", "〈動〉〜を禁止する", "A future ban could outlaw imports linked to land grabs.", "将来の禁止令は土地収奪と結びつく輸入を禁じうる。", "zkai2026_round04_section7_questions"),
    (7, 19, "tribe", "〈名〉民族", "The slide mentions a tribe restoring mangroves after storms.", "スライドは嵐のあとマングローブを復元する民族に触れる。", "zkai2026_round04_section7_questions"),
    (7, 20, "turn A to B", "〈表現〉AをBに向ける", "Investors turn profits to community-led nurseries.", "投資家は利益を住民主導の育苗に向ける。", "zkai2026_round04_section7_questions"),
]

# 第8問 不健康食品課税（本文）
ROWS += [
    (8, 0, "evidence", "〈名〉証拠", "Health officials cite evidence that soda taxes cut sales.", "公衆衛生当局はソーダ税が販売を減らす証拠を挙げる。", "zkai2026_round04_section8_passage"),
    (8, 1, "currently", "〈副〉現在", "No prefecture currently taxes sweetened drinks uniformly.", "今のところどの県も加糖飲料を一律課税していない。", "zkai2026_round04_section8_passage"),
    (8, 2, "junk food", "〈名〉ジャンクフード（高カロリー低栄養の食品）", "Junk food ads still target teens on late-night streams.", "ジャンクフードの広告は深夜のストリームでティーンを狙う。", "zkai2026_round04_section8_passage"),
    (8, 3, "bring in ~", "〈表現〉〜を導入する", "Lawmakers may bring in tiered taxes on saturated fat.", "議員は飽和脂肪に段階課税を導入しうる。", "zkai2026_round04_section8_passage"),
    (8, 4, "obesity", "〈名〉肥満", "Childhood obesity rates alarm school nurses nationwide.", "小児肥満の率が全国的に養護教諭を不安にさせる。", "zkai2026_round04_section8_passage"),
    (8, 5, "a wide range of ~", "〈表現〉幅広い〜；さまざまな〜", "Studies cover a wide range of income levels and snacks.", "研究は所得層とスナックの幅広い範囲を扱う。", "zkai2026_round04_section8_passage"),
    (8, 6, "budget", "〈名〉予算", "Low-income households stretch food budgets with bulk rice.", "低所得家庭は米のまとめ買いで食費予算をやりくりする。", "zkai2026_round04_section8_passage"),
    (8, 7, "relatively", "〈副〉比較的", "Sugar becomes relatively cheap when subsidies favor corn.", "補助金がトウモロコシを有利にすると砂糖は比較的安くなる。", "zkai2026_round04_section8_passage"),
    (8, 8, "have an impact on ~", "〈表現〉〜に影響を与える", "Price hikes have an impact on impulse buys at checkouts.", "値上げはレジでの衝動買いに影響を与える。", "zkai2026_round04_section8_passage"),
    (8, 9, "treat", "〈名〉ごほうび", "Kids see candy as a treat after stressful exams.", "子どもはつらい試験のあとキャンディをごほうびに見る。", "zkai2026_round04_section8_passage"),
    (8, 10, "physical activity", "〈名〉身体活動", "More physical activity does not cancel out a sugary breakfast.", "身体活動を増やしても加糖の朝食は帳消しにならない。", "zkai2026_round04_section8_passage"),
    (8, 11, "overweight", "〈形〉太りすぎの", "Overweight teens still need nutrients, not just fewer calories.", "太りすぎのティーンもカロリー削減だけでなく栄養が要る。", "zkai2026_round04_section8_passage"),
    (8, 12, "factor", "〈名〉要因", "Stress is one factor behind midnight convenience runs.", "ストレスは深夜のコンビニ利用の一因だ。", "zkai2026_round04_section8_passage"),
    (8, 13, "device", "〈名〉機器", "Wearable devices nudge wearers toward stair-climbing goals.", "ウェアラブル機器が使用者を階段目標へと促す。", "zkai2026_round04_section8_passage"),
    (8, 14, "manufacturer", "〈名〉製造業者", "Manufacturers reformulate drinks to slip below sugar thresholds.", "製造業者は糖の基準下になるよう飲料を改良する。", "zkai2026_round04_section8_passage"),
    (8, 15, "sugar content", "〈名〉糖含量；糖度", "Labels now highlight sugar content per 100 milliliters.", "表示は100ミリリットルあたりの糖含量を強調する。", "zkai2026_round04_section8_passage"),
    (8, 16, "motivate ~ to do", "〈表現〉〜に…するよう動機付ける", "Subsidies for vegetables could motivate families to cook.", "野菜補助が家族に料理するよう動機付けうる。", "zkai2026_round04_section8_passage"),
    (8, 17, "income", "〈名〉所得", "Higher sugary taxes hit low-income shoppers hardest.", "加糖税の上昇は低所得の買い物客をいちばん打つ。", "zkai2026_round04_section8_passage"),
    (8, 18, "sugary", "〈形〉砂糖の入った", "Sugary cereals crowd the bottom supermarket shelves.", "加糖シリアルがスーパーの下の棚を占める。", "zkai2026_round04_section8_passage"),
]
ROWS += [
    (8, 19, "consume", "〈動〉〜を消費する；摂取する", "The chart shows teens consume more soda than adults do.", "グラフはティーンが大人よりソーダを多く摂取することを示す。", "zkai2026_round04_section8_questions"),
    (8, 20, "alternative", "〈名〉代替品；選択肢", "Question ④ asks for a healthier alternative than chips.", "設問④はポテチより健康的な代替品を求める。", "zkai2026_round04_section8_questions"),
    (8, 21, "profit", "〈名〉利益", "Critics argue companies prioritize profit over reformulation.", "批判者は企業が改良より利益を優先すると言う。", "zkai2026_round04_section8_questions"),
    (8, 22, "focus on ~", "〈表現〉〜に焦点をあてる", "Policymakers should focus on inequality, not only calories.", "政策担当者はカロリーだけでなく不平等に焦点を当てるべきだ。", "zkai2026_round04_section8_questions"),
    (8, 23, "strategy", "〈名〉戦略", "A national strategy needs local stocking rules for fresh food.", "国の戦略には生鮮食品の地域ごとの陳列規則が要る。", "zkai2026_round04_section8_questions"),
    (8, 24, "proportion", "〈名〉割合", "The graph compares the proportion of sugary purchases by income.", "グラフは所得別の加糖購入の割合を比較する。", "zkai2026_round04_section8_questions"),
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
    n3p = sum(1 for r in ROWS if r[0] == 3 and r[6] == "zkai2026_round04_section3_passage")
    n3q = sum(1 for r in ROWS if r[0] == 3 and r[6] == "zkai2026_round04_section3_questions")
    n4p = sum(1 for r in ROWS if r[0] == 4 and r[6] == "zkai2026_round04_section4_passage")
    n4q = sum(1 for r in ROWS if r[0] == 4 and r[6] == "zkai2026_round04_section4_questions")
    n5p = sum(1 for r in ROWS if r[0] == 5 and r[6] == "zkai2026_round04_section5_passage")
    n5q = sum(1 for r in ROWS if r[0] == 5 and r[6] == "zkai2026_round04_section5_questions")
    n7p = sum(1 for r in ROWS if r[0] == 7 and r[6] == "zkai2026_round04_section7_passage")
    n7q = sum(1 for r in ROWS if r[0] == 7 and r[6] == "zkai2026_round04_section7_questions")
    n8p = sum(1 for r in ROWS if r[0] == 8 and r[6] == "zkai2026_round04_section8_passage")
    n8q = sum(1 for r in ROWS if r[0] == 8 and r[6] == "zkai2026_round04_section8_questions")
    meta = {
        "exam": "Z会 共通テスト実戦模試 2026年 第4回",
        "source": "data/zkai/2026/round04/data.json（各問 vocabulary 準拠・例文は手作業・scripts/generate_zkai2026_round04_vocab_json.py）",
        "sections_in_data": [1, 2, 3, 4, 5, 6, 7, 8],
        "section1_passage_vocab": {"label": "第1問 語句（交換留学選考）", "count": counts.get(1, 0)},
        "section2_passage_vocab": {"label": "第2問 語句（AI と医療・ポッドキャスト）", "count": counts.get(2, 0)},
        "section3_passage_vocab": {"label": "第3問 語句・本文（科学博物館）", "count": n3p},
        "section3_questions_vocab": {"label": "第3問 設問語句", "count": n3q},
        "section4_passage_vocab": {"label": "第4問 語句・本文（塾・個別学習）", "count": n4p},
        "section4_questions_vocab": {"label": "第4問 設問語句", "count": n4q},
        "section5_passage_vocab": {"label": "第5問 語句・本文（ティーンの睡眠）", "count": n5p},
        "section5_questions_vocab": {"label": "第5問 設問語句", "count": n5q},
        "section6_passage_vocab": {"label": "第6問 語句（Grandmother's Secret Recipes）", "count": counts.get(6, 0)},
        "section7_passage_vocab": {"label": "第7問 語句・本文（カーボンオフセット）", "count": n7p},
        "section7_questions_vocab": {"label": "第7問 設問語句", "count": n7q},
        "section8_passage_vocab": {"label": "第8問 語句・本文（不健康食品課税）", "count": n8p},
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
