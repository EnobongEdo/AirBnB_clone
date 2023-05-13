#!/usr/bin/python3
"""
A BaseModel class that defines all common attributes/methods for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
    """Defines the BaseModel class"""

    def __init__(self):
        """Initialises the Basemodel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
            Prints a dictionary representaion of the classname, id
            and dictionary
        """
        return ("[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
            Updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        baseDict = dict(self.__dict__)
        baseDict["__class__"] = self.__class__.__name__
        baseDict["created_at"] = self.created_at.isoformat()
        baseDict["updated_at"] = self.updated_at.isoformat()
        return baseDict
