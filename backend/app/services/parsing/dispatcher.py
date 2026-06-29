"""포맷 감지 -> 파서 라우팅. 입력: 파일경로 / 출력: {pages:[{page_no,text,image_path}]}"""
from pathlib import Path
from app.services.parsing import pdf_parser, office_parser, hwp_parser

def dispatch(file_path: str) -> dict:
    ext = Path(file_path).suffix.lower()
    if ext == ".pdf":           return pdf_parser.parse(file_path)
    elif ext == ".pptx":        return office_parser.parse_pptx(file_path)
    elif ext == ".docx":        return office_parser.parse_docx(file_path)
    elif ext == ".xlsx":        return office_parser.parse_xlsx(file_path)
    elif ext == ".hwp":         return hwp_parser.parse(file_path)
    elif ext == ".hwpx":        return hwp_parser.parse_hwpx(file_path)
    elif ext in (".txt",".md"): return _plain(file_path)
    elif ext in (".png",".jpg",".jpeg"): return pdf_parser.parse_image(file_path)
    else: raise ValueError(f"지원하지 않는 포맷: {ext}")

def _plain(path):
    text = Path(path).read_text(encoding="utf-8", errors="ignore")
    return {"pages": [{"page_no": 1, "text": text, "image_path": None}]}
