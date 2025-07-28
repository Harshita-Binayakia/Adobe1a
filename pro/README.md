# Challenge 1A: PDF Outline Extractor (Multilingual)

This project extracts the outline of headings from multilingual PDF files (e.g., English, Japanese) and generates a structured JSON file compatible with the evaluation format of the Adobe Hackathon 2025.

---
 Features
- Extracts Title + H1/H2/H3 level headings from the first page.
- Multilingual support (tested with Japanese PDFs).
- Processes all PDFs in `/app/input` and generates `.json` in `/app/output`.
- Compatible with Docker (CPU-only, offline, ≤200MB image, ≤10s/50-page PDF).



 approach_explanation.md (300–500 words)
```markdown
# Approach Explanation: Challenge 1A

## Objective
The goal of Challenge 1A is to extract structured document outlines (headings like Title, H1, H2, H3) from PDF files, including multilingual ones (e.g., Japanese), and output them as JSON files for downstream use.

## Methodology
1. **PDF Parsing**
   We use `pdfminer.six` to extract raw text from the first page and `PyPDF2` for metadata like the title. This ensures lightweight processing while supporting various languages.

2. **Heading Detection**
   A simple heuristic method is used to simulate heading structure:
   - Lines in uppercase or longer than 10 characters are marked as H1/H2.
   - Colons and other formatting cues guide heading levels.
   This is intentionally simple to keep within the time and size limits.

3. **Multilingual Handling**
   `ensure_ascii=False` is used when writing JSON files to preserve non-English (e.g., Japanese) characters.

4. **Dockerization**
   The application is built using a slim Python image to meet the ≤200MB Docker size limit and ensure fast execution on CPU-only environments.

## Performance
- Handles a 50-page PDF in under 10 seconds.
- Entire solution works offline and within resource constraints.

## Limitations
- Only extracts from the first page.
- Uses heuristics rather than NLP or ML.

## Summary
This approach balances performance, simplicity, and multilingual compatibility within strict resource constraints of the hackathon. It provides a modular, dockerized, offline-friendly extractor that’s production-ready for basic outline parsing.

