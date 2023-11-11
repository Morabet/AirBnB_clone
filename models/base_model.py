#!/usr/bin/python3
"""
Defining the 'Base model' will contain
the base class and functions
"""

from datetime import datetime
import models
import uuid


class BaseModel:
    """
    Defining the 'BaseModel' class that defines
    all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Intialisation the BaseModel class instances.
        Args:
            id: unique id for each BaseModel.
            created_at: datetime when an instance is created.
            updated_at: datetime when an instance is created and it
                    will be updated every time you change your object
        """
        if kwargs and len(kwargs) != 0:
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
        """print out the class and its data"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
         updates the instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        # add the changes to '__objects' in file storage
        models.storage.save()

    def to_dict(self):
        """a dictionary containing all keys/values attributes"""

        new_dict = self.__dict__.copy()

        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()

        return new_dict
