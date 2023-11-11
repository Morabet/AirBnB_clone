#!/usr/bin/python3
"""Defining the 'city' model"""

from models.base_model import BaseModel


class City(BaseModel):
    """Defining the 'City' class"""

    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """Initialize from parent class"""
        super().__init__(*args, **kwargs)
