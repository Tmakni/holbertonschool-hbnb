import json
"""
Import JSON
"""


class FileStorage:
    """
   Class file storages, file_path chemin ou enregistre Obj,
   __objects dictionnaire qui contien les objects dans la mémoire
    """
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """
        Retroune les Objects enregistrer
        """
        return self.__objects

    def new(self, obj):
        """
        Ajout de nouveau OBJ a l'enregistrement
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Convertit tous les objets en dictionnaires
        """
        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Ouvre storage.json et charge les données
        """
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            pass
