#!/usr/bin/python3
"""Defines an amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """represents an amenity.

    Attributes:
        name(str): name of an amenity.
    """

    name = ""
