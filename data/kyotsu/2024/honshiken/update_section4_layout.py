import json
import os

def main():
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, 'data.json')

    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for sec in data.get('sections', []):
        if sec.get('section_number') == 4:
            passages = sec.get('passages', [])
            for sub in sec.get('subsections', []):
                passages.extend(sub.get('passages', []))
            
            for p in passages:
                if p.get('id') == 'article_4':
                    p['framed'] = True
                    sents = p.get('sentences', [])
                    if sents:
                        # 0:2, 2:9, 9:13, 13:17, 17:19
                        p['paragraphs'] = [
                            sents[0:2],
                            sents[2:9],
                            sents[9:13],
                            sents[13:17],
                            sents[17:19]
                        ]
                        del p['sentences']
                        
                elif p.get('id') == 'questionnaire_4':
                    sents = p.get('sentences', [])
                    if sents:
                        # Filter out 4_q1_data
                        sents = [s for s in sents if s['id'] != '4_q1_data']
                        
                        # Insert 'Main comments:' after 4_q2
                        new_sents = []
                        for s in sents:
                            new_sents.append(s)
                            if s['id'] == '4_q2':
                                new_sents.append({
                                    'id': '4_q2_sub',
                                    'en': 'Main comments:',
                                    'ja': '主なコメント：'
                                })
                        
                        # Put each sentence in its own paragraph
                        p['paragraphs'] = [[s] for s in new_sents]
                        del p['sentences']
                        
                        # Add image after Q1 (which is paragraph index 0)
                        p['images'] = [
                            {
                                "src": "images/s4_graph.png",
                                "paragraph_index": 0
                            }
                        ]
                        
                elif p.get('id') == 'handout_4':
                    p['framed'] = True
                    sents = p.get('sentences', [])
                    if sents:
                        p['paragraphs'] = [[s] for s in sents]
                        del p['sentences']

    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print("Section 4 layout updated successfully!")

if __name__ == '__main__':
    main()
