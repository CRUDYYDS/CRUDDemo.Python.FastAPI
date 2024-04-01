from fastapi import FastAPI, Depends
import models
from db import engine, SessionLocal
import crud
from sqlalchemy.orm import Session

# create the database tables on app startup or reload
models.Base.metadata.create_all(bind=engine)

# initailize FastApi instance
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# define endpoint
@app.post("/user/create")
def create_user(name: str, age: int, address: str, db: Session = Depends(get_db)):
    user = crud.create_user(db=db, name=name, age=age, address=address)
    # return object created
    return {"user": user}


# get/retrieve user
@app.get("/user/get/{id}/")  # id is a path parameter
def get_user(id: int, db: Session = Depends(get_db)):
    """
    the path parameter for id should have the same name as the argument for id
    so that FastAPI will know that they refer to the same variable
Returns a friend object if one with the given id exists, else null
    """
    user = crud.get_user(db=db, id=id)
    return user


@app.get("/user/list")
def list_users(db: Session = Depends(get_db)):
    """
    Fetch a list of all User object
    Returns a list of objects
    """
    users_list = crud.list_users(db=db)
    return users_list


@app.put("/user/update/{id}/")  # id is a path parameter
def update_user(id: int, name: str, age: int, address: str, db: Session = Depends(get_db)):
    # get friend object from database
    db_friend = crud.get_user(db=db, id=id)
    # check if friend object exists
    if db_friend:
        updated_user = crud.update_user(db=db, id=id, name=name, age=age, address=address)
        return updated_user
    else:
        return {"error": f"User with id {id} does not exist"}


@app.delete("/user/delete/{id}/")  # id is a path parameter
def delete_user(id: int, db: Session = Depends(get_db)):
    # get friend object from database
    db_user = crud.get_user(db=db, id=id)
    # check if friend object exists
    if db_user:
        return crud.delete_user(db=db, id=id)
    else:
        return {"error": f"Friend with id {id} does not exist"}


# define endpoint
@app.get("/")
def home():
    return {"Ahoy": "Captain"}