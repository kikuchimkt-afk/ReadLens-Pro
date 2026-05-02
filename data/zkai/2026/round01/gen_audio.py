"""Generate MP3 audio for Section 1 of Sundai 2026 Round 02 using edge-tts."""
import asyncio
import edge_tts
import os

VOICE = "en-US-JennyNeural"
OUT_DIR = os.path.join(os.path.dirname(__file__), "audio")
os.makedirs(OUT_DIR, exist_ok=True)

TEXTS = {
    # Stars Beyond Reach
    "s1_review_sbr": (
        "Stars Beyond Reach, written in 2016, is a mysterious science fiction novel. "
        "In this story, characters go on a space adventure full of mysterious challenges. "
        "The book combines the vastness of space exploration with exciting unsolved mysteries, "
        "making it interesting for readers with its detailed worlds and surprising story turns. "
        "I can't believe this is Skyler's first work! "
        "This book is a top pick for those who love space mysteries and stories highlighting people's strengths."
    ),
    # Whispers of the Past
    "s1_review_wp": (
        "Whispers of the Past describes a slightly unusual love story. "
        "The main characters find letters that show a love story from 100 years ago that leaves them with a lot of questions. "
        "Hart's academic background in linguistics and great imagination result in a smooth and exciting romance novel "
        "full of discoveries of hidden secrets, making this book one of the greatest hits of 2018. "
        "This book takes you on a trip that demonstrates the strong power of love and old secrets."
    ),
    # The Final Clue
    "s1_review_tfc": (
        "The Final Clue is an exciting mystery book from start to end. "
        "The main character, Detective Laura Hale, works to solve a difficult mystery in London, "
        "making readers think and keeping them interested. "
        "This book, which took five years to complete from its start in 2017 to publication, "
        "is not only about solving mysteries but also features unique characters and detailed descriptions of London. "
        "It will attract a wide range of novel readers as well as mystery enthusiasts this year."
    ),
}

async def main():
    for name, text in TEXTS.items():
        out_path = os.path.join(OUT_DIR, f"{name}.mp3")
        print(f"Generating {name}.mp3 ...")
        comm = edge_tts.Communicate(text, VOICE)
        await comm.save(out_path)
        print(f"  -> Saved: {out_path}")

if __name__ == "__main__":
    asyncio.run(main())
