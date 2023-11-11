#!/usr/bin/python3
"""Defining the 'user' module"""

from models.base_model import BaseModel


class User(BaseModel):
    """Implementing the 'User' class to manipulate users data"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the instance"""

        super().__init__(*args, **kwargs)
