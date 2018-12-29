from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()

class User(Base):
    __tablename__ = 'person'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///:users.db:', echo=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()

# Insert into table
user = User()
user.id = 0
user.username = 'alpha'

session.add(user)
session.commit()

# Querying table
users = session.query(User).all()
for user in users:
    print(f'User with username={user.username} and id={user.id}')

session.close()