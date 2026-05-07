import json
import os
import asyncio
import sys
import re
import tempfile
import argparse

async def generate_audio_for_file(data_file, target_section=None):
    audio_dir = os.path.join(os.path.dirname(data_file), "audio")
    os.makedirs(audio_dir, exist_ok=True)
    
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    voice = 'en-US-JennyNeural'
    
    tasks = [] # (filename, text)
    
    def extract_text(sentences_or_para):
        if not sentences_or_para:
            return ""
            
        ignore_roles = {"pamphlet_heading", "title", "heading", "outline_title", "outline_subheader"}
        
        if isinstance(sentences_or_para, dict):
            # object paragraph {id, en, ja}
            if sentences_or_para.get("role") in ignore_roles:
                return ""
            return sentences_or_para.get("en", "")
        else:
            # list of sentences
            parts = []
            for s in sentences_or_para:
                if isinstance(s, dict) and "en" in s:
                    if s.get("role") in ignore_roles:
                        continue
                    parts.append(s.get("en", ""))
            return " ".join(parts)

    # handle flattened subsections if any
    for section in data.get('sections', []):
        sec_num = section.get('section_number')
        
        if target_section is not None and sec_num != target_section:
            continue
            
        subsections = section.get('subsections', [])
        
        passages = section.get('passages', [])
        if subsections:
            passages = []
            for sub in subsections:
                if 'passages' in sub:
                    passages.extend(sub['passages'])

        for passage in passages:
            passage_id = passage.get('id', '')
            if not passage_id or passage.get('is_notes'):
                continue

            # 1. passage.authors
            if 'authors' in passage:
                for author in passage['authors']:
                    author_id = author['name']['en'].split('(')[0].strip().replace(' ', '_').lower()
                    for pi, para in enumerate(author.get('paragraphs', [])):
                        text = extract_text(para)
                        if text.strip():
                            filename = f"s{sec_num}_{author_id}_p{pi+1}.mp3"
                            tasks.append((filename, text))

            # 2. passage.sources
            if 'sources' in passage:
                for source in passage['sources']:
                    source_id = source['name']['en'].replace(' ', '_').lower()
                    for pi, para in enumerate(source.get('paragraphs', [])):
                        text = extract_text(para)
                        if text.strip():
                            filename = f"s{sec_num}_{source_id}_p{pi+1}.mp3"
                            tasks.append((filename, text))

            # 3. paragraphs
            if 'paragraphs' in passage:
                # normal paragraphs
                for pi, para in enumerate(passage['paragraphs']):
                    text = extract_text(para)
                    if text.strip():
                        filename = f"s{sec_num}_{passage_id}_p{pi+1}.mp3"
                        tasks.append((filename, text))

            # 4. sentences and advertisement_sections
            if 'sentences' in passage and 'authors' not in passage and 'sources' not in passage and 'paragraphs' not in passage:
                text = extract_text(passage['sentences'])
                if text.strip():
                    filename = f"s{sec_num}_{passage_id}.mp3"
                    tasks.append((filename, text))
                    
    print(f"[{data_file}] Found {len(tasks)} audio tasks.")
    
    # Generate MP3s
    for filename, text in tasks:
        # cleanup text for tts
        clean_text = text.replace('\\n', ' ').replace('\n', ' ').replace('\r', '').replace('\t', ' ')
        clean_text = re.sub(r'<[^>]+>', '', clean_text)
        clean_text = re.sub(r'\[\s*\d+\s*\]', '', clean_text).strip()
        clean_text = re.sub(r'\(\s*\d+\s*\)', '', clean_text).strip()
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        
        if not clean_text:
            continue
            
        out = os.path.join(audio_dir, filename)
        if os.path.exists(out) and os.path.getsize(out) > 0:
            print(f"  Skip existing: {filename}")
            continue
            
        print(f"  Generating: {filename}...")
        
        with tempfile.NamedTemporaryFile('w', encoding='utf-8', delete=False) as tf:
            tf.write(clean_text)
            temp_path = tf.name
            
        proc = await asyncio.create_subprocess_shell(
            f'"{sys.executable}" -m edge_tts --voice "{voice}" --f "{temp_path}" --write-media "{out}"',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        await proc.communicate()
        os.remove(temp_path)
        
        size = os.path.getsize(out) if os.path.exists(out) else 0
        if size == 0:
            print(f"  FAILED: {filename}")
        else:
            print(f"  OK: {size} bytes")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate audio files using edge-tts.")
    parser.add_argument("files", nargs="+", help="Path to data.json file(s)")
    parser.add_argument("--section", type=int, default=None, help="Specific section number to generate audio for")
    args = parser.parse_args()
    
    for data_file in args.files:
        print(f"Processing {data_file}...")
        asyncio.run(generate_audio_for_file(data_file, target_section=args.section))
        print(f"Finished {data_file}")

