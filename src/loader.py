import os
from pypdf import PdfReader
from src.config import DOCS_DIR


def load_documents(docs_dir=DOCS_DIR):
    pages = []
    for name in sorted(os.listdir(docs_dir)):
        path = os.path.join(docs_dir, name)
        lower = name.lower()
        if lower.endswith(".pdf"):
            reader = PdfReader(path)
            for i, page in enumerate(reader.pages):
                text = page.extract_text() or ""
                if text.strip():
                    pages.append({"text": text, "source": name, "page": i + 1})
        elif lower.endswith((".txt", ".md")):
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            if text.strip():
                pages.append({"text": text, "source": name, "page": 1})
    return pages
