import json
from models import Author, Quote


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
                    author_name = item.get('author')
                    if author := Author.objects(fullname=author_name).first():
                        item['author'] = author
                    else:
                        print(
                            f"Author '{author_name}' not found for quote: {item['quote']}")

                collection(**item).save()
