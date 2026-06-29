"""BM25 키워드 인덱스 — rank-bm25 + kiwipiepy"""
import pickle
from pathlib import Path
from rank_bm25 import BM25Okapi
from kiwipiepy import Kiwi
from app.config import settings

_kiwi = Kiwi()
_INDEX_PATH = Path(settings.STORAGE_DIR) / "index" / "bm25.pkl"

def tokenize(text: str) -> list:
    return [t.form for t in _kiwi.tokenize(text)]

def add_chunks(chunk_ids: list, texts: list):
    tokens = [tokenize(t) for t in texts]
    data = {"ids": chunk_ids, "bm25": BM25Okapi(tokens)}
    _INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    _INDEX_PATH.write_bytes(pickle.dumps(data))

def search(query: str, top_k: int = 10) -> list:
    if not _INDEX_PATH.exists(): return []
    data = pickle.loads(_INDEX_PATH.read_bytes())
    scores = data["bm25"].get_scores(tokenize(query))
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:top_k]
    return [(data["ids"][i], s) for i, s in ranked]
