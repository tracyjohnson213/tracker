# import the MongoClient class
from pymongo import MongoClient

# create an instance of MongoClient()
client = MongoClient(
    host="mongodb+srv://admin:1studentDeveloper@firstcluster.b5ihz.mongodb.net/tracker?retryWrites=true&w=majority",
    serverSelectionTimeoutMS=3000,  # 3 second timeout
    username="admin",
    password="1studentDeveloper"
)

# get the server information
server_info = client.server_info()
print(server_info)
print("\nserver info keys:", server_info.keys())

# get the MongoDB server version string
print("\nserver version:", server_info["version"])

# get the database_names from the MongoClient()
database_names = client.list_database_names()
print("\ndatabases:", database_names)

# create database & collection instances
db = client.some_db
col = db.some_col

# find one document stored on the collection
doc = col.find_one()
print("\nfind_one() result:", doc)
