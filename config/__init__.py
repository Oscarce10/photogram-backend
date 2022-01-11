from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config import urls


app = FastAPI(
    title="Photogram Backend",
    description="",
    version="v1",
    docs_url="/docs"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    urls.urls
)
