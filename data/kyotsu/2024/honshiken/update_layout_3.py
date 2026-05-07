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
                
                # 1. Add floating aside to blog_3a, remove rules_3a
                rules_passage = None
                blog_passage = None
                passages = sub.get('passages', [])
                
                for p in passages:
                    if p.get('id') == 'rules_3a':
                        rules_passage = p
                    elif p.get('id') == 'blog_3a':
                        blog_passage = p
                
                if rules_passage and blog_passage:
                    # Build floating aside
                    floating_aside = {
                        "title": rules_passage.get("title"),
                        "sentences": []
                    }
                    for s in rules_passage.get("sentences", []):
                        en = s.get("en", "")
                        ja = s.get("ja", "")
                        # Remove leading bullets
                        if en.startswith('• '): en = en[2:]
                        if en.startswith('・'): en = en[1:]
                        if ja.startswith('・'): ja = ja[1:]
                        if ja.startswith('• '): ja = ja[2:]
                        floating_aside["sentences"].append({
                            "id": s.get("id"),
                            "en": en,
                            "ja": ja
                        })
                    
                    blog_passage["floating_aside"] = floating_aside
                    
                    # Remove rules_3a from passages
                    sub['passages'] = [p for p in passages if p.get('id') != 'rules_3a']

                # 2. Make article_3b framed
                for p in sub.get('passages', []):
                    if p.get('id') == 'article_3b':
                        p['framed'] = True

    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print("Data updated successfully for floating aside and framed article_3b!")

if __name__ == '__main__':
    main()
