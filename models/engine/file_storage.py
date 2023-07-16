#!/usr/bin/python3
"""Implements serialization and deserialization of objects"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON and deserializes JSON to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file path"""
        dict_1 = FileStorage.__objects
        obj_dict = {i: dict_1[i].to_dict() for i in dict_1.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                a_dict = json.load(f)
                for obj in a_dict.values():
                    name = obj["__class__"]
                    if isinstance(name, str) and type(eval(name)) == type:
                        self.new(eval(name)(**obj))
