import os

from pymongo import MongoClient


class Queryset:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))

    def get_all_categories(self):
        db = self.client.photogram
        collection = db.categories
        return list(collection.find({}, {"_id": 0}))
