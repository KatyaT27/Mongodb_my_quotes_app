from mongoengine import connect

MONGO_URI = "mongodb+srv://web13user:1234@cluster0.kgddv8w.mongodb.net/"
DB_NAME = "web13"


def connect_to_db():
    connect(DB_NAME, host=MONGO_URI)
