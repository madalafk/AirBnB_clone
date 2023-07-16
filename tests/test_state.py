#!/usr/bin/python3
"""unittests for models/state.py.

Unittest classes:
    class TestState
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_name_initialization(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_name_assignment(self):
        state = State()
        state.name = "New Mexico"
        self.assertEqual(state.name, "New Mexico")


if __name__ == '__main__':
    unittest.main()
