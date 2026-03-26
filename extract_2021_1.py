import fitz
import os
import sys

pdf_mondai = r"D:\Files\(Z会)共通テスト過去問\2021_第1日程_英語リーディング.pdf"
pdf_kaitou = r"D:\Files\(Z会)共通テスト過去問\2021_第1日程_英語リーディング_解答.pdf"
out_dir = r"g:\マイドライブ\ReadLens Pro\data\kakomon\2021_1\images"

def extract_pdf(pdf_path, prefix):
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return
    
    print(f"Opening {pdf_path}")
    doc = fitz.open(pdf_path)
    for i in range(len(doc)):
        page = doc.load_page(i)
        pix = page.get_pixmap(dpi=300)
        out_path = os.path.join(out_dir, f"{prefix}_p{i+1}.png")
        pix.save(out_path)
        print(f"Saved {out_path}")

os.makedirs(out_dir, exist_ok=True)
extract_pdf(pdf_mondai, "mondai")
extract_pdf(pdf_kaitou, "kaitou")
print("Extraction complete!")
