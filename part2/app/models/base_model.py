#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())

        now = datetime.utcnow()
        self.created_at = now
        self.updated_at = now

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
