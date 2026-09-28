from src.config import CHUNK_SIZE, CHUNK_OVERLAP


def chunk_documents(pages, size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    chunks = []
    for p in pages:
        text = " ".join(p["text"].split())
        start = 0
        while start < len(text):
            piece = text[start:start + size]
            if piece.strip():
                chunks.append({"text": piece, "source": p["source"], "page": p["page"]})
            start += size - overlap
    return chunks
