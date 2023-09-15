import pymongo

# MongoDB connection settings
MONGO_URI = "mongodb+srv://web13user:MXiZgtXDqEC5hN8U@cluster0.kgddv8w.mongodb.net/"
DB_NAME = "web13"

# Function to search quotes by author name
def search_by_author(author_name, collection):
    # Create a MongoDB client
    client = pymongo.MongoClient(MONGO_URI)

    # Access the database and collection
    db = client[DB_NAME]

    # Search for quotes by author name in the "quotes" collection
    query = {"author.fullname": author_name}  # Note the change in query structure
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
