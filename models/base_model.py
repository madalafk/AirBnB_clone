#!/usr/bin/python3
"""Defines a base class for all other classes"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represents all common attributes/methods for other classes.

    Args:
        *args(any): unused
        **kwargs(dict): k-v pairs of attributes and respective values.
    """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_form)
                elif k == "__class__":
                    continue
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Print the string representation of a base model instance"""
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dict containing all k:v of __dict__ of the instance"""
        n_dict = self.__dict__.copy()
        n_dict["__class__"] = self.__class__.__name__
        n_dict["created_at"] = self.created_at.isoformat()
        n_dict["updated_at"] = self.updated_at.isoformat()
        return n_dict
