#!/usr/bin/python3
"""
Review instance from BaseModel
"""
from .base_model import BaseModel


class Review(BaseModel):
    """Review class from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
