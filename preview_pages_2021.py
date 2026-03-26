import fitz
doc1 = fitz.open(r"D:\Files\(Z会)共通テスト過去問\2021_第1日程_英語リーディング.pdf")
doc2 = fitz.open(r"D:\Files\(Z会)共通テスト過去問\2021_第1日程_英語リーディング_解答.pdf")
print("=== Mondai ===")
for i in range(len(doc1)):
    print(f"Page {i+1}: {doc1[i].get_text()[:100].replace(chr(10), ' ')}")
print("\n=== Kaitou ===")
for i in range(len(doc2)):
    print(f"Page {i+1}: {doc2[i].get_text()[:100].replace(chr(10), ' ')}")
