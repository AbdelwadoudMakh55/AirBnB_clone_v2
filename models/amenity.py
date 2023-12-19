#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
=======
from sqlalchemy import Column, Integer, String
>>>>>>> 791d92177282905c456674d2e47566bb57506da0

storage_type = getenv("HBNB_TYPE_STORAGE")

<<<<<<< HEAD

class Amenity(BaseModel, Base):
    """ documment doc """
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary='place_amenity',
                                       back_populates="amenities")
    else:
        name = ""
=======
class Amenity(BaseModel):
    """ This is the amenity class """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = 
>>>>>>> 791d92177282905c456674d2e47566bb57506da0
