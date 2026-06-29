from pydantic import BaseModel
from typing import List, Optional
class SearchFilters(BaseModel):
    company: Optional[str] = None
    project: Optional[str] = None
    researcher: Optional[str] = None
    category: Optional[str] = None
    date_from: Optional[str] = None
    date_to: Optional[str] = None
    file_type: Optional[str] = None
class SearchRequest(BaseModel):
    query: str
    filters: SearchFilters = SearchFilters()
    top_k: int = 10
    summarize: bool = False
class ResultCard(BaseModel):
    version_id: int
    original_name: str
    original_path: str
    page_no: int
    snippet: str
    page_image_url: Optional[str] = None
    category: Optional[str] = None
    score: float
    is_representative: bool = False
class SearchResponse(BaseModel):
    results: List[ResultCard]
    summary: Optional[str] = None
