#!/usr/bin/python3
"""Module for our user for the app"""
from models.base_model import BaseModel


class User(BaseModel):
    """class defining user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
