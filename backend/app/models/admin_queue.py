from sqlalchemy import Column, Integer, Text, Float, DateTime, ForeignKey
from app.db import Base
class OcrFlag(Base):
    __tablename__ = "ocr_flags"
    id         = Column(Integer, primary_key=True)
    version_id = Column(Integer, ForeignKey("document_versions.id"))
    page_no    = Column(Integer)
    confidence = Column(Float)
    status     = Column(Text, default="open")
    created_at = Column(DateTime)
class ParseFailure(Base):
    __tablename__ = "parse_failures"
    id            = Column(Integer, primary_key=True)
    version_id    = Column(Integer, ForeignKey("document_versions.id"))
    original_name = Column(Text)
    reason        = Column(Text)
    status        = Column(Text, default="open")
    created_at    = Column(DateTime)
