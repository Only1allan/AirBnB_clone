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
        self.assertEqual(object.updated_at.date(), updated_at.date())
        object.save()

        updated_at = datetime.now()
        self.assertEqual(object.updated_at.date(), updated_at.date())
        self.assertTrue(isfile("file.json"))

    def test_to_dict(self):
        """ Function that checking object can be converted in dictionary"""
        required = ("id", "created_at", "updated_at", "__class__")
        object = BaseModel()
        actual = object.to_dict()
        self.asserEqual(sorted(tuple(actual.keys()))), sorted(required)

    def test_kwargs_to_dict(self):
        """ Tests whether kwargsis converted to dict correctly"""
        required = ("id", "created_at", "updated_at", "__class__", "name")
        object = BaseModel(**{
            "id": "1",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "name": "Grace Allan"
        })
        tupleobj = tuple(object.to_dict().keys())
        self.assertEqual(sorted(tupleobj), sorted(required))

    def test_str(self):
        """Test str method"""
        object = BaseModel()
        id = object.id
        self.assertEqual(str(object), f"[BaseModel] ({id}) {object.__dict__}")
