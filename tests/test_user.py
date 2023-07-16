#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    class TestUser
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_email_initialization(self):
        user = User()
        self.assertEqual(user.email, "")

    def test_password_initialization(self):
        user = User()
        self.assertEqual(user.password, "")

    def test_first_name_initialization(self):
        user = User()
        self.assertEqual(user.first_name, "")

    def test_last_name_initialization(self):
        user = User()
        self.assertEqual(user.last_name, "")

    def test_email_assignment(self):
        user = User()
        user.email = "fkmadal@alx.com"
        self.assertEqual(user.email, "fkmadala@alx.com")

    def test_password_assignment(self):
        user = User()
        user.password = "password123456"
        self.assertEqual(user.password, "password123456")

    def test_first_name_assignment(self):
        user = User()
        user.first_name = "ALX"
        self.assertEqual(user.first_name, "SWE")

    def test_last_name_assignment(self):
        user = User()
        user.last_name = "SWE"
        self.assertEqual(user.last_name, "ALX")


if __name__ == '__main__':
    unittest.main()
