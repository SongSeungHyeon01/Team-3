"""PyMuPDF(텍스트 레이어) + EasyOCR(스캔/이미지 페이지)"""
import fitz   # PyMuPDF
import easyocr
from app.config import settings

_ocr = None
def _get_ocr():
    global _ocr
    if _ocr is None: _ocr = easyocr.Reader(["ko","en"], gpu=False)
    return _ocr

def parse(file_path: str) -> dict:
    doc = fitz.open(file_path)
    pages = []
    for page in doc:
        text = page.get_text("text").strip()
        img_path = _render_page(page, file_path)
        if not text:
            text, conf = _ocr_page(page)
            if conf < settings.OCR_CONF_THRESHOLD:
                _flag_ocr(file_path, page.number + 1, conf)
        pages.append({"page_no": page.number + 1, "text": text, "image_path": img_path})
    return {"pages": pages}

def parse_image(file_path: str) -> dict:
    results = _get_ocr().readtext(file_path)
    text = " ".join(r[1] for r in results)
    conf = sum(r[2] for r in results) / len(results) if results else 0
    if conf < settings.OCR_CONF_THRESHOLD: _flag_ocr(file_path, 1, conf)
    return {"pages": [{"page_no": 1, "text": text, "image_path": file_path}]}

def _render_page(page, path): ...  # TODO: 페이지 PNG 렌더 저장
def _ocr_page(page): ...           # TODO: 페이지 이미지 -> EasyOCR
def _flag_ocr(path, page_no, conf): ...  # TODO: DB ocr_flags 등록
