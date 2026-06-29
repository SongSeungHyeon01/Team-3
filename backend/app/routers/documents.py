from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
router = APIRouter(tags=["documents"])

@router.get("/documents/{doc_id}")
async def get_document(doc_id: int, db: Session = Depends(get_db)):
    pass

@router.get("/documents/{doc_id}/history")
async def get_history(doc_id: int, db: Session = Depends(get_db)):
    pass

@router.get("/documents/{version_id}/file")
async def download_file(version_id: int, dl: bool = False):
    pass
