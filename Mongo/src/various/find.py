from pymongo import MongoClient

client = MongoClient()
db = client.mydatabase

authors_collections = db.authors

print(f'{db.authors.find()=}')

# print(authors_collections.find_one({fullname: 'Albert Einstein'}))

authors_collection = db.authors
author = authors_collection.find_one({'fullname': 'Albert Einstein'})
if author:
    quotes_collection = db.quotes
    quotes = quotes_collection.find({'author': author['_id']})
    print(list(quotes))