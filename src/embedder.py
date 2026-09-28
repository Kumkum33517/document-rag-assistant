import numpy as np
from sentence_transformers import SentenceTransformer
from src.config import EMBED_MODEL

_model = None


def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBED_MODEL)
    return _model


def embed_texts(texts):
    vecs = get_model().encode(texts, normalize_embeddings=True, show_progress_bar=False)
    return np.array(vecs, dtype="float32")
