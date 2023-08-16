#!/usr/bin/python3
"""Base Class for the entire project"""

from datetime import datetime
import uuid
import models


class BaseModel:

    """Public instance attributes definition

    Args: *args - Non pair arguments
          **kwargs - pair argumentd
    """
    def __init__(self, *args, **kwargs):
    
        if args:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    v = datetime.fromisoformat(v)
                    self.__dict__[k] = v
                else:
                    self.__dict__[k] = str(v)

    def __str__(self):
        """return str representation of class object"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """updates the public instance with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary represenation of all keys and values """
        dict = self.__dict__.copy()
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        dict["id"] = self.id
        dict["__class__"] = self.__class__.__name__

        return dict
