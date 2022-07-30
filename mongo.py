import os
import pymongo


def mongo_db():
    mongo_url = os.getenv('MONGO')
    client = pymongo.MongoClient(mongo_url)
    db = client['appointments']
    print('Mongo connected')
    collections(db)


def collections(db):
    specialist_collection = db['specialist']
    user_collection = db['users']
    appointment_collection = db['appointments']