#!/usr/bin/python3
"""
User instance from BaseModel
"""
from .base_model import BaseModel


class User(BaseModel):
    """User class from BaseModel
    """
    def __init__(self):
        """Initial parameters
        """
        super().__init__(id)
        email = ""
        password = ""
        first_name = ""
        last_name = ""
