import fitz

pdf_mondai = r"D:\Files\(Z会)共通テスト過去問\2021_第1日程_英語リーディング.pdf"
doc = fitz.open(pdf_mondai)

print("=== Section search ===")
for i in range(len(doc)):
    text = doc[i].get_text()
    if "第6問" in text or "第 6 問" in text or "A" in text:
        # just print first 200 chars to identify
        preview = text.replace('\n', ' ')[:200]
        if "第" in preview:
            print(f"Page {i+1}: {preview}")
