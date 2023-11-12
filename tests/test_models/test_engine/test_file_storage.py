#!/usr/bin/python3
"""Testing the 'file_storage' model"""

from datetime import datetime
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import unittest

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorage(unittest.TestCase):
    """Testing the FileStorage class"""

    def test_all(self):
        """Test that 'all' method returns 'FileStorage.__objects' attr"""

        storage = FileStorage()
        all_dict = storage.all()
        self.assertEqual(type(all_dict), dict)
        self.assertIs(all_dict, storage._FileStorage__objects)

    def test_new(self):
        """test if 'new' adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                obj = value()
                obj_key = obj.__class__.__name__ + "." + obj.id
                storage.new(obj)
                test_dict[obj_key] = obj
                self.assertEqual(test_dict, storage._FileStorage__objects)

        FileStorage._FileStorage__objects = save

    def test_save(self):
        """Test saving objects to file.json"""

        if os.path.exists("file.json"):
            os.remove("file.json")
        storage = FileStorage()
        new_dict = {}

        for k, v in classes.items():
            obj = v()
            obj_key = obj.__class__.__name__ + "." + obj.id
            new_dict[obj_key] = obj

        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()

        FileStorage._FileStorage__objects = save

        for k, v in new_dict.items():
            new_dict[k] = v.to_dict()

        string = json.dumps(new_dict)

        with open("file.json", "r") as f:
            data = f.read()

        self.assertEqual(json.loads(string), json.loads(data))


if __name__ == "__main__":
    unittest.main()
