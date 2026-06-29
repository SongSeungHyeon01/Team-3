"""SQLite 메타데이터 모델.

담당: 김기빈
역할:
  - 업로드된 문서 메타데이터 영구 저장
  - 검색 로그 기록 (쿼리·결과 수·지연시간)
"""
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)          # 저장 파일명 (uuid_원본명)
    original_name = Column(String(255), nullable=False)     # 원본 파일명
    file_path = Column(String(512), nullable=False)
    file_size = Column(Integer)
    mime_type = Column(String(100))
    category = Column(String(50))                           # spec / research / presentation / report
    content_text = Column(Text)                             # 파싱된 텍스트 (최대 50,000자)
    page_count = Column(Integer)
    ocr_flagged = Column(Boolean, default=False)            # 신뢰도 0.7 미만 페이지 존재 여부
    flagged_pages = Column(String(500))                     # JSON 배열: [0, 3, 7]
    vector_id = Column(String(100))                         # turbovec 인덱스 식별자
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SearchLog(Base):
    __tablename__ = "search_logs"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(String(500), nullable=False)
    result_count = Column(Integer)
    search_type = Column(String(20))                        # hybrid-rrf / bm25 / vector
    latency_ms = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
