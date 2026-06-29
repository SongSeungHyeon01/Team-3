"""백그라운드 파싱 워커"""
from app.services.parsing import dispatcher, chunker
from app.services.parsing import markdown as md_svc
from app.services.indexing import bm25_index, vector_store, embedder

def process_version(version_id: int, file_path: str):
    result = dispatcher.dispatch(file_path)
    if result is None:
        _update_status(version_id, "failed"); return
    pages = result["pages"]
    md_svc.save_markdown(pages, version_id)
    chunks = chunker.chunk_pages(pages, version_id)
    _save_chunks(version_id, chunks)
    bm25_index.add_chunks([c["chunk_index"] for c in chunks], [c["text"] for c in chunks])
    vecs = embedder.encode([c["text"] for c in chunks])
    for c, v in zip(chunks, vecs):
        vector_store.add(v, meta={"version_id": version_id, "chunk": c})
    _update_status(version_id, "done")

def _save_chunks(version_id, chunks): ...
def _update_status(version_id, status): ...
