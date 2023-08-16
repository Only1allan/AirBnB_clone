#!/usr/bin/python3
"""Tests for Amenity class"""
import unittest
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """class to test the amenity class"""

    def test_new_amenity(self):
        """tests name property of amenity object"""
        inst = Amenity()
        self.assertEqual(inst.name, "")
