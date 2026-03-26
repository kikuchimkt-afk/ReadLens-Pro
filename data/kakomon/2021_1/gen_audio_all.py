"""
edge-ttsを使って不足している音声ファイルを一括生成するスクリプト
"""
import json
import asyncio
import os
import edge_tts

VOICE = "en-US-AriaNeural"  # 高品質な女性音声
AUDIO_DIR = "audio"

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(AUDIO_DIR, exist_ok=True)

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 必要な音声ファイルリストを構築
tasks = []
for sec in data["sections"]:
    sec_num = sec["section_number"]
    for passage in sec.get("passages", []):
        pid = passage["id"]
        paras = passage.get("paragraphs", [])
        for pi, para in enumerate(paras):
            fname = f"s{sec_num}_{pid}_p{pi+1}.mp3"
            fpath = os.path.join(AUDIO_DIR, fname)
            
            # 既に存在するならスキップ
            if os.path.exists(fpath):
                continue
            
            # 英文テキストを結合
            if isinstance(para, list):
                en_text = " ".join(s.get("en", "") for s in para if s.get("en"))
            else:
                en_text = para.get("en", "")
            
            if en_text.strip():
                tasks.append((fname, fpath, en_text.strip()))

print(f"生成対象: {len(tasks)} ファイル")

async def generate_one(fname, fpath, text):
    try:
        communicate = edge_tts.Communicate(text, VOICE, rate="-5%")
        await communicate.save(fpath)
        print(f"  ✓ {fname}")
    except Exception as e:
        print(f"  ✗ {fname}: {e}")

async def main():
    for i, (fname, fpath, text) in enumerate(tasks):
        await generate_one(fname, fpath, text)
        if (i + 1) % 10 == 0:
            print(f"  --- {i+1}/{len(tasks)} 完了 ---")
    print(f"\n=== 全 {len(tasks)} ファイル生成完了 ===")

asyncio.run(main())
