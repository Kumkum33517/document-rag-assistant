from src.loader import load_documents
from src.chunker import chunk_documents
from src.vector_store import build_index, load_index
from src.retriever import retrieve
from src.generator import generate_answer


def ingest():
    pages = load_documents()
    if not pages:
        raise ValueError("No documents found in data/docs")
    chunks = chunk_documents(pages)
    build_index(chunks)
    return len(pages), len(chunks)


def ask(question):
    index, chunks = load_index()
    if index is None:
        raise RuntimeError("Index not built yet. Click 'Build / Rebuild index' first.")
    contexts = retrieve(question, index, chunks)
    answer = generate_answer(question, contexts)
    return answer, contexts
