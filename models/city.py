#!/usr/bin/python3
"""Defines a City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """represents a city.

    Attributes:
        state_id(str): the state id.
        name(str): name of the city.
    """

    state_id = ""
    name = ""
