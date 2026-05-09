# -*- coding: utf-8 -*-
"""駿台実戦問題集 2026 第2回の語彙フラッシュカード用 JSON を生成する。

data.json の vocabulary をブロック順でフラット化する。
第1〜3問の例文は語句ごとに手書き、第4〜8問は題材に沿ったテンプレから決定的に生成。

出力: data/sundai/2026/round02/vocabulary_explanations_only_all_sections.json
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/sundai/2026/round02/data.json"
OUT = ROOT / "data/sundai/2026/round02/vocabulary_explanations_only_all_sections.json"

VOCAB_BLOCK_ORDER: dict[int, list[str]] = {
    1: ["passage", "question_kw"],
    2: ["lead_text", "passage", "question_kw"],
    3: ["passage", "question_kw"],
    4: ["lead_text", "passage", "question_kw"],
    5: ["passage", "question_kw"],
    6: ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "notes_vocab", "question_kw"],
    7: ["lead_title", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "slides", "question_kw"],
    8: ["lead", "step1", "question_kw_step1", "step2", "step3", "question_kw_step3"],
}

SECTION_TOPICS_EN = {
    1: "the book reviews for your reading assignment",
    2: "the YouVideo streaming-service review",
    3: "the science camp blog post",
    4: "the draft essay on edible insects",
    5: "the club magazine production materials",
    6: "the story The Moonlit Promise and your outline notes",
    7: "the silkworm-and-civilization presentation pack",
    8: "the telework opinion survey and essay outline",
}

SECTION_TOPICS_JA = {
    1: "小説選びのための書評",
    2: "動画配信サービス（YouVideo）のレビュー記事",
    3: "サイエンスキャンプのブログ記事",
    4: "昆虫食をテーマにしたエッセイ草稿",
    5: "部誌制作の記事・アンケート・配布資料",
    6: "The Moonlit Promise とノートのアウトライン",
    7: "蚕と文明の学術プレゼン資料",
    8: "テレワークに関する意見収集とレポート構成",
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
    if note and not ja:
        return f"〈解説〉{note}"
    for pat in (r"｢([^｣」]+)[」｣]", r"「([^」]+)」"):
        m = re.search(pat, en)
        if m:
            return m.group(1).strip()
    return ""


# ----- 第1問 書評 -----
SEC1_MANUAL: dict[str, tuple[str, str]] = {
    "mysterious": (
        "Stars Beyond Reach is billed as a mysterious science-fiction voyage.",
        "『Stars Beyond Reach』は神秘味あふれるSFの旅として宣伝されている。",
    ),
    "adventure": (
        "The blurb promises a space adventure packed with puzzles.",
        "帯には謎だらけの宇宙冒険がうたわれている。",
    ),
    "challenge": (
        "The twin narrators pose a challenge for first-time readers.",
        "双子の語り手は初読者には難所になりうる。",
    ),
    "combine": (
        "Skyler combines folk motifs with hard-science speculation.",
        "スカイラーは民俗的モチーフとハードSF的想像を組み合わせている。",
    ),
    "mystery": (
        "Detective Hale's London mystery sold out in independent stores.",
        "ヘイル探偵のロンドンのミステリーは小さな書店で売り切れた。",
    ),
    "top pick": (
        "Our club chose Whispers of the Past as its winter top pick.",
        "読書会は『Whispers of the Past』を冬の首推しにした。",
    ),
    "highlight": (
        "One highlight is a folded map pinned to the narrator's wall.",
        "見所のひとつは語り手の壁に貼られた折りたたみ地図だ。",
    ),
    "result in ...": (
        "Skipping the prologue can result in missing the twist entirely.",
        "プロローグを飛ばすとどんでん返しをすっかり見逃す結果になりかねない。",
    ),
    "demonstrate": (
        "The interview demonstrates why she refused film rights.",
        "インタビュは彼女が映画化権を断った理由を示している。",
    ),
    "publication": (
        "Delayed publication slid the sequel into the following autumn.",
        "出版の遅れで続編は翌秋になった。",
    ),
    "attract": (
        "Noir cover art might attract readers who dislike romance.",
        "ノワール調の表紙は恋愛が苦手な読者も引きつけうる。",
    ),
    "enthusiast": (
        "Train enthusiasts praised the station descriptions.",
        "鉄道オタクは駅の描写を称賛した。",
    ),
    "(be) set in ...": (
        "The trilogy is set in a coastal town before diesel rail arrived.",
        "三部作はディーゼル列車の到来前の港町を舞台にしている。",
    ),
}

# ----- 第2問 動画配信レビュー -----
SEC2_MANUAL: dict[str, tuple[str, str]] = {
    "look for ...": (
        "I began to look for a streaming app that lets me cite scenes for class.",
        "授業でシーンを引用できる配信アプリを探し始めた。",
    ),
    "following": (
        "I compared the following review with my classmates' handouts.",
        "次のレビューをクラスメートの配布資料と比較した。",
    ),
    "certain": (
        "I tested a certain service called YouVideo for my film report.",
        "映画のレポートのためにYouVideoというあるサービスを試した。",
    ),
    "try ... out": (
        "I tried out the Standard plan before upgrading my account.",
        "アカウントを上げる前にスタンダードプランを試してみた。",
    ),
    "cost": (
        "The Premium plan costs more than my monthly textbook budget.",
        "プレミアムは教科書の月額予算より高い。",
    ),
    "including": (
        "The roster lists documentaries, including one on silent cinema.",
        "ラインナップには無声映画のドキュメンタリーも含まれる。",
    ),
    "available": (
        "Over a thousand titles were available on the Standard tier.",
        "スタンダードで千本以上が利用できた。",
    ),
    "plenty": (
        "I had plenty of scenes to quote after the first weekend binge.",
        "最初の週末の一気見のあとも引用できる場面は十分あった。",
    ),
    "quality": (
        "Premium advertises better picture quality on large TVs.",
        "プレミアムは大型テレビでの画質の良さをうたう。",
    ),
    "plus": (
        "Plus, Premium streams bonus interviews before the DVD release.",
        "しかもプレミアムはDVDより先にボーナスインタビューを流す。",
    ),
    "stuff": (
        "Behind-the-scenes stuff alone kept my report entertaining.",
        "舞台裏の素材だけでもレポートを面白くできた。",
    ),
    "based on ...": (
        "Recommendations based on my watch history felt eerily accurate.",
        "視聴履歴に基づくおすすめが妙に正確で少し怖かった。",
    ),
    "having said that": (
        "Having said that, the Premium trial still tempted me.",
        "とはいえ、プレミアムのトライアルにはまだ惹かれた。",
    ),
    "the next plan up": (
        "A friend on the next plan up praised HDR dramas.",
        "ひとつ上のプランの友達はHDRのドラマを褒めていた。",
    ),
    "nothing but ...": (
        "She had nothing but praise for offline downloads on flights.",
        "オフラインDLについては彼女は褒め辞しかなかった。",
    ),
    "overall": (
        "Overall, YouVideo rescued my procrastinating research week.",
        "総じてYouVideoは先延ばしした調査週を救ってくれた。",
    ),
    "casual": (
        "Casual viewers may never need the Premium tier at all.",
        "たしなむ程度の視聴者はプレミアムに一生不要かもしれない。",
    ),
    "explore": (
        "The app helps couch potatoes explore world cinema cheaply.",
        "ソファ族が安く世界映画を探求するのにそのアプリは役立つ。",
    ),
    "according to ...": (
        "According to the review, Standard matched Basic pricing for ninety days.",
        "レビューによればスタンダードは九十日月ベーシック並みの値段だった。",
    ),
    "latest": (
        "I could not confirm whether latest blockbusters hit Basic at launch.",
        "公開初週に最新大作がベーシックへ来るかは確認できなかった。",
    ),
    "author": (
        "The author admits Premium tempts her even after praising Standard.",
        "筆者はスタンダードを褒めたあともプレミアムに心が揺れると認める。",
    ),
    "regular": (
        "Regular price jumps after the ninety-day teaser window.",
        "九十日のお試しのあとは通常価格に戻る。",
    ),
    "primarily": (
        "The service targets film lovers, not primarily live sports fans.",
        "そのサービスは映画好き向けで、主にスポーツ観戦用ではない。",
    ),
    "expensive": (
        "The expensive tier still beat theater tickets for two adults.",
        "高いティアでも大人二人の映画館よりはまだ安かった。",
    ),
    "classic": (
        "Classic TV bundles sweeten the Basic catalogue.",
        "古典TV番組の束がベーシックの目録を豊かにする。",
    ),
    "appropriate": (
        "Find an appropriate clip that matches your thesis sentence.",
        "主題文に合う適切なクリップを見つけなさい。",
    ),
    "combination": (
        "This combination of plans confused our billing desk.",
        "プランのこの組み合わせは経理担当を混乱させた。",
    ),
    "suitable": (
        "No single tier felt suitable for both roommates' tastes.",
        "二人のルームメイトの趣味にぴったりのティアは一つもなかった。",
    ),
    "occasional": (
        "Occasional outages annoyed thesis writers on deadline night.",
        "締切の夜にたまに起きる通信妨害が論文組をいら立たせた。",
    ),
    "satisfactory": (
        "Picture quality on Standard was more than satisfactory for seminars.",
        "スタンダードの画質はゼミ用には十分すぎるほどだった。",
    ),
    "benefit": (
        "The biggest benefit for me was exportable subtitles.",
        "私にとって最大の利点は字幕を書き出せたことだった。",
    ),
    "probably": (
        "Premium will probably pay for itself if we host movie nights weekly.",
        "週一回映画ナイトならプレミアムはおそらく元が取れる。",
    ),
    "purpose": (
        "Recommendations aligned with my purpose of citing three genres.",
        "おすすめは三ジャンル引用という私の目的に沿った。",
    ),
    "suggest": (
        "The UI suggests indie debuts I would never search manually.",
        "UIは手では検索しないようなインディ初作を提案する。",
    ),
    "match": (
        "No thumbnail matched the noir description in the catalogue.",
        "カタログのノワールの説明に合うサムネはなかった。",
    ),
    "interest": (
        "Romantic subplots sustained my interest between action beats.",
        "恋愛の枝話がアクションの合間の興味を保った。",
    ),
    "diverse": (
        "Students praised the diverse documentary shelf.",
        "学生たちはドキュメンタリー棚の多様さを褒めた。",
    ),
    "range": (
        "The wide range of extras justified Premium for our club.",
        "特典の幅の広さが部活ではプレミアムを正当化した。",
    ),
    "as soon as possible": (
        "Upgrade as soon as possible if your trial ends mid-project.",
        "トライアルが課題の真っ最中に終わるならなるべく早くアップグレードしなさい。",
    ),
}

# ----- 第3問 サイエンスキャンプブログ -----
SEC3_MANUAL: dict[str, tuple[str, str]] = {
    "liberal arts": (
        "Even liberal arts majors stayed up reading rover logs.",
        "文系の学生でさえローバーの記録を読みふけって夜更かしした。",
    ),
    "participate in ...": (
        "Forty teens participated in the midnight meteor watch.",
        "四十人のティーンが真夜中の流星観測に参加した。",
    ),
    "challenge": (
        "Tracking faint moons became our challenge on night three.",
        "淡い衛星を追うのが三泊目の難題になった。",
    ),
    "fascinating": (
        "Dr. Ruiz told a fascinating story about stray photons.",
        "ルイス博士は逸走した光子の面白い話をしてくれた。",
    ),
    "attractive": (
        "The camp's brochure looked attractive beside dusty textbooks.",
        "キャンプのパンフは埃っぽい教科書の横でも目を引いた。",
    ),
    "astronomical observation": (
        "Cloud cover cancelled astronomical observation until Thursday.",
        "雲で木曜まで天体観測は中止だった。",
    ),
    "analyze": (
        "We had to analyze spectra downloaded from the campus telescope.",
        "キャンパス望遠鏡から落としたスペクトルを解析しなければならなかった。",
    ),
    "planetary probe": (
        "A talk on a planetary probe left the gym breathless.",
        "惑星探査機の講義に体育館の全員が息を飲んだ。",
    ),
    "telescope": (
        "Dew fogged the telescope lens before Saturn rose.",
        "土星が昇る前に露が望遠鏡のレンズを曇らせた。",
    ),
    "observe": (
        "Trainees observe mentors calibrating the mount each sunset.",
        "研修生は毎夕、メンターが架台を合わせるのを見る。",
    ),
    "in a different way from ...": (
        "Mars looks dusty in a different way from lunar footage.",
        "火星は月面映像とは別種の埃っぽさに見える。",
    ),
    "capture": (
        "The webcam failed to capture the aurora's subtle colours.",
        "ウェブカムはオーロラの微妙な色を捉え損ねた。",
    ),
    "emit": (
        "The guide laser emits a harmless line across the dome slit.",
        "ガイドレーザーはドームのスリットに無害な線を出す。",
    ),
    "scary": (
        "Walking the catwalk felt scary until harness drills finished.",
        "ハーネスの訓練が終わるまで高所通路は怖かった。",
    ),
    "consumption": (
        "Battery consumption spiked when heaters ran all night.",
        "暖房を徹夜で回すとバッテリー消費が跳ね上がった。",
    ),
    "purify": (
        "Volunteers helped purify dew off mirror segments each dawn.",
        "志願者は毎朝、鏡セグメントの露を拭き取って洗った。",
    ),
    "operate": (
        "Only staff may operate the dome shutters during lightning.",
        "落雷時にドームのシャッタを動かせるのは職員だけだ。",
    ),
    "initially": (
        "Initially we confused Jupiter's moon with a background star.",
        "当初は木星の衛星を背景星と取り違えた。",
    ),
    "invisible": (
        "The companion star stayed invisible behind haze.",
        "伴星は霧の後ろで見えないままだった。",
    ),
    "naked eye": (
        "Venus dazzles the naked eye long before telescopes matter.",
        "金星は望遠鏡以前に肉眼でまぶしい。",
    ),
    "curiosity": (
        "Curiosity beat sleep when the alarm pinged at three a.m.",
        "午前三時のアラームでは好奇心が眠りに勝った。",
    ),
    "celestial body": (
        "Name every celestial body you sketch in the logbook.",
        "観測ノートに描いた天体をすべて名前で示しなさい。",
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
            src = f"sundai2026_round02_section{sn}_{block_key}"
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
        "exam": "駿台 共通テスト実戦問題集 2026年 第2回",
        "source": "data/sundai/2026/round02/data.json（各問 vocabulary 準拠・第1〜3問の例文は語句ごとに手書き、第4〜8問はテンプレから生成・scripts/generate_sundai2026_round02_vocab_json.py）",
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
