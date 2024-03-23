from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, Column, String, Date

Base = declarative_base()  

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    birthdate = Column(Date())
    experience_years = Column(Integer())
    age = Column(Integer())

    def __repr__(self):
        return f'Player(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'age={self.age})'

