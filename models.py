from sqlalchemy import Column, Integer, String

from db import Base

# model/table
class  User(Base):
    __tablename__ = "user"

    # users
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(20))
    age = Column(Integer)
    address = Column(String(100))