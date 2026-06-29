"""하이브리드 검색 — BM25 || turbovec -> RRF 융합 -> 출처 조인"""
from app.services.indexing import bm25_index, vector_store, embedder
from app.config import settings

def retrieve(query: str, filters: dict, top_k: int = 10) -> list:
    bm25_res = bm25_index.search(query, top_k * 2)
    q_vec    = embedder.encode([query])[0]
    vec_res  = vector_store.search(q_vec, top_k * 2)
    fused    = _rrf(bm25_res, vec_res)[:top_k]
    return _attach_metadata(fused, filters)

def _rrf(bm25: list, vec: list, k: int = 60) -> list:
    # TUNE: k=60
    scores: dict = {}
    for rank, (chunk_id, _) in enumerate(bm25):
        scores[chunk_id] = scores.get(chunk_id, 0) + 1 / (k + rank + 1)
    # TODO: vec_results vector_id -> chunk_id 역매핑
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

def _attach_metadata(fused: list, filters: dict) -> list:
    # TODO: chunks -> document_versions -> documents 조인
    return []
