from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.base import Base, Player

engine = create_engine('sqlite:///rookies.db')
Base.metadata.create_all(engine)

sessioncreator = sessionmaker(bind=engine)