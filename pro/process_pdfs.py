import os
import json
from pathlib import Path
from PyPDF2 import PdfReader
from pdfminer.high_level import extract_text

def get_document_title(pdf):
    try:
        meta = pdf.metadata
        name = meta.title
        if name:
            return name
    except:
        pass
    return "Untitled Document"

def pull_headings(raw_text):
    sections = []
    lines = raw_text.splitlines()
    count = 0
    for i in range(len(lines)):
        current = lines[i].strip()
        if not current:
            continue

        if current.isupper() and len(current) > 5:
            tag = "H1"
        elif current.endswith(":") or len(current) > 10:
            tag = "H2"
        else:
            tag = "H3"

        sections.append({
            "level": tag,
            "text": current,
            "page": 1
        })
        
        count += 1
        if count == 10:
            break

    return sections

def convert_pdf_folder():
    base_path = Path("/app/input")
    save_path = Path("/app/output")
    save_path.mkdir(parents=True, exist_ok=True)

    pdf_files = list(base_path.glob("*.pdf"))

    for doc in pdf_files:
        print(f" Reading: {doc.name}")
        try:
            opened = PdfReader(str(doc))
            heading = get_document_title(opened)
            body = extract_text(str(doc), maxpages=1)
            structure = pull_headings(body)

            packed = {
                "title": heading,
                "outline": structure
            }

            final = save_path / f"{doc.stem}.json"
            with open(final, "w", encoding="utf-8") as out_file:
                json.dump(packed, out_file, indent=2, ensure_ascii=False)

            print(f" Done: {doc.stem}.json")
        except Exception as issue:
            print(f" Couldn’t handle {doc.name}: {issue}")

if _name_ == "_main_":
    convert_pdf_folder()