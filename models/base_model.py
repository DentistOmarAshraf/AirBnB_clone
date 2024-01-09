#!/usr/bin/env python3
import json
import uuid
from datetime import datetime

class BaseModel:

    def __init__(self, *args, **kwargs):
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        if kwargs:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                    continue
                if key == "created_at":
                    self.created_at = datetime.fromisoformat(val)
                    continue
                if key == "updated_at":
                    self.updated_at = datetime.fromisoformat(val)
                    continue
                if key != "__class__":
                    setattr(self, key, val)
        
    def __str__(self):
        string = "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
        return string

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic


"""THIS WAS FOR TESTING"""
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
