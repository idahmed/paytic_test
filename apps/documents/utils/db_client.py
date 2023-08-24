from pymongo import MongoClient
from pymongo.server_api import ServerApi
from django.conf import settings


def connect():
    uri = settings.MONGO_URI
    client = MongoClient(uri, server_api=ServerApi("1"))
    db = client["paytic"]
    return db["transaction"]
