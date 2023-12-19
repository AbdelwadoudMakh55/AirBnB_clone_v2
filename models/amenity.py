#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class Amenity(BaseModel):
    """ This is the amenity class """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
