from fastapi import FastAPI
from config import urls


app = FastAPI(
    title="Photogram Backend",
    description="",
    version="v1",
    docs_url="/documentation"
)

app.include_router(
    urls.urls
)
