#!/usr/bin/env python3
import json
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    data = storage.all()

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
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
        else:
            storage.new(self)

    def __str__(self):
        string = "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
        return string

    def save(self):
        self.updated_at = datetime.now()
        if self.to_dict() not in BaseModel.data.values():
            storage.new(self)
            storage.save()

    def to_dict(self):
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
