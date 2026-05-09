# -*- coding: utf-8 -*-
"""Generate audio for Tsuishiken Section 8."""
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
    sec8 = [s for s in data["sections"] if s["section_number"] == 8][0]
    for passage in sec8["passages"]:
        pid = passage["id"]
        for pi, para in enumerate(passage.get("paragraphs", []), 1):
            text = " ".join(strip_html(s["en"]) for s in para if not s["id"].endswith("_h"))
            if not text.strip():
                continue
            outpath = os.path.join(AUDIO_DIR, f"s8_{pid}_p{pi}.mp3")
            if os.path.exists(outpath):
                print(f"  skip {os.path.basename(outpath)}")
                continue
            await generate_audio(text, outpath)
    print("Done!")

if __name__ == "__main__":
    asyncio.run(main())
