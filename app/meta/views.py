from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse


router = APIRouter()


@router.get("/", tags=["meta"])
async def root():
    return JSONResponse(
        status_code=200,
        content={"Communications log": "API REST is ready"}
    )


@router.get("/version", tags=["meta"])
async def version():
    response = {
        "version": "v1",
        "message": "API REST version"
    }
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response
    )


@router.get("/health", tags=["status"])
async def health_check():
    response = {"status": "ok"}
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response
    )