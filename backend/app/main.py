from datetime import datetime
from fastapi import FastAPI, HTTPException
#from typing import List
#from uuid import uuid4
#from models import Priority, Error, ErrorUpdateRequest
from config.database import collection_name
from models.priority_model import Priority
from models.error_model import Error
from models.updated_error_model import ErrorUpdateRequest
import schemas
from schemas.error_schema import error_serializer, errors_serializer
from schemas.updated_error_schema import updated_error_serializer, updated_errors_serializer
import datetime

app = FastAPI()


@app.get("/")
def root():
    return {"Hello":"World"}


@app.get("/api/v1/errors")
async def fetch_errors():
    #return db
    return errors_serializer(collection_name.find())


@app.get("/api/v1/errors/{error_name}")
async def fetch_error_by_name(error_name: str):
    if collection_name.find_one({"name": error_name}) == None: 
        raise HTTPException(
        status_code=404,
        detail=f"error called {error_name} does not found")
        #return {"detail": "Not found"}
    return error_serializer(collection_name.find_one({"name": error_name}))


@app.post("/api/v1/errors")
async def register_error(new_error: Error):
    error_already_exist = collection_name.find_one({"name": dict(new_error)["name"]})
    if(error_already_exist != None):
        raise HTTPException(
            status_code=409,
            detail=f"error called {dict(new_error)['name']} already exist"
        )
    collection_name.insert_one(dict(new_error)) #last change
    return error_serializer(collection_name.find_one({"name": dict(new_error)["name"]}))


@app.delete("/api/v1/errors/{error_name}")
async def delete_error(error_name: str):

    if collection_name.find_one({'name': error_name}) != None:
        collection_name.delete_many({"name": error_name})
            #db.remove(error)
        return {f"error {error_name}":"removed successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"error called {error_name} does not found"
    )


@app.put("/api/v1/errors/{error_name}")
async def update_error(error_update: ErrorUpdateRequest, error_name: str):
    normalize_updated_error = dict(error_update)
    exist_error = collection_name.find_one({"name": error_name})
    if exist_error != None: 
        print(dict(error_update))
        if normalize_updated_error['priority'] is not None:
            collection_name.update_one({"name": error_name},{"$set": {"priority": normalize_updated_error['priority']}})
        if normalize_updated_error['involved'] is not None:
            collection_name.update_one({"name": error_name},{"$set": {"involved": normalize_updated_error['involved']}})
        if normalize_updated_error['next_step'] is not None:
            collection_name.update_one({"name": error_name},{"$set": {"next_step": normalize_updated_error['next_step']}})
        if normalize_updated_error['update_date'] is not None:
            collection_name.update_one({"name": error_name},{"$set": {"update_date": normalize_updated_error['update_date']}})
        return error_serializer(collection_name.find_one({"name": error_name}))
    print(1)
    print(dict(error_update))
    raise HTTPException(
        status_code=404,
        detail=f"error called {error_name} does not found"
    )
    