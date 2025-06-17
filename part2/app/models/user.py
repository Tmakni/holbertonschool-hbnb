#!/usr/bin/python3
class User (BaseModel):

    def __init__(self, first_name: str, last_name: str, email: str, **kwargs):
        if not first_name:
            raise TypeError("Add first name")
        if not last_name:
            raise TypeError("Add last name")
        if not email:
            raise TypeError("Add a email")
        if email and "@" not in email:
            raise ValueError("format invalid")

        self.first_name = first_name
        self.last_ame = last_name
        self.email = email
        super().__init__(**kwargs)
