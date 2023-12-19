#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
<<<<<<< HEAD
from os import getenv
=======
>>>>>>> 791d92177282905c456674d2e47566bb57506da0

storage_type = getenv("HBNB_TYPE_STORAGE")

<<<<<<< HEAD

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', cascade="all,delete", backref="user")
        reviews = relationship('Review', cascade="all,delete", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
=======
class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", backref="user")
    reviews = relationship("Review", backref="user")
>>>>>>> 791d92177282905c456674d2e47566bb57506da0
