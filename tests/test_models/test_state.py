#!/usr/bin/python3
"""testing the 'state' model"""

import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestState(unittest.TestCase):
    """Testing the 'State' class"""

    def test_for_instantiation(self):
        """Tests instantiation of State class."""
        st = State()
        self.assertEqual(str(type(st)), "<class 'models.state.State'>")
        self.assertIsInstance(st, State)
        self.assertTrue(issubclass(type(st), BaseModel))

    def test_for_id(self):
        """ check if id is str"""
        self.assertEqual(str, type(State().id))

    def test_for_created_at(self):
        """ check if created_at is datetime """
        self.assertEqual(datetime, type(State().created_at))

    def test_for_updated_at(self):
        """ check id update_at is datetime """
        self.assertEqual(datetime, type(State().updated_at))

    def test_for_name(self):
        """check if name is str"""
        self.assertEqual(str, type(State.name))

    def test_states_unique_ids(self):
        """ test id is unique """
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)

    def test_different_created_at(self):
        """ check the created_at are differences"""
        st1 = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st1.created_at, st2.created_at)

    def test_different_updated_at(self):
        """ check the update_at are differences"""
        st1 = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st1.updated_at, st2.updated_at)


if __name__ == '__main__':
    unittest.main()
