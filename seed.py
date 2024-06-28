"""seed file to make sample data for db"""

from app import app
from models import db, Pet

# Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()
    Pet.query.delete()
    
    # add sample pets
    p1 = Pet(name="Olive", species="cat", photo_url="https://hips.hearstapps.com/hmg-prod/images/cute-cat-photos-1593441022.jpg?crop=0.670xw:1.00xh;0.167xw,0&resize=640:*", age=4, notes="Kind of cute, kind of chonk")
    p2 = Pet(name="Cookie", species="dog", photo_url="https://cdn.britannica.com/55/236455-050-58F1F4FD/Bichon-frise-dog.jpg", age=17, notes="A little blind")
    
    db.session.add_all([p1,p2])
    db.session.commit()
    