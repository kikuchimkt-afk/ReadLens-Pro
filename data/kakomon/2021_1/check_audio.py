"""
data.jsonから各セクションの必要な音声ファイル一覧を出力するスクリプト
"""
import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

existing_files = [
    "s6A_article_p1.mp3", "s6A_article_p2.mp3", "s6A_article_p3.mp3",
    "s6A_article_p4.mp3", "s6A_article_p5.mp3", "s6A_article_p6.mp3",
    "s6A_article_p7.mp3", "s6A_notes_p1.mp3", "s6A_notes_p2.mp3",
    "s6A_notes_p3.mp3", "s6A_notes_p4.mp3", "s6A_notes_p5.mp3",
    "s6A_notes_p6.mp3", "s6A_notes_p7.mp3", "s6B_textbook_p1.mp3",
    "s6B_textbook_p2.mp3", "s6B_textbook_p3.mp3", "s6B_textbook_p4.mp3",
    "s6B_textbook_p5.mp3", "s6B_textbook_p6.mp3"
]

needed = []
for sec in data["sections"]:
    sec_num = sec["section_number"]
    for passage in sec.get("passages", []):
        pid = passage["id"]
        paras = passage.get("paragraphs", [])
        for pi, para in enumerate(paras):
            fname = f"s{sec_num}_{pid}_p{pi+1}.mp3"
            status = "EXISTS" if fname in existing_files else "MISSING"
            # Collect English text for TTS
            if isinstance(para, list):
                en_text = " ".join(s.get("en", "") for s in para)
            else:
                en_text = para.get("en", "")
            needed.append((fname, status, en_text[:80]))

print(f"必要な音声ファイル数: {len(needed)}")
print(f"既存: {sum(1 for _,s,_ in needed if s=='EXISTS')}")
print(f"不足: {sum(1 for _,s,_ in needed if s=='MISSING')}")
print()

for fname, status, text in needed:
    marker = "✓" if status == "EXISTS" else "✗"
    print(f"  {marker} {fname}  {text[:60]}...")
