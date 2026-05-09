# -*- coding: utf-8 -*-
"""Z会実戦模試2026第3回の語彙フラッシュカード用 JSON を生成する（data.json 準拠・例文は手作業）。第5〜8問は語彙ブロックなし。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/zkai/2026/round03/vocabulary_explanations_only_all_sections.json"

# (section_number, flashcard_order, term_en, term_ja, example_en, example_ja, source)
ROWS = [
    # === 第1問 旅行サイト・夜市 ===
    (1, 0, "midday", "〈名〉真昼；正午（⇔ midnight）", "Enjoy an evening walk out of the midday heat at East Park.", "東公園の夜市では、真昼の暑さを避けて夕方の散歩ができる。", "zkai2026_round03_section1_passage"),
    (1, 1, "speciality", "〈名〉名物（料理）；特産品（米国英語では specialty）", "You can taste speciality foods made by local people.", "地元の人が手がける名物の食品を味わえる。", "zkai2026_round03_section1_passage"),
    (1, 2, "stand", "〈名〉売店；露店", "Food stands are open every night from 6 p.m. to 10 p.m.", "屋台は毎晩午後6時から10時まで営業している。", "zkai2026_round03_section1_passage"),
    (1, 3, "on a lead", "〈表現〉（飼い犬などが）ひもでつながれた", "No pets are allowed, even on a lead or in carriers.", "ひもでつないでもキャリーに入れても、ペットは一切不可である。", "zkai2026_round03_section1_passage"),
    (1, 4, "carrier", "〈名〉運ぶための入れ物", "Carriers do not make pets welcome at the Night Market.", "キャリーに入れても夜市へのペット持ち込みは認められない。", "zkai2026_round03_section1_passage"),
    (1, 5, "tip for ~（問1④）", "〈名〉〜のコツ；秘訣", "Choice ④ offered tips for walking safely at night, yet the notice focuses on the event.", "選択肢④は夜の安全な歩き方のコツだが、通知の目的はイベント紹介である。", "zkai2026_round03_section1_passage"),
    # === 第2問 在宅勤務の記事＋コメント ===
    (2, 0, "telecommuting", "〈名〉在宅勤務", "The article discusses how telecommuting changes daily routines.", "記事は在宅勤務が日課をどう変えるかを論じる。", "zkai2026_round03_section2_passage"),
    (2, 1, "update", "〈動〉〜を更新する", "The ACS updated their statistics on the telecommuting population.", "ACSは在宅勤務人口の統計を更新した。", "zkai2026_round03_section2_passage"),
    (2, 2, "as of ~", "〈前〉〜の時点で", "As of 2016, about 3.2% of workers telecommuted most days.", "2016年時点では労働者の約3.2%が半分以上を在宅で過ごしていた。", "zkai2026_round03_section2_passage"),
    (2, 3, "utility / utilities", "〈名〉（電気・ガス・水道などの）公共設備；光熱費を含む運営コストのイメージも", "Employers save transportation and utilities costs when staff stay home.", "スタッフが在宅なら雇用主は交通費や光熱費を抑えられる。", "zkai2026_round03_section2_passage"),
    (2, 4, "opinion vs fact（問2・問3）", "〈対比〉意見＝主張・評価；事実＝データ・定義など検証可能な記述", "Identify whether each sentence states an opinion or a measurable fact.", "各文が意見か検証可能な事実かを見極めなさい。", "zkai2026_round03_section2_passage"),
    (2, 5, "save + 人 + 物（問2③の型）", "〈型〉save employees commuting time ＝通勤時間という負担を（在宅によって）省く", "Telecommuting saves employees commuting time that feels wasted.", "在宅勤務は無駄に感じる通勤時間という負担を省く。", "zkai2026_round03_section2_passage"),
    # === 第3問 オープンキャンパス・ブログ ===
    (3, 0, "campus", "〈名〉キャンパス；（大学などの）構内", "The open day started with a guided tour of the campus.", "オープンキャンパスはガイド付きの構内ツアーから始まった。", "zkai2026_round03_section3_passage"),
    (3, 1, "focused", "〈形〉集中した；専念した", "She stayed focused on realistic goals for university life.", "彼女は大学生活の現実的な目標に集中した。", "zkai2026_round03_section3_passage"),
    (3, 2, "dorm (= dormitory)", "〈名〉寮", "Students debated whether life in a dorm would suit them.", "寮生活が自分に合うかどうかを学生たちは話し合った。", "zkai2026_round03_section3_passage"),
    (3, 3, "impress", "〈動〉〜に強い印象を与える；感銘を与える", "The science lab failed to impress visitors that rainy afternoon.", "その雨の午後、理科室は来場者の心をつかめなかった。", "zkai2026_round03_section3_passage"),
    (3, 4, "current", "〈形〉現在の；（地位などに）ある", "Her current worries mix exams with choosing a major.", "彼女の今の悩みは試験と専攻選択が混ざっている。", "zkai2026_round03_section3_passage"),
    (3, 5, "struggle", "〈名〉苦闘；難局", "Every freshman faces the struggle of balancing clubs and grades.", "どの1年生もサークルと成績の両立という難局に直面する。", "zkai2026_round03_section3_passage"),
    (3, 6, "freshman", "〈名〉（大学の）1年生", "As a freshman blogger, Mio described crowded lecture halls.", "1年生のブロガーとしてミオは講義室の混雑を書いた。", "zkai2026_round03_section3_passage"),
    (3, 7, "feel inspired to do", "〈表現〉…しようという気になる", "She felt inspired to do more research on exchange programs.", "彼女は留学プログラムをもっと調べようという気になった。", "zkai2026_round03_section3_passage"),
    (3, 8, "senior year", "〈名〉（高校・大学などの）最終学年", "Choosing a university still feels distant before senior year.", "最終学年の前では大学選びはまだ遠い感じがする。", "zkai2026_round03_section3_passage"),
    (3, 9, "impact（問1①）", "〈名〉影響", "The question asks which choice names the essay's largest impact.", "設問はエッセイで最も強調されている影響を選ばせる。", "zkai2026_round03_section3_passage"),
    (3, 10, "hang around（問1④）", "〈動〉ぶらぶらする；のんびり過ごす", "Hang around downtown after class if you love street food.", "屋台が好きなら放課後は都心をぶらぶらしてもいい。", "zkai2026_round03_section3_passage"),
    (3, 11, "suit（問3④）", "〈動〉（人・目的などに）合う；向いている", "Pick the degree track that suits your strengths.", "自分の強みに合ったコースを選びなさい。", "zkai2026_round03_section3_passage"),
]

# 第4問 本文（大気汚染エッセイ）
ROWS += [
    (4, 0, "skyline", "〈名〉スカイライン（空を背景とした建物のシルエット）", "In the old photo the skyline was barely visible through smog.", "古い写真ではスモッグ越しにスカイラインがかすんでいた。", "zkai2026_round03_section4_passage"),
    (4, 1, "barely", "〈副〉ほとんど〜ない", "We could barely see the hills until the wind cleared the air.", "風が空気を澄ますまで山並みはほとんど見えなかった。", "zkai2026_round03_section4_passage"),
    (4, 2, "visible", "〈形〉目に見える", "PM2.5 made the moon barely visible that night.", "その夜はPM2.5で月がかすかにしか見えなかった。", "zkai2026_round03_section4_passage"),
    (4, 3, "global scale", "〈名〉世界規模", "We must tackle air pollution on a global scale.", "大気汚染は世界規模で取り組まなければならない。", "zkai2026_round03_section4_passage"),
    (4, 4, "estimate that ...", "〈表現〉…と推定する", "The WHO estimates that millions die early because of dirty air.", "WHOは汚れた空気が早熟死を招くと何百万人も推定している。", "zkai2026_round03_section4_passage"),
    (4, 5, "move towards ~", "〈表現〉〜への移行〔変化〕", "Cities need a faster move towards electric buses and trams.", "都市は電気バスや路面電車への移行を速める必要がある。", "zkai2026_round03_section4_passage"),
    (4, 6, "cause", "〈名〉原因；（〈動〉〜を引き起こす）", "Cars remain a major cause of urban smog.", "自動車は都市スモッグの主要因のままだ。", "zkai2026_round03_section4_passage"),
    (4, 7, "practical", "〈形〉現実的な；実際的な", "Buying an EV is still not practical without chargers nearby.", "近くに充電器がなければEV購入はまだ現実的ではない。", "zkai2026_round03_section4_passage"),
    (4, 8, "designated", "〈形〉指定された", "London uses designated low emission zones to cut traffic fumes.", "ロンドンは排気を減らす指定の低排出ゾーンを使う。", "zkai2026_round03_section4_passage"),
    (4, 9, "emission", "〈名〉排出（量）；（多く複数形で）排出ガス", "Older trucks fail the newest emission standards.", "古いトラックは最新の排出ガス基準を満たさない。", "zkai2026_round03_section4_passage"),
    (4, 10, "basically", "〈副〉基本的に", "Basically, drivers pay to enter if their engines are dirty.", "基本的にエンジンが汚い運転者は入域に金を払う。", "zkai2026_round03_section4_passage"),
    (4, 11, "standard", "〈名〉基準", "Japan could tighten exhaust standards for delivery vans.", "日本は配送バンの排気基準を厳しくしてもよい。", "zkai2026_round03_section4_passage"),
    (4, 12, "policy", "〈名〉政策", "National policy still relies on hoping consumers choose EVs.", "国の政策は消費者がEVを選ぶことを願う依存度がまだ高い。", "zkai2026_round03_section4_passage"),
    (4, 13, "suck up ~", "〈表現〉〜を吸い上げる", "Street trees suck up carbon dioxide while shading shoppers.", "街路樹は買い物客に日陰を与えつつ二酸化炭素を吸い上げる。", "zkai2026_round03_section4_passage"),
    (4, 14, "carbon dioxide", "〈名〉二酸化炭素", "Citizens track carbon dioxide levels on their phones.", "市民はスマホで二酸化炭素濃度を確認する。", "zkai2026_round03_section4_passage"),
    (4, 15, "global citizen", "〈名〉地球市民", "We should act as global citizens even when smog feels local.", "スモッグが身近に感じなくても地球市民として行動すべきだ。", "zkai2026_round03_section4_passage"),
    (4, 16, "toxic", "〈形〉有毒な", "Factories must filter toxic gases before releasing smoke.", "工場は煙を出す前に有毒ガスをろ過しなければならない。", "zkai2026_round03_section4_passage"),
    (4, 17, "entire ~", "〈形〉〜全体の", "What we do here affects the entire global ecosystem.", "ここでの行いは地球の生態系全体に影響する。", "zkai2026_round03_section4_passage"),
    (4, 18, "minor", "〈形〉ささいな；ちょっとした", "The teacher asked only for minor revisions to the draft.", "先生は草稿にささいな修正だけを求めた。", "zkai2026_round03_section4_passage"),
]
# 第4問 設問語句
ROWS += [
    (4, 19, "as of ~（問1）", "〈前〉〜の時点で", "As of 2023, only 3% of cars in Japan were electric.", "2023年時点で日本の車の3%しか電気自動車ではなかった。", "zkai2026_round03_section4_questions"),
    (4, 20, "in contrast（問2①）", "〈接続〉対照的に；その一方で", "Japan hopes buyers choose EVs; in contrast, European cities regulate entry.", "日本は購入を願うのに対し、欧州の都市は入域を規制する。", "zkai2026_round03_section4_questions"),
    (4, 21, "in particular（問2②）", "〈副〉特に", "Smog harms children, in particular those who walk to school on busy roads.", "スモッグは子どもに害し、特に幹線道路脇を歩く子に厳しい。", "zkai2026_round03_section4_questions"),
    (4, 22, "nevertheless（問2③）", "〈接続〉それにもかかわらず", "Fuel prices fell; nevertheless, diesel trucks stayed on the roads.", "燃料価格は下がったが、ディーゼルトラックは道路に残った。", "zkai2026_round03_section4_questions"),
    (4, 23, "keep up with ~（問4③）", "〈表現〉〜に遅れずについていく", "Tokyo must keep up with other cities in controlling toxic gas.", "東京は有毒ガス抑制で他都市に遅れを取らないようにしなければならない。", "zkai2026_round03_section4_questions"),
    (4, 24, "contribution（問4④）", "〈名〉貢献", "Choice ④ oddly stresses financial contribution instead of air policy.", "選択肢④は大気政策ではなく財政貢献を奇妙に強調する。", "zkai2026_round03_section4_questions"),
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
    n4p = sum(1 for r in ROWS if r[0] == 4 and r[6] == "zkai2026_round03_section4_passage")
    n4q = sum(1 for r in ROWS if r[0] == 4 and r[6] == "zkai2026_round03_section4_questions")
    meta = {
        "exam": "Z会 共通テスト実戦模試 2026年 第3回",
        "source": "data/zkai/2026/round03/data.json（各問 vocabulary 準拠・例文は手作業・scripts/generate_zkai2026_round03_vocab_json.py）",
        "sections_in_data": [1, 2, 3, 4],
        "section1_passage_vocab": {"label": "第1問 語句（旅行サイト・夜市）", "count": counts.get(1, 0)},
        "section2_passage_vocab": {"label": "第2問 語句（在宅勤務）", "count": counts.get(2, 0)},
        "section3_passage_vocab": {"label": "第3問 語句（オープンキャンパス）", "count": counts.get(3, 0)},
        "section4_passage_vocab": {"label": "第4問 語句・本文（大気汚染エッセイ）", "count": n4p},
        "section4_questions_vocab": {"label": "第4問 設問語句", "count": n4q},
    }
    return {"meta": meta, "entries": entries}


def main():
    data = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({len(data['entries'])} entries)")


if __name__ == "__main__":
    main()
