from app.core.querysets import Queryset


class CategoriesProcess:
    @staticmethod
    def get_categories():
        qs = Queryset()
        res = qs.get_all_categories()
        return {
            "status": 200,
            "data": res
        }

    @staticmethod
    def get_photos(
            current_page: int,
            items_per_page: int,
            order_by: str
    ):
        qs = Queryset()
        return qs.get_all_photos(
            current_page,
            items_per_page,
            order_by
        )

    @staticmethod
    def like_dislike_photo(photo_id: int, action: str):
        qs = Queryset()
        return qs.like_dislike_photo(photo_id, action)
