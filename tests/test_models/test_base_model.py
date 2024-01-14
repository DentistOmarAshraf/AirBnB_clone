#!/usr/bin/env python3
"""
Testing BaseModel Class
"""
import unittest
import models
import os
import uuid
from io import StringIO
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """BaseModel Tests"""

    model_a = BaseModel()
    model_b = BaseModel()

    def test_init(self):
        """Testing __init__(**kwargs)"""
        model_c = BaseModel(**(self.model_a.to_dict()))
        self.assertEqual(self.model_a.id, model_c.id)
        self.assertEqual(self.model_a.created_at, model_c.created_at)
        self.assertEqual(self.model_a.updated_at, model_c.updated_at)
        self.assertNotEqual(self.model_a, model_c)
        self.assertEqual(self.model_a.to_dict(), model_c.to_dict())

    def test_instance(self):
        """Testing Is Instance"""
        self.assertIsInstance(self.model_a, BaseModel)
        self.assertIsInstance(self.model_b, BaseModel)

    def test_id(self):
        """Testing UUID4"""
        self.assertNotEqual(self.model_a.id, self.model_b.id)
        self.assertEqual(type(self.model_a.id), str)
        self.assertEqual(type(self.model_b.id), str)
        self.assertIsInstance(uuid.UUID(self.model_a.id), uuid.UUID)

    def test_datetime(self):
        """Testing DateTime"""
        self.assertIsInstance(self.model_a.created_at, datetime)
        self.assertIsInstance(self.model_b.created_at, datetime)
        self.assertIsInstance(self.model_a.updated_at, datetime)
        self.assertIsInstance(self.model_b.updated_at, datetime)
        datetimeiso = self.model_a.created_at.isoformat()
        from_dict = self.model_a.to_dict()["created_at"]
        self.assertEqual(datetimeiso, from_dict)

    def test_represent_str(self):
        """Testing instance __str__()"""
        string = self.model_a.__str__()
        with patch('sys.stdout', new=StringIO()) as dis:
            print(self.model_a, end="")
            self.assertEqual(dis.getvalue(), string)
        string = self.model_b.__str__()
        with patch('sys.stdout', new=StringIO()) as dis:
            print(self.model_b, end="")
            self.assertEqual(dis.getvalue(), string)

    def test_save(self):
        """Testing instance save()"""
        t1 = self.model_a.updated_at
        self.model_a.save()
        t2 = self.model_b.updated_at
        self.assertNotEqual(t1, t2)
        self.assertTrue(os.path.exists("file.json"))

    def test_storage_object(self):
        """Testing Storage new method"""
        restored = models.storage.all()
        key = "BaseModel.{}".format(self.model_a.id)
        self.assertEqual(restored[key], self.model_a)
        key = "BaseModel.{}".format(self.model_b.id)
        self.assertEqual(restored[key], self.model_b)
        os.remove("file.json")

    def test_to_dict(self):
        """Testing to_dict"""
        model_dict = self.model_a.__dict__
        to_dict_ret = self.model_a.to_dict()
        self.assertNotEqual(model_dict, to_dict_ret)

    def test_addattr(self):
        """Testing adding attribute"""
        self.model_a.some = "some"
        self.model_a.num = 30
        self.assertTrue(hasattr(self.model_a, "some"))
        self.assertTrue(hasattr(self.model_a, "num"))
        self.assertIsInstance(self.model_a.some, str)
        self.assertIsInstance(self.model_a.num, int)


if __name__ == "__main__":
    unittest.main()
