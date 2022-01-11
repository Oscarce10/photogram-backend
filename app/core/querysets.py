import math
import os

from pymongo import MongoClient


class Queryset:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))

    def get_all_categories(self):
        db = self.client.photogram
        collection = db.categories
        return list(collection.find({}, {"_id": 0}))

    def get_all_photos(
            self,
            current_page: int,
            items_per_page: int,
            order_by: str,
    ):
        db = self.client.photogram
        collection = db.photos
        count = collection.count_documents({})
        photos = list(
            collection.find(
                {},
                {
                    "_id": 0
                }
            ).skip(
                (current_page - 1) * items_per_page
            ).limit(
                items_per_page
            ).sort(
                order_by
            )
        )
        return {
            "status": 200,
            "data": photos,
            "meta": {
                "current_page": current_page,
                "items_per_page": items_per_page,
                "total_items": count,
                "total_pages": math.ceil(count / items_per_page)
            }
        }
