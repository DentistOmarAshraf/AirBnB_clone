#!/usr/bin/env python3
"""
Testing Place Class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.place import Place


class Test_Place(unittest.TestCase):
    """Testing Place Class"""

    model = Place()

    def test_instance(self):
        """Testing Is Instance"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model, Place)
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
        self.assertTrue(hasattr(self.model, "city_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "description"))
        self.assertTrue(hasattr(self.model, "number_rooms"))
        self.assertTrue(hasattr(self.model, "number_bathrooms"))
        self.assertTrue(hasattr(self.model, "max_guest"))
        self.assertTrue(hasattr(self.model, "price_by_night"))
        self.assertTrue(hasattr(self.model, "latitude"))
        self.assertTrue(hasattr(self.model, "longitude"))
        self.assertTrue(hasattr(self.model, "amenity_ids"))

    def test_attribute_type(self):
        """Testing Type of attr"""
        self.assertIsInstance(self.model.city_id, str)
        self.assertIsInstance(self.model.user_id, str)
        self.assertIsInstance(self.model.name, str)
        self.assertIsInstance(self.model.description, str)
        self.assertIsInstance(self.model.number_rooms, int)
        self.assertIsInstance(self.model.number_bathrooms, int)
        self.assertIsInstance(self.model.description, str)
        self.assertIsInstance(self.model.number_rooms, int)
        self.assertIsInstance(self.model.number_bathrooms, int)
        self.assertIsInstance(self.model.max_guest, int)
        self.assertIsInstance(self.model.price_by_night, int)
        self.assertIsInstance(self.model.latitude, float)
        self.assertIsInstance(self.model.longitude, float)
        self.assertIsInstance(self.model.amenity_ids, list)

    def test_addattr(self):
        """Testing add attribute"""
        self.model.some = "some"
        self.assertTrue(hasattr(self.model, "some"))


if __name__ == "__main__":
    unittest.main()
