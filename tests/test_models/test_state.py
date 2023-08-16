#!/usr/bin/python3
"""Test for State class"""
import unittest
from models.state import State


class test_State(unittest.TestCase):
    """Class to test state model."""
    def test_new_state(self):
        """test if new state is created correctly"""
        state = State()
        self.assertEqual(state.name, "")
