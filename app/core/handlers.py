from app.core.process import CategoriesProcess


class CategoriesHandler:
    @staticmethod
    def get_categories():
        return CategoriesProcess().get_categories()
