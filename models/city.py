#!/usr/bin/python3
"""city module for project"""
from models.base_model import BaseModel


class City(BaseModel):
    """City classs containing name and ID"""
    state_id = ""
    name = ""
