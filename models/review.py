#!/usr/bin/python3
"""Defining the 'review' model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defining the 'Review' class"""

    place_id = ""
    user_id = ""

    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize the instance"""

        super().__init__(*args, **kwargs)
