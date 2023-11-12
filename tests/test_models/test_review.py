#!/usr/bin/python3
"""testing the 'review' model"""

import unittest
from models.review import Review
from models.base_model import BaseModel
import uuid
from datetime import datetime
from time import sleep


class TestReview(unittest.TestCase):
    """Testing the 'Review' class"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.review = Review()
        cls.review.user_id = str(uuid.uuid4())
        cls.review.place_id = str(uuid.uuid4())
        cls.review.text = "St. Petesburg"

    def test_is_subclass(self):
        """ Test that Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel))

    def test_id_is_public_str(self):
        """ check if id is str """
        self.assertEqual(str, type(Review().id))

    def test_for_created_at(self):
        """ check if created_at is datetime"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_for_updated_at(self):
        """ check if update_at is datetime"""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_for_place_id(self):
        """ check if id is str"""
        self.assertEqual(str, type(Review.place_id))

    def test_reviews_unique_ids(self):
        """ test id is unique"""
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_different_created_at(self):
        """ check the created_at are differences"""
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_different_updated_at(self):
        """ check the update_at are differences"""
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)


if __name__ == '__main__':
    unittest.main()
