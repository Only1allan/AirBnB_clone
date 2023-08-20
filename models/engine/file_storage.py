#!/usr/bin/python3
"""
File storage class that serializes and deserializes certain instances
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """class for serialization and deserialization"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return dict objects"""
        return FileStorage.__objects

    def new(self, obj):
        """add new object to storage"""
        newkey = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[newkey] = obj

    def save(self):
        """save storage dictionary to file"""
        with open(FileStorage.__file_path, 'w')as f:
            obj = {}
            obj.update(FileStorage.__objects)
            for k, v in obj.items():
                obj[k] = v.to_dict()
            json.dump(obj, f)

    def reload(self):
        """deserialization of json to objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for k, v in temp.items():
                    name = v["__class__"]
                    del v["__class__"]
                    FileStorage.__objects[k] = eval(name + "(**v)")
        except FileNotFoundError:
            pass
