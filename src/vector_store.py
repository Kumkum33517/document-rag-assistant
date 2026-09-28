import os
import pickle
import faiss
from src.config import INDEX_DIR
from src.embedder import embed_texts

INDEX_FILE = os.path.join(INDEX_DIR, "faiss.index")
META_FILE = os.path.join(INDEX_DIR, "chunks.pkl")


def build_index(chunks):
    os.makedirs(INDEX_DIR, exist_ok=True)
    vecs = embed_texts([c["text"] for c in chunks])
    index = faiss.IndexFlatIP(vecs.shape[1])
    index.add(vecs)
    faiss.write_index(index, INDEX_FILE)
    with open(META_FILE, "wb") as f:
        pickle.dump(chunks, f)
    return index


def load_index():
    if not (os.path.exists(INDEX_FILE) and os.path.exists(META_FILE)):
        return None, None
    index = faiss.read_index(INDEX_FILE)
    with open(META_FILE, "rb") as f:
        chunks = pickle.load(f)
    return index, chunks
