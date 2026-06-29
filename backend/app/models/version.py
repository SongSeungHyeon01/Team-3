from sqlalchemy import Column, Integer, Text, Boolean, DateTime, ForeignKey
from app.db import Base
class DocumentVersion(Base):
    __tablename__ = "document_versions"
    id               = Column(Integer, primary_key=True)
    document_id      = Column(Integer, ForeignKey("documents.id"))
    original_name    = Column(Text)
    original_path    = Column(Text)
    storage_path     = Column(Text)
    markdown_path    = Column(Text)
    file_format      = Column(Text)
    file_size        = Column(Integer)
    version_label    = Column(Text)
    page_count       = Column(Integer)
    parse_status     = Column(Text, default="pending")
    file_modified_at = Column(DateTime)
    uploaded_at      = Column(DateTime)
    visibility       = Column(Text, default="all")
