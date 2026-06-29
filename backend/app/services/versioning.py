"""최신 표준 문서 후보 산정 (자동 판별 = 제안만, 확정은 관리자 수동)"""
import re
from datetime import datetime

def score_version(version: dict) -> float:
    score = 0.0
    if version.get("file_modified_at"):
        days = (datetime.now() - version["file_modified_at"]).days
        score += max(0, 1 - days / 365) * 0.5   # 가중치 0.5 TUNE
    label = (version.get("version_label") or "").lower()
    m = re.search(r"v(\d+)", label)
    if m: score += min(int(m.group(1)) / 10, 1.0) * 0.3  # TUNE
    if any(k in label for k in ("final","latest","최종")): score += 0.3
    path = (version.get("original_path") or "").lower()
    score += -0.2 if any(k in path for k in ("old","archive","backup")) else 0.2
    return min(max(score, 0.0), 1.0)
