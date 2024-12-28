from pymongo import MongoClient

class MongoHandler:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]


    # Saves processed lesson chunks into the MongoDB database.
    def insert_lesson_chunks(self, lesson_id, chunks):
        try:
            collection = self.db["lesson_chunks"]
            document = {"lessonId": lesson_id, "chunks": chunks}
            collection.insert_one(document)
        except Exception as e:
            print(f"Error inserting lesson chunks: {e}")

    # Retrieves saved lesson chunks from the MongoDB database for further use.
    def get_lesson_chunks(self, lesson_id):
        try:
            collection = self.db["lesson_chunks"]
            result = collection.find_one({"lessonId": lesson_id})
            if not result:
                return None
            return result.get("chunks", [])
        except Exception as e:
            print(f"Erro retrieving lesson chunks: {e}")
            return None