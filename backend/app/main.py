"""FastAPI 앱 진입점"""
from fastapi import FastAPI
from app.routers import upload, search, documents, admin
from app.db import Base, engine
Base.metadata.create_all(bind=engine)
app = FastAPI(title="사내 지식관리 플랫폼 API", version="1.0.0")
app.include_router(upload.router,    prefix="/api")
app.include_router(search.router,    prefix="/api")
app.include_router(documents.router, prefix="/api")
app.include_router(admin.router,     prefix="/api")
