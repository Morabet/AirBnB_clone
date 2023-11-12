#!/usr/bin/python3
"""testing the 'base_model' """

from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

import unittest
from unittest import mock
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for the 'BaseModel' class"""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """remove test methods"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """reset FileStorage"""
        FileStorage._FileStorage__objects = {}

        # check if a file was created and remove it
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    # ------------------
    # ---- testing -----

    def test_instantiation(self):
        """Test the instantiation of 'BaseModel' class."""

        self.resetStorage()

        b = BaseModel()
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_init_no_args(self):
        """Testing initialization without args"""

        self.resetStorage()

        base = BaseModel()

        self.assertTrue(hasattr(base, "id"))
        self.assertEqual(type(getattr(base, "id")), str)
        self.assertTrue(hasattr(base, "created_at"))
        self.assertEqual(type(getattr(base, "created_at")), datetime)
        self.assertTrue(hasattr(base, "updated_at"))
        self.assertEqual(type(getattr(base, "updated_at")), datetime)

    def test_init_kwargs(self):
        """Testing initialization with kwargs"""
        self.resetStorage()

        args = {"name": "john wick", "age": 42}
        base = BaseModel(**args)
        self.assertTrue(hasattr(base, "name"))
        self.assertEqual(type(getattr(base, "name")), str)
        self.assertEqual(getattr(base, "name"), "john wick")
        self.assertTrue(hasattr(base, "age"))
        self.assertEqual(type(getattr(base, "age")), int)
        self.assertEqual(getattr(base, "age"), 42)

    def test_datetime_created(self):
        """Tests if updated_at & created_at are current at creation."""

        date_now = datetime.now()
        base = BaseModel()
        diff = base.updated_at - base.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_to_dict(self):
        """Test obj.to_dict()"""

        b = BaseModel()
        b.name = "Ali"
        b.my_number = 89
        d = b.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Ali")
        self.assertEqual(d['my_number'], 89)

    def test_to_dict_values(self):
        """test 'to_dict()' values are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(type(d["created_at"]), str)
        self.assertEqual(type(d["updated_at"]), str)
        self.assertEqual(d["created_at"], b.created_at.strftime(time_format))
        self.assertEqual(d["updated_at"], b.updated_at.strftime(time_format))

    def test_str(self):
        """test '__str__'"""
        b = BaseModel()
        string = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(string, str(b))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that 'save' method updates `updated_at` and calls
        `storage.save`"""
        b = BaseModel()
        old_created_at = b.created_at
        old_updated_at = b.updated_at
        b.save()
        new_created_at = b.created_at
        new_updated_at = b.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)


if __name__ == "__main__":
    unittest.main()
