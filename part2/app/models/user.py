def __init__(self, first_name: str, last_name: str, email: str):
    if not first_name:
        raise TypeError("Add first name")
    if not last_name:
        raise TypeError("Add last name")
    if not email:
        raise TypeError("Add a email")
    if email and "@" not in email:
        raise ValueError("format invalid")
    super().__init__(**kwargs)
