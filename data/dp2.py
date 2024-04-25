#!/usr/bin/env python3

## Setup:
from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

## Connection:
MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
# specify a database
db = client.ktq3td
# specify a collection
collection = db.ClassData

## Listing Directory Contents:
path = "."

# Iterating Through the Data
for (root, dirs, file) in os.walk(path):
    for f in file:
        # print(f)
        # loading/opening the json file
        with open(f) as file:
            try:
                file_data = json.load(file)
                # print(file_data)
        # Importing JSON file into MongoDB collection
                try:
                    if isinstance(file_data, list): #is file_data each ind. file? 
                        collection.insert_many(file_data)
                        print("Successful Import: ", f)
                except Exception as e:
                    print("Error Inserting File for ", f, ":", e)
                    continue
                else:
                    collection.insert_one(file_data)
                    print("Successful Import: ", f)     
            except Exception as e:
                print("Error Loading File for ", f, ": ", e)
                
client.close()   