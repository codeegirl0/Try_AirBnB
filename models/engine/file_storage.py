#!/usr/bin/python3
"""the class of FileStorage."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """storage engine reprisentation.
    Attributes:
        __file_path (str): The file name.
        __objects (dict): The object dictionary.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """dictionary __objects returning."""
        return FileStorage.__objects

    def new(self, obj):
        """Add to  __objects using key"""
        myocnaming = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(myocnaming, obj.id)] = obj

    def save(self):
        """adding to the json file."""
        myoodictt = FileStorage.__objects
        theobdicti = {obj: myoodictt[obj].to_dict() for obj in myoodictt.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(theobdicti, f)

    def reload(self):
        """removing and cutting the json file."""
        try:
            with open(FileStorage.__file_path) as f:
                theobdicti = json.load(f)
                for m in theobdicti.values():
                    theclss_name = m["__class__"]
                    del m["__class__"]
                    self.new(eval(theclss_name)(**m))
        except FileNotFoundError:
            return
