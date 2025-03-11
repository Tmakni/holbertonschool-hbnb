import json


class FileStorage:
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """
        Retroune les Objects enregistrer
        """
        return self.__objects

    def new(self, obj):

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj