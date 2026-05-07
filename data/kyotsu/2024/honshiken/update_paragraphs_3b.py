import json
import os

def main():
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, 'data.json')

    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for sec in data.get('sections', []):
        if sec.get('section_number') == 3:
            for sub in sec.get('subsections', []):
                for p in sub.get('passages', []):
                    if p.get('id') == 'article_3b':
                        sentences = p.get('sentences', [])
                        if not sentences:
                            continue
                            
                        # Split sentences into paragraphs
                        p1 = sentences[0:2]
                        p2 = sentences[2:5]
                        p3 = sentences[5:12]
                        p4 = sentences[12:17]
                        p5 = sentences[17:19]
                        
                        p['paragraphs'] = [p1, p2, p3, p4, p5]
                        del p['sentences']
                        
                        # Update images paragraph_index since paragraph 4 is index 3 (0-indexed in array but wait!)
                        # In viewer.js, passage.images checks `img.paragraph_index === pi`.
                        # 'pi' is the 0-based index of the paragraph in the loop!
                        # The starry sky image is in paragraph 4 ("In the evening...").
                        # So its paragraph_index should be 3.
                        for img in p.get('images', []):
                            if img['src'] == 'images/s3b_starry_sky.png':
                                img['paragraph_index'] = 3

    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print("Data updated successfully for article_3b paragraphs!")

if __name__ == '__main__':
    main()
