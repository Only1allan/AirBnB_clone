#!/usr/bin/python3
"""defines test for user class"""
import unittest
from models.user import User


class test_User(unittest.TestCase):
    """test case for the user model."""
    def test_new_user(self):
        """tests if a new user is created correctly"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
