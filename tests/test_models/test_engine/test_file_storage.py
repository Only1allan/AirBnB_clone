#!/usr/bin/python3
"""Files storage test"""
import unittest
from models.engine.file_storage import FileStorage


class TestStorage(unittest.TestCase):
    """Test files storage class."""
    def test_new_reload(self):
        """test reload method"""
        file = FileStorage()
        database = file.all()
        self.assertTrue(len(database) > 0)
