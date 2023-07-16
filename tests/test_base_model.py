#!/usr/bin/python3
"""a unittests for models/base_model.py.
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_creation(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_timestamps_creation(self):
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsInstance(self.base_model.created_at, datetime)

        self.assertIsNotNone(self.base_model.updated_at)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_string_representation(self):
        expected_output = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_output)

    def test_save_updates_timestamp(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dict(self):
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)

    def test_to_dict_contains_correct_values(self):
        base_model_dict = self.base_model.to_dict()

        self.assertEqual(base_model_dict["id"], self.base_model.id)
        self.assertEqual(base_model_dict["created_at"], self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict["updated_at"], self.base_model.updated_at.isoformat())
        self.assertEqual(base_model_dict["__class__"], "BaseModel")

    def test_to_dict_excludes_methods(self):
        base_model_dict = self.base_model.to_dict()
        excluded_keys = ["save", "to_dict"]

        for key in excluded_keys:
            self.assertNotIn(key, base_model_dict)


if __name__ == '__main__':
    unittest.main()

