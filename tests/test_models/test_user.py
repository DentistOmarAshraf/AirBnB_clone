#!/usr/bin/env python3
"""
Testing User Class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.user import User


class Test_User(unittest.TestCase):
    """Testing User Class"""

    model = User()

    def test_instance(self):
        """Testing Is Instance"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model, User)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_attributes(self):
        """Testing has attribute"""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertTrue(hasattr(self.model, "__init__"))

    def test_attributes_a(self):
        """Testing has attribute"""
        self.assertTrue(hasattr(self.model, "email"))
        self.assertTrue(hasattr(self.model, "password"))
        self.assertTrue(hasattr(self.model, "first_name"))
        self.assertTrue(hasattr(self.model, "last_name"))

    def test_attribute_type(self):
        """Testing Type of attr"""
        self.assertIsInstance(self.model.email, str)
        self.assertIsInstance(self.model.password, str)
        self.assertIsInstance(self.model.first_name, str)
        self.assertIsInstance(self.model.last_name, str)

    def test_addattr(self):
        """Testing add attribute"""
        self.model.some = "some"
        self.assertTrue(hasattr(self.model, "some"))


if __name__ == "__main__":
    unittest.main()
