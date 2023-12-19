#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'

    if storage_type == "db":
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(Text(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
=======
from sqlalchemy import Column, Integer, String, ForeignKey

class Review(BaseModel):
    """ Review class to store review information """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), nullable=False, ForeignKey("places.id"))
    user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
>>>>>>> 791d92177282905c456674d2e47566bb57506da0
