from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fstapi.routers import chat, doc_prc, build_index
import uvicorn 


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # or  specify methods like ["GET", "POST"]
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/v1")
app.include_router(doc_prc.router, prefix="/api/v1")
app.include_router(build_index.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7007)