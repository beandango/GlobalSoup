import os
from pymongo import MongoClient

mongo = MongoClient(os.environ['MONGO_URL'])
db = mongo['Soup']
Usages = db['usages']

async def get_and_increment_usage(user_id: int):
    document = Usages.find_one({"_id": user_id})

    if document is not None:
        # If user exists, increment the 'total' field and return the new value
        new_total = document['total'] + 1
        Usages.update_one({"_id": user_id}, {"$set": {"total": new_total}})
        return new_total
    else:
        # If user does not exist, create a new document with 'total' field set to 1
        Usages.insert_one({"_id": user_id, "total": 1})
        return 1

async def get_usage(user_id: int):
    document = Usages.find_one({"_id": user_id})

    if document is not None:
        # If user exists, return the value
        return document['total']
    else:
        return 0