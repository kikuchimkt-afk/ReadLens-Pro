# -*- coding: utf-8 -*-
"""Generate audio MP3 files for Section 7 paragraphs using edge-tts."""
import asyncio, json, os

VOICE = "en-US-JennyNeural"
DATA_JSON = os.path.join(os.path.dirname(__file__), "data.json")
AUDIO_DIR = os.path.join(os.path.dirname(__file__), "audio")

async def generate_audio(text, outpath):
    import edge_tts
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(outpath)
    print(f"  -> {os.path.basename(outpath)}")

async def main():
    os.makedirs(AUDIO_DIR, exist_ok=True)
    with open(DATA_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    sec7 = [s for s in data["sections"] if s["section_number"] == 7][0]
    article = sec7["passages"][0]  # article passage with paragraphs

    for pi, para in enumerate(article["paragraphs"], 1):
        text = " ".join(s["en"].replace("<em>", "").replace("</em>", "") for s in para)
        outpath = os.path.join(AUDIO_DIR, f"s7_article_p{pi}.mp3")
        if os.path.exists(outpath):
            print(f"  skip {os.path.basename(outpath)} (exists)")
            continue
        await generate_audio(text, outpath)

    print("Done!")

if __name__ == "__main__":
    asyncio.run(main())
