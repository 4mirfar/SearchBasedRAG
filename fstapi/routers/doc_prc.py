from fastapi import APIRouter


from process_docs import prr_doc



router = APIRouter(prefix="/prdoc", tags=["prDoc"])

@router.post("process_document")
async def process_documents():
    prr_doc()
    return {
        "status": "OK",
        "message": "documents sucessfully embedded"
    }