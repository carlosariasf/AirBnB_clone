#!/usr/bin/python3
"""
User instance from BaseModel
"""
from .base_model import BaseModel


class User(BaseModel):
    """User class from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
