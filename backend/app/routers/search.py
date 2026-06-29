from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.schemas.search import SearchRequest, SearchResponse
router = APIRouter(tags=["search"])

@router.post("/search", response_model=SearchResponse)
async def search(request: SearchRequest, db: Session = Depends(get_db)):
    """2단계 하이브리드 검색 (BM25 + turbovec)"""
    pass
