from pymongo import MongoClient

import os

def connectDB():
    try: 
        client = MongoClient(os.getenv("MONGODB_URI"))
        
        print("Connected to MongoDB")
        
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        