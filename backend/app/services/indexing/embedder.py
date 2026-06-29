"""MiniLM 임베딩 — 청크 텍스트 -> 384차원 벡터"""
from sentence_transformers import SentenceTransformer
from app.config import settings
_model = None
def get_model():
    global _model
    if _model is None: _model = SentenceTransformer(settings.EMBED_MODEL)
    return _model
def encode(texts: list) -> list:
    return get_model().encode(texts, batch_size=32, show_progress_bar=False).tolist()
