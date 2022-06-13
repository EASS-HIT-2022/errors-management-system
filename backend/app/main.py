from datetime import datetime
from fastapi import FastAPI, HTTPException
from typing import List
from uuid import uuid4
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

'''db: List[Error] = [
    Error(
        id=uuid4(),
        name="404 NOT FOUND",
        priority=Priority.blocker,
        involved=['David', 'Moshe', 'Shay', 'Saar'],
        next_step="Update the analysts and write all to On-call channel",
        accept_date=datetime.date(2022,4,25),
        ),
    Error(
        id=uuid4(),
        name="200 OK",
        priority=Priority.low,
        involved=['David Rimon', 'Chen Ben Ezra'],
        next_step="keep monitor",
        accept_date=datetime.date(2022,2,2),
        )
]'''

'''local error serializer
def error_serializer(error) -> dict:
    serialize_error = {
        "id": str(error["_id"]),
        "name": error["name"],
        "priority": error["priority"],
        "involved": error["involved"],
        "next_step": error["next_step"],
        "accept_date": error["accept_date"],
    }
    if error["update_date"] != None:
        serialize_error["update_date"] = error["update_date"]
    return serialize_error

def errors_serializer(errors) -> list:
    return [error_serializer(error) for error in errors]'''


@app.get("/")
def root():
    return {"Hello":"World"}


@app.get("/api/v1/errors")
async def fetch_errors():
    #return db
    return errors_serializer(collection_name.find())


@app.get("/api/v1/errors/{error_name}")
async def fetch_error_by_name(error_name: str):
    '''for error in db:
        if error.name == error_name:
            return error
    raise HTTPException(
        status_code=404,
        detail=f"error called {error_name} does not found"
    )'''
    return error_serializer(collection_name.find_one({"name": error_name}))

# still needs to fix
@app.post("/api/v1/errors")
async def register_error(new_error: Error):
    '''for error in db:
        if error.name == new_error.name:
            raise HTTPException(
                status_code = 409,
                detail=f"error called {new_error.name} already exists"
            )
    db.append(new_error)
    return {"id":new_error.id}'''
    #error = collection_name.insert_one(dict(new_error))
    #return {"id": error["_id"]}
    collection_name.insert_one(dict(new_error)) #last change
    #return dumps(new_error)
    return error_serializer(collection_name.find_one({"name": dict(new_error)["name"]}))



@app.delete("/api/v1/errors/{error_name}")
async def delete_error(error_name: str):
    #for error in db:
    #    if error.name == error_name:
    #if (collection_name > 0):
    if 'name' in collection_name.find_one({'name': error_name}).keys():
        collection_name.delete_many({"name": error_name})
            #db.remove(error)
        return {f"error {error_name}":"removed successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"error called {error_name} does not found"
    )


@app.put("/api/v1/errors/{error_name}")
async def update_error(error_update: ErrorUpdateRequest, error_name: str):
    for error in db:
        if error.name == error_name:
            if error_update.priority is not None:
                error.priority = error_update.priority
            if error_update.involved is not None:
                error.involved = error_update.involved
            if error_update.next_step is not None:
                error.next_step = error_update.next_step
            error.update_date = error_update.update_date
            return {f"error {error_update.name}":"updated seccessfully"}
    raise HTTPException(
        status_code=404,
        detail=f"error called {error_name} does not found"
    )
    