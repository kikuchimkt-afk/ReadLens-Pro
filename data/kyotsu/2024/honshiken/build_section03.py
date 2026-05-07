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

    # 2. Extract section 3
    section_data = None
    for sec in kakomon_data.get('sections', []):
        if sec.get('section_number') == 3:
            section_data = copy.deepcopy(sec)
            break
            
    if not section_data:
        print("Section 3 not found in kakomon 2024 data.")
        return

    # 3. Clean up fields
    for field in ['pdf_pages', 'passage_images', 'explanation_images', 'vocabulary']:
        if field in section_data:
            del section_data[field]

    # 4. Load honshiken data
    if os.path.exists(honshiken_path):
        with open(honshiken_path, 'r', encoding='utf-8') as f:
            honshiken_data = json.load(f)
    else:
        honshiken_data = {"exam_info": {}, "sections": []}

    # 5. Append/Replace section
    sections = [s for s in honshiken_data.get('sections', []) if s.get('section_number') != 3]
    sections.append(section_data)
    # Sort sections just in case
    sections.sort(key=lambda x: x.get('section_number'))
    honshiken_data['sections'] = sections

    # 6. Update implemented_sections
    implemented = honshiken_data.get('exam_info', {}).setdefault('implemented_sections', [])
    if 3 not in implemented:
        implemented.append(3)
        implemented.sort()

    # 7. Save honshiken data
    with open(honshiken_path, 'w', encoding='utf-8') as f:
        json.dump(honshiken_data, f, ensure_ascii=False, indent=2)
        
    print("Section 3 added successfully!")

if __name__ == '__main__':
    main()
