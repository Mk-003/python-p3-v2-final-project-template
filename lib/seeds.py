from faker import Faker
from database import sessioncreator
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine

from models import Player




# engine = create_engine('sqlite:///rookies.db')
# Base.metadata.create_all(engine)

# sessioncreator = sessionmaker(bind=engine)
# mysession = sessioncreator()

fakedata = Faker()

print('Seeding Players')

if __name__ == '__main__':

    mysession = sessioncreator()

    for i in range(17):  
        player = Player(
            name=fakedata.name(),
            birthdate=fakedata.date_of_birth(),
            experience_years=fakedata.random_int(min=0, max=7),
            age=fakedata.random_int(min=18, max=40)
        ) 
        mysession.add(player)
    mysession.commit()  

print('All players Seeded, They should now be in your Database')
    
    
