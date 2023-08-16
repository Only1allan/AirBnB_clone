#!/usr/bin/python3
""" Test for the main class base model"""
import unittest
from os.path import isfile
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test case to test the functionality of the Base Model Class."""

    def test_save(self):
        """Function that tests if a new instance is saved into the database"""
        object = BaseModel()
        updated_at = datetime.now()
        update1 = object.updated_at

        self.assertEqual(object.updated_at.date(), updated_at.date())
        object.save()

        updated_at = datetime.now()
        update2 = object.updated_at
        self.assertEqual(object.updated_at.date(), updated_at.date())
        self.assertTrue(isfile("file.json"))
        self.assertLess(update1, update2, "Error")

    def test_to_dict(self):
        """ Function that checking object can be converted in dictionary"""
        required = ("id", "created_at", "updated_at", "__class__")
        object = BaseModel()
        actual = object.to_dict()
        self.assertEqual(sorted(tuple(actual.keys())), sorted(required))
        