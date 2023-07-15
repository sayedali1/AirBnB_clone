#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.my_model = BaseModel()
        cls.my_model.name = "My_First_Model"
        cls.my_model.my_number = 89

    def test_init(self):
        self.assertTrue(isinstance(self.my_model, BaseModel))

    def test_save(self):
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at,
                            self.my_model.updated_at)

    def test_to_dict(self):
        dic = self.my_model.to_dict()
        self.assertEqual(self.my_model.__class__.__name__, dic["__class__"])
        self.assertIsInstance(dic["updated_at"], str)
        self.assertIsInstance(dic["updated_at"], str)

    def test_MethodsNotEmpty(self):
        self.assertIsNotNone(self.my_model.__doc__)
        self.assertIsNotNone(self.my_model.save.__doc__)
        self.assertIsNotNone(self.my_model.to_dict.__doc__)

    def test_attribute(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))


if __name__ == "__main__":
    unittest.main()
