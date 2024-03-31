import pymongo
import os
from pymongo.errors import DuplicateKeyError

url = os.getenv("mongodb")
url = "mongodb+srv://awstestuser1998:awstestuser1998@cluster0.nb2lq1w.mongodb.net/"

client = pymongo.MongoClient(url)