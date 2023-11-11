#!/usr/bin/python3
"""
Defining the 'file_storage' module
will be used to store objects in files as a Json Format
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }


class FileStorage:
    """
    Defining the 'FileStorage' class
    to implement (serialization <-> deserialization) of objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__class__.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__class__.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        path = self.__class__.__file_path
        data = {}

        for k, v in self.__class__.__objects.items():
            data[k] = v.to_dict()

        with open(path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """deserializes the JSON file to __objects"""

        path = self.__class__.__file_path
        data = {}

        try:
            with open(path, "r") as file:
                data = json.load(file)

            for k, v in data.items():
                self.__class__.__objects[k] = classes[v["__class__"]](**v)

        except FileNotFoundError:
            pass
