#!/usr/bin/python3
"""Review module for the app"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class to store review info"""
    place_id = ""
    user_id = ""
    text = ""
