#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the DBStorage engine."""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Represents a database storage engine.
    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """
=======
""" This is the db_storage module """
from sqlalchemy import create_engine
import os

class DBStorage:
>>>>>>> 791d92177282905c456674d2e47566bb57506da0

    __engine = None
    __session = None

    def __init__(self):
<<<<<<< HEAD
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the curret database session all objects of the given class.
        If cls is None, queries all types of objects.
        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
=======
        """ Instantiation of engine """
        user = os.getenv(HBNB_MYSQL_USER)
        pwd = os.getenv(HBNB_MYSQL_PWD)
        host = os.getenv(HBNB_MYSQL_HOST)
        db = os.getenv(HBNB_MYSQL_DB)
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)
        env = os.getenv(HBNB_ENV)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returning the objects """
        if cls is not None:
            objs = {}
            for obj in self.__session.query(cls).all():
                objs[cls.__name__ + "." + obj.id] = obj
            return objs
        else:
            objs = {}
            for obj in self.__session.query(User, State, City, Amenity, Place,
                                     Review).all():
                objs[cls.__name__ + "." + obj.id] = obj
            return objs

    def new(self, obj):
        """ Adding new objects """
        self.__session.add(obj)

    def save(self):
        """ Commiting changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete obj if not None """
>>>>>>> 791d92177282905c456674d2e47566bb57506da0
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
<<<<<<< HEAD
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()
=======
        """ Create the tables in the database """
        from sqlalchemy.orm import sessionmaker
        from models.base_model import BaseModel, Base
        from models.state import State
        from models.city import City
        from models.review import Review
        from models.amenity import Amenity
        from models.place import Place
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(expire_on_commit=True)
        Session = scoped_session(Session)
        Session.configure(bind=self.__engine)
        self.__session = Session()
>>>>>>> 791d92177282905c456674d2e47566bb57506da0
