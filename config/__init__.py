import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import sentry_sdk

from config import urls


app = FastAPI(
    title="Photogram Backend",
    description="",
    version="v1",
    docs_url="/docs"
)


sentry_sdk.init(
    os.environ.get("SENTRY_DSN"),   

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
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
