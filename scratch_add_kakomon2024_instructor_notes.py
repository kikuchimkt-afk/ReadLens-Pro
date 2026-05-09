import json
from pathlib import Path

DATA_PATH = Path("c:/Users/user/Documents/GitHub/ReadLens-Pro/data/kakomon/2024/data.json")


def build_note(question):
    ex = question.get("explanation", {})
    evidence = ex.get("evidence_sentences", [])
    evidence_text = "・".join(evidence) if evidence else "本文該当箇所"
    answer = question.get("answer")
    stem_ja = question.get("stem", {}).get("ja", "")
    stem_en = question.get("stem", {}).get("en", "").lower()
    has_multi = bool(question.get("answer_numbers") or question.get("unordered_slots"))
    has_figure = "figure_image" in question or "choice_grid_image" in question

    if has_multi:
        intro = "複数空所（順不同）型です。空所ごとの条件を分けて本文根拠に対応づけると、安定して得点できます。"
        p4 = "順不同でも、各空所で文法・意味のつながりが自然かを最後に確認する。"
    elif has_figure:
        intro = "図と本文の対応を問う問題です。図中ラベル・位置関係と本文語句を1つずつ照合しましょう。"
        p4 = "図だけで判断せず、本文根拠文と一致する選択肢を最終的に選ぶ。"
    elif "infer" in stem_en or "推察" in stem_ja:
        intro = "推察問題です。本文の事実に筆者の語気（評価語）を重ねて、言える範囲を見極めるのがコツです。"
        p4 = "本文にない背景知識を足さず、本文内で支持できる結論だけを選ぶ。"
    elif "最も適切" in stem_ja or "最適" in stem_ja:
        intro = "要点把握問題です。設問語と同義の本文表現を先に特定すると判断がぶれません。"
        p4 = "迷ったら、断定が強すぎる選択肢や本文にない比較表現を優先的に除外する。"
    else:
        intro = "条件照合問題です。先に本文根拠を固定してから選択肢比較に進むと精度が上がります。"
        p4 = "数量・比較・主語の一致を確認し、部分一致の選択肢を避ける。"

    return {
        "ja": intro,
        "points": [
            f"まず {evidence_text} を確認し、設問が問う条件（対象・理由・結果）を短く整理してから選択肢を読む。",
            f"正解は {answer}。本文の中心情報との一致が取れているため、根拠一致で選べる。",
            "誤答は、本文語句を含んでいても範囲の拡大・因果の逆転・断定の強化が起きていないかを確認する。",
            p4,
        ],
    }


def iter_questions(section):
    if "subsections" in section:
        for sub in section.get("subsections", []):
            for q in sub.get("questions", []):
                yield q
    else:
        for q in section.get("questions", []):
            yield q


def main():
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    updated = 0

    for sec in data.get("sections", []):
        for q in iter_questions(sec):
            ex = q.get("explanation")
            if isinstance(ex, dict) and "instructor_note" not in ex:
                ex["instructor_note"] = build_note(q)
                updated += 1

    DATA_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"updated={updated}")


if __name__ == "__main__":
    main()
