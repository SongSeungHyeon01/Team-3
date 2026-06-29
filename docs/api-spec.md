# API 명세 — 사내 지식관리 플랫폼
Base URL: http://localhost:8000/api
Swagger UI: http://localhost:8000/docs

| Method | Path | 설명 |
|--------|------|------|
| POST | /upload | 파일 업로드 |
| GET  | /upload/{id}/status | 파싱 진행 폴링 |
| POST | /search | 하이브리드 검색 |
| GET  | /documents/{id} | 문서 상세 |
| GET  | /documents/{id}/history | 버전 타임라인 |
| GET  | /documents/{version_id}/file | 파일 다운로드 |
| GET  | /admin/ocr-flags | OCR 큐 |
| GET  | /admin/parse-failures | 파싱 실패 큐 |
| PUT  | /admin/documents/{id}/representative | 대표 문서 지정 |
