#!/usr/bin/python3
"""Testing the "city" model"""

from datetime import datetime
from models.city import City
from models.base_model import BaseModel

import unittest


class TestCity(unittest.TestCase):
    """Testing the 'City' class"""

    def test_is_subclass_of_basemode(self):
        """Test that 'City' is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_has_name_attr(self):
        """Test that 'City' has the name attr"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_values(self):
        """test that values are valid and correct in 'to_dict()'"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        city = City()
        new_d = city.to_dict()

        self.assertTrue("__class__" in new_d.keys())
        self.assertEqual(new_d["__class__"], "City")

        self.assertTrue("created_at" in new_d.keys())
        self.assertEqual(type(new_d["created_at"]), str)

        self.assertTrue("updated_at" in new_d.keys())
        self.assertEqual(type(new_d["updated_at"]), str)

        self.assertEqual(new_d["created_at"],
                         city.created_at.strftime(time_format))
        self.assertEqual(new_d["updated_at"],
                         city.updated_at.strftime(time_format))


if __name__ == "__main__":
    unittest.main()
