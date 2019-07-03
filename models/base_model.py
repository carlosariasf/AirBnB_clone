#!/usr/bin/python3
""" Comments for python CML"""


import uuid
import datetime
import models


class BaseModel():
    """ Comment of the class Base Model """

    def __init__(self, *args, **kwargs):
        """  initial definition """
        if kwargs:
            """
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])
            """
            self.__dict__.update(kwargs)
            self.__dict__["created_at"] = datetime.datetime.strptime(
                    self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__["updated_at"] = datetime.datetime.strptime(
                    self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """ updates the public instance attribute updated_at """
        models.storage.save()
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values """
        dict_n = self.__dict__
        dict_n["updated_at"] = self.updated_at.isoformat()
        dict_n["created_at"] = self.created_at.isoformat()
        dict_n["__class__"] = self.__class__.__name__
        return dict_n

    def __str__(self):
        """ Str print info  """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
