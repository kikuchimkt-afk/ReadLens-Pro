# -*- coding: utf-8 -*-
"""駿台実戦問題集 2026 第3回の語彙フラッシュカード用 JSON を生成する。

data.json の vocabulary をブロック順でフラット化する。
第1〜3問の例文は語句ごとに手書き、第4〜8問は題材に沿ったテンプレから決定的に生成。

出力: data/sundai/2026/round03/vocabulary_explanations_only_all_sections.json
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/sundai/2026/round03/data.json"
OUT = ROOT / "data/sundai/2026/round03/vocabulary_explanations_only_all_sections.json"

VOCAB_BLOCK_ORDER: dict[int, list[str]] = {
    1: ["passage"],
    2: ["passage", "questions"],
    3: ["situation", "passage", "questions"],
    4: ["situation", "passage", "comments", "questions"],
    5: ["passage"],
    6: ["title", "para1", "para2", "para3", "para4", "para5", "para6", "para7", "para8", "para9", "notes", "questions"],
    7: ["lead", "para1", "para2", "para3", "para4", "para5", "para6", "slides", "questions"],
    8: ["lead", "step1", "step2", "step3"],
}

SECTION_TOPICS_EN = {
    1: "the language-school website about summer drama seminars",
    2: "the Limit Tech Challenge report and reader comments",
    3: "the blog about staging a children's quiz race outdoors",
    4: "the draft essay on AI image tools and art class",
    5: "the transition-to-university article, survey, and handout",
    6: "the story More Than a Maths Problem and your presentation notes",
    7: "the Svalbard seed vault presentation pack and slides",
    8: "the group-work survey steps for your teamwork essay",
}

SECTION_TOPICS_JA = {
    1: "語学学校のサマードラマ・セミナーサイト",
    2: "テクノ制限チャレンジのレポートとコメント",
    3: "子ども向けクイズレース企画のブログ",
    4: "AI画像生成と美術のエッセイ改訂",
    5: "大学生活への移行の記事・アンケート・資料",
    6: "More Than a Maths Problem と発表ノート",
    7: "世界種子貯蔵庫の発表資料とスライド",
    8: "グループワークの意見整理とエッセイ構成",
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
    if note and not ja:
        return f"〈解説〉{note}"
    en = (item.get("en") or "").strip()
    for pat in (r"｢([^｣」]+)[」｣]", r"「([^」]+)」"):
        m = re.search(pat, en)
        if m:
            return m.group(1).strip()
    return ""


# ----- 第1問 語学学校ウェブサイト -----
SEC1_MANUAL: dict[str, tuple[str, str]] = {
    "descriptive": (
        "Seminar pages promise descriptive feedback on pronunciation and gesture.",
        "セミナー案内は発音と身振りについて記述的なフィードバックがあると約束している。",
    ),
    "introduce": (
        "Display Week instructors introduce new staging tricks each morning.",
        "ディスプレイ週の講師は毎朝新しい演出の仕掛けを紹介する。",
    ),
    "Prizes available!": (
        "Posters by the lift still shout Prizes available! for the improv slam.",
        "エレベータ横のポスターは即興大会の賞品を今も叫んでいる。",
    ),
    "visual": (
        "Story seminar applicants must upload a visual sample under two megabytes.",
        "ストーリー・セミナーは2MB未満の視覚資料の提出を求める。",
    ),
    "adaptation": (
        "Their adaptation trims Shakespeare to forty classroom minutes.",
        "その脚色版はシェイクスピアを授業40分に削る。",
    ),
    "dialogue": (
        "Rewrite stiff dialogue so teenage actors sound natural in English.",
        "高校生役者が英語で自然に聞こえるよう堅い対話を書き換えなさい。",
    ),
}

# ----- 第2問 レポート＋コメント -----
SEC2_MANUAL: dict[str, tuple[str, str]] = {
    "app": (
        "Our debate downloaded the school's pilot wellbeing app for reference.",
        "議論の参考に学校のウェルビーイング試用アプリをダウンロードした。",
    ),
    "go online": (
        "Boarders could not go online until mentors released the evening code.",
        "寄宿生はメンターが夜のコードを公開するまでネットに出られなかった。",
    ),
    "sign up": (
        "Only forty day students could sign up before the waiting list closed.",
        "待ちリストが閉まる前に通学40人だけが登録できた。",
    ),
    "Looking at some comments (given below)": (
        "Looking at some comments (given below), I tracked anxiety spikes on day two.",
        "（以下の）コメントを見ると、二日目に不安が跳ね上がるのがわかった。",
    ),
    "I'm so used to ... that limited time online made me anxious": (
        "I'm so used to streaming labs that limited time online made me anxious.",
        "実験を配信で見るのに慣れすぎていて、オンライン時間が短いと不安になった。",
    ),
    "staying offline": (
        "Staying offline forced me to rehearse speeches on paper.",
        "オフラインでい続けるのでスピーチを紙に書いて練習せざるを得なかった。",
    ),
    "log on": (
        "Mentors let us log on briefly to submit reflection forms.",
        "振り返り用紙の提出のためだけ短くログオンを許された。",
    ),
    "Getting ideas from the Net": (
        "Getting ideas from the Net was off limits during the twenty-hour mute.",
        "二十時間の禁音中はネットからのアイディアは禁止だった。",
    ),
    "boost": (
        "Shared silence oddly gave my attention span a boost.",
        "不思議と共同の静寂が集中度を押し上げた。",
    ),
    "struggle to-": (
        "Many teens struggle to sleep when phones rest in another room.",
        "スマホを別室に置くと多くのティーンは眠れなく苦労する。",
    ),
    "switch ... off / switch off ...": (
        "House rules made us switch our routers off by ten p.m.",
        "寮則で夜十時までにルータを切らなければならなかった。",
    ),
}

# ----- 第3問 クイズレース・ブログ -----
SEC3_MANUAL: dict[str, tuple[str, str]] = {
    "one a British woman designed": (
        "We imitated the warm-up race one a British woman designed for scouts.",
        "私たちはスカウト向けにある英国人女性が考えたウォームアップ競争を真似た。",
    ),
    'a Fun "Quiz Race"': (
        'Advertise a Fun "Quiz Race" only after the park permit clears.',
        "公園の許可が下りてから楽しい「クイズ競争」を宣伝しなさい。",
    ),
    "Read my ideas to make your own!": (
        "Read my ideas to make your own!, then tag our borough on the post.",
        "（私のアイディアを読んで自分用に！）あと投稿で市区名をメンションしなさい。",
    ),
    "nature reserve": (
        "We staged photo clues across the reed beds in the nature reserve.",
        "自然保護区の葦原に写真の手がかりをばらまいた。",
    ),
    "kids finding yellow flowers or crawling under a blanket": (
        "Teams earned stickers when kids finding yellow flowers or crawling under a blanket checked in.",
        "黄花を見つけた子や毛布の下を這う子がチェックインしたらチームにシールが付いた。",
    ),
    "while holding balloons": (
        "Disqualify selfies snapped while holding balloons in the shot.",
        "風船を写し込んだ自撮りは失格にしなさい。",
    ),
    "construction": (
        "Avoid the west gate because weekend construction blocks ramps.",
        "西門は週末の工事でスロープが塞がるので避けなさい。",
    ),
    "Just place household things you already own somewhere difficult to find.": (
        "Just place household things you already own somewhere difficult to find to save money.",
        "見つけにくい場所へすでにある日用品を置くだけならお金がかからない。",
    ),
    "our kids had to video-call the adult responsible for their team and either do their challenge on camera or prove that ...": (
        "Each round, our kids had to video-call the adult responsible for their team first.",
        "各ラウンドで子どもはまずチーム担当の大人にビデオ通話しなければならなかった。",
    ),
    "when planning": (
        "Print evacuation arrows when planning races near the pond.",
        "池のそばの競争を計画するときは避難矢印を印刷しておきなさい。",
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
            src = f"sundai2026_round03_section{sn}_{block_key}"
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
        "exam": "駿台 共通テスト実戦問題集 2026年 第3回",
        "source": "data/sundai/2026/round03/data.json（各問 vocabulary 準拠・第1〜3問の例文は語句ごとに手書き、第4〜8問はテンプレから生成・scripts/generate_sundai2026_round03_vocab_json.py）",
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
