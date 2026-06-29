from sqlalchemy import Column, Integer, Text, ForeignKey
from app.db import Base
class Chunk(Base):
    __tablename__ = "chunks"
    id              = Column(Integer, primary_key=True)
    version_id      = Column(Integer, ForeignKey("document_versions.id"))
    page_no         = Column(Integer)
    chunk_index     = Column(Integer)
    text            = Column(Text)
    char_start      = Column(Integer)
    page_image_path = Column(Text)
    vector_id       = Column(Text)
