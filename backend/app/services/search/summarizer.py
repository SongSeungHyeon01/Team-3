"""Ollama + Gemma 3 4B 요약 (보조 기능, 실패해도 검색 결과는 반환)"""
import requests
from app.config import settings

def summarize(query: str, snippets: list) -> str | None:
    prompt = (
        f"다음 발췌문을 참고해 질문에 간결히 답하세요. 원본 문서를 직접 확인하도록 안내하세요.\n\n"
        f"질문: {query}\n\n" + "\n---\n".join(snippets[:5])
    )
    try:
        r = requests.post(
            f"{settings.OLLAMA_HOST}/api/generate",
            json={"model": settings.LLM_MODEL, "prompt": prompt, "stream": False},
            timeout=30,
        )
        return r.json().get("response","").strip() or None
    except Exception:
        return None
