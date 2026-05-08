import json
import pathlib
import re
import subprocess

import fitz


PDF_PATH = pathlib.Path(
    r"c:\Users\user\Documents\GitHub\ReadLens-Pro\original_PDFs\Kyotuu-Test-2023\2023_本試験_英語リーディング_解答.pdf"
)
OUT_PATH = pathlib.Path(
    r"c:\Users\user\Documents\GitHub\ReadLens-Pro\data\kyotsu\2023\honshiken\vocabulary_seed.json"
)
TMP_DIR = pathlib.Path(
    r"c:\Users\user\Documents\GitHub\ReadLens-Pro\data\kyotsu\2023\honshiken\images\_ocr_tmp"
)
TESS_EXE = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
TESSDATA_DIR = r"c:\Users\user\Documents\GitHub\ReadLens-Pro\data\tessdata"


EN_STOP = {
    "the",
    "and",
    "for",
    "from",
    "with",
    "into",
    "that",
    "this",
    "these",
    "those",
    "your",
    "their",
    "have",
    "will",
}


def norm_spaces(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip())


def clean_en(s: str) -> str:
    s = norm_spaces(s)
    s = re.sub(r"^[^A-Za-z]+", "", s)
    s = re.sub(r"[^A-Za-z'\-\s~]$", "", s)
    return norm_spaces(s)


def clean_ja(s: str) -> str:
    s = norm_spaces(s)
    s = re.sub(r"^[\]】）\)\]・:：\-~]+", "", s)
    return norm_spaces(s)


def is_valid_term(term: str) -> bool:
    if not term:
        return False
    if len(term) < 3 or len(term) > 40:
        return False
    words = term.lower().split()
    if len(words) > 4:
        return False
    if words[0] in EN_STOP:
        return False
    if sum(1 for c in term if c.isalpha()) < 3:
        return False
    return True


def ocr_image(path: pathlib.Path) -> str:
    cmd = [
        TESS_EXE,
        str(path),
        "stdout",
        "-l",
        "jpn+eng",
        "--tessdata-dir",
        TESSDATA_DIR,
    ]
    out = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    return out.decode("utf-8", errors="ignore")


def parse_lines(text: str, page_num: int):
    entries = []
    for raw in text.splitlines():
        line = norm_spaces(raw)
        if not line:
            continue
        # 例: "1.17 feature 他 ～を呼び物にする"
        m = re.search(
            r"(?:[I1l]\.?\s*\d{1,2}|\d{1,2}\.?\d{1,2})\s+([A-Za-z][A-Za-z'\-\s~]{1,40}?)(?:\s+[他名形副動]\s+|\s{2,}|(?=\s*[ぁ-んァ-ヶ一-龥]))(.+)$",
            line,
        )
        if not m:
            continue
        term = clean_en(m.group(1))
        ja = clean_ja(m.group(2))
        if not is_valid_term(term):
            continue
        if not ja or len(ja) < 2:
            continue
        entries.append(
            {
                "term_en": term,
                "term_ja": ja,
                "question_id": "vocabulary",
                "source_page": page_num,
            }
        )
    return entries


def main():
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF_PATH)
    found = {}

    for i, page in enumerate(doc, start=1):
        rect = page.rect
        # 語句欄が置かれやすい右カラムを優先OCR
        clip_right = fitz.Rect(rect.width * 0.68, rect.height * 0.12, rect.width * 0.99, rect.height * 0.97)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=clip_right, alpha=False)
        img = TMP_DIR / f"page_{i:02d}_right.png"
        pix.save(img.as_posix())
        text = ocr_image(img)
        page_entries = parse_lines(text, i)

        for e in page_entries:
            key = e["term_en"].lower()
            rec = found.get(key)
            if not rec:
                found[key] = e
            else:
                # 既存訳が短すぎる場合は長い方を採用
                if len(e["term_ja"]) > len(rec["term_ja"]):
                    rec["term_ja"] = e["term_ja"]

    # 既存seedを温存しつつマージ
    existing = []
    if OUT_PATH.exists():
        try:
            j = json.loads(OUT_PATH.read_text(encoding="utf-8"))
            existing = j.get("entries", []) if isinstance(j.get("entries", []), list) else []
        except Exception:
            existing = []

    merged = {}
    for e in existing:
        term = str(e.get("term_en", "")).strip()
        ja = str(e.get("term_ja", "")).strip()
        if term and ja:
            merged[term.lower()] = {
                "term_en": term,
                "term_ja": ja,
                "section_number": e.get("section_number"),
                "question_id": e.get("question_id", "vocabulary"),
            }
    for key, e in found.items():
        if key not in merged:
            merged[key] = {
                "term_en": e["term_en"],
                "term_ja": e["term_ja"],
                "section_number": None,
                "question_id": "vocabulary",
            }

    out = {
        "meta": {
            "source": "2023 answer PDF OCR (all pages, right-column priority)",
            "total_entries": len(merged),
        },
        "entries": sorted(merged.values(), key=lambda x: x["term_en"].lower()),
    }
    OUT_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"written {OUT_PATH} entries={len(out['entries'])}")


if __name__ == "__main__":
    main()

