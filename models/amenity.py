#!/usr/bin/python3
"""Defining the 'amenity' model"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defining the 'Amenity' class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the instance"""
        super().__init__(*args, **kwargs)
