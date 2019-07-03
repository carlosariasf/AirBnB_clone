#!/usr/bin/python3
"""
Comments for python CML

"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
    Comment of the class Base Model

    """

    def __init__(self, *args, **kwargs):
        """
        initial definition

        """
        if kwargs:
            """
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])
            """
            self.__dict__.update(kwargs)
            self.__dict__["created_at"] = datetime.strptime(
                    self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__["updated_at"] = datetime.strptime(
                    self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at

        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values

        """
        dict_n = self.__dict__.copy()
        dict_n["__class__"] = type(self).__name__
        dict_n["updated_at"] = self.updated_at.isoformat()
        dict_n["created_at"] = self.created_at.isoformat()
        return dict_n

    def __str__(self):
        """
        Str print info

        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)
