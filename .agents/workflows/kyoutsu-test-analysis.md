---
description: 共通テスト英語リーディング問題PDFの解析・JSON化・解答追記の完全ワークフロー
---

# 共通テスト英語リーディング 解析ワークフロー

## 概要
出版社の共通テスト対策模試PDFから、問題・選択肢・解答・解説を構造化JSONに変換するワークフロー。
最終目標は共通テスト対策用のインタラクティブWebアプリ教材の開発。

---

## ★ 重要：プロジェクトの基本情報

### ディレクトリ構成
```
c:\Users\makoto\Documents\共通テスト英語リーディング問題解析\
├── [出版社名]\[年]\[第N回]\          ← 各模試のデータ
│   ├── data.json                     ← 問題・解答・解説の構造化データ
│   └── images\                       ← スクリーンショット画像
│       ├── mondai_pXX.png            ← 問題PDFの各ページ
│       └── kaitou_pXX.png            ← 解答PDFの各ページ
├── 第1回_問題.pdf                     ← 元のPDFファイル
└── 第1回_解答.pdf                     ← 元の解答PDFファイル
```

### 現在の進捗（駿台 2025 第1回）
- ✅ 問題PDF全ページスクリーンショット済み（p2-p38, 37枚）
- ✅ 解答PDF p1 スクリーンショット済み（1枚）
- ✅ 全8大問のデータ入力完了（解答番号1-46, 配点合計100点, 35問）
- ❌ 解答（answer）と解説（explanation）は未入力（全て null）
- ❌ 解答PDFの残りページ（p2以降）のスクリーンショット未撮影

---

## Phase 1: PDFを開く（★最重要★）

### ⚠️ PDFの開き方の注意事項
- PDFはブラウザで開く必要がある（`browser_subagent` を使用）
- ローカルファイルなので `file:///` プロトコルを使う
- **日本語パスはURLエンコードが必要**
- ブラウザがすでに開いている場合は、そのページを再利用する

### 手順

#### 1-1. 問題PDFを開く場合
```
URL: file:///C:/Users/makoto/Documents/%E5%85%B1%E9%80%9A%E3%83%86%E3%82%B9%E3%83%88%E8%8B%B1%E8%AA%9E%E3%83%AA%E3%83%BC%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E5%95%8F%E9%A1%8C%E8%A7%A3%E6%9E%90/%E7%AC%AC1%E5%9B%9E_%E5%95%8F%E9%A1%8C.pdf
```
→ これは `c:\Users\makoto\Documents\共通テスト英語リーディング問題解析\第1回_問題.pdf`

#### 1-2. 解答PDFを開く場合
```
URL: file:///C:/Users/makoto/Documents/%E5%85%B1%E9%80%9A%E3%83%86%E3%82%B9%E3%83%88%E8%8B%B1%E8%AA%9E%E3%83%AA%E3%83%BC%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E5%95%8F%E9%A1%8C%E8%A7%A3%E6%9E%90/%E7%AC%AC1%E5%9B%9E_%E8%A7%A3%E7%AD%94.pdf
```
→ これは `c:\Users\makoto\Documents\共通テスト英語リーディング問題解析\第1回_解答.pdf`

#### 1-3. ブラウザでPDFを開くタスクの書き方
```
browser_subagent:
  Task: "ブラウザで以下のURLを開いてください: [URL]
         ページが完全にロードされるまで待ってください。
         ロード完了後、現在のページ番号と全体のページ数を報告してください。"
```

#### 1-4. ページ移動の方法
PDFビューワーのページ番号入力フィールド（画面上部中央）をクリック → Ctrl+A → ページ番号を入力 → Enter

---

## Phase 2: スクリーンショット撮影

### 手順
1. PDFの対象ページに移動（Phase 1-4 の方法で）
2. 1秒待機してレンダリング完了を確認
3. `capture_browser_screenshot` でスクリーンショット撮影
   - 命名規則: `mondai_pXX` (問題) / `kaitou_pXX` (解答)
4. artifactディレクトリに保存される
5. **逐次** `images/` ディレクトリにコピー:
   ```powershell
   $src = "C:\Users\makoto\.gemini\antigravity\brain\[会話ID]"
   $dest = "[出版社]\[年]\[第N回]\images"
   Copy-Item "$src\kaitou_pXX_*.png" "$dest\kaitou_pXX.png" -Force
   ```

### ⚠️ 注意
- スクリーンショットは日本語パス名のせいでファイル名にタイムスタンプが付与される（例: `kaitou_p02_1774018235781.png`）
- コピー時にワイルドカード `kaitou_pXX_*.png` でマッチさせ、`kaitou_pXX.png` にリネームする
- **撮影したら必ずすぐにコピーする**（エラーで中断した場合のデータ保護）

---

## Phase 3: テキスト読み取りとJSON入力

### 3-1. スクリーンショットの確認
- `view_file` で撮影した画像を確認
- テキスト、選択肢、配点、解答番号を正確に読み取る

### 3-2. JSONデータ構造
各セクション（大問）の基本構造:
```json
{
  "section_number": 1,
  "title": "第1問",
  "points": 6,
  "pdf_pages": [2, 3],
  "passage_images": ["images/mondai_p02.png", "images/mondai_p03.png"],
  "situation": "場面設定テキスト",
  "passages": [
    {
      "title": "パッセージタイトル",
      "text": "本文テキスト"
    }
  ],
  "questions": [
    {
      "question_id": "問1",
      "answer_number": 1,
      "stem": "問題文 [1]",
      "choices": ["選択肢1", "選択肢2", "選択肢3", "選択肢4"],
      "answer": null,
      "explanation": null
    }
  ]
}
```

### 3-3. 特殊な問題タイプ
- **並び替え問題**: `"type": "ordering"`, `"answer_numbers": [12, 13]`, `"events": [...]`
- **複数解答**: `"answer_numbers": [22, 23]`, `"choices_22": [...]`, `"choices_23": [...]`
- **エッセイ添削**: `"teacher_comments": [...]`
- **ハンドアウト形式**: passagesに `"type": "handout"` を含むネスト構造
- **プレゼンスライド形式**: `"presentation_slides": {...}`

### 3-4. データの逐次保存
- **必ず大問ごとにdata.jsonを保存する**
- `replace_file_content` で末尾の `}  ]  }` を置換して新しいセクションを追加
- 保存後、pythonで `json.load()` してJSON妥当性を検証

---

## Phase 4: 解答・解説の追記（★次のタスク★）

### 4-1. 解答PDFのスクリーンショット
1. 解答PDF（`第1回_解答.pdf`）をブラウザで開く（Phase 1-2のURLを使用）
2. 各ページのスクリーンショットを撮影
   - 命名: `kaitou_p01.png`, `kaitou_p02.png`, ...
3. `images/` にコピー

### 4-2. 解答の入力
1. 解答PDFのスクリーンショットから正解番号を読み取る
2. `data.json` の各問題の `"answer": null` を正解に書き換える
   - 例: `"answer": 1` (選択肢①が正解の場合)
   - 並び替え: `"answer": [4, 1, 5, 3]`
   - 複数解答: `"answer": {"22": 5, "23": 3}`

### 4-3. 解説の入力
1. 解答PDFの解説ページのスクリーンショットを撮影
2. 解説画像のパスを `"explanation_image": "images/kaitou_pXX.png"` に設定
3. 必要に応じてテキストでの解説も `"explanation"` に入力

---

## Phase 5: 検証

### 検証スクリプト
```python
import json
path = r'[出版社]\[年]\[第N回]\data.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
print(f"Sections: {len(data['sections'])}")
total_pts = sum(s['points'] for s in data['sections'])
print(f"Total points: {total_pts}")
# 解答番号の連続性チェック
all_nums = []
for s in data['sections']:
    for q in s['questions']:
        if 'answer_number' in q:
            all_nums.append(q['answer_number'])
        if 'answer_numbers' in q:
            all_nums.extend(q['answer_numbers'])
all_nums.sort()
print(f"Answer numbers: {all_nums[0]}-{all_nums[-1]} ({len(all_nums)} total)")
# 未回答チェック
unanswered = sum(1 for s in data['sections'] for q in s['questions'] if q.get('answer') is None)
print(f"Unanswered: {unanswered}")
```

---

## Phase 6: 新しい模試の追加

### 6-1. ディレクトリ作成
```powershell
$base = "c:\Users\makoto\Documents\共通テスト英語リーディング問題解析"
$publisher = "駿台"  # or "河合塾", "Z会" etc.
$year = "2025"
$round = "第2回"
mkdir "$base\$publisher\$year\$round\images"
```

### 6-2. PDFの配置
- 問題PDF → ベースディレクトリに `第N回_問題.pdf` として配置
- 解答PDF → ベースディレクトリに `第N回_解答.pdf` として配置
- ※ すでにベースディレクトリにある場合はそのまま使用

### 6-3. URLエンコード
新しいPDFのURLを作成する際は日本語ファイル名をURLエンコードする:
```python
import urllib.parse
path = "共通テスト英語リーディング問題解析/第2回_問題.pdf"
encoded = urllib.parse.quote(path)
url = f"file:///C:/Users/makoto/Documents/{encoded}"
```

### 6-4. 初期JSON作成
```json
{
  "exam_info": {
    "title": "共通テスト英語（リーディング）",
    "publisher": "[出版社名]",
    "year": "[年]",
    "round": "[第N回]",
    "subject": "英語（リーディング）",
    "time_limit_minutes": 80,
    "total_answer_numbers": null,
    "source_pdf": {
      "mondai": "[第N回]_問題.pdf",
      "kaitou": "[第N回]_解答.pdf"
    }
  },
  "sections": []
}
```

### 6-5. Phase 2〜5 を繰り返す

---

## 参考: 駿台2025第1回の構成

| 大問 | 配点 | 解答番号 | PDFページ | トピック |
|------|------|----------|-----------|---------|
| 第1問 | 6 | 1-3 | 2-5 | School Trip / Band T-shirt |
| 第2問 | 10 | 4-8 | 4-6 | Bank Account / Soccer Cleat |
| 第3問 | 9 | 9-14 | 8-10 | Volunteer Day Report |
| 第4問 | 12 | 15-18 | 12-14 | Sleep Essay (添削) |
| 第5問 | 16 | 19-24 | 16-20 | Debate Club |
| 第6問 | 18 | 25-31 | 22-27 | Voting Age Essay |
| 第7問 | 15 | 32-40 | 28-33 | Sam's School (物語) |
| 第8問 | 14 | 41-46 | 34-38 | Dietary Fiber |
| **合計** | **100** | **46** | **38p** | |
