#!/usr/bin/python3
"""The class of City."""
from models.base_model import BaseModel


class City(BaseModel):
    """the city reprisentation.
    Attributes:
        state_id (str): the id status.
        name (str): The city name.
    """

    state_id = ""
    name = ""
