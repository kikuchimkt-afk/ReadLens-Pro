import json
import os
import copy

def main():
    base_dir = os.path.dirname(__file__)
    kakomon_path = os.path.join(base_dir, '..', '..', '..', 'kakomon', '2024', 'data.json')
    honshiken_path = os.path.join(base_dir, 'data.json')

    # 1. Load kakomon data
    with open(kakomon_path, 'r', encoding='utf-8') as f:
        kakomon_data = json.load(f)

    # 2. Extract section 2
    section2 = None
    for sec in kakomon_data.get('sections', []):
        if sec.get('section_number') == 2:
            section2 = copy.deepcopy(sec)
            break
            
    if not section2:
        print("Section 2 not found in kakomon 2024 data.")
        return

    # 3. Clean up fields and add images
    for field in ['pdf_pages', 'passage_images', 'explanation_images', 'vocabulary']:
        if field in section2:
            del section2[field]

    # Insert images into 2A
    for p in section2['subsections'][0]['passages']:
        if p.get('id') == 'header_2a':
            p['image'] = {
                "src": "data/kyotsu/2024/honshiken/images/s2a_shogi.png",
                "alt": "Shogi piece",
                "float": "left",
                "width": "80px"
            }
            # Adding a second image to the header is tricky. We'll add the chess piece to intro_2a instead, floating right.
        elif p.get('id') == 'intro_2a':
            p['image'] = {
                "src": "data/kyotsu/2024/honshiken/images/s2a_chess.png",
                "alt": "Chess knight",
                "float": "right",
                "width": "80px"
            }
        elif p.get('id') == 'activities_2a':
            p['image'] = {
                "src": "data/kyotsu/2024/honshiken/images/s2a_go.png",
                "alt": "Go board",
                "float": "right",
                "width": "150px"
            }

    # 4. Load honshiken data
    if os.path.exists(honshiken_path):
        with open(honshiken_path, 'r', encoding='utf-8') as f:
            honshiken_data = json.load(f)
    else:
        honshiken_data = {"exam_info": {}, "sections": []}

    # 5. Append/Replace section 2
    sections = [s for s in honshiken_data.get('sections', []) if s.get('section_number') != 2]
    sections.append(section2)
    # Sort sections just in case
    sections.sort(key=lambda x: x.get('section_number'))
    honshiken_data['sections'] = sections

    # 6. Update implemented_sections
    implemented = honshiken_data.get('exam_info', {}).setdefault('implemented_sections', [])
    if 2 not in implemented:
        implemented.append(2)
        implemented.sort()

    # 7. Save honshiken data
    with open(honshiken_path, 'w', encoding='utf-8') as f:
        json.dump(honshiken_data, f, ensure_ascii=False, indent=2)
        
    print("Section 2 added successfully!")

if __name__ == '__main__':
    main()
