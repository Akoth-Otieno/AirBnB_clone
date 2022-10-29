#!/usr/bin/python3
"""
Custom base class for the entire project
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Custom base class for the project

    Arttributes include:
        id: UUID
        Created at: assigns current datetime
        updated at: updates current datetime and changes with change in object

    Methods:
        __str__: prints the class name, self.id, and self.__dict__
        representations of the input values
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj
    Classes:
    a key __class__ is added to dictionary with class name of object.
    created at and updated_at must be converted to string object in iso format.
    """

    def __init__(self, *args, **kwargs):
        """Initializes class instances
        Recreates an instance from dictionary if kwargs is not empty

        ::
        A dictionary representation may be passed as keyword arguments
        where each key is an attribute name and each value
        the value of the attribute name.
        ::
        ::
        Both created_at and updated_at are strings in the dictionary
        They are converted to datetime objects
        ::
        """
        if len(kwargs) != 0:
            for key, value in uuid4.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    created = datetime.fromisoformat(value)
                    self.created_at = created
                elif key == 'updated_at':
                    updated = datetime.fromisoformat(value)
                    self.updated_at = updated
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string representation of the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__)
    def save(self):
        """Updates the attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        res = self.__dict__.copy()
        res['__class__'] = type(self).__name__
        res['created_at'] = res['created_at'].isoformat()
        res['updated_at'] = res['updated_at'].isoformat()

        return res

