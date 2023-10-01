import pymongo
from models import Author, Quote

MONGO_URI = "mongodb+srv://web13user:1234@cluster0.kgddv8w.mongodb.net/"
DB_NAME = "web13"


def search_by_author(author_name, collection):
    # Create a MongoDB client
    client = pymongo.MongoClient(MONGO_URI)

    # Access the database and collection
    db = client[DB_NAME]

    # Search for quotes by author name in the "quotes" collection
    # Note the change in query structure
    query = {"author.fullname": author_name}
    quotes = db[collection].find(query)

    return list(quotes)

# Function to search quotes by tag


def search_by_tag(tag, collection):
    # Create a MongoDB client
    client = pymongo.MongoClient(MONGO_URI)

    # Access the database and collection
    db = client[DB_NAME]

    # Search for quotes by tag in the "quotes" collection
    query = {"tags": tag}
    quotes = db[collection].find(query)

    return list(quotes)

# Function to search quotes by a combination of tags


def search_by_tags(tags, collection):
    # Create a MongoDB client
    client = pymongo.MongoClient(MONGO_URI)

    # Access the database and collection
    db = client[DB_NAME]

    # Split the input tags by commas
    tag_list = tags.split(",")

    # Search for quotes with any of the specified tags in the "quotes" collection
    query = {"tags": {"$in": tag_list}}
    quotes = db[collection].find(query)

    return list(quotes)


def print_quotes(quotes):
    for quote in quotes:
        print(quote["quote"].encode("utf-8"))
