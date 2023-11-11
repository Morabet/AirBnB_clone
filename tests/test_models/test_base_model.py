#!/usr/bin/python3
"""
testing the 'base_model'
"""

from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

import unittest
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for the 'BaseModel' class"""

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

    def test_3_datetime_created(self):
        """Tests if updated_at & created_at are current at creation."""

        date_now = datetime.now()
        base = BaseModel()
        diff = base.updated_at - base.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)


if __name__ == '__main__':
    unittest.main()
