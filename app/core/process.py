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
