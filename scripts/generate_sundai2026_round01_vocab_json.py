# -*- coding: utf-8 -*-
"""駿台実戦問題集 2026 第1回の語彙フラッシュカード用 JSON を生成する。

data.json の各セクション vocabulary を決められたブロック順でフラット化し、
例文はセクション題材に合わせて人手設計のテンプレ群から決定的に付与する。
（語義・見出しは data.json 準拠）

出力: data/sundai/2026/round01/vocabulary_explanations_only_all_sections.json
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/sundai/2026/round01/data.json"
OUT = ROOT / "data/sundai/2026/round01/vocabulary_explanations_only_all_sections.json"

# 解説冊子の語彙ブロックを読む順（本文→設問の流れ）
VOCAB_BLOCK_ORDER: dict[int, list[str]] = {
    1: ["lead_text", "passage", "questions_and_choices"],
    2: ["lead_text", "passage", "questions_and_choices"],
    3: ["lead_text", "passage", "questions_and_choices"],
    4: ["lead_text", "passage", "comments", "questions_and_choices"],
    5: ["lead_text", "tanaka_email", "ricardo_reply", "questions_and_choices"],
    6: ["lead_text", "p1", "p2", "p4", "p5", "p6", "p7", "p8", "feedback_email", "questions_and_choices"],
    7: ["title", "p1", "p2", "p3", "p4_tail", "p5", "outline_kw", "question_kw"],
    8: ["passage_outline", "question_kw"],
}

SECTION_TOPICS_EN = {
    1: "the garden-centre leaflet on insect-eating plants",
    2: "the UBI magazine article",
    3: "the exchange-student story about saving a family restaurant",
    4: "the draft essay on volunteering",
    5: "the International Society emails about the food fair",
    6: "David's tortoise story and your feedback email",
    7: "the Saharan silver ant article and the presentation outline",
    8: "the electric-car essay steps and supporting sources",
}

SECTION_TOPICS_JA = {
    1: "食虫植物の園芸店パンフレット",
    2: "UBI の雑誌記事",
    3: "家族レストランを救う交換留学生の物語",
    4: "ボランティアの恩恵を論じる草稿",
    5: "国際フードフェアの往復メール",
    6: "陸ガメの物語と感想メール",
    7: "サハラギンアリの記事と発表の概要",
    8: "電気自動車レポートの構成と情報源",
}


def _short_ja(ja: str, limit: int = 42) -> str:
    s = ja.replace("「", "").replace("」", "").strip()
    if not s:
        return "（語義は解説の日本語注意）"
    if len(s) > limit:
        return s[: limit - 1] + "…"
    return s


def _pick_variant(*parts: str, n: int) -> int:
    h = hashlib.md5("|".join(parts).encode("utf-8")).hexdigest()
    return int(h, 16) % n


def infer_term_ja(item: dict[str, Any]) -> str:
    """data.json の ja が空のとき、note や en 内の括弧から補う。"""
    ja = (item.get("ja") or "").strip()
    if ja:
        return ja
    note = (item.get("note") or "").strip()
    en = (item.get("en") or "").strip()
    # 設問語彙で note のみ（分詞句など）
    if note and not ja and "covering" in en.lower():
        return "（the hairs にかかる）現在分詞句：〜の体表を覆う"
    if note and not ja:
        return f"〈解説〉{note}"
    # en 内の ｢…」 「…」 を抽出（解説冊子の OCR 混じり表記）
    for pat in (r"｢([^｣」]+)[」｣]", r"「([^」]+)」"):
        m = re.search(pat, en)
        if m:
            return m.group(1).strip()
    return ""


# 第1問（園芸店・食虫植物パンフレット）: 語句ごとに英文和文を手で用意
SEC1_MANUAL: dict[str, tuple[str, str]] = {
    "shop for ...": (
        "Saturday I will shop for perlite and a wider plastic tray for my pitcher plant.",
        "土曜日に、壺草用にパーライトと口の広いプラスチックのトレイを買いに行く。",
    ),
    "garden centre": (
        "Staff at the garden centre warned that tap water may harm sensitive roots.",
        "園芸店の店員は、水道水は繊細な根を傷めるかもしれないと注意してくれた。",
    ),
    "exotic plant": (
        "The leaflet groups insect-eating species with other exotic plants from warm regions.",
        "パンフレットは食虫種を、温暖な地域の他の外来植物とまとめて紹介している。",
    ),
    "insect-eating plant": (
        "An insect-eating plant still needs moist air even when it catches its own food.",
        "食虫植物でも、自ら餌を取っても空気は湿らせておく必要がある。",
    ),
    "if grown inside": (
        "If grown inside, the sundew may need brighter LED light than the brochure suggests.",
        "屋内で育てる場合、そのモウセンゴケはパンフレットの示すより明るいLEDが必要かもしれない。",
    ),
    "tap water": (
        "Let tap water sit overnight so chlorine escapes before you water the soil.",
        "土に水をやる前に、水道水は一晩置いて塩素を抜いておきなさい。",
    ),
    "tray": (
        "Stand the pot in a shallow tray so extra water drains back upward slowly.",
        "鉢を浅いトレイに載せて、余った水がゆっくり吸い上がるようにする。",
    ),
    "every two weeks": (
        "Feed the tiny leaves every two weeks during the growing season only.",
        "生育期だけ、二週間ごとに小さな葉へ餌を与える。",
    ),
    "shed": (
        "Old leaves shed naturally as long as the crown stays green and firm.",
        "成長点が緑でしっかりしていれば、古い葉は自然に落ちる。",
    ),
    "throw ... away": (
        "Never throw peat moss away; seal it and reuse it for seedlings next spring.",
        "ピートモスは捨てずに封し、来年春の苗に再利用しなさい。",
    ),
    "store": (
        "Store opened bags of soil in a dry closet away from radiators.",
        "開封した培土袋は、暖房の近くを避けた乾いた物置に保管する。",
    ),
    "moist": (
        "Spritz the air until the moss feels lightly moist but not soggy.",
        "苔が軽く湿るが水溜まりにならないまで、空気にミストをかける。",
    ),
    "be aimed at ...": (
        "The tips are aimed at beginners who just bought their first Venus flytrap.",
        "その助言は、初めてハエトリソウを買った初心者向けだ。",
    ),
    "water (動詞)": (
        "Water the compost from below so minerals do not wash onto sticky traps.",
        "ミネラルが粘液のわなを汚さないよう、培養土は下から水を与える。",
    ),
}


# 第2問（UBI 雑誌記事）
SEC2_MANUAL: dict[str, tuple[str, str]] = {
    "essay": (
        "Your teacher expects a five-paragraph essay on whether cash grants work.",
        "現金給付が機能するかどうかについて五段落のレポート（エッセイ）を書くよう求められている。",
    ),
    "universal basic income (UBI)": (
        "Debate on universal basic income returned after the pilot numbers faded.",
        "試行データが色あせたあとも、ユニバーサルベーシックインカムを巡る議論は戻ってきた。",
    ),
    "magazine article": (
        "I clipped the magazine article because every graph was easy to reuse.",
        "どのグラフも転載しやすかったので、雑誌記事を切り抜いた。",
    ),
    "take over ...": (
        "The welfare office will take over card renewals from the private firm.",
        "福祉事務所が民間企業からカード更新の業務を引き継ぐ。",
    ),
    "the money they earn from working": (
        "The money they earn from working barely covers childcare in this city.",
        "この街では労働で得るお金では保育費がかろうじて賄える程度だ。",
    ),
    "economics conference": (
        "At the economics conference, one panel compared Finland and Kenya.",
        "経済会議のパネルではフィンランドとケニアが比較された。",
    ),
    "up to ...": (
        "Some towns tested payments of up to four hundred euros per adult.",
        "一部の町では大人あたり最大400ユーロの給付が試された。",
    ),
    "state that ...": (
        "The OECD may state that cash pilots shrink informal work less than hoped.",
        "OECDは現金パイロットが非正規労働を思ったほど減らさないと述べうる。",
    ),
    "affect": (
        "Fuel taxes could affect grocery prices before wages move at all.",
        "賃金が動く前に燃料税が食料品価格に影響を及ぼしうる。",
    ),
    "not just ...": (
        "The reform helps not just parents but also elderly renters.",
        "その改革は親だけでなく高齢の借り手も助ける。",
    ),
    "involve": (
        "Any national UBI rollout would involve weeks of server testing.",
        "全国規模のUBI導入なら何週間ものサーバー試験を伴う。",
    ),
    "suggest that ...": (
        "Early surveys suggest that stress falls right after the first deposit.",
        "初期の調査は、最初の振り込みの直後にストレスが下がることを示唆する。",
    ),
    "in order to -": (
        "Cities layered ID checks in order to stop duplicate registrations.",
        "都市は重複登録を防ぐため、身分確認を何層も重ねた。",
    ),
    "take responsibility for ...": (
        "Ministers must take responsibility for late transfers to rural banks.",
        "大臣たちは地方銀行への遅れた振り込みの責任を負わねばならない。",
    ),
    "in contrast": (
        "In contrast, wage subsidies only reach workers already on payrolls.",
        "対照的に、賃金補助はすでに給与名簿にある労働者にしか届かない。",
    ),
    "make sure that ...": (
        "Auditors want offices to make sure that every audit log stays sealed.",
        "監査人は事務所に各監査ログを密封したまま保てと求める。",
    ),
    "given out ...": (
        "Cash was given out at civic halls on the first Monday each month.",
        "現金は毎月最初の月曜に市民ホールで配られた。",
    ),
    "fairly": (
        "Lottery slots were assigned fairly across each income band.",
        "抽選枠は各所得層に公平に割り当てられた。",
    ),
    "mention that ...": (
        "The editorial forgot to mention that petrol prices could erase gains.",
        "社説はガソリン価格が恩恵を消しうることに触れるのを忘れた。",
    ),
    "against": (
        "Forty senators voted against freezing student aid.",
        "40人の上院議員が学生援助の停止に反対票を投じた。",
    ),
    "trust O to -": (
        "Voters trust the agency to publish raw anonymised spending files.",
        "有権者はその機関が匿名化された生の支出ファイルを公表すると信じている。",
    ),
    "agree on ...": (
        "Parties still cannot agree on whether tests should stay income-based.",
        "政党は資産調査の要否についてもなお一致していない。",
    ),
    "field": (
        "She publishes in the field of public finance, not welfare anthropology.",
        "彼女は福祉人類学ではなく財政学の分野で発表している。",
    ),
    "wealthy": (
        "One wealthy backer matched every small donation during the pilot.",
        "ある富裕な支援者が試行期間中に小口寄付を一枚ごと釣り上げた。",
    ),
    "most likely": (
        "Young renters are most likely to drop out if payments arrive late.",
        "家賃支払い層の若者は、給付が遅れれば最も参加をやめやすい。",
    ),
    "lack": (
        "The lack of childcare keeps parents from night shifts they need.",
        "保育の欠如が、必要な夜勤を親たちから遠ざけている。",
    ),
    "trust in ...": (
        "Public trust in the trial jumped after the mayor apologised on TV.",
        "市長がテレビで謝罪したあと、試行への国民の信頼は跳ね上がった。",
    ),
    "have a ... effect on ~": (
        "Rent freezes can have a mixed effect on new construction starts.",
        "家賃凍結は新規着工に複合的な影響を及ぼしうる。",
    ),
    "insignificant": (
        "The bump was statistically insignificant once seasonality was removed.",
        "季節性を除けば、その上振れは統計的に意味がなかった。",
    ),
    "help O +原形": (
        "Child credits might help parents afford healthier groceries.",
        "児童クレジットが親により健康的な買い物を可能にするかもしれない。",
    ),
    "develop": (
        "Cities develop simple apps so riders can watch deposits land.",
        "都市は振込が入るのを追える簡単なアプリを開発する。",
    ),
    "take away ...": (
        "Critics fear new taxes could take away the incentive to report income.",
        "批判者は新税が申告意欲を奪うと危惧する。",
    ),
    "the benefits UBI brings to companies": (
        "The sidebar lists the benefits UBI brings to companies during recessions.",
        "欄外は不況時の企業へのUBIの恩恵を列挙している。",
    ),
    "the disadvantages UBI will bring to ordinary citizens": (
        "Discuss the disadvantages UBI will bring to ordinary citizens before cheering.",
        "手を叩く前に、UBIが一般市民にもたらす不利益を論じなさい。",
    ),
    "the influence of A on B": (
        "Figure 2 charts the influence of migration on tax receipts.",
        "図2は移動が税収に与える影響を図示している。",
    ),
    "the tax AI companies pay": (
        "Analysts compared the tax AI companies pay in Dublin and Seoul.",
        "分析者はダブリンとソウルのAI企業の税金を比較した。",
    ),
}


# 第3問（交換留学生・レストランの物語）
SEC3_MANUAL: dict[str, tuple[str, str]] = {
    "exchange student": (
        "As an exchange student, I needed a story that fits our unit on service work.",
        "交換留学生として、サービス業の単元に合う物語が必要だった。",
    ),
    "ask O to -": (
        "The teacher asked us to underline every verb about saving the café.",
        "先生はカフェを救う動詞をすべて下線するよう求めた。",
    ),
    "to talk about": (
        "We wanted a story to talk about in class without boring anyone.",
        "誰も退屈させずに授業で話せる物語が欲しかった。",
    ),
    "owned by my best friend Leo's family": (
        "The tiny trattoria, owned by my best friend Leo's family, smelled of garlic.",
        "親友レオの家族が所有する小さなトラットリアにはニンニクの香りがした。",
    ),
    "help O to -": (
        "Weekend volunteers helped Leo to repaint the faded signboard.",
        "週末のボランティアが看板の色褪せを直すのをレオを手伝った。",
    ),
    "serve": (
        "Waiters serve regulars slowly so every plate leaves the hot kitchen perfect.",
        "ウェイターは常連にはゆっくり料理を運び、熱い厨房から完璧な皿を出し続ける。",
    ),
    "customer": (
        "One loyal customer brought twenty classmates after the viral clip.",
        "一人の常連がバズった動画のあとクラスメイト二十人を連れてきた。",
    ),
    "business": (
        "Seasonal business picked up once the patio lights went on.",
        "パティオの灯りが点くと季節の売上が持ち直した。",
    ),
    "go well": (
        "If tonight's dinner rush does not go well, they may close early.",
        "今夜のディナー忙しさがうまくいかなければ早じまいする。",
    ),
    "be scared that ...": (
        "Leo was scared that the bank would call the loan by Friday.",
        "レオは金曜までに銀行が融資を取り上げるのではと心配していた。",
    ),
    "close down": (
        "Fancy chains rarely close down quietly on this avenue.",
        "この大通りでは高級チェーンでさえ静かに閉店することは稀だ。",
    ),
    "quit": (
        "He refused to quit even when two cousins left for corporates.",
        "いとこが二人会社へ戻っても彼はやめることを拒んだ。",
    ),
    "We can't let it close down": (
        "We shouted, \"We can't let it close down,\" and booked four extra shifts.",
        "「店を閉めるわけにはいかない」と叫び、シフトを四つ増やした。",
    ),
    "empty": (
        "By nine the dining room looked empty except for cousins texting.",
        "9時にはいとこたちがメールする以外客がいないほど空いていた。",
    ),
    "Why don't we ...?": (
        "Why don't we host a pop-up brunch on Sunday?",
        "日曜に期間限定のブランチをやってみない？",
    ),
    "try -ing": (
        "Let's try live-streaming the kitchen for one weekend.",
        "一週末だけ厨房をライブ配信してみよう。",
    ),
    "get O -ing": (
        "Funny hashtags got students lining up before five p.m.",
        "面白いハッシュタグで学生が午後五時前に列をなした。",
    ),
    "limited-time": (
        "Their limited-time tiramisu drew cameras from three blogs.",
        "期間限定のティラミスは三つのブログからカメラを引き付けた。",
    ),
    "posting ...": (
        "Posting clips every hour, she forgot to sleep before exam week.",
        "試験週の前に毎時動画を投稿してしまい、眠るのを忘れた。",
    ),
    "post": (
        "Only interns may post live stories with the owner's badge.",
        "オーナーのバッジ付きでライブストーリーを投稿できるのは実習生だけだ。",
    ),
    "invite O to -": (
        "They invited food critics to judge the midnight gnocchi throwdown.",
        "批評家たちを真夜中のニョッキ対決の審査に招いた。",
    ),
    "in exchange for ...": (
        "He washed pans in exchange for pizza and goodwill stories.",
        "ピザと胸温まる話と引き換えに鍋を洗った。",
    ),
    "review": (
        "A harsh review still doubled reservations for Saturday.",
        "厳しいレビューでも土曜の予約は倍になった。",
    ),
    "one month after ...": (
        "One month after the pop-up, profits almost matched rent.",
        "ポップアップの一か月後には利益がほぼ家賃に追いついた。",
    ),
    "not ... anymore": (
        "She does not cry about tips anymore; she tracks each coin online.",
        "もうチップに泣きつかない；小銭までオンラインで追う。",
    ),
    "offer to -": (
        "Regulars offered to roll dough when the mixer broke.",
        "常連がミキサー故障時に生地をこねると申し出た。",
    ),
    "decline": (
        "The reviewer watched the lunch crowd decline after the holiday.",
        "批評家は休暇後に昼の客が減ったのを目にした。",
    ),
    "confused": (
        "I felt confused when the timeline skipped a whole summer.",
        "物語が一夏を飛ばしたので混乱した。",
    ),
    "disappointed": (
        "Customers were disappointed that tiramisu sold out again.",
        "ティラミスがまた売り切れたことに客はがっかりした。",
    ),
    "guilty": (
        "He felt guilty skipping rehearsal to knead dough.",
        "練習を抜けて生地をこねに行ったことに罪悪感があった。",
    ),
    "relieved": (
        "She was relieved when the loan officer smiled at the folder.",
        "担当者がファイルを見て微笑むと彼女はほっとした。",
    ),
}


def _display_term_for_sentence(te: str) -> str:
    """極端に長い見出しは短くして例文に埋め込む。"""
    if len(te) <= 62:
        return te.replace('"', "'")
    return te[:30].rstrip() + " …"


def craft_examples(section: int, block: str, flash_order: int, term_en: str, term_ja: str) -> tuple[str, str]:
    """第1〜3問は語句ごとに手書き例。第4問以降は題材に沿ったテンプレから決定的に生成。"""
    if section == 1 and term_en in SEC1_MANUAL:
        return SEC1_MANUAL[term_en]
    if section == 2 and term_en in SEC2_MANUAL:
        return SEC2_MANUAL[term_en]
    if section == 3 and term_en in SEC3_MANUAL:
        return SEC3_MANUAL[term_en]

    te_raw = term_en.replace('"', "'")
    tj = term_ja.strip() or _short_ja(infer_term_ja({"ja": "", "en": term_en}))
    ja_short = _short_ja(tj)
    te = _display_term_for_sentence(te_raw)

    topic_en = SECTION_TOPICS_EN[section]
    topic_ja = SECTION_TOPICS_JA[section]

    # 第2問以降: 読みの練習のため、語・連語を短い英文に埋め込む（解説調の語は使わない）
    templates: list[tuple[str, str]] = [
        (
            'Skimming {topic}, underline "{term}" where it matches 「{ja}」.',
            "{topic_ja}を速読するとき、「{term}」を見つけたら意味が「{ja_short}」になる印をつける。",
        ),
        (
            'One sentence in {topic} hinges on "{term}" understood as 「{ja}」.',
            "{topic_ja}の一文は、「{term}」を「{ja_short}」と読めたかがカギになる。",
        ),
        (
            'Rewrite the line with "{term}" into Japanese using 「{ja}」.',
            "「{term}」の行を日本語に直すときは「{ja_short}」の語感で置き換える。",
        ),
        (
            'The phrase "{term}" should ring as 「{ja}」, not a false friend.',
            "「{term}」は偽友ではなく、「{ja_short}」と聞こえるか確認する。",
        ),
        (
            'Ask yourself whether "{term}" here points to 「{ja}」.',
            "ここで「{term}」が指すのが「{ja_short}」か、自分に問い直す。",
        ),
        (
            'Colour-code "{term}" in the margin and jot 「{ja}」.',
            "余白で「{term}」に色をつけ、その横に「{ja_short}」と書く。",
        ),
        (
            'Slow reading fixes "{term}" as 「{ja}」 before you tackle the questions.',
            "設問に進む前に、ゆっくり読んで「{term}」を「{ja_short}」に固定する。",
        ),
        (
            'Notice how "{term}" ties to the idea of 「{ja}」 in this context.',
            "この文脈で「{term}」が「{ja_short}」という発想につながる点に気づく。",
        ),
        (
            'Without 「{ja}」, the clause containing "{term}" collapses.',
            "「{ja_short}」が取れると、「{term}」を含む節が意味を失う。",
        ),
        (
            'Your annotation for "{term}" can be a single gloss: 「{ja}」.',
            "「{term}」へのメモは、ひと言「{ja_short}」で十分なことが多い。",
        ),
        (
            'Compare two drafts: only the sentence with "{term}" should say 「{ja}」.',
            "二つの草稿を比べ、「{term}」の文だけが「{ja_short}」と言いたい内容か確かめる。",
        ),
        (
            'Translate silently: "{term}" → 「{ja}」, then read on.',
            "心の中で「{term}」→「{ja_short}」と置いてから先を読む。",
        ),
        (
            'Peer discussion often starts with "{term}" and its gloss 「{ja}」.',
            "仲間と読むときは、まず「{term}」とその訳「{ja_short}」から話し合う。",
        ),
        (
            'If "{term}" feels vague, lock it to 「{ja}」 and reread the paragraph.',
            "「{term}」が曖昧なら「{ja_short}」に決め打ちして段落を読み返す。",
        ),
        (
            'Exam practice: use "{term}" in a fresh English sentence, meaning 「{ja}」.',
            "試験対策として、「{term}」を「{ja_short}」の意味で新しい英文を作る。",
        ),
        (
            'The distractor fails because it misreads "{term}" as something other than 「{ja}」.',
            "誤答肢は、「{term}」を「{ja_short}」以外に解釈したときだけ選ばれる。",
        ),
        (
            'A one-word note beside "{term}"—「{ja}」—saves review time.',
            "「{term}」の横に「{ja_short}」と一語だけ書いておくと復習が速い。",
        ),
        (
            'Read aloud: "{term}" should match the tone of 「{ja}」 in your mind.',
            "声に出すと、「{term}」が心の中の「{ja_short}」と調子が合うかわかる。",
        ),
        (
            'Parallel structure hinges on "{term}" carrying 「{ja}」 in both clauses.',
            "平行構造では、「{term}」が両方の節で同じ「{ja_short}」を担うかに注目する。",
        ),
        (
            'Swap synonyms only after you are sure "{term}" is not 「{ja}」 in disguise.',
            "類語に置き換えるのは、「{term}」が「{ja_short}」の仮面をかぶった語ではないと確信してからだ。",
        ),
        (
            'Timed review: glance at "{term}" and recall 「{ja}」 in five seconds.',
            "タイムドリチェックでは、「{term}」を見て5秒で「{ja_short}」を思い出す。",
        ),
        (
            'The heading and "{term}" together signal the gloss 「{ja}」.',
            "見出しと「{term}」が重なるところで、意味は「{ja_short}」と決まることが多い。",
        ),
        (
            'Before marking the answer sheet, refix "{term}" as 「{ja}」 in the stem.',
            "マーク前に、問題文の「{term}」を心の中で「{ja_short}」に置き直す。",
        ),
        (
            'Listening to a classmate, check whether they keep "{term}" on 「{ja}」.',
            "友達の説明を聞いて、「{term}」を「{ja_short}」からズラしていないか確かめる。",
        ),
        (
            'Mental paraphrase: replace "{term}" with a Japanese chunk containing 「{ja}」.',
            "言い換え練習では、「{term}」を「{ja_short}」を含む日本語の塊に置き換える。",
        ),
        (
            'The safest reading keeps "{term}" anchored to 「{ja}」 through the whole line.',
            "一行の終わりまで「{term}」を「{ja_short}」に固定して読むのがもっとも安全だ。",
        ),
    ]

    if len(te_raw) > 58 or te_raw.count(" ") > 12:
        long_intro: list[tuple[str, str]] = [
            (
                'Split the long expression "{term}" and assign 「{ja}」 to each piece.',
                "長い「{term}」を区切り、各部分に「{ja_short}」に相当する訳を当てはめる。",
            ),
            (
                'The clause beginning with "{term}" should still boil down to 「{ja}」.',
                "「{term}」で始まる節も、要する所は「{ja_short}」という整理でよい。",
            ),
        ]
        templates = long_intro + templates

    i = _pick_variant(str(section), block, str(flash_order), te_raw, "natural", n=len(templates))
    en_t, ja_t = templates[i]
    ex_en = en_t.format(topic=topic_en, topic_ja=topic_ja, term=te, ja=tj, ja_short=ja_short)
    ex_ja = ja_t.format(topic_ja=topic_ja, term=te, ja=tj, ja_short=ja_short)
    return ex_en, ex_ja


def build_entries(data: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    counts_by_section: dict[int, int] = {}
    counts_by_block: dict[str, int] = {}

    for sec in data["sections"]:
        sn = sec["section_number"]
        vocab = sec.get("vocabulary") or {}
        order = 0
        for block_key in VOCAB_BLOCK_ORDER[sn]:
            blk = vocab.get(block_key)
            if not blk:
                raise KeyError(f"section {sn} missing vocabulary.{block_key}")
            items = blk.get("items") or []
            src = f"sundai2026_round01_section{sn}_{block_key}"
            counts_by_block[src] = len(items)
            for it in items:
                term_en = (it.get("en") or "").strip()
                if not term_en:
                    continue
                term_ja = infer_term_ja(it)
                ex_en, ex_ja = craft_examples(sn, block_key, order, term_en, term_ja)
                entry: dict[str, Any] = {
                    "term_en": term_en,
                    "term_ja": term_ja or "（訳は解説冊子の語彙表を参照）",
                    "example_en": ex_en,
                    "example_ja": ex_ja,
                    "flashcard_order": order,
                    "occurrences": [
                        {
                            "section_number": sn,
                            "question_id": "vocabulary",
                            "answer_number": None,
                            "source": src,
                        }
                    ],
                }
                note = (it.get("note") or "").strip()
                if note:
                    entry["vocabulary_note"] = note
                entries.append(entry)
                order += 1
                counts_by_section[sn] = counts_by_section.get(sn, 0) + 1

    # flashcard_order をセクション内 0..n-1 にそろえ直す（上で付与済み）
    meta = {
        "exam": "駿台 共通テスト実戦問題集 2026年 第1回",
        "source": "data/sundai/2026/round01/data.json（各問 vocabulary 準拠・第1〜3問の例文は語句ごとに手書き、第4〜8問はテンプレから生成・scripts/generate_sundai2026_round01_vocab_json.py）",
        "sections_in_data": list(range(1, 9)),
        "counts_by_section": {f"section{k}": counts_by_section[k] for k in sorted(counts_by_section)},
        "counts_by_source_prefix": counts_by_block,
    }
    for k in range(1, 9):
        meta[f"section{k}_label"] = next(
            (s.get("description") or s.get("title") for s in data["sections"] if s["section_number"] == k),
            "",
        )
    return entries, meta


def main() -> None:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    entries, meta = build_entries(payload)
    out_obj = {"meta": meta, "entries": entries}
    OUT.write_text(json.dumps(out_obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(entries)} entries -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
