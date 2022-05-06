import certifi
from flask_pymongo import PyMongo
import pymongo
mongo = PyMongo()

CONNECTION_STRING = 'mongodb+srv://admin:admin@user.7bepw.mongodb.net/user?retryWrites=true&w=majority'

client = pymongo.MongoClient(CONNECTION_STRING,tlsCAFile=certifi.where())
db = client.get_database('user')
user_collection = pymongo.collection.Collection(db, 'user')

