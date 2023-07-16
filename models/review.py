#!/usr/bin/python3
"""Defines a Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents review made by users.

    Attributes:
        place_id(str): the place id.
        user_id(str): the user id.
        text(str): the text added as review.
      """
    place_id = ""
    user_id = ""
    text = ""
