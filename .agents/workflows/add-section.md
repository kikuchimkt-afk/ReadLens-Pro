---
description: ReadLens Pro — 共通テスト英語問題DBに新しい大問を追加するワークフロー
---

# 大問追加ワークフロー（ReadLens Pro）

## プロジェクト概要

- **アプリ名**: ReadLens Pro
- **コピーライト**: © 2025 ECC藍住・北島中央・大学前
- **デプロイ先**: Vercel（Git連携）
- **ローカル開発サーバー**: `npx -y http-server "g:\マイドライブ\ReadLens Pro" -p 8091 --cors -c-1`
- **サーバー起動バッチ**: `g:\マイドライブ\ReadLens Pro\start-server.bat`

## ファイル構成

```
g:\マイドライブ\ReadLens Pro\
├── index.html          # LP（ランディングページ）
├── app.js              # LPのカード一覧描画
├── style.css           # LP用CSS（グラスモーフィズム＋パステルエンジ色）
├── viewer.html         # 問題ビューア
├── viewer.js           # ビューアのロジック
├── viewer.css          # ビューア用CSS（エンジ色ヘッダー）
├── print.html          # 印刷プレビューページ
├── print.js            # 印刷用レンダリング
├── print.css           # 印刷用CSS
├── images/
│   └── bg-hero.png     # LP背景画像（野花の草原）
└── data/{publisher}/{year}/round{NN}/
    ├── data.json       # 問題データ
    ├── audio/          # MP3音声ファイル
    └── images/         # 問題中の図版画像
```

## 前提パス

- **解析データ元**: `c:\Users\makoto\Documents\共通テスト英語リーディング問題解析\{出版社}\{年}\{回}\`
- **問題PDF画像**: `同上\images\mondai_p{NN}.png`
- **解答PDF画像**: `同上\images\kaitou_p{NN}.png`
- **アプリデータ配置先**: `g:\マイドライブ\ReadLens Pro\data\{出版社}\{年}\round{NN}\`

---

## 現在の進捗

### 駿台 2025 第1回
| 大問 | 状態 | 設問タイプ | 特殊レイアウト |
|------|------|----------|------------|
| 第1問〜第6問 | ✅ 完了 | 通常4択 / ordering / 複数解答 | sentences / paragraphs / essay-table / authors |
| 第7問〜第8問 | ❌ 未着手 | — | — |

### 駿台 2025 第2回
| 大問 | 状態 | 設問タイプ | 特殊レイアウト |
|------|------|----------|------------|
| 第1問〜第8問 | ✅ 完了 | — | — |

### 駿台 2025 第3回
| 大問 | 状態 | 設問タイプ | 特殊レイアウト |
|------|------|----------|------------|
| 第1問〜第4問 | ✅ 完了 | 通常4択 / ordering / essay-table | — |
| 第5問〜第8問 | ❌ 未着手 | — | — |

---

## 🔴 最優先: テキスト生成の禁止と原文忠実性

> [!CAUTION]
> **日本語訳・解説文・設問訳・選択肢訳・図表説明を自分で生成・要約・言い換えしない。**
> 必ず既存の読み取りデータまたは解答ページ画像から**原文をそのまま転記**すること。
> AIが推論でテキストを生成すると、原文にない情報が混入したり意味が変わり、誤った解説につながる。

### ❌ 生成禁止（原文転記のみ）

| 項目 | ソース | 禁止事項 |
|------|--------|----------|
| `explanation.ja` | ソースJSON `explanation` | 要約・言い換え・短縮禁止 |
| `passages[].ja` | ソースJSON `translations` | AI翻訳禁止 |
| `stem.ja` | 解答ページ画像 `answer_page_*.png` | AI翻訳禁止 |
| `choices[].ja` | 解答ページ画像 `answer_page_*.png` | AI翻訳禁止 |
| `lead_text.ja` | ソースJSON `theme_translation` | AI翻訳禁止 |
| `why_others_wrong[].reason` | ソースJSON `explanation` から切り出し | AI生成禁止 |
| 図表・画像 | ユーザー提供スクリーンショットのみ | AI生成禁止 |

### ✅ 生成してよいもの（唯一）

| 項目 | 説明 |
|------|------|
| `evidence_sentences` | 解説文中の言及（「第N文(...)」等）から文IDをマッピング |
| `why_others_wrong[].ref_sentences` | 誤答理由テキスト中の言及から文IDをマッピング |

### 既存データの場所

```
g:\マイドライブ\ReadLens Pro\別作成データ類\data\sundai\2025\round{NN}\section{N}.json
```

（旧パス `C:\Users\makoto\Documents\共通テスト英語リーディング問題解析\別作成データ類\` にもコピーあり）

### 各section{N}.json に含まれるデータ

| フィールド | 内容 | data.json への転記先 |
|-----------|------|---------------------|
| `passage` | 英語本文（段落単位） | `passages[].sentences/paragraphs[].en` |
| `translations` | 日本語全訳（解答冊子の全訳そのまま） | `passages[].sentences/paragraphs[].ja` |
| `theme_translation` | リード文の日本語訳 | `lead_text.ja` |
| `questions[].question_text` | 設問の英文 | `questions[].stem.en` |
| `questions[].choices` | 選択肢の英文 | `questions[].choices[].en` |
| `questions[].answer` | 正解番号 | `questions[].answer` |
| `questions[].explanation` | 設問解説（解答冊子の解説そのまま） | `questions[].explanation.ja` |

### 転記手順

1. **最初に**既存データファイルを `view_file` で読み込む
2. 英語本文 → `passage` フィールドからそのまま転記
3. 日本語訳 → `translations` フィールドからそのまま転記（AI翻訳禁止）
4. リード文訳 → `theme_translation` フィールドからそのまま転記
5. 設問の解説 → `explanation` フィールドからそのまま転記（一字一句、句読点まで忠実に）
6. 設問・選択肢の日本語訳 → 解答画像（`answer_page_*.png`）から `view_file` で読み取り転記
7. `why_others_wrong` → ソース `explanation` テキスト中の不正解選択肢に関する記述を**原文のまま切り出し**て構造化。ソースに個別の誤答解説がない場合は作成しない
8. `evidence_sentences` → 解説文中の「第N文(...)」「○○のコメントに…」から文IDをマッピング

> [!WARNING]
> - evidence_sentences は解説テキストから論理的に導出する。推測で追加しない
> - `why_others_wrong` の `reason` は**ソース解説原文からの切り出し**のみ。AIが独自に誤答理由を書かない
> - ソースに個別の誤答解説がない場合、`why_others_wrong` は空でよい（無理に作成しない）

---

## ステップ0: ソースJSON原文忠実性の事前検証

> [!CAUTION]
> **実装を開始する前に、必ずソースJSONの内容が解答冊子の原文と一致しているか確認すること。**
> ソースJSON自体が別のAIセッションで作成されている場合、誤訳や要約が含まれている可能性がある。

### 検証手順

1. ソースJSON（`section{N}.json`）を `view_file` で開く
2. 解答ページ画像（`answer_page_*.png`）を `view_file` で開く
3. 以下を照合する:
   - `explanation` フィールドの内容が解答ページ画像の解説文と一致するか
   - `translations` が解答ページ画像の全訳部分と一致するか
   - `theme_translation` が解答ページ画像のリード文訳と一致するか
4. **不一致がある場合**: 解答ページ画像（PNG）を正とし、ソースJSONの内容ではなくPNG画像の内容を転記する
5. 不一致箇所をユーザーに報告する

---

## ステップ0.5: 問題PNGでレイアウトを正確に確認する

> [!CAUTION]
> **レイアウトを勝手に作成しない。** 必ず問題PDFのスクリーンショット（`mondai_p{NN}.png`）を `view_file` で表示し、原文の以下の要素を正確に把握すること。

1. **段落構造**: 段落の区切り位置を正確に確認し、`paragraphs`（配列の配列）で再現する
2. **枠線**: 本文が枠線で囲まれているか確認（大問ごとに異なる場合がある）
3. **図版・表・グラフの配置**: 右寄せ・左寄せ・センタリング等の位置を確認
4. **セクション分け**: 水平線で区切られているか、複数の独立した文章があるか
5. **タイトル・サブタイトル**: ヘッダー部分の構成を確認
6. **特殊レイアウト**: エッセイ+コメント欄の2列構成など（大問4参照）

### データ構造の使い分け

| 構造 | 用途 | 例 |
|------|------|-----|
| `sentences` | 段落分けが不要な場合（1段落の文章、ツアー説明など） | 大問1の各ツアー |
| `paragraphs` | 複数段落に分かれた長文記事 | 大問2の銀行口座記事 |

```json
// sentences: 全文を1つの段落として表示
"sentences": [{ "id": "s1", "en": "...", "ja": "..." }, ...]

// paragraphs: 段落ごとに分割して表示（段落間にスペース、訳も段落・文ごとに改行）
"paragraphs": [
  [{ "id": "s1", "en": "...", "ja": "..." }],
  [{ "id": "s2", ... }, { "id": "s3", ... }],
  ...
]
```

## ステップ1: 解析データの確認

1. 対象大問の解析済み `data.json` を確認する
2. 必要なフィールドが揃っているか確認:
   - `sections[].passages[]` — 本文のセンテンス（en/ja）
   - `sections[].questions[]` — 設問・選択肢・解説・根拠文ID
   - `sections[].situation` — 場面設定（あれば）

## ステップ2: 図版・画像の処理

> [!IMPORTANT]
> **AI生成画像は使用禁止。** ユーザーが貼ったスクリーンショットのみを使用する。

1. 対象大問に図・表・グラフ・イラストがあるか確認
2. **ある場合**: ユーザーにスクリーンショットの提供を依頼
3. ユーザーがチャットに画像を貼り付ける
4. `uploaded_media_*.png` として保存されるので、以下にコピーする:
   ```
   g:\マイドライブ\ReadLens Pro\data\{出版社}\{年}\round{NN}\images\{descriptive_name}.png
   ```
5. `data.json` の該当パッセージに `image` フィールドを追加:
   ```json
   "image": {
     "src": "data/{出版社}/{年}/round{NN}/images/{descriptive_name}.png",
     "alt": "説明テキスト",
     "float": "right"
   }
   ```
6. **再現困難な図の場合**: ユーザーに事前に知らせ、スクショ提供を依頼

## ステップ3: 音声MP3の生成

> [!IMPORTANT]
> **パラグラフごとにMP3を生成する。** `sentences`形式のpassageは1ファイル、`paragraphs`形式は段落ごとに1ファイル。

1. `edge-tts`（Python）を使用してMP3を生成する
2. ボイス: `en-US-JennyNeural`（自然な女性音声）
3. 命名規則:
   - `sentences`形式: `s{section_number}_{passage_id}.mp3`
   - `paragraphs`形式: `s{section_number}_{passage_id}_p{N}.mp3`
4. 保存先: `g:\マイドライブ\ReadLens Pro\data\{出版社}\{年}\round{NN}\audio\`

// turbo
```powershell
python C:\Users\makoto\AppData\Local\Temp\gen_audio.py
```

## ステップ4: data.json をアプリ用ディレクトリにコピー

// turbo
```powershell
Copy-Item "c:\Users\makoto\Documents\共通テスト英語リーディング問題解析\{出版社}\{年}\{回}\data.json" "g:\マイドライブ\ReadLens Pro\data\{出版社}\{年}\round{NN}\data.json" -Force
```

## ステップ5: EXAM_REGISTRY に登録（新しい回の場合のみ）

1. `app.js` の `EXAM_REGISTRY` 配列に新エントリを追加
2. `viewer.js` の `EXAM_PATHS` にも同じパスを追加
3. `print.js` の `EXAM_PATHS` にも同じパスを追加

## ステップ6: ビューアで動作確認

1. ローカルサーバーが起動中か確認（ポート8091、`start-server.bat`で起動）
2. ブラウザで以下を確認:
   - LP (`http://127.0.0.1:8091/index.html`) — カードが表示されるか
   - ビューア (`http://127.0.0.1:8091/viewer.html?exam={id}&section={N}`) — 以下を検証:
     - [ ] 左ペイン: 本文が **原文PNG準拠のレイアウト** で表示される（段落・枠・配置）
     - [ ] 左ペイン: 図版が正しい位置に表示される（浮動配置）
     - [ ] 右ペイン: 設問・選択肢が表示される
     - [ ] 選択肢クリック → 正答/不正答フィードバック
     - [ ] 「解」ボタン → 正解選択肢ハイライト＋全解説＋全根拠表示
     - [ ] 根拠文ハイライト（色分け）
     - [ ] 根拠文クリック → 和訳ポップアップ表示
     - [ ] ヒントボタン動作（設問パネル右上）
     - [ ] 「訳」ボタン → 和訳表示（段落ごと・文ごと改行）
     - [ ] 「根」ボタン → 全根拠一括ハイライト
     - [ ] リセットボタン → 全状態クリア
     - [ ] 全画面ボタン → フルスクリーン切替
   - 印刷 (`http://127.0.0.1:8091/print.html?exam={id}&mode=passage&section={N}`) — 問題印刷プレビュー
   - 印刷 (`http://127.0.0.1:8091/print.html?exam={id}&mode=questions&section={N}`) — 設問印刷プレビュー
   - 印刷 (`http://127.0.0.1:8091/print.html?exam={id}&mode=all`) — 全問題一括印刷プレビュー

---

## data.json のパッセージ仕様

| フィールド | 型 | 説明 |
|-----------|-----|------|
| `sentences` | array | フラットなセンテンス配列（1段落表示） |
| `paragraphs` | array of arrays | 段落ごとのセンテンス配列（段落分け表示） |
| `image.src` | string | アプリルートからの相対パス |
| `image.alt` | string | 代替テキスト |
| `image.float` | `"right"` / `"left"` | テキスト回り込みの方向 |
| `margin_comments` | array | エッセイ添削用のコメント（大問4型） |
| `teacher_comment` | object | 教師の総合コメント（`en`/`ja`） |
| `comment_marker` | string | センテンスに付与するコメントマーカー（`"(1)"`等） |

## 設問タイプ別の対応

| `question_type` | 用途 | UIの挙動 |
|----------------|---------|----------|
| (未指定/通常) | 4択問題 | 選択肢クリック→即座に正誤判定 |
| `"ordering"` | 整序問題（完答） | 空欄スロットに順番にクリックで埋めていく。全部埋め → 正誤判定。`answer_sequence` (数値配列) が必要 |

### ordering型 data.json 例
```json
{
  "question_type": "ordering",
  "answer": "④→①→③→②",
  "answer_sequence": [4, 1, 3, 2],
  "choices": [
    { "label": "①", "en": "...", "ja": "..." },
    ...
  ]
}
```

### 大問4型（エッセイ添削）data.json 例
```json
{
  "title": { "en": "How to Improve Your Sleep" },
  "paragraphs": [
    [
      { "id": "s1", "en": "...", "ja": "...", "comment_marker": "(1)" },
      ...
    ]
  ],
  "margin_comments": [
    { "marker": "(1)", "en": "You have used the wrong connecting expression here.", "ja": "接続表現が間違っています。" }
  ],
  "teacher_comment": {
    "en": "Good effort! Please revise the marked parts.",
    "ja": "よく書けています。マークした部分を修正してください。"
  }
}
```

### 大問6型（複数意見統合＋Step型構成）

共通テスト最新設問パターン（大問8個型）で出題される形式。3つのStepと情報源（Source A/B）で構成される。

#### 全体構造（passageの順序）

```
passages[0]: step1_sources  — Step1: 複数著者の意見（authors形式）
passages[1]: step2_position — Step2: 立場を決める
passages[2]: step3_outline  — Step3: エッセイのアウトライン
passages[3]: source_a       — 情報源A（テキスト、paragraphs形式）
passages[4]: source_b       — 情報源B（テキスト＋棒グラフ画像）
```

#### 設問と対応するStep

| 設問 | 対応する本文 | 誘導バナーの位置 |
|------|------------|----------------|
| 問1, 問2 | Step1（著者の意見） | Step1の後 |
| 問3 | Step2（立場を決める） | Step2の後 |
| 問4, 問5 | Source A, Source B | Source Bの後 |

#### 誘導バナー

`viewer.js` の `renderPassage()` 内で、各Stepの後に自動挿入される。
バナーをクリックすると右パネルの該当設問へスクロール＋フラッシュハイライト。

```html
<div class="step-nav-cue" data-target-qids="問1,問2">
  <span class="step-nav-icon">📝</span>
  <span class="step-nav-text">ここまで読んだら <strong>問1</strong> と <strong>問2</strong> を解答 →</span>
</div>
```

対応するCSS: `.step-nav-cue` in `viewer.css`
対応するJS: `setupStepNavCues()` in `viewer.js`

#### passage[0]: authors形式（Step1）

```json
{
  "id": "step1_sources",
  "title": { "en": "[Step 1] Read various sources", "ja": "[Step 1] さまざまな情報源を読む" },
  "authors": [
    {
      "id": "author_a",
      "label": { "en": "Author A (High school student)", "ja": "著者A（高校生）" },
      "sentences": [
        { "id": "aa_s1", "en": "...", "ja": "..." },
        ...
      ]
    },
    ...
  ]
}
```

- 音声ファイル: `s6_{author.id}.mp3`（例: `s6_author_a.mp3`）
- レンダラー: `passage.authors` ブロック in `renderPassage()`
- CSS: `.author-block`, `.author-label`

#### passage[1]: Step2（立場を決める）

```json
{
  "id": "step2_position",
  "title": { "en": "[Step 2] Take a position", "ja": "[Step 2] 立場を決める" },
  "is_step2": true,
  "position": {
    "en": "The voting age should not be lowered to 16.",
    "ja": "選挙年齢は16歳まで下げられるべきではない。"
  },
  "position_details": [
    { "en": "Authors [27] and [28] support your position.", "ja": "..." },
    { "en": "The main argument of the two authors: [29].", "ja": "..." }
  ]
}
```

- `[27]` 等は `answer-slot` として描画される
- レンダラー: `passage.is_step2` ブロック

#### passage[2]: Step3（アウトライン）

```json
{
  "id": "step3_outline",
  "title": { "en": "[Step 3] Create an outline using sources A and B", "ja": "..." },
  "is_step3": true,
  "outline": {
    "essay_title": { "en": "Should the Voting Age Be Lowered to 16?", "ja": "..." },
    "introduction": { "en": "...", "ja": "..." },
    "body": [
      { "en": "Reason 1: [30]", "ja": "..." },
      { "en": "Reason 2: ...", "ja": "..." },
      { "en": "Reason 3: [31]", "ja": "..." }
    ],
    "conclusion": { "en": "...", "ja": "..." }
  }
}
```

#### passage[3]: Source A（テキスト情報源）

```json
{
  "id": "source_a",
  "title": { "en": "Source A", "ja": "情報源A" },
  "paragraphs": [
    [
      { "id": "sa_s1", "en": "...", "ja": "..." },
      ...
    ]
  ]
}
```

- 音声ファイル: `s6_source_a_p1.mp3`（paragraphs形式の命名規則に従う）

#### passage[4]: Source B（テキスト＋グラフ画像）

```json
{
  "id": "source_b",
  "title": { "en": "Source B", "ja": "情報源B" },
  "sentences": [
    { "id": "sb_s1", "en": "...", "ja": "..." },
    ...
  ],
  "chart_image": {
    "src": "data/{pub}/{year}/round{NN}/images/s6_source_b_chart.png",
    "alt": "Support Voting Rights for 16- & 17-Year-Olds (By Age)"
  },
  "is_source_with_chart": true
}
```

- 音声ファイル: `s6_source_b.mp3`（sentences形式の命名規則に従う）
- グラフ画像: ユーザーのスクリーンショットを使用（AI生成禁止）
- レンダラー: `passage.is_source_with_chart` ブロック

#### 設問タイプ: 複数解答＋順不同スロット

問3のように複数の空欄に答える設問で、一部のスロットが順不同の場合：

```json
{
  "question_id": "問3",
  "question_text": {
    "en": "Choose the best options to complete [27], [28], and [29].",
    "ja": "..."
  },
  "answer_numbers": [27, 28, 29],
  "unordered_slots": [27, 28],
  "choices_27": [
    { "label": "①", "en": "A", "ja": "A", "is_correct": true },
    ...
  ],
  "choices_28": [ ... ],
  "choices_29": [ ... ],
  "answer": { "27": "①", "28": "④", "29": "④" },
  "answer_note": "[27]と[28]は順不同。正解は①と④の組み合わせ。",
  "explanation": {
    "ja": "正解は...",
    "evidence_sentences": ["aa_s2", "ad_s3"]
  }
}
```

> [!IMPORTANT]
> - `unordered_slots`: 順不同のスロット番号の配列。判定時にセットとして比較する
> - `answer_note`: 解説表示時に正解テキストの末尾に括弧付きで表示される
> - 通常の4択問題は `stem` ではなく `question_text`（`en`/`ja`）でも動作する（`viewer.js` は `q.stem || q.question_text` でフォールバック）

#### 設問タイプ: 通常4択（answer未設定の場合）

`answer` フィールドがなくても `choices` の `is_correct` から正解を導出する：

```json
{
  "question_id": "問1",
  "question_text": { "en": "Both Authors B and E mention that [25].", "ja": "..." },
  "answer_number": 25,
  "choices": [
    { "label": "①", "en": "...", "ja": "...", "is_correct": false },
    { "label": "④", "en": "...", "ja": "...", "is_correct": true }
  ],
  "explanation": {
    "ja": "正解は④。...",
    "evidence_sentences": ["ab_s4", "ae_s4"]
  }
}
```

## 印刷機能

LP（トップページ）から操作:
- **各カード内**: 📄問題 / 📝設問 の印刷リンク
- **タイトル横**: 🖨 全問題印刷 ボタン

| モード | URLパラメータ | 動作 |
|--------|-------------|------|
| 問題 | `?mode=passage&section=N` | 大問Nの本文のみ印刷 |
| 設問 | `?mode=questions&section=N` | 大問Nの設問のみ印刷 |
| 全問題 | `?mode=all` | 大問1問題→設問→大問2問題→設問…の順 |

各セクション: `page-break-after: always` で自動改ページ

## デザイン仕様

### LP（index.html + style.css）
- **背景**: `images/bg-hero.png`（野花の草原、アウトフォーカス）固定表示
- **ヘッダー**: 半透明エンジ色グラデーション + backdrop-filter blur
- **カード/パネル**: グラスモーフィズム（すりガラス透明感）
- **カラーパレット**: パステルエンジ色（`#9e4a5b`）基調、差し色ティール（`#4a9e8e`）・ラベンダー（`#8b7ab8`）

### ビューア（viewer.html + viewer.css）
- **ヘッダー**: エンジ色グラデーション（`#7e2e40` → `#9e4a5b` → `#b46478`）
- **ボタン**: 白文字 + 半透明白背景、active時は白背景+エンジ文字

## 画像の保存手順

ユーザーがチャットに画像を貼ると `media__*.png` として以下に保存される：
```
C:\Users\makoto\.gemini\antigravity\brain\{会話ID}\media__*.png
```

最新のファイルを特定するには：
```powershell
Get-ChildItem "C:\Users\makoto\.gemini\antigravity\brain\{会話ID}" -Filter "media__*" | Sort-Object LastWriteTime -Descending | Select-Object -First 3
```

## 注意事項（バグ防止）

> [!WARNING]
> - **イベントリスナーの重複禁止**: `renderQuestions()` と `setupControls()` で同じ要素にリスナーを二重登録しない。デリゲート方式（`setupControls`内）を優先する
> - **CSSの欠落チェック**: 新しいHTML要素/クラスを追加したら、対応するCSSが存在するか必ず確認
> - **リセットの網羅**: 新UI要素を追加したらリセットハンドラ（`btnReset.addEventListener`内）にもクリア処理を追加すること
> - **CSS変数の整合性**: style.cssとviewer.cssで異なるCSS変数を使用している。style.cssの変数をviewer.cssで参照しないこと（viewer.cssはハードコード値を使用）
> - **HTMLネスト禁止**: `<a>`タグの中に`<a>`タグをネストしない。カードは`<div>` + `onclick`で実装
> - **EXAM_PATHSの同期**: `app.js`, `viewer.js`, `print.js` の3ファイルでパスを同期すること
