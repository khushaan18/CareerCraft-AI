from pathlib import Path
import io,fitz
from docx import Document
def extract_text(filename,data):
    ext=Path(filename).suffix.lower()
    if ext==".pdf":
        doc=fitz.open(stream=data,filetype="pdf"); return "\n".join(p.get_text() for p in doc).strip()
    if ext==".docx":
        doc=Document(io.BytesIO(data)); return "\n".join(p.text for p in doc.paragraphs).strip()
    if ext==".txt": return data.decode("utf-8",errors="ignore").strip()
    raise ValueError("Unsupported file type. Use PDF, DOCX, or TXT.")
