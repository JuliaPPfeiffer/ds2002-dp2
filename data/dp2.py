#!/usr/bin/env python3

## Setup:
from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

## Connection:
MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='JuliaPPfeiffer', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
# specify a database
db = client.ktq3td
# specify a collection
collection = db.ClassData

## Listing Directory Contents:
path = "."

# Iterating Through the Data
for (root, dirs, file) in os.walk(path):
    for f in file:
        print(f)
        # loading/opening the json file
        with open(f) as file:
            file_data = json.load(file)
            print(file_data)
            # inserting json file into collection
        # if isinstance(file_data, list):
        #     collection.insert_many(file_data)  
        # else:
        #     collection.insert_one(file_data)    


        # need to find an 'exception' command 
        # allows files to continue importing when error occurs


## Importing: code to insert single JSON file into MongoDB

# Loading or Opening the json file

     
# # Inserting the loaded data in the collection




## Testing your collection----
# use ktq3td               # specify your database name
# db.ClassData.drop()    # where COLLECTION is the name of your collection


## Import Count----- write this in count.txt

# number of docs imported; 
# number of docs that couldn't be imported- is this supposed to be 0?
# number of corruped documents in the fileset