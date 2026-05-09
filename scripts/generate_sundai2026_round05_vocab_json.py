# -*- coding: utf-8 -*-
"""駿台実戦問題集 2026 第5回の語彙フラッシュカード用 JSON を生成する。

data.json の vocabulary をブロック順でフラット化する。
第1〜3問の例文は語句ごとに手書き、第4〜7問は題材に沿ったテンプレから決定的に生成。

（本テストは第8問なし: implemented_sections は 1〜7）

出力: data/sundai/2026/round05/vocabulary_explanations_only_all_sections.json
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/sundai/2026/round05/data.json"
OUT = ROOT / "data/sundai/2026/round05/vocabulary_explanations_only_all_sections.json"

VOCAB_BLOCK_ORDER: dict[int, list[str]] = {
    1: ["lead_text", "passage"],
    2: ["lead_text", "passage"],
    3: ["lead_text", "passage"],
    4: ["lead_text", "passage", "questions_and_choices"],
    5: ["passage"],
    6: ["lead_text", "passage", "questions_and_choices"],
    7: ["lead_text", "p1", "p2", "p3", "p4", "p5", "p6", "questions_and_choices"],
}

SECTION_TOPICS_EN = {
    1: "the web ad for a creative writing summer course",
    2: "the school newspaper article on student health initiatives",
    3: "the article on kitchen routines and staying organized",
    4: "the essay revision with teacher comments on cohesion",
    5: "the long essay on language teaching methods",
    6: "the article with blanks to complete your notes",
    7: "the biology article and presentation slide cues",
}

SECTION_TOPICS_JA = {
    1: "クリエイティブライティング夏期講座のウェブ広告",
    2: "生徒の健康対策についての学校記事",
    3: "キッチンの整理とルーティーンの記事",
    4: "教師コメントに基づくエッセイのつなぎ・置換・要約",
    5: "言語教授法を論じる長文論説",
    6: "メモ完成形式の記事読解",
    7: "生物学の長文と発表スライドの手がかり",
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


# ----- 第1問 ウェブ広告 -----
SEC1_MANUAL: dict[str, tuple[str, str]] = {
    "creative writing": (
        "The banner promises daily workshops in creative writing and peer review.",
        "バナーは創作と相互批評の日課ワークショップをうたっている。",
    ),
    "summer course": (
        "Places in the July summer course vanish once lottery results post.",
        "七月の夏期講座の枠は抽選結果が出るとすぐ埋まる。",
    ),
    "annual": (
        "This annual retreat sells out before spring break every year.",
        "この年一回の合宿は毎年春休み前に売り切れる。",
    ),
    "intensive": (
        "Intensive mornings cover plotting; afternoons stay elective.",
        "集中の午前はプロット、午後は選択制だ。",
    ),
    "accommodation": (
        "Optional dorm accommodation lists on another registration page.",
        "寮宿泊は別の登録ページに載る。",
    ),
    "available": (
        "Few scholarships stay available after the first lottery window.",
        "初回抽選のあと残る奨学金はわずかだ。",
    ),
    "analyze": (
        "Small groups analyze mentor scripts before pitching scenes.",
        "ピッチの前に少人数班でメンター原稿を分析する。",
    ),
    "award-winning": (
        "An award-winning novelist hosts Friday campfire readings.",
        "受賞歴のある小説家が金曜のキャンプファイア読書を司会する。",
    ),
    "screenwriter": (
        "One visiting screenwriter edits our dialogue beats line by line.",
        "招かれた脚本家が台詞のビートを一行ずつ直す。",
    ),
    "perform": (
        "Pairs perform a two-page scene under the pine awning.",
        "ペアが松の軒下で二ページのシーンを演じる。",
    ),
    "campmate": (
        "Your campmate may critique voice but never shame genre choices.",
        "キャンプ仲間は文体を批評してもジャンルを嘲笑してはならない。",
    ),
    "novelist": (
        "The resident novelist signs paperbacks on closing night.",
        "滞在作家は最終夜に文庫本にサインする。",
    ),
    "complete": (
        "You must complete the waiver before touching studio lights.",
        "スタジオの照明に触れる前に免責へ署名し終えなければならない。",
    ),
    "state": (
        "The FAQ states that minors need a guardian email on file.",
        "FAQは未成年者には保護者メールの登録が要ると明記する。",
    ),
    "confirmation": (
        "Expect a confirmation code within ten minutes of paying.",
        "支払い後十分以内に確認コードが届く。",
    ),
    "note": (
        "The sidebar note warns that lake boats cancel in lightning.",
        "欄外の注意は湖畔のボートが雷雨で中止になると書いている。",
    ),
    "at random": (
        "Mentor groups form at random after icebreakers Monday.",
        "月曜のアイスブレイク後はメンター班が無作為に決まる。",
    ),
}

# ----- 第2問 学校記事 -----
SEC2_MANUAL: dict[str, tuple[str, str]] = {
    "student council": (
        "Student council minutes posted this pilot before winter exams.",
        "冬の試験前に生徒会がこの試行案を掲示した。",
    ),
    "in addition": (
        "In addition, hall monitors now carry allergy kits.",
        "その上、走廊の当番は今アレルギー用キットを持つ。",
    ),
    "previous": (
        "Compared with previous semesters, vending machines stock juice only.",
        "前の学期より自販機はジュースだけになった。",
    ),
    "unhealthy": (
        "The nurse linked unhealthy snacks to afternoon crashes.",
        "看護師は不健康な間食と午後のだるさを結びつけた。",
    ),
    "overweight": (
        "Charts tracked overweight trends without naming individuals.",
        "図表は個人名を出さず肥満傾向を追った。",
    ),
    "be worried about ...": (
        "Parents used to be worried about bike helmets; now phones dominate.",
        "昔は自転車のヘルメットを心配していた保護者が、今はスマホを心配する。",
    ),
    "safety": (
        "Safety drills now include bus evacuations twice a term.",
        "安全訓練は学期に二度バスからの避難を含む。",
    ),
    "on a trial basis": (
        "Meatless Mondays run on a trial basis through March.",
        "ミートレス月曜は三月まで試行的に実施する。",
    ),
    "supervisor": (
        "Each floor supervisor logs late arrivals after nine p.m.",
        "各階の監督員が午後九時以降の遅刻を記録する。",
    ),
    "feedback": (
        "Cafeteria feedback boards fill with spice requests.",
        "食堂の感想ボードは香辛料の要望であふれる。",
    ),
    "thanks to ...": (
        "Thanks to new filters, tap water tastes neutral again.",
        "新しい浄水器のおかげで水道水がまろやかになった。",
    ),
    "in the beginning": (
        "In the beginning, clubs resisted moving practice indoors.",
        "当初は部活が屋内練習に反対した。",
    ),
    "trust O to -": (
        "Teachers trust monitors to lock roofs after astronomy club.",
        "教師は天文部のあと屋上を施錠するよう当番を信頼している。",
    ),
    "motivate O to -": (
        "Sticker charts motivate younger kids to climb stairs.",
        "シール表が幼い子たちを階段で上らせる気にさせる。",
    ),
}

# ----- 第3問 キッチン整理の記事 -----
SEC3_MANUAL: dict[str, tuple[str, str]] = {
    "messy": (
        "Our messy drawer hid graters behind chipped mugs.",
        "散らかった引き出しは欠けたマグのうしろにおろし金を隠していた。",
    ),
    "organize": (
        "She uses Sunday nights to organize spice jars by cuisine.",
        "彼女は日曜夜に香辛料を料理ジャンル別に整理する。",
    ),
    "maximize": (
        "Open shelving maximizes light in a narrow galley kitchen.",
        "オープン棚は狭いギャレーキッチンの光を最大にする。",
    ),
    "on schedule": (
        "Batch cooking stays on schedule if rice starts first.",
        "米を先に炊けば作り置きは予定通り進む。",
    ),
    "decrease": (
        "Labelled bins decreased our food waste within a month.",
        "ラベル付き容器で一か月以内に食品ロスが減った。",
    ),
    "tidy up": (
        "We tidy up counters before the inspector's photo.",
        "検査員の写真の前にカウンターを片付ける。",
    ),
    "get rid of ...": (
        "Get rid of chipped plastic before it contaminates flour jars.",
        "欠けたプラスチックを小麦粉瓶を汚す前に捨てなさい。",
    ),
    "clutter": (
        "Magnetic rails reduce clutter near the stove.",
        "マグネットレールがコンロ周りの乱雑さを減らす。",
    ),
    "plate": (
        "Stack plates by size so guests grab sets faster.",
        "皿は大きさ順に積めば客がセットを取りやすい。",
    ),
    "dish": (
        "Run the heavy dish cycle after greasy brunch pans.",
        "油のついたブランチ用パンのあとは強洗浄で皿洗いを回す。",
    ),
    "pan": (
        "Hang carbon-steel pans dry to stop rust specks.",
        "炭素鋼のフライパンは錆を防ぐため乾かして吊す。",
    ),
    "free up ...": (
        "Wall hooks free up drawer space for linens.",
        "壁フックが引出しをタオル類が入る空きにする。",
    ),
    "storage": (
        "Clear storage lets you spot pasta before it stales.",
        "透明容器ならパスタが古くなる前にわかる。",
    ),
    "cooker": (
        "The pressure cooker's steam scorched the cabinet paint once.",
        "圧力なべの蒸気で一度キャビネットの塗装が焦げた。",
    ),
    "right-handed": (
        "Right-handed cooks keep knives to the right of the sink.",
        "右利きの料理人は包丁をシンク右に置く。",
    ),
    "coffee machine": (
        "Descale the coffee machine before relatives visit.",
        "親戚の訪問前にコーヒーマシンを除石灰しなさい。",
    ),
    "focus on ...": (
        "This week we focus on vertical fridge zones only.",
        "今週は冷蔵庫の縦ゾーンだけに集中する。",
    ),
    "replacement": (
        "Order replacement seals when the blender leaks.",
        "ミキサーから漏れたらパッキンを取り寄せなさい。",
    ),
    "flour": (
        "Sift flour twice when humidity spikes above seventy percent.",
        "湿度が70%を超えるときは小麦粉を二度ふるいなさい。",
    ),
    "virtual": (
        "She keeps a virtual pantry list synced to her phone.",
        "彼女は仮想の食材棚リストをスマホと同期している。",
    ),
    "recipe": (
        "Pin the recipe card to the hood during stir-fry night.",
        "炒め物の夜はレシピカードをレンジフードに留める。",
    ),
    "scrap": (
        "Compost vegetable scraps unless the bin smells sour.",
        "生ゴミが酸っぱくなければ野菜くずを堆肥に回す。",
    ),
    "notepad": (
        "Keep a notepad on the fridge for odd guest requests.",
        "来客の変わった要望は冷蔵庫のメモ帳に書く。",
    ),
    "a pile of ...": (
        "A pile of lids slid when someone yanked the wrong drawer.",
        "誰かが違う引き出しを勢いよく開けて蓋の山が滑った。",
    ),
    "photograph": (
        "Photograph spices before donating the shaker rack.",
        "スパイス棚を寄付する前に写真に撮っておきなさい。",
    ),
    "store": (
        "Store onions in mesh bags away from potatoes.",
        "玉ねぎはじゃがいもから離してメッシュ袋で保管する。",
    ),
    "turn": (
        "Take turns scrubbing tile grout each Sunday.",
        "日曜ごとにタイル目地を交代で磨く。",
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
            src = f"sundai2026_round05_section{sn}_{block_key}"
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

    nums = sorted(counts_by_section.keys())
    meta = {
        "exam": "駿台 共通テスト実戦問題集 2026年 第5回",
        "source": "data/sundai/2026/round05/data.json（各問 vocabulary 準拠・第1〜3問の例文は語句ごとに手書き、第4〜7問はテンプレから生成・scripts/generate_sundai2026_round05_vocab_json.py）",
        "sections_in_data": nums,
        "counts_by_section": {f"section{k}": counts_by_section[k] for k in nums},
        "counts_by_source_prefix": counts_by_block,
    }
    for k in nums:
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
