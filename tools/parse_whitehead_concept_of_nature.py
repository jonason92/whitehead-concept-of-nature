import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

SOURCE_URL = "https://www.gutenberg.org/files/18835/18835-h/18835-h.htm"
WORK_ID = "whitehead_concept_of_nature_1920"

EXPECTED_CHAPTERS = [
    {"num": "I",   "title": "Nature and Thought",                     "page_orig": 1},
    {"num": "II",  "title": "Theories of the Bifurcation of Nature",  "page_orig": 26},
    {"num": "III", "title": "Time",                                   "page_orig": 49},
    {"num": "IV",  "title": "The Method of Extensive Abstraction",     "page_orig": 74},
    {"num": "V",   "title": "Space and Motion",                        "page_orig": 99},
    {"num": "VI",  "title": "Congruence",                              "page_orig": 120},
    {"num": "VII", "title": "Objects",                                 "page_orig": 143},
    {"num": "VIII","title": "Summary",                                 "page_orig": 164},
    {"num": "IX",  "title": "The Ultimate Physical Concepts",         "page_orig": 185},
]

ROMAN_TO_INT = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
                "VI": 6, "VII": 7, "VIII": 8, "IX": 9}

import re
from pathlib import Path

def extract_orig_pages(elem):
    """v1.2: Original-Paginierung (pagenum-Spans) innerhalb eines Absatzes sammeln."""
    pages = []
    for span in elem.find_all("span", class_="pagenum"):
        m = re.search(r"Page\s*(\S+)", span.get("title", "") or "")
        if m:
            pages.append(m.group(1))
    return pages

def clean_text(text):
    return re.sub(r"\s+", " ", text).strip()

def text_of(elem):
    parts = []
    for child in elem.children:
        if isinstance(child, NavigableString):
            parts.append(str(child))
        elif isinstance(child, Tag):
            parts.append(text_of(child))
    return "".join(parts)

def is_chapter_heading(h):
    txt = clean_text(h.get_text()).upper()
    return bool(re.match(r"^CHAPTER\s+[IVX]+", txt))

def split_chapter_title(heading_text):
    m = re.match(r"^CHAPTER\s+([IVX]+)\s+(.*)$", clean_text(heading_text))
    if not m:
        raise ValueError(f"Unparsbares Kapitel-Heading: {heading_text!r}")
    roman, title = m.group(1), m.group(2)
    title = title.title().replace("'S", "'s")
    return roman, title

def main(output_path="corpus.json"):
    html_path = Path("18835-h.htm")
    if not html_path.exists():
        print(f"[!] HTML-Datei nicht gefunden: {html_path}")
        sys.exit(1)

    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "lxml")
    headings = soup.find_all(["h1", "h2", "h3"])

    chapter_spans = []
    for h in headings:
        if is_chapter_heading(h):
            roman, title = split_chapter_title(h.get_text())
            chapter_spans.append((roman, title, h))

    if len(chapter_spans) != len(EXPECTED_CHAPTERS):
        print(f"[WARNUNG] {len(chapter_spans)} Kapitel gefunden, "
              f"{len(EXPECTED_CHAPTERS)} erwartet")

    chapters_out = []
    for idx, (roman, title, h) in enumerate(chapter_spans):
        chap_num_int = ROMAN_TO_INT[roman]
        paragraphs = []
        node = h.find_next()
        while node is not None and not (
            getattr(node, "name", None) in ("h1", "h2", "h3")
            and is_chapter_heading(node)
        ):
            if getattr(node, "name", None) == "p":
                txt = clean_text(text_of(node))
                if txt and not txt.startswith("[") and len(txt) > 20:
                    pages = extract_orig_pages(node)
                    paragraphs.append({"text": txt, "orig_pages": pages})
            node = node.find_next()

        para_records = [
            {"pid": f"ch{chap_num_int}-p{i:03d}", "text": rec["text"], "orig_pages": rec["orig_pages"]}
            for i, rec in enumerate(paragraphs, start=1)
        ]

        chapters_out.append({
            "id": f"ch{chap_num_int}",
            "num": roman,
            "title": title,
            "page_orig": EXPECTED_CHAPTERS[idx]["page_orig"],
            "in_lecture_series": chap_num_int <= 7,
            "paragraph_count": len(para_records),
            "paragraphs": para_records,
        })
        print(f"[+] Kapitel {roman}: {title} ({len(para_records)} Absaetze)")

    corpus = {
        "work": {
            "id": WORK_ID,
            "title": "The Concept of Nature",
            "subtitle": "The Tarner Lectures Delivered in Trinity College, November 1919",
            "author": "Alfred North Whitehead",
            "publisher_orig": "Cambridge University Press, 1920",
            "digital_source": "Project Gutenberg EBook #18835",
            "source_url": SOURCE_URL,
            "license": "Public Domain (US)",
            "errata_applied": [
                "p.51: sight -> touch (PG correction, Transcribers Note)",
                "p.180: universely -> inversely (PG correction, Transcribers Note)",
            ],
        },
        "chapters": chapters_out,
        "parser_meta": {
            "parsed_with": "parse_whitehead_concept_of_nature.py v1.2",
            "expected_paragraph_total": sum(c["paragraph_count"] for c in chapters_out),
        },
    }

    out = Path(output_path)
    out.write_text(json.dumps(corpus, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[OK] Geschrieben: {out} "
          f"({corpus['parser_meta']['expected_paragraph_total']} Absaetze gesamt)")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "corpus.json"
    main(out)
