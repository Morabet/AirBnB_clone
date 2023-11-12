#!/usr/bin/python3
"""testing the 'user' model"""

import unittest
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Testing the 'User' class"""

    @classmethod
    def setUpClass(cls):
        """ setup the instance """
        cls.user = User()
        cls.user.email = "el@gmail.com"
        cls.user.password = "112233"
        cls.user.first_name = "ismail"
        cls.user.last_name = "ali"

    def test_for_instance(self):
        """ Tests instantiation of User class """
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_is_subclass(self):
        """ Test that User is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel))

    def test_for_id(self):
        self.assertEqual(str, type(User().id))

    def test_for_created_at(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_has_attributes(self):
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_email_attr(self):
        """Test that User has attr email, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_hasattr(self):
        """Test that User has attr """
        user = User()
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_password_attr(self):
        """Test that User has attr password, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_first_name_attr(self):
        """Test that User has attr first_name, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name_attr(self):
        """Test that User has attr last_name, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def test_str(self):
        """test that the str method has the correct output"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))

    def test_save(self):
        """ check if create_at not equal update_at"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)


if __name__ == '__main__':
    unittest.main()
