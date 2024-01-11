#!/usr/bin/env python3
"""Class FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
import models


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
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            data = {}
            for k, v in FileStorage.__object.items():
                data[k] = v.to_dict()
            json.dump(data, f, indent=4)

    def reload(self):
        """reload json file to the endpoint"""
        classes = {"BaseModel": BaseModel, "User": User}
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                restored = json.load(f)
                for k, v in restored.items():
                    cls = classes[v['__class__']]
                    obj = cls(**v)
                    FileStorage.__object[k] = obj
        except FileNotFoundError:
            pass
