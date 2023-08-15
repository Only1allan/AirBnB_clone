#!/usr/bin/python3
"""Defines test for Place class"""
import unittest
from models.place import Place


class test_Place(unittest.TestCase):
    """Test cases for the place model."""
    def test_new_place(self):
        """Tests if a new instance of a place is created correctly"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
