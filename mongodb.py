from pymongo import MongoClient
from dotenv import load_dotenv
from typing import List, Dict
import os

# take environment variables from .env
load_dotenv()


class EasyMongo:
    """
    A simple wrapper for MongoDB Client.
    """

    def __init__(self):
        """
        Constructor for EasyMongo.
        """
        self.URI = os.getenv("MONGO_URI")
        self.DB = os.getenv("MONGO_DB")
        self.COLLECTION = os.getenv("MONGO_COLLECTION")

    def get_database(self):
        """
        Create a connection to MongoDB Atlas url and return NoSQL Database.
        """
        client = MongoClient(self.URI)

        # Connect the database
        return client[self.DB]

    def get_collection(self):
        """
        Get collection from Database.
        """
        dbname = self.get_database()
        return dbname[self.COLLECTION]

    def insert_many(self, documents: List[Dict]):
        """
        Insert multiple documents to MongoDB.

        :param documents: List of Dictionaries.
        :type documents: List[Dict]
        """
        collection = self.get_collection()

        try:
            # Insert documents
            result = collection.insert_many(documents)
            print(f"Inserted {len(result.inserted_ids)} documents")
            print(f"Inserted document IDs: {result.inserted_ids}")
        except Exception as e:
            print(f"Error: {e}")

    def test_data(self):
        """
        Dummy data to test MongoDB connection.
        """
        user_content = {"role": "user", "content": "What is machine learning in 200 characters?"}
        ai_content = {"role": "assistant", "content": "Machine learning is a subset of artificial intelligence that "
                                                      "enables computers to learn and improve their performance on a "
                                                      "task without explicitly programmed instructions, by using "
                                                      "algorithms and statistical models to analyze and learn "
                                                      "from data."}
        user_content2 = {"role": "user", "content": "What is deep learning in 200 characters?"}
        ai_content2 = {"role": "assistant", "content": "Deep learning is a subset of machine learning that utilizes "
                                                       "neural networks with multiple layers to learn and represent "
                                                       "complex patterns in data. It enables AI models to recognize "
                                                       "and make decisions based on intricate relationships within "
                                                       "the data, leading to improved accuracy and efficiency in "
                                                       "various applications such as image recognition, natural "
                                                       "language processing, and speech recognition."}

        self.insert_many([user_content, ai_content, user_content2, ai_content2])
