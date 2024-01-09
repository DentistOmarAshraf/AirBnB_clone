#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from io import StringIO

class Test_BaseModel(unittest.TestCase):

    def test_init(self):
        a = BaseModel()
        a.name = "someName"
        dic = a.to_dict()
        b = BaseModel(**dic)
        self.assertEqual(a.id, b.id)
        self.assertEqual(a.created_at, b.created_at)
        self.assertEqual(a.updated_at, b.updated_at)
        self.assertEqual(a.name, b.name)
        self.assertEqual(a.__class__, b.__class__)
        self.assertNotEqual(a, b)
    
    def test_id(self):
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_create(self):
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.created_at, b.created_at)

    def test_update(self):
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.updated_at, b.updated_at)

    def test_str(self):
        a = BaseModel()
        string = a.__str__()
        with patch('sys.stdout', new=StringIO()) as dis:
            print(a, end="")
            self.assertEqual(dis.getvalue(), string)

    def test_save(self):
        a = BaseModel()
        T1 = a.updated_at
        a.save()
        T2 = a.updated_at
        self.assertNotEqual(T1, T2)

    def test_to_dict(self):
        a = BaseModel()
        model_dict = a.__dict__
        to_dict_ret = a.to_dict()
        self.assertNotEqual(model_dict, to_dict_ret)
