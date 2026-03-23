---
description: ReadLens Pro — 共通テスト過去問（6AB型）の大問追加ワークフロー
---

# 共通テスト過去問（6AB型）大問追加ワークフロー

## 概要

共通テスト本試験（2024年度以前）は大問6個構成で、第6問がA/Bに分かれる「6AB型」。
駿台実戦問題集（大問8個型）とは以下の点が異なる：

| 項目 | 8個型（駿台） | 6AB型（過去問） |
|------|-----------|------------|
| 大問数 | 8 | 6（6Aと6B） |
| 合計点 | 100 | 100 |
| 第6問 | 独立した1問 | AとB（各12点） |
| `section_number` | 整数 1-8 | 整数 1-5 + 文字列 "6A", "6B" |

## フォルダ構成

```
g:\マイドライブ\ReadLens Pro\data\
  kakomon\
    {年度}\              例: 2024
      data.json           全大問データ
      images\             図版・イラスト
      audio\              音声MP3
```

## 前提パス

- **解析データ元**: `c:\Users\makoto\Documents\共通テスト英語リーディング問題解析\{年度}_本試験\`
- **問題PDF画像**: `同上\images\mondai_p{NN}.png`
- **解答PDF画像**: `同上\images\kaitou_p{NN}.png`
- **アプリデータ配置先**: `g:\マイドライブ\ReadLens Pro\data\kakomon\{年度}\`

## section_number の扱い

6AB型では `section_number` に以下の値を使用する：

| section_number | 対応する大問 | 配点 |
|----------------|---------|------|
| 1 | 第1問 | 10 |
| 2 | 第2問 | 20 |
| 3 | 第3問 | 15 |
| 4 | 第4問 | 16 |
| 5 | 第5問 | 15 |
| "6A" | 第6問A | 12 |
| "6B" | 第6問B | 12 |

> [!IMPORTANT]
> `section_number` は第6問のみ文字列（`"6A"`, `"6B"`）、他は整数。
> app.js / viewer.js / print.js での比較時に型に注意すること。

## exam_info の構造

```json
{
  "exam_info": {
    "title": "大学入学共通テスト 英語（リーディング）",
    "year": 2024,
    "round": "本試験",
    "subject": "英語（リーディング）",
    "time_limit_minutes": 80,
    "total_points": 100,
    "total_answer_numbers": 49,
    "format": "6AB",
    "section_list": [1, 2, 3, 4, 5, "6A", "6B"]
  }
}
```

> [!IMPORTANT]
> `format: "6AB"` と `section_list` を必ず含めること。
> app.js のカード描画で `section_list` を参照してカードを生成する。

## 🔴 テキスト生成の禁止と原文忠実性

> [!CAUTION]
> **日本語訳・解説文・設問訳・選択肢訳を自分で生成・要約・言い換えしない。**
> 必ず解答ページ画像（`kaitou_p{NN}.png`）から**原文をそのまま転記**すること。

### ❌ 生成禁止

| 項目 | ソース |
|------|--------|
| `explanation.ja` | 解答ページ画像の解説文 |
| `passages[].sentences[].ja` | 解答ページ画像の全訳 |
| `stem.ja` | 解答ページ画像の設問訳 |
| `choices[].ja` | 解答ページ画像の選択肢訳 |
| `situation.ja` | 解答ページ画像の場面設定訳 |

### ✅ 生成してよいもの

| 項目 | 説明 |
|------|------|
| `evidence_sentences` | 解説文中の言及から文IDをマッピング |
| `why_others_wrong[].ref_sentences` | 誤答理由テキスト中の言及から文IDをマッピング |

---

## ステップ1: 問題ページで構造を確認

1. `mondai_p{NN}.png` を `view_file` で表示
2. 以下を確認：
   - 段落構造（paragraphs vs sentences）
   - 枠線の有無
   - 図版・イラストの配置
   - セクション分け（A/B等）

## ステップ2: 解答ページで全訳・解説を読み取り

1. `kaitou_p{NN}.png` を `view_file` で表示
2. **原文をそのまま転記**：
   - 全訳 → `sentences[].ja` / `paragraphs[][].ja`
   - 場面設定訳 → `situation.ja`
   - 設問訳 → `stem.ja`
   - 選択肢訳 → `choices[].ja`
   - 解説 → `explanation.ja`
   - 語句・表現 → `vocabulary`

## ステップ3: 図版・イラストの処理

1. ユーザーが提供した画像を `data/kakomon/{年度}/images/` にコピー
2. `data.json` の該当パッセージに `image` フィールドを追加：
   ```json
   "image": {
     "src": "data/kakomon/{年度}/images/{name}.png",
     "alt": "説明",
     "float": "right"
   }
   ```

## ステップ4: data.json の作成

### 第1問の構造（大問1A + 大問1B を1つの section にまとめる）

```json
{
  "section_number": 1,
  "title": "第1問",
  "points": 10,
  "points_per_question": 2,
  "subsections": [
    {
      "label": "A",
      "situation": { "en": "...", "ja": "..." },
      "passages": [...],
      "questions": [問1, 問2]
    },
    {
      "label": "B",
      "situation": { "en": "...", "ja": "..." },
      "passages": [...],
      "questions": [問1, 問2, 問3]
    }
  ]
}
```

> [!WARNING]
> 第1問〜第5問は `subsections` でA/Bをまとめる（section_number は整数）。
> 第6問のみ `"6A"`, `"6B"` として別セクションに分割する。

### 第6問A/B の構造

```json
{
  "section_number": "6A",
  "title": "第6問 A",
  "points": 12,
  "situation": { "en": "...", "ja": "..." },
  "passages": [...],
  "notes": {...},
  "questions": [問1, 問2, 問3, 問4]
}
```

## ステップ5: 音声MP3の生成

// turbo-all
```powershell
python C:\Users\makoto\AppData\Local\Temp\gen_audio.py
```

- ボイス: `en-US-JennyNeural`
- `sentences`形式: `s{N}_{passage_id}.mp3`
- `paragraphs`形式: `s{N}_{passage_id}_p{M}.mp3`

## ステップ6: EXAM_REGISTRY に登録

### app.js

```javascript
{
  id: "kakomon_2024",
  publisher: "共通テスト",
  series: "過去問",
  year: 2024,
  round: "本試験",
  label: "共通テスト 2024年度 本試験",
  dataPath: "data/kakomon/2024/data.json",
  icon: "🏫"
}
```

### app.js のカード描画修正

`for (let num = 1; num <= 8; num++)` を以下に変更：

```javascript
const sectionList = data?.exam_info?.section_list || [1,2,3,4,5,6,7,8];
for (const num of sectionList) {
  const sec = sections.find(s => String(s.section_number) === String(num));
  // ...
}
```

### viewer.js / print.js

`EXAM_PATHS` に追加：
```javascript
kakomon_2024: "data/kakomon/2024/data.json"
```

## ステップ7: ビューアで動作確認

1. LP でカードが正しく表示されるか確認（6AB型は7カード）
2. 各大問のビューア動作確認
3. 印刷プレビュー確認

## 注意事項

> [!WARNING]
> - `section_number` の型混在（整数 vs 文字列）に注意
> - `subsections` をサポートするために viewer.js の `renderPassage()` と `renderQuestions()` の修正が必要になる可能性あり
> - 第1問〜第5問もA/B構成だが、subsections でまとめることでsection_number は整数のまま維持

### subsections 実装時の必須ルール

1. **問題番号のユニーク化**: A/B内の `question_id` は大問全体で一意にする
   - ❌ A:問1,問2 / B:問1,問2,問3（重複）
   - ✅ A:問1,問2 / B:問3,問4,問5（`answer_number` ベース）
   
2. **`no_divider` フラグ**: 1つのフライヤー/広告等として表示すべきpassage群には `"no_divider": true` を設定
   - 例: 1Aの International Night フライヤーの各passageは罫線不要
   - ツアー情報等は罫線で区切るのが原文に忠実

3. **画像の回り込み**: `image.float` を `"right"` or `"left"` で指定
   - CSS `.passage-img--right/--left` で `float` が適用される
   - 原文のイラスト配置を確認して忠実に設定すること

4. **エビデンス**: `evidence_sentences` は各subsection内のsentence IDを使用（`1a_s1`, `1b_s1` 等）
   - `question_id` がユニークであれば、エビデンスハイライトは自動的に正しくスコープされる
