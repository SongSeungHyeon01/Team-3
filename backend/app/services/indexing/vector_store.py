"""turbovec 벡터 저장 · 유사도 검색 (CPU, 16배 압축)"""
from pathlib import Path
from app.config import settings
# TODO: turbovec 설치 후 실제 API로 교체
_INDEX_PATH = Path(settings.STORAGE_DIR) / "index" / "turbovec.idx"

def add(vector, meta: dict) -> str:
    raise NotImplementedError("turbovec API 구현 필요")

def search(query_vector, top_k: int = 10) -> list:
    raise NotImplementedError("turbovec API 구현 필요")
