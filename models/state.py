#!/usr/bin/python3
"""Defining the 'state' model"""

from models.base_model import BaseModel


class State(BaseModel):
    """Defining the 'State' class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the instance"""
        super().__init__(*args, **kwargs)
