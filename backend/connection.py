from pymongo import MongoClient
from os import environ

mongo_host = environ.get("MONGO_HOST", "localhost")
mongo_port = environ.get("MONGO_PORT", "27017")

mongo_uri = f"mongodb://{mongo_host}:{mongo_port}"

#MONGO_HOST = environ.get('MONGO_HOST', 'localhost')

client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)

db = client['pythonapp_db'] 

coll = db['names']