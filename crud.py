from sqlalchemy.orm import Session

"""
Session manages persistence operations for ORM-mapped objects.
Let's just refer to it as a database session for simplicity
"""

from models import User


def create_user(db:Session, name, age, address):
    """
    function to create a user model object
    """
    # create user instance
    new_user = User(name=name, age=age, address=address)
    #place object in the database session
    db.add(new_user)
    #commit your instance to the database
    db.commit()
    #reefresh the attributes of the given instance
    db.refresh(new_user)
    return new_user


def get_user(db:Session, id:int):
    """
    get the first record with a given id, if no such record exists, will return null
    """
    db_user = db.query(User).filter(User.id==id).first()
    return db_user


def list_users(db:Session):
    """
    Return a list of all existing Friend records
    """
    all_users = db.query(User).all()
    return all_users


def update_user(db: Session, id: int, name: str, age: int, address: str):
    """
    Update a User object's attributes
    """
    db_user = get_user(db=db, id=id)
    db_user.name = name
    db_user.age = age
    db_user.address = address

    db.commit()
    db.refresh(db_user) #refresh the attribute of the given instance
    return db_user


def delete_user(db:Session, id:int):
    """
    Delete a Friend object
    """
    db_user = get_user(db=db, id=id)
    db.delete(db_user)
    db.commit() #save changes to db