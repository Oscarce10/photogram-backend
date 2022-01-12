from app.core.process import CategoriesProcess


class CategoriesHandler:
    @staticmethod
    def get_categories():
        return CategoriesProcess().get_categories()

    @staticmethod
    def get_photos(
            current_page: int,
            items_per_page: int,
            order_by: str
    ):
        return CategoriesProcess().get_photos(
            current_page=current_page,
            items_per_page=items_per_page,
            order_by=order_by
        )

    @staticmethod
    def like_dislike_photo(photo_id: int, action: str):
        return CategoriesProcess().like_dislike_photo(
            photo_id=photo_id,
            action=action
        )

