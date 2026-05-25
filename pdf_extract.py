import fitz
def extract_resume_text(pdf_path: str) -> str:
    """Extract text from PDF file"""
    doc = fitz.open(pdf_path)
    text = []

    for page in doc:
        page_text = page.get_text()
        if page_text:
            text.append(page_text)

    return "\n".join(text)