import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Met à jour le timestamp `updated_at` lors de la modification de l'objet"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Met à jour les attributs de l'objet à partir d'un dictionnaire"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Mise à jour du timestamp `updated_at`
