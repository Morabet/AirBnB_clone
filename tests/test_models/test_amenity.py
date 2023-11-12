#!/usr/bin/python3
"""Defining the test file for 'amenity' model"""

from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel

import unittest


class TestAmenity(unittest.TestCase):
    """Testing the 'Amenity' class"""

    def test_is_subclass_of_basemodel(self):
        """Test that 'Amenity' is a subclass of 'BaseModel'"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_has_name_attr(self):
        """Test that 'Amenity' has the name attr"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_to_dict(self):
        """test 'amenity.to_dict()' has valide and correct values"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        amenity = Amenity()
        new_d = amenity.to_dict()

        self.assertTrue("id" in new_d.keys())

        self.assertTrue("__class__" in new_d.keys())
        self.assertEqual(new_d["__class__"], "Amenity")

        self.assertTrue("created_at" in new_d.keys())
        self.assertEqual(type(new_d["created_at"]), str)

        self.assertTrue("updated_at" in new_d.keys())
        self.assertEqual(type(new_d["updated_at"]), str)

        self.assertEqual(new_d["created_at"],
                         amenity.created_at.strftime(time_format))

        self.assertEqual(new_d["updated_at"],
                         amenity.updated_at.strftime(time_format))

    def test_str(self):
        """test '__str__' method"""

        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))


if __name__ == "__main__":
    unittest.main()
