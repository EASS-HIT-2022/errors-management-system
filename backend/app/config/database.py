from pymongo import MongoClient
from models.error_model import Error
from models.priority_model import Priority
from uuid import uuid4
from typing import List
import datetime



client = MongoClient("mongodb://root:rootpassword@mongo:27017")
db = client["error_application"]
collection_name = db["errors"]

first_error = Error(
        #id=uuid4(),
        name="404 NOT FOUND",
        priority=Priority.blocker,
        involved=['David', 'Moshe', 'Shay', 'Saar'],
        next_step="Update the analysts and write all to On-call channel",
        accept_date=datetime.datetime(2022,4,25),
        )
second_error = Error(
        #id=uuid4(),
        name="200 OK",
        priority=Priority.low,
        involved=['David Rimon', 'Chen Ben Ezra'],
        next_step="keep monitor",
        accept_date=datetime.datetime(2022,2,2),
        )

errors_list = [
    first_error,
    second_error
]

'''config_list =  []

cur = collection_name.find()

result = list(cur)

if len(result) == 0:
        #for error in errors_list:
        config_list.append(dict(errors_list))
        
collection_name.insert_many(config_list)'''