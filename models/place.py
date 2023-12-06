#!/usr/bin/python3
"""The class of Place."""
from models.base_model import BaseModel


class Place(BaseModel):
    """place reprisentation.
    Attributes:
        city_id (str): The id of city.
        user_id (str): The id of user.
        name (str): The place name.
        description (str): The place description.
        number_rooms (int): The place num.
        number_bathrooms (int): The bath num.
        max_guest (int): The max num of guess.
        price_by_night (int): The night price.
        latitude (float): The place latt.
        amenity_ids (list): A id list.
        longitude (float): The place longtt.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
