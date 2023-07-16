"""Defines unittests for models/review.py.

Unittest classes:
   class TestReview
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_place_id_initialization(self):
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_user_id_initialization(self):
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_text_initialization(self):
        review = Review()
        self.assertEqual(review.text, "")

    def test_place_id_assignment(self):
        review = Review()
        review.place_id = "123"
        self.assertEqual(review.place_id, "123")

    def test_user_id_assignment(self):
        review = Review()
        review.user_id = "456"
        self.assertEqual(review.user_id, "456")

    def test_text_assignment(self):
        review = Review()
        review.text = "satisfied !"
        self.assertEqual(review.text, "satisfied !")


if __name__ == '__main__':
    unittest.main()
