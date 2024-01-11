#!/usr/bin/env python3
"""Testing Class User"""
import unittest
from unittest.mock import patch
from models.user import User
from models.base_model import BaseModel
from io import StringIO
import os


class Test_user(unittest.TestCase):
    """Testing Class User"""

    def test_init(self):
        """testing __init__()"""
        a = User()
        a.email = "somemail@ml"
        a.password = "root1"
        a.first_name = "Omar"
        a.last_name = "Afifi"
        b = User()
        b.email = "othermail@ml"
        b.password = "root2"
        b.first_name = "Mostafa"
        b.last_name = "Lotfy"
        self.assertNotEqual(a.id, b.id)
        self.assertNotEqual(a.created_at, b.created_at)
        self.assertNotEqual(a.updated_at, b.updated_at)
        self.assertNotEqual(a.email, b.email)
        self.assertNotEqual(a.password, b.password)
        self.assertNotEqual(a.first_name, b.first_name)
        self.assertNotEqual(a.last_name, b.last_name)

    def test_str(self):
        """testing instance str()"""
        a = User()
        string = a.__str__()
        with patch('sys.stdout', new=StringIO()) as dis:
            print(a, end="")
            self.assertEqual(dis.getvalue(), string)

    def test_save(self):
        """testing datetime"""
        a = User()
        T1 = a.updated_at
        a.save()
        T2 = a.updated_at
        self.assertNotEqual(T1, T2)
        os.remove("file.json")

    def test_to_dict(self):
        """testing to_dict"""
        a = User()
        model_dict = a.__dict__
        to_dict_ret = a.to_dict()
        self.assertNotEqual(model_dict, to_dict_ret)
