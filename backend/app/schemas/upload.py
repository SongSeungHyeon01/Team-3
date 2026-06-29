from pydantic import BaseModel
from typing import List
class UploadItem(BaseModel):
    version_id: int
    original_name: str
    parse_status: str
class UploadResponse(BaseModel):
    batch_id: str
    items: List[UploadItem]
class StatusResponse(BaseModel):
    items: List[UploadItem]
