from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/ocr-flags")
async def list_ocr_flags(db: Session = Depends(get_db)): pass

@router.get("/parse-failures")
async def list_parse_failures(db: Session = Depends(get_db)): pass

@router.post("/reprocess/{version_id}")
async def reprocess(version_id: int, db: Session = Depends(get_db)): pass

@router.put("/ocr-flags/{flag_id}")
async def resolve_ocr_flag(flag_id: int, db: Session = Depends(get_db)): pass

@router.put("/documents/{doc_id}/representative")
async def set_representative(doc_id: int, db: Session = Depends(get_db)): pass

@router.get("/categories")
async def list_categories(db: Session = Depends(get_db)): pass
