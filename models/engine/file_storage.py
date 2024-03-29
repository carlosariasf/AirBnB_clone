#!/usr/bin/python3
""" serialization-deserialization  """


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """ that serializes instances to a JSON file and deserializes JSON  """

    __file_path = "file.json"
    __objects = {}
    name_cls = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}

    def all(self):
        """ another comment """
        return self.__objects

    def new(self, obj):
        """ another comment """
        self.__objects.update({'{}.{}'.format(
            type(obj).__name__, obj.id): obj})

    def remove(self, key):
        """ another comment """
        del self.__objects[key]
        self.save()

    def update_attr(self, key, attr, value):
        """Update data form object
        """
        obj_tmp = self.__objects[key]
        self.remove(key)
        setattr(obj_tmp, attr, value)
        self.new(obj_tmp)
        self.save()

    def save(self):
        """ another comment """
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            if self.__objects:
                tmp = {}
                for key, obj in self.__objects.items():
                    tmp.update({key: obj.to_dict()})
                f.write(json.dumps(tmp))

    def counter(self, cls):
        """Counter items dic
        """
        count = 0
        dict_tmp = self.__objects
        for key, val in dict_tmp.items():
            if cls in key:
                count += 1
        print(count)

    def reload(self):
        """ another comment """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                data = f.read()
                if data:
                    data = json.loads(data)
                    for key, obj in sorted(data.items()):
                        obt = key.split(".")[0]
                        obtn = self.name_cls.get(obt)
                        data.update({key: obtn(**obj)})
                    self.__objects = data
        except FileNotFoundError:
            pass
