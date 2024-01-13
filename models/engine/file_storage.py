#!/usr/bin/env python3
"""Class FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class FileStorage:
    """Class FileStorage"""
    __file_path = "file.json"
    __object = {}

    def all(self):
        """return all Data"""
        return FileStorage.__object

    def new(self, obj):
        """save instance in .__object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__object[key] = obj

    def save(self):
        """saving in .json file"""
        with open(FileStorage.__file_path, "w") as f:
            data = {}
            for k, v in FileStorage.__object.items():
                data[k] = v.to_dict()
            json.dump(data, f, indent=4)

    def reload(self):
        """reload json file to the endpoint"""
        classes = {"User": User, "State": State, "BaseModel": BaseModel,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review
                   }
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                restored = json.load(f)
                for k, v in restored.items():
                    if '__class__' in v.keys():
                        cls = classes[v['__class__']]
                        obj = cls(**v)
                        FileStorage.__object[k] = obj
                    else:
                        FileStorage.__object[k] = v
