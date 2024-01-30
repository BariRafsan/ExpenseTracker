import os
from dotenv import load_dotenv
import pymongo
from icecream import ic
# Load environment variables from the .env file
load_dotenv()
ic("Loading environment variables")
mongo_client = pymongo.MongoClient(os.getenv("connection_string"))
