#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the State class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import os
import models
from models.city import City
=======
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
>>>>>>> 791d92177282905c456674d2e47566bb57506da0


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
<<<<<<< HEAD
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

    else:
        name = ""

        @property
        def cities(self):
            """Return City list"""
            state_list = []
            obj_dict = models.storage.all(City)
            for key, value in obj_dict.items():
                if value.state_id == self.id:
                    state_list.append(obj_dict[key])
            return state_list
=======
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        from models import storage
        obj_list = storage.all()
        cities = []
        for obj in obj_list:
            if type(obj) is City:
                if obj.state_id == self.id:
                    cities.append(obj)
        return cities
>>>>>>> 791d92177282905c456674d2e47566bb57506da0
