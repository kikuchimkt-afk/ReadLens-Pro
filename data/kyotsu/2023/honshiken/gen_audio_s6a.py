# -*- coding: utf-8 -*-
"""Generate audio for 2023 Honshiken Section 6A."""
import asyncio, json, os, re

VOICE = "en-US-JennyNeural"
DATA_JSON = os.path.join(os.path.dirname(__file__), "data.json")
AUDIO_DIR = os.path.join(os.path.dirname(__file__), "audio")

def strip_html(t):
    return re.sub(r'<[^>]+>', '', t)

async def generate_audio(text, outpath):
    import edge_tts
    c = edge_tts.Communicate(text, VOICE)
    await c.save(outpath)
    print(f"  -> {os.path.basename(outpath)}")

async def main():
    os.makedirs(AUDIO_DIR, exist_ok=True)
    with open(DATA_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    sec6a = [s for s in data["sections"] if str(s["section_number"]) == "6A"][0]
    
    for passage in sec6a["passages"]:
        pid = passage["id"]
        
        # Audio for article paragraphs
        if "paragraphs" in passage:
            for pi, para in enumerate(passage["paragraphs"], 1):
                text = " ".join(strip_html(s["en"]) for s in para)
                if not text.strip(): continue
                outpath = os.path.join(AUDIO_DIR, f"s6a_{pid}_p{pi}.mp3")
                if os.path.exists(outpath):
                    print(f"  skip {os.path.basename(outpath)}")
                    continue
                await generate_audio(text, outpath)
                
        # Audio for slides/notes
        if "slides" in passage:
            for si, slide in enumerate(passage["slides"], 1):
                texts = []
                if "title" in slide and "en" in slide["title"]:
                    texts.append(strip_html(slide["title"]["en"]))
                for content in slide.get("content", []):
                    if "text" in content and "en" in content["text"]:
                        texts.append(strip_html(content["text"]["en"]))
                text = " ".join(texts)
                if not text.strip(): continue
                outpath = os.path.join(AUDIO_DIR, f"s6a_{pid}_slide{si}.mp3")
                if os.path.exists(outpath):
                    print(f"  skip {os.path.basename(outpath)}")
                    continue
                await generate_audio(text, outpath)
                
    print("Done!")

if __name__ == "__main__":
    asyncio.run(main())
