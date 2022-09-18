#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models

    Attributes:
        id (Column): A column in a database
        created_at (Column): A column in a database
        updated_at (Column): A column in a database
    """
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)
        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)
            if key == 'created_at' or key == 'updated_at':
                setattr(self, key, datetime.fromisoformat(value))

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.tmp_dict())

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        if '_sa_instance_state' in self.__dict__:
            del self.__dict__['_sa_instance_state']
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """ Delete the current Instance from the storage """
        from models import storage
        storage.delete()

    def tmp_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        if '_sa_instance_state' in self.__dict__:
            del self.__dict__['_sa_instance_state']
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        return dictionary
