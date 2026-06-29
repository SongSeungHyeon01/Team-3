"""HWP: pyhwp(1차) -> LibreOffice headless(2차) -> 실패 알림"""
from app.services.parsing import pdf_parser

def parse(file_path: str) -> dict:
    try:
        return _pyhwp(file_path)
    except Exception:
        try:
            pdf_path = _libreoffice_convert(file_path)
            return pdf_parser.parse(pdf_path)
        except Exception as e:
            _register_failure(file_path, str(e))
            return None

def parse_hwpx(file_path: str) -> dict:
    """HWPX: XML 직접 파싱"""
    import zipfile, xml.etree.ElementTree as ET
    # TODO: HWPX ZIP 내 body.xml 파싱
    return {"pages": [{"page_no": 1, "text": "", "image_path": None}]}

def _pyhwp(path): ...
def _libreoffice_convert(path) -> str: ...
def _register_failure(path, reason): ...
