import pymongo

DEFAULT_CONNECTION_URL = "mongodb://localhost:27017/"
DB_NAME = "pybron_1"
client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)

#create DB
database = client[DB_NAME]

record = {
    'company_name':"pybron",
    "product":"Affordable_AI",
    'course_offered': "deep learning for computer vission"
}
collection_name = "pybron_product"
collection = database[collection_name]

collection.insert_one(record)
