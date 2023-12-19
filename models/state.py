#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
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
