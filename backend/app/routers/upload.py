from fastapi import APIRouter, UploadFile, File, Form, BackgroundTasks
from typing import List
from app.schemas.upload import UploadResponse, StatusResponse
router = APIRouter(tags=["upload"])

@router.post("/upload", status_code=202, response_model=UploadResponse)
async def upload_files(background_tasks: BackgroundTasks, files: List[UploadFile] = File(...), paths: List[str] = Form(...), category: str = Form(None)):
    """파일 저장 -> DB 등록 -> 백그라운드 파싱 enqueue"""
    pass

@router.get("/upload/{batch_id}/status", response_model=StatusResponse)
async def get_upload_status(batch_id: str):
    """파싱 진행 상태 폴링"""
    pass
