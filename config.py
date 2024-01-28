import os
from dotenv import load_dotenv
import pymongo
# Load environment variables from the .env file
load_dotenv()

mongo_client = pymongo.MongoClient(os.getenv("connection_string"))
