from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# define sqlite connection url
SQLALCHEMY_DATABASE_URL = "postgresql://root:123456@localhost:5432/postgres"

# create new engine instance
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


