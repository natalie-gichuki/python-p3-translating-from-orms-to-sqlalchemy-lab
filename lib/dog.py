from models import Dog, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_table(base, engine):
    Base.metadata.create_all(engine)
    pass

def save(session, dog):
    session.add(dog)
    session.commit()
    pass

def get_all(session):
    return session.query(Dog).all()
    pass

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()
    pass

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()
    pass

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    pass

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    pass


#id | name  | breed
#---------------------
#1  | Joey  | cocker spaniel
#And you run this code:

#joey = session.query(Dog).filter_by(name="Joey").first()
#update_breed(session, joey, "bulldog")
#Now the database will look like this:


#id | name  | breed
#---------------------
#1  | Joey  | bulldog
