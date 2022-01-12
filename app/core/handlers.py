from app.core.process import CategoriesProcess, PhotosProcess


class CategoriesHandler:
    @staticmethod
    def get_categories():
        return CategoriesProcess().get_categories()

    @staticmethod
    def get_category(category_id: int):
        return CategoriesProcess().get_category(category_id)

    @staticmethod
    def get_photos(
            current_page: int,
            items_per_page: int,
            order_by: str
    ):
        return PhotosProcess().get_photos(
            current_page=current_page,
            items_per_page=items_per_page,
            order_by=order_by
        )

    @staticmethod
    def like_dislike_photo(photo_id: int, action: str):
        return PhotosProcess().like_dislike_photo(
            photo_id=photo_id,
            action=action
        )
