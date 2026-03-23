---
description: ReadLens Pro — 大問データの包括的検証ワークフロー（エビデンス・レイアウト・印刷）
---

# 包括的検証ワークフロー

大問をdata.jsonに追加した後、以下の6項目を検証する。

## 前提
- ローカルサーバーが http://127.0.0.1:8091 で起動していること
- data.jsonがアプリ側 (`g:\マイドライブ\ReadLens Pro\data\sundai\2025\roundXX\data.json`) にコピー済みであること

---

## 1. データ整合性チェック（Pythonスクリプト）

以下を一括で検証するスクリプトを実行する:

### 1-1. evidence_sentences の検証
- 全設問の `explanation.evidence_sentences` が実在する文IDを参照しているか
- 空のevidence_sentencesがないか（根拠がある設問で）

### 1-2. why_others_wrong の検証
- `explanation.why_others_wrong` の `reason` がソースJSONの `explanation` テキスト内に存在するか（AI生成でないことの確認）
- `ref_sentences` が実在する文IDを参照しているか
- ソース解説に個別の誤答解説がない場合は空でよい（無理に作成しない）

### 1-3. 原文忠実性の検証
- 全設問の `explanation.ja` がソースJSONの `explanation` と完全一致するか
- `lead_text.ja` がソースJSONの `theme_translation` と一致するか
- `stem.ja` と `choices[].ja` が解答ページ画像と一致するか
- AIが要約・言い換えしたテキストが混入していないか

### 1-4. 解答構造の検証
- `question_type: "ordering"` の設問に `answer_sequence` があるか
- `answer_numbers` のある設問に対応する `choices_XX` があるか
- 単一解答設問に `answer` フィールドがあるか

```python
# 検証スクリプトの実行例
# python C:\Users\makoto\AppData\Local\Temp\verify_all.py
```

---

## 2. ビューア表示確認（ブラウザ）

各大問のviewerページを開いて確認:
```
http://127.0.0.1:8091/viewer.html?exam=sundai_2025_XX&section=N
```

### 2-1. レイアウト忠実性
確認ポイント（大問タイプ別）:
- **大問4（エッセイ添削型）**: コメント付きテーブル表示、Teacher's Comment
- **大問5（2記事比較型）**: 2つの記事表示、graph_image（段落後）
- **大問6（複数意見統合型）**: 著者ブロック5人、Source A/B、chart_image
- **大問7（物語文読解）**: 物語段落、Notes（story_outline、slots）
- **大問8（プレゼン型）**: 段落表示、配点表示

### 2-2. 配点表示
- `points_per_question` が設定されている場合: 「配点 XX点（各Y点×Z問）」
- 未設定の場合: 「配点 XX点（Z問）」（undefinedが出ないこと）

---

## 3. 整序問題の検証（大問7 問3等）

- 並べ替えUI（ドラッグ可能なスロット）が表示されること
- `answer_sequence` の内容が正しいこと
- 「解」ボタン押下で正解シーケンスが表示されること

---

## 4. 順不同正解の検証

複数スロット型の設問が正しく動作するか確認:
- `answer_numbers` + `choices_XX` 形式: [27][28][29], [38][39], [42][43] 等
- 各スロットに独立した選択肢セットが表示されること

---

## 5. 解説表示の検証

「解」ボタンを押して確認:
- **エビデンスハイライト**: 左ペインの本文に色分けハイライトが表示されること
- **正解表示**: 正答選択肢にマークが付くこと
- **解説テキスト**: `explanation.ja` が表示されること
- **他選択肢の解説**: 「他の選択肢の解説」アコーディオンを開いて、各誤答の理由が表示されること

---

## 6. 印刷レイアウト検証

ヘッダーの📄（問題印刷）と📝（設問印刷）ボタンを押して print.html の表示を確認:

### 6-1. 問題印刷
- 本文のレイアウトがViewer表示と一致すること
- **画像の表示**: graph_image / chart_image が印刷プレビューでも表示されること
- エッセイのコメント付きテーブルが正常に表示されること
- Notes / Story outlineのセクションが正しく表示されること

### 6-2. 設問印刷
- 各設問と選択肢が整理されたリストで表示されること
- answer_numbersの複数スロット型も正しく表示されること
- answer-slotのプレースホルダー（[32]等）が正しく表示されること

---

## よくある問題と修正パターン

| 問題 | 原因 | 修正方法 |
|------|------|----------|
| evidence not found | 文IDのtypo | data.jsonの文IDを確認・修正 |
| `why_others_wrong` の `reason` がソース解説原文の切り出しでない（AI生成） | ソース解説からの切り出し忘れ | ソース`explanation`から原文を切り出して再構築 |
| explanation.jaが不一致 | AIが要約・言い換えした | ソースJSONのexplanationをそのまま転記 |
| 「各undefined点」 | points_per_question未定義 | 値を設定するかviewer.jsでnullチェック |
| 印刷でグラフ欠落 | print.jsにgraph_image未対応 | print.jsの段落ループにgraph_image挿入処理追加 |
| notes表示でクラッシュ | story_outline.endがnull | viewer.js/print.jsにnullチェック追加 |
| 読み込み中で停止 | JSONフィールド名エラーやnull参照 | ブラウザコンソールでエラー確認 |
