#!/usr/bin/python3
"""defines test for review class"""
import unittest
from models.review import Review


class test_Review(unittest.TestCase):
    """test case to check the functionality of the review model."""
    def test_new_review(self):
        """Test if a new instance is created successfully"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
