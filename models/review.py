#!/usr/bin/python3

from models.base_model import BaseModel

"""
cls Review that inherts from BaseModel
"""


class Review(BaseModel):
    """
    Attributes:
        place_id - empty string
        user_id - empty string
        text - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
