#!/usr/bin/python3
""" serialization-deserialization  """


import json
from models.base_model import BaseModel


class FileStorage():
    """ that serializes instances to a JSON file and deserializes JSON  """

    __file_path = "file.json"
    __objects = {}
    name_cls = {
                "BaseModel": BaseModel}

    def all(self):
        """ another comment """
        return self.__objects

    def new(self, obj):
        """ another comment """
        self.__objects.update({'{}.{}'.format(
            type(obj).__name__, obj.id): obj})

    def save(self):
        """ another comment """
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            if self.__objects:
                tmp = {}
                for key, obj in self.__objects.items():
                    tmp.update({key: obj.to_dict()})
                f.write(json.dumps(tmp))

    def reload(self):
        """ another comment """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                data = json.loads(f.read())
                for key, obj in sorted(data.items()):
                    obt = key.split(".")[0]
                    obtn = self.name_cls.get(obt)
                    data.update({key: obtn(**obj)})
                self.__objects = data
        except FileNotFoundError:
            pass
