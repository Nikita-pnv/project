from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///./todo.db'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(engine)

Base = declarative_base() 

