"""파싱 결과 -> Markdown 정규화 후 저장"""
from pathlib import Path
from app.config import settings

def save_markdown(pages: list, version_id: int) -> str:
    out_dir = Path(settings.STORAGE_DIR) / "markdown" / f"v_{version_id:06d}"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "content.md"
    with open(out_path, "w", encoding="utf-8") as f:
        for p in pages:
            f.write(f"## Page {p['page_no']}\n\n{(p['text'] or '').strip()}\n\n---\n\n")
    return str(out_path)
