import json
f = open("data.json","r",encoding="utf-8")
d = json.load(f)
f.close()
print("Keys:", list(d.keys()))
print("Sections:", len(d.get("sections",[])))
for s in d.get("sections",[]):
    sn = s.get("section_number","?")
    t = s.get("title","?")
    print(f"  Section {sn}: {t}")
