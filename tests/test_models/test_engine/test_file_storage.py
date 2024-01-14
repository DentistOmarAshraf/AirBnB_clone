#!/usr/bin/env python3
"""
Testing FileStorage Class
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class Test_FileStorage(unittest.TestCase):
    """Testing FileStorage Class"""

    model_st = FileStorage()
    model_bs = BaseModel()

    def test_all(self):
        """Test all method"""
        self.assertIsInstance(self.model_st, FileStorage)
        self.assertIsInstance(self.model_st.all(), dict)

    def test_new(self):
        """Test new function"""
        key = "BaseModel.{}".format(self.model_bs.id)
        self.model_st.new(self.model_bs)
        self.assertEqual(self.model_st.all()[key], self.model_bs)

    def test_save(self):
        """Testing save"""
        self.model_st.save()
        self.assertTrue(os.path.exists("file.json"))
        os.remove("file.json")

    def test_err(self):
        """Testing Error"""
        with self.assertRaises(TypeError):
            self.model_st.all("no")
        with self.assertRaises(TypeError):
            self.model_st.reload("no")
        with self.assertRaises(TypeError):
            self.model_st.new("om", "n")


if __name__ == "__main__":
    unittest.main()
