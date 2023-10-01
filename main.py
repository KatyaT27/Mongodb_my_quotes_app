from search import search_by_author, search_by_tag, search_by_tags,  print_quotes
from db import connect_to_db
from load_data import load_data_from_json  # Import the load_data function

# Connect to the MongoDB database
connect_to_db()

# Load authors from a JSON file into MongoDB (Uncomment these lines if needed)
# load_data_from_json('authors.json', 'authors')

# Load quotes from a JSON file into MongoDB (Uncomment these lines if needed)
# load_data_from_json('quotes.json', 'quotes')

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

    print_quotes(quotes)
