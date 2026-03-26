"""
全セクション(1-6)を統合して data.json を最終生成
sub_sectionsを持つセクション(1,2,3)はA/Bに展開して独立セクション化
"""
import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

sections_out = []
section_list = []

# セクション1-3: sub_sectionsを展開
for i in range(1, 4):
    fname = f"section{i}.json"
    with open(fname, "r", encoding="utf-8") as f:
        sec = json.load(f)
    
    for sub in sec.get("sub_sections", []):
        sub_label = sub.get("sub_section", "")
        sec_id = f"{i}{sub_label}"  # "1A", "1B" etc.
        
        new_sec = {
            "section_number": sec_id,
            "title": f"第{i}問 {sub_label}",
            "points": sub.get("points", sec.get("points", 0)),
        }
        
        # optional fields
        if "situation" in sub:
            new_sec["situation"] = sub["situation"]
        elif "situation" in sec:
            new_sec["situation"] = sec["situation"]
        
        if "passages" in sub:
            new_sec["passages"] = sub["passages"]
        
        if "questions" in sub:
            new_sec["questions"] = sub["questions"]
        
        if "passage_images" in sec:
            new_sec["passage_images"] = sec.get("passage_images", [])
        
        if "explanation_images" in sec:
            new_sec["explanation_images"] = sec.get("explanation_images", [])
        
        sections_out.append(new_sec)
        section_list.append(sec_id)
        print(f"  Created section {sec_id}: {new_sec['title']} ({len(sub.get('questions',[]))} questions)")

# セクション4-5: そのまま
for i in range(4, 6):
    fname = f"section{i}.json"
    with open(fname, "r", encoding="utf-8") as f:
        sec = json.load(f)
    sections_out.append(sec)
    section_list.append(i)
    print(f"  Loaded section {i}: {sec['title']} ({len(sec.get('questions',[]))} questions)")

# セクション6A/6B
for ab in ["a", "b"]:
    fname = f"sec6{ab}.json"
    with open(fname, "r", encoding="utf-8") as f:
        sec = json.load(f)
    sec_id = f"6{ab.upper()}"
    sec["section_number"] = sec_id
    sec["title"] = f"第6問 {ab.upper()}"
    if "sub_section" in sec:
        del sec["sub_section"]
    sections_out.append(sec)
    section_list.append(sec_id)
    print(f"  Loaded section {sec_id}: {sec['title']} ({len(sec.get('questions',[]))} questions)")

# exam_info
exam_info = {
    "title": "共通テスト 2021年度 第1日程",
    "year": 2021,
    "session": 1,
    "subject": "英語（リーディング）",
    "time_limit_minutes": 80,
    "total_points": 100,
    "format": "6AB",
    "section_list": section_list
}

data = {
    "exam_info": exam_info,
    "sections": sections_out
}

# 書き出し
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 統計
total_q = sum(len(s.get("questions", [])) for s in sections_out)
print(f"\n=== 統合完了 ===")
print(f"セクション数: {len(sections_out)}")
print(f"総問題数: {total_q}")
print(f"section_list: {section_list}")
for s in sections_out:
    print(f"  {s.get('title','?')}: {len(s.get('questions', []))}問")
print(f"\ndata.json を更新しました")
