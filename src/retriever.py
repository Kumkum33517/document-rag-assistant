from src.embedder import embed_texts
from src.config import TOP_K


def retrieve(query, index, chunks, k=TOP_K):
    qv = embed_texts([query])
    scores, ids = index.search(qv, k)
    results = []
    for score, i in zip(scores[0], ids[0]):
        if i == -1:
            continue
        c = dict(chunks[i])
        c["score"] = float(score)
        results.append(c)
    return results
