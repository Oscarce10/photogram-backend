from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.api.v1.serializers import ResponseSerializer, SortSerializer
from app.core.handlers import CategoriesHandler

router = APIRouter()


@router.get(
    "/categories",
    tags=["Get all categories"],
    response_model=ResponseSerializer,
    responses={
        500: {"content": {
            "application/json": {
                "example": "Internal Server Error"
            }
        }, }
    },
)
async def get_categories_view():
    """ **Register Warranty**

    Pending

    **Returns**

    dict: with the warranty response information
    """

    try:
        response = CategoriesHandler.get_categories()
        return JSONResponse(
            content=response,
            status_code=response["status"]
        )
    except Exception as e:
        return JSONResponse(
            content={
                "status": 500,
                "message": str(e)
            }, status_code=500
        )


@router.get(
    "/photos",
    tags=["Get all photos"],
    response_model=ResponseSerializer,
    responses={
        500: {"content": {
            "application/json": {
                "example": "Internal Server Error"
            }
        }, }
    },
)
async def get_photos_view(
        current_page: int = 1,
        items_per_page: int = 10,
        order_by: SortSerializer = "desc"
):
    """ **Register Warranty**

    Pending

    **Returns**

    dict: with the warranty response information
    """

    try:
        response = CategoriesHandler.get_photos(
            current_page=current_page,
            items_per_page=items_per_page,
            order_by=order_by
        )
        return JSONResponse(
            content=response,
            status_code=response["status"]
        )
    except Exception as e:
        return JSONResponse(
            content={
                "status": 500,
                "message": str(e)
            }, status_code=500
        )
