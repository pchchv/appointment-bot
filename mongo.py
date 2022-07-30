import os
import pymongo


def mongo_db():
    mongo_url = os.getenv('MONGO')
    client = pymongo.MongoClient(mongo_url)
    db = client.test
    print('Mongo connected')
