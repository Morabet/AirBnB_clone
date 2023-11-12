#!/usr/bin/python3
<<<<<<< HEAD
"""Testing the 'place' model"""

from datetime import datetime
from models.place import Place
from models.base_model import BaseModel
=======
"""testing the 'place' model"""
>>>>>>> fa8cb9416d45eb621bbb042ee4ea4cd1278a33ae

import unittest


class TestPlace(unittest.TestCase):
<<<<<<< HEAD
    """Testing 'Place' class"""

    def test_is_subclass(self):
        """Test that Place is a subclass of BaseModel"""

        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_city_id_attr(self):
        """Test that 'Place' has the 'city_id' attr"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_has_user_id_attr(self):
        """Test that 'Place' has the 'user_id' attr"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")

    def test_has_name_attr(self):
        """Test that 'Place' has the 'name' attr"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_has_description_attr(self):
        """Test that 'Place' has the 'description' attr"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_has_number_rooms_attr(self):
        """Test 'Place' has the 'number_rooms' atttr"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(place.number_rooms, 0)

    def test_has_number_bathrooms_attr(self):
        """Test that 'Place' has the 'number_bathrooms'"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(place.number_bathrooms, 0)

    def test_has_max_guest_attr(self):
        """Test that 'Place' has the 'max_guest' attr"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(place.max_guest, 0)

    def test_has_price_by_night_attr(self):
        """Test that 'Place' has the 'price_by_night'"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(place.price_by_night, 0)

    def test_has_latitude_attr(self):
        """Test that 'Place' has the 'latitude' attr"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(place.latitude, 0.0)

    def test_has_longitude_attr(self):
        """Test that 'Place' has the 'longitude' attr"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(place.longitude, 0.0)

    def test_has_amenity_ids_attr(self):
        """Test that 'Place' has the 'amenity_ids' attr"""
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(len(place.amenity_ids), 0)

    def test_values(self):
        """test that the values are valid and correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        place = Place()
        new_d = place.to_dict()

        self.assertTrue("__class__" in new_d.keys())
        self.assertEqual(new_d["__class__"], "Place")

        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"],
                         place.created_at.strftime(time_format))
        self.assertEqual(new_d["updated_at"],
                         place.updated_at.strftime(time_format))

    def test_str(self):
        """test the '__str__' method"""
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))


if __name__ == "__main__":
=======
    """Testing the 'Place' class"""

    pass


if __name__ == '__main__':
>>>>>>> fa8cb9416d45eb621bbb042ee4ea4cd1278a33ae
    unittest.main()
