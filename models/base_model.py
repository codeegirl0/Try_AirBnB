#!/usr/bin/python3
"""The class of BaseModel."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ BaseModel reprisentation."""

    def __init__(self, *args, **kwargs):
        """create the BaseModel.
        Arguments:
            *args (any): it is unused.
            **kwargs (dict): the value and keys attributes.
        """
        timing = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timing)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """updating date time."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """the BaseModel instance dictionary.
        it has the pair representing.
        """
        myrrdic = self.__dict__.copy()
        myrrdic["created_at"] = self.created_at.isoformat()
        myrrdic["updated_at"] = self.updated_at.isoformat()
        myrrdic["__class__"] = self.__class__.__name__
        return myrrdic

    def __str__(self):
        """returning the pair."""
        thecname = self.__class__.__name__
        return "[{}] ({}) {}".format(thecname, self.id, self.__dict__)
