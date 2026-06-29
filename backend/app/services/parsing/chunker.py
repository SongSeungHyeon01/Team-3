"""페이지 단위 청킹. 512토큰 초과 시 문장 경계로 분할."""
import re
from app.config import settings

def chunk_pages(pages: list, version_id: int) -> list:
    chunks = []
    for page in pages:
        for idx, (text, char_start) in enumerate(_split(page["text"] or "")):
            chunks.append({
                "version_id": version_id, "page_no": page["page_no"],
                "chunk_index": idx, "text": text, "char_start": char_start,
                "page_image_path": page.get("image_path"),
            })
    return chunks

def _split(text: str) -> list:
    max_chars = settings.CHUNK_TOKENS * 2  # 1토큰 ≈ 2자 추정
    if len(text) <= max_chars: return [(text, 0)]
    sents = re.split(r"(?<=[.!?\n])\s+", text)
    sub, start, out = "", 0, []
    for s in sents:
        if len(sub) + len(s) > max_chars and sub:
            out.append((sub.strip(), start)); start += len(sub); sub = ""
        sub += s + " "
    if sub.strip(): out.append((sub.strip(), start))
    return out or [(text[:max_chars], 0)]
