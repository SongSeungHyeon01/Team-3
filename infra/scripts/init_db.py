"""DB 초기화 — 테이블 생성 + 카테고리 기본값"""
from app.db import Base, engine, SessionLocal
from app.models.document import Document
from app.models.version import DocumentVersion
from app.models.chunk import Chunk
from app.models.admin_queue import OcrFlag, ParseFailure
from sqlalchemy import text
Base.metadata.create_all(bind=engine)
db = SessionLocal()
db.execute(text("""INSERT OR IGNORE INTO categories (code, label) VALUES
  (
