#!/usr/bin/python3
""" define module basemodel """
import uuid
from datetime import datetime
import models


class BaseModel():
    """ define class basemodel """

    def __init__(self, *args, **kwargs):
        """ define the basemodel instance """

        if (kwargs):
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                else:
                    if k == "created_at" or k == "updated_at":
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ should print string """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """  updates the updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ a dictionary containing all keys/values attributes"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()

        return (my_dict)
