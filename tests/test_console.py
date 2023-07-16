#!/usr/bin/python3
"""unittests for console.py.

Unittest classes:
   class TestHBNBCommand
 
"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_do_EOF(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.do_EOF(None))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")

    def test_do_quit(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_quit(None)
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")
    
    def test_do_create(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_create("BaseModel")
            output = fake_out.getvalue().strip()
            self.assertTrue(len(output) > 0)
            obj_id = output
            obj = storage.all().get(f"BaseModel.{obj_id}")
            self.assertIsNotNone(obj)
            self.assertIsInstance(obj, BaseModel)

    def test_do_show(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_show("BaseModel 123")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

            obj = BaseModel()
            obj_id = obj.id
            storage.all()[f"BaseModel.{obj_id}"] = obj

            self.console.do_show("BaseModel " + obj_id)
            output = fake_out.getvalue().strip()
            self.assertEqual(output, str(obj))

    def test_do_destroy(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_destroy("BaseModel 123")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

            obj = BaseModel()
            obj_id = obj.id
            storage.all()[f"BaseModel.{obj_id}"] = obj

            self.console.do_destroy("BaseModel " + obj_id)
            self.assertIsNone(storage.all().get(f"BaseModel.{obj_id}"))

    def test_do_all(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_all("BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "[]")

            obj = BaseModel()
            storage.all()[f"BaseModel.{obj.id}"] = obj

            self.console.do_all("BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, str([obj]))

    def test_do_update(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_update("BaseModel 123 attr_name attr_value")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

            obj = BaseModel()
            obj_id = obj.id
            storage.all()[f"BaseModel.{obj_id}"] = obj

            self.console.do_update("BaseModel " + obj_id + " attr_name attr_value")
            self.assertEqual(getattr(obj, "attr_name"), "attr_value")


if __name__ == '__main__':
    unittest.main()

