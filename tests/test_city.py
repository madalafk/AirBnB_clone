#!/usr/bin/python3
"""a unittests for models/city.py.

Unittest classes:
    test_state_id_initialization
    test_name_initialization
    test_state_id_assignment
    test_name_assignment
"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_state_id_initialization(self):
        city = City()
        self.assertEqual(city.state_id, "")

    def test_name_initialization(self):
        city = City()
        self.assertEqual(city.name, "")

    def test_state_id_assignment(self):
        city = City()
        city.state_id = "123"
        self.assertEqual(city.state_id, "123")

    def test_name_assignment(self):
        city = City()
        city.name = "New York"
        self.assertEqual(city.name, "New York")

if __name__ == '__main__':
    unittest.main()

