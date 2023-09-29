import json
from mongoengine import connect, Document, StringField, ListField, ReferenceField, ObjectIdField

import pymongo


# MongoDB connection settings
MONGO_URI = "mongodb+srv://web13user:1234@cluster0.kgddv8w.mongodb.net/"
DB_NAME = "web13"

# Function to load JSON data into MongoDB


# Define Mongoengine models for authors and quotes
class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField()


# Connect to the MongoDB database
connect(DB_NAME, host=MONGO_URI)

# Function to load JSON data into MongoDB


def load_data_from_json(file_path, collection_name):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        collection = None

        if collection_name == 'authors':
            collection = Author
        elif collection_name == 'quotes':
            collection = Quote

        if collection:
            for item in data:
                if collection_name == 'quotes':
                    # Find the author in the Author collection and set it as a ReferenceField
                    author = Author.objects(fullname=item['author']).first()
                    if author:
                        item['author'] = author
                    else:
                        print(
                            f"Author '{item['author']}' not found for quote: {item['quote']}")

                collection(**item).save()


# Load authors from a JSON file into MongoDB
load_data_from_json('web13/authors.json', 'authors')

# Load quotes from a JSON file into MongoDB
load_data_from_json('web13/quotes.json', 'quotes')

# Function to search quotes by author name


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


# Main loop for the script
while True:
    command = input("Enter a command (name, tag, tags, exit): ").strip()

    if command == "exit":
        print("Exiting the script.")
        break
    elif command.startswith("name:"):
        author_name = command.split(":", 1)[1].strip()
        quotes = search_by_author(author_name, "quotes")
    elif command.startswith("tag:"):
        tag = command.split(":", 1)[1].strip()
        quotes = search_by_tag(tag, "quotes")
    elif command.startswith("tags:"):
        tags = command.split(":", 1)[1].strip()
        quotes = search_by_tags(tags, "quotes")
    else:
        print("Invalid command. Please use 'name:', 'tag:', 'tags:', or 'exit'.")
        continue

    # Print the search results in UTF-8 format
    for quote in quotes:
        print(quote["quote"].encode("utf-8"))
