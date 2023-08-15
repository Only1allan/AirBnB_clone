#!/usr/bin/python3
"""Unit test for city class"""
import unittest
from models.city import City


class test_City(unittest.TestCase):
    """Test case to check city requirements."""
    def test_new_city(self):
        """ Test for City instance"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
