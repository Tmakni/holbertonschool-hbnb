#!/usr/bin/python3


from .basemodel import BaseModel
from .place import Place
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z{2,}$'
    if re.match(pattern, email):
        return email
    raise ValueError("Error format email")

def validate_name(name):
    if not isinstance(name, str):
        raise ValueError("Name must be a string")
    return name

class User(BaseModel):

    def __init__(self, first_name=None, last_name=None, email=None, isadmin=False):
        if first_name = None:
            raise ValueError("first name requiered")
        if last_name = None:
            raise ValueError("last name requiered")
        if email = None:
            raise ValueError("email requiered")
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.isadmin = isadmin
        self.places = []

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value):
        if isinstance(value, bool):
            self__is_damin = value #verify is_admin is False or True
        else:
            raise ValueError("isadmin must be True or False")
    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if validate_email(value) == value:
            self.__email = value

    @property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, value):
        if validate_name == value:
            self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if validate_name == value:
            self.__last_name = value
