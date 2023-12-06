#!/usr/bin/python3
"""the class of User."""
from models.base_model import BaseModel


class User(BaseModel):
    """User reprisentation.
    Attributes:
        email (str): The user email.
        password (str): The user password.
        first_name (str): The user firstname.
        last_name (str): The user last name.
    """

    first_name = ""
    last_name = ""
    email = ""
    password = ""
