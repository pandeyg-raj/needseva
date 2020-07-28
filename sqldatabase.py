from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
import datetime, os
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    username = Column(String, primary_key=True)
    hash = Column(String)

    def __init__(self, username, hash):
        self.username = username
        self.hash = hash

class Recover(Base):
    __tablename__ = 'recoverPass'
    username = Column(String, primary_key=True)
    question = Column(String)
    answer = Column(String)

    def __init__(self, username, question, answer):
        self.username = username
        self.question = question
        self.answer = answer

class Details(Base):
    __tablename__ = 'details'
    username = Column(String, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    Address = Column(String)
    Zip = Column(Integer)
    email = Column(String)
    phone = Column(Integer)

    def __init__(self, username, FirstName, LastName, Address, Zip, email, phone):
        self.username = username
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address
        self.Zip = Zip
        self.email = email
        self.phone = phone

class Queries(Base):
    __tablename__ = 'queries'
    username = Column(String, primary_key=True)
    query = Column(String)
    date = Column(String, default=datetime.datetime.today)
    def __init__(self,username,query):
        self.username = username
        self.query = query

if __name__  == "__main__":
    database_string = os.getenv('DB_STRING')
    if not database_string:
        print('no database name available, setting default')
        os.environ['DB_STRING'] = "sqlite:///needseva.db"
        print('trying again after setting')
        database_string = os.getenv('DB_STRING')
    print(database_string)
    engine2 = create_engine(database_string, echo=True)
    Base.metadata.create_all(bind=engine2)
