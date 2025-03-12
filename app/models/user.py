from datetime import datetime
from app.models.base_model import BaseModel 
"""
import Basemode / data
"""

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False, **kwargs):
        """
        Enfant de Basemode1, super() appelle Basemode1, Initialise name, mail, admin
        """
        super().__init__(**kwargs)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
