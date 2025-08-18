from fastapi import APIRouter

from process_docs import prr_doc
from build_faiss_index import build_faiss_index


router = APIRouter(prefix="/index_build", tags=["bldIndex"])

@router.post("build_index")
async def build_index():
    build_faiss_index()
    return {
        "status": "OK",
        "message": "faiss index built successfully"
    }