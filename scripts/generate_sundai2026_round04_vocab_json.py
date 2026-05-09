# -*- coding: utf-8 -*-
"""駿台実戦問題集 2026 第4回の語彙フラッシュカード用 JSON を生成する。

data.json の vocabulary をブロック順でフラット化する。
第1〜3問の例文は語句ごとに手書き、第4〜8問は題材に沿ったテンプレから決定的に生成。

出力: data/sundai/2026/round04/vocabulary_explanations_only_all_sections.json
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/sundai/2026/round04/data.json"
OUT = ROOT / "data/sundai/2026/round04/vocabulary_explanations_only_all_sections.json"

VOCAB_BLOCK_ORDER: dict[int, list[str]] = {
    1: ["passage", "stem_choices"],
    2: ["passage", "review"],
    3: ["passage", "stem_choices"],
    4: ["lead_text", "passage", "comments", "questions_and_choices"],
    5: ["passage", "survey"],
    6: ["lead", "passage"],
    7: ["p1", "p2", "p3", "p4", "p5"],
    8: ["lead", "step1", "step2", "step3"],
}

SECTION_TOPICS_EN = {
    1: "the fitness club website and pricing plans",
    2: "the Miyakojima hotel brochure and guest review",
    3: "the Gap in Communication article for study-abroad readers",
    4: "the essay draft on eye health with teacher comments",
    5: "the study-abroad group-discussion article, survey, and handout",
    6: "the twins article and notes on oral English presentations",
    7: "the light pollution report for environmental class",
    8: "the club-morning-practice survey for your teamwork essay",
}

SECTION_TOPICS_JA = {
    1: "フィットネスクラブのウェブサイトと料金プラン",
    2: "宮古島のホテル案内と宿泊客レビュー",
    3: "留学志望者向け『コミュニケーションの隔たり』の記事",
    4: "目の健康と教師コメントのあるエッセイ草稿",
    5: "留学・グループディスカッションの記事・アンケート・資料",
    6: "双子の記事と英語口頭発表のメモ",
    7: "光害（Light Pollution）の環境記事",
    8: "部活朝練をテーマにした意見収集とエッセイ構成",
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
    ja = (item.get("ja") or "").strip()
    if ja:
        return ja
    note = (item.get("note") or "").strip()
    if note and not ja:
        return f"〈解説〉{note}"
    en = (item.get("en") or "").strip()
    for pat in (r"｢([^｣」]+)[」｣]", r"「([^」]+)」"):
        m = re.search(pat, en)
        if m:
            return m.group(1).strip()
    return ""


# ----- 第1問 フィットネスクラブ・ウェブサイト -----
SEC1_MANUAL: dict[str, tuple[str, str]] = {
    "simple goal": (
        "The Daytime plan promotes one simple goal: move with friends weekly.",
        "デイタイムプランは友達と週に一度動くという単純な目標を打ち出している。",
    ),
    "specifically designed": (
        "The lap pool is specifically designed for interval swimmers.",
        "周遊プールはインターバル泳者向けに特化して設計されている。",
    ),
    "flexible": (
        "Flexible morning slots suit parents who drive teens to school.",
        "柔軟な朝の枠は送迎のある保護者に合う。",
    ),
    "rate": (
        "Compare the student rate before the April deadline.",
        "四月の締切前に学生料金を比較しなさい。",
    ),
    "equipment": (
        "Technicians calibrate cardio equipment every Monday dawn.",
        "有酸素マシンは毎週月曜明け方に校正される。",
    ),
    "specifically": (
        "This month trainers speak specifically about shoulder mobility.",
        "今月の講習は肩の可動域だけに特化して話す。",
    ),
    "motivate O to −": (
        "Bright class playlists motivate members to stay for the cool-down.",
        "明るい授業用プレイリストがクールダウンまで残る気にさせる。",
    ),
    "elevate": (
        "Partner drills can elevate your heart rate in five minutes.",
        "ペアドリルなら五分で心拍を高められる。",
    ),
    "enroll": (
        "You may enroll online, then show ID at your first visit.",
        "ネットで登録して初回に身分証を見せなさい。",
    ),
    "affordable": (
        "The family bundle stays affordable even with pool access.",
        "プール付きでも家族割は手ごろなままだ。",
    ),
    "brand new": (
        "Brand new treadmills face the garden windows.",
        "最新のルームランナーが庭窓向きに並ぶ。",
    ),
    "welcoming": (
        "Volunteer greeters keep the lobby welcoming at six a.m.",
        "朝六時にもボランティアがロビーを快く保つ。",
    ),
    "can't help but −": (
        "After the trial spin class you can't help but join the group chat.",
        "体験スピン後はグループチャットに入らずにはいられない。",
    ),
    "workout": (
        "Log every workout so coaches adjust next week's sheet.",
        "すべてのトレーニングを記録し、コーチが翌週の表を調整できるようにしなさい。",
    ),
    "lottery": (
        "Summer kids' camp seats open through an online lottery.",
        "子どもサマーキャンプはオンライン抽選で枠が決まる。",
    ),
    "in addition": (
        "In addition, seniors swim free on Wednesday mornings.",
        "その上、水曜午前はシニアが無料で泳げる。",
    ),
    "original": (
        "Members taste-test an original recovery drink each quarter.",
        "四半期ごとにオリジナルのリカバリー飲料を試飲する。",
    ),
    "opportunity": (
        "This relay event is your opportunity to meet marathon coaches.",
        "このリレー大会はマラソンコーチに会う好機だ。",
    ),
    "plus": (
        "The spa day pass is ninety dollars, plus city tax.",
        "スパデイパスは九十ドルに市税が上乗せだ。",
    ),
    "facility": (
        "The ski simulator is not covered under the family facility pass.",
        "スキーシミュレーターは家族の施設パス対象外だ。",
    ),
    "charge": (
        "Front desk staff charge five dollars for towel rentals.",
        "タオルレンタルは受付が五ドル請求する。",
    ),
    "promotion": (
        "May's promotion pairs PT sessions with massage credits.",
        "五月のキャンペーンは個人トレとマッサージ券を組み合わせる。",
    ),
    "bathing suit": (
        "Bring a spare bathing suit because dryers stay busy.",
        "乾燥機は混むので予備の水着を持参しなさい。",
    ),
    "enrollment": (
        "Late enrollment still qualifies for the spring fee freeze.",
        "遅い入会でも春の据え置き料金の対象になる。",
    ),
    "practical": (
        "Trainers showed practical stretches beside the weight tree.",
        "コーチがダンベル棚脇で実用的なストレッチを見せた。",
    ),
    "for free": (
        "Guests may sample reformer Pilates for free on Sundays.",
        "日曜はゲストがリフォーマー・ピラティスを無料で試せる。",
    ),
    "footwear": (
        "Studio B demands clean indoor footwear every season.",
        "スタジオBはどの季節も清潔な室内履き必須だ。",
    ),
    "one-on-one": (
        "Lottery winners book one-on-one bike fits first.",
        "抽選当選者からマンツーマンのバイク調整を先に取る。",
    ),
}

# ----- 第2問 宮古島ホテル案内＋レビュー -----
SEC2_MANUAL: dict[str, tuple[str, str]] = {
    "notable [形]": (
        "Notable coral gardens sit a short shuttle ride away.",
        "サンゴの名所がシャトルですぐの距離にある。",
    ),
    "attraction [名]": (
        "Night kayaking became the resort's headline attraction.",
        "ナイトカヤックがリゾートの目玉コースになった。",
    ),
    "plenty of ...": (
        "There are plenty of late-night ramen spots along the coastal road.",
        "海岸道路沿いに深夜ラーメンがたくさんある。",
    ),
    "return to -": (
        "Guests return to stretch on the sunset deck every evening.",
        "宿泊客は毎夕、夕陽デッキでストレッチに戻ってくる。",
    ),
    "soundproofed [形]": (
        "Soundproofed family rooms face the tennis garden.",
        "防音のファミリールームはテニス庭園向きだ。",
    ),
    "entertainment [名]": (
        "Evening entertainment includes island folk dancers.",
        "夜の催しには島の民俗舞踊も含まれる。",
    ),
    "satellite channel": (
        "Each room lists satellite channels on laminated cards.",
        "各部屋に衛星チャンネル一覧のラミネートカードがある。",
    ),
    "fridge [名]": (
        "Stock the minibar fridge with allergy-safe snacks only.",
        "ミニバーの冷蔵庫にはアレルギー対応の軽食だけを入れなさい。",
    ),
    "laundry [名]": (
        "The laundry on three accepts cashless laundry packs.",
        "三階のランドリーはキャッシュレス洗濯パックに対応する。",
    ),
    "elevator [名]": (
        "Glass elevators overlook the courtyard koi pond.",
        "ガラスのエレベーターは中庭の鯉の池を見下ろす。",
    ),
    "separate [形]": (
        "Book separate twin rooms if snoring bothers your partner.",
        "いびきが気になるなら別々のツインを予約しなさい。",
    ),
    "landmark [名]": (
        "The red lighthouse remains the island's favourite photo landmark.",
        "赤い灯台は島で一番人気の記念撮影スポットだ。",
    ),
    "with ... nearby": (
        "We chose a villa with reef snorkel desks nearby.",
        "サンゴシュノーケルカウンターが近いヴィラを選んだ。",
    ),
    "description [名]": (
        "The allergy description on the buffet card spared us trouble.",
        "ビュッフェ札のアレルゲン詳細のおかげでトラブルを避けられた。",
    ),
    "dine [動]": (
        "You may dine on the terrace until nine thirty p.m.",
        "テラスでの夕食は午後九時半まで可能だ。",
    ),
    "feature [動]": (
        "Suites on six feature deep soaking tubs.",
        "六階のスイートは深い湯船付きが売りだ。",
    ),
    "LCD TV": (
        "Every LCD TV mirrors your phone for workout videos.",
        "各液晶テレビはワークアウト映像をスマホにミラーリングできる。",
    ),
    "convenience [名]": (
        "Beach showers add convenience after sandy walks.",
        "砂浜のあとに便利な屋外シャワーがある。",
    ),
    "amenity [名]": (
        "Complimentary yoga mats are a thoughtful amenity.",
        "無料ヨガマットは嬉しいサービスだ。",
    ),
    "facility [名]": (
        "The kids' facility stays open until ten for teens.",
        "ティーン向けキッズ施設は十時まで開いている。",
    ),
    "seasonal [形]": (
        "Seasonal mango desserts rotate on the room-service menu.",
        "ルームサービスは季節のマンゴースイーツを入れ替える。",
    ),
    "charger [名]": (
        "USB-C chargers sit in every locker at the spa lounge.",
        "スパラウンジの各ロッカーにUSB-C充電器がある。",
    ),
    "gorgeous [形]": (
        "The blogger called the sunrise pool gorgeous beyond photos.",
        "ブロガーは朝日のプールを写真では足りないほど見事だと書いた。",
    ),
    "buffet [名]": (
        "Breakfast buffet lines stay shady under sailcloth roofs.",
        "朝食ビュッフェの列は帆布屋根の下で涼しい。",
    ),
    "drawback [名]": (
        "One drawback is shuttle buses stopping at nine.",
        "欠点のひとつはシャトルが九時終了なことだ。",
    ),
    "lifeguard [名]": (
        "A lifeguard flagged rough swells at the lagoon bar.",
        "ライフガードがラグーン横のバーで高波を告げた。",
    ),
    "option [名]": (
        "Late checkout became an affordable paid option this season.",
        "レイトアウトが今季は手頃な有料オプションになった。",
    ),
    "humidity [名]": (
        "Humidity spiked after noon, so we skipped the nature walk.",
        "午後は湿気が跳ね上がったので自然散策はやめた。",
    ),
}

# ----- 第3問 異文化コミュニケーション記事 -----
SEC3_MANUAL: dict[str, tuple[str, str]] = {
    "miscommunication [名]": (
        "His story begins with simple miscommunication about silence.",
        "彼の話は沈黙の誤解から始まる。",
    ),
    "cultural exchange": (
        "Homestay rules say cultural exchange beats perfect grammar.",
        "ホームステイ規約は文化交流を完璧な文法より重んじる。",
    ),
    "have trouble −ing": (
        "New arrivals have trouble reading sarcasm over text.",
        "新参者は文章の皮肉を読み取るのに苦労する。",
    ),
    "get used to ...": (
        "You'll get used to bowing lightly in shop queues.",
        "店の列では浅くおじぎをするのに慣れる。",
    ),
    "nod [動]": (
        "A quick nod can mean \"I follow\" in his class.",
        "彼の授業ではうなずきが「理解した」の合図になりうる。",
    ),
    "be supposed to −": (
        "Guests are supposed to remove hallway shoes at the genkan.",
        "来客は玄関で廊下用の靴を脱ぐことになっている。",
    ),
    "slightly [副]": (
        "She sounded slightly annoyed, though she smiled.",
        "微笑んでいても声はわずかにいらだった。",
    ),
    "confused [形]": (
        "I felt confused when nobody laughed at the pun.",
        "しゃれを言っても誰も笑わず困惑した。",
    ),
    "a while ago": (
        "A while ago she warned me about classroom eye contact norms.",
        "少し前に彼女が教室での目線の慣習について教えてくれた。",
    ),
    "accompany [動]": (
        "Formal letters accompany internship offers in spring.",
        "春のインターン内定には正式書簡が添う。",
    ),
    "lead to": (
        "Skipping small talk can lead to awkward first meetings.",
        "雑談を飛ばすと初対面がぎこちなくなりかねない。",
    ),
    "serious [形]": (
        "Silence during feedback felt serious instead of shy.",
        "フィードバック中の沈黙は恥ずかしさではなく深刻さに聞こえた。",
    ),
    "misunderstanding [名]": (
        "We cleared the misunderstanding during tea after class.",
        "誤解は授業後のお茶で解けた。",
    ),
    "Why don't we ... ?": (
        "Why don't we compare notes before emailing the host mum?",
        "ホスト母にメールする前にメモを照合しませんか。",
    ),
    "account [名]": (
        "Give a short account of your hometown slide first.",
        "最初に出身地スライドの説明を短くしなさい。",
    ),
    "might have caused ...": (
        "That joke might have caused silence in Kyoto offices.",
        "その冗談は京都のオフィスでは沈黙を招きかねなかった。",
    ),
    "editor [名]": (
        "The editor invites readers to mail fresh examples.",
        "編集部は読者に新しい例をメールで募る。",
    ),
    "contact address": (
        "The contact address sits on the magazine's last page.",
        "連絡先は雑誌の最終ページにある。",
    ),
    "issue [名]": (
        "This issue reprints the chart on bow angles.",
        "この号はお辞儀の角度表を再掲している。",
    ),
    "inconsistent [形]": (
        "Her answers sound inconsistent with the earlier survey.",
        "彼女の答えは前のアンケートと矛盾して聞こえる。",
    ),
    "follow [動]": (
        "I could not follow his rapid after-class summary.",
        "放課後の速い要約は追えなかった。",
    ),
    "state [動]": (
        "The guidelines state that gifts must stay modest.",
        "ガイドラインは贈り物は控えめにと明言する。",
    ),
}


def _display_term_for_sentence(te: str) -> str:
    if len(te) <= 62:
        return te.replace('"', "'")
    return te[:30].rstrip() + " …"


def craft_examples(section: int, block: str, flash_order: int, term_en: str, term_ja: str) -> tuple[str, str]:
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
            src = f"sundai2026_round04_section{sn}_{block_key}"
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

    meta = {
        "exam": "駿台 共通テスト実戦問題集 2026年 第4回",
        "source": "data/sundai/2026/round04/data.json（各問 vocabulary 準拠・第1〜3問の例文は語句ごとに手書き、第4〜8問はテンプレから生成・scripts/generate_sundai2026_round04_vocab_json.py）",
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
    OUT.write_text(json.dumps({"meta": meta, "entries": entries}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(entries)} entries -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
