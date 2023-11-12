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
from models import storage
import json
import os
import unittest

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorage(unittest.TestCase):
    """Testing the FileStorage class"""

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

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
        """ testing the 'save' method"""
        obj = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload_from_nonexistent(self):
        """if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_type_objects(self):
        """ test if '__objects' is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ test if 'key' is correct"""
        obj = BaseModel()
        obj.save()
        obj_id = obj.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + obj_id)


if __name__ == "__main__":
    unittest.main()
