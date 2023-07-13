#!/usr/bin/python3
import json
from models.base_model import BaseModel

""" 
model to covert dict to a json and store in file
"""

class FileStorage:
    """  
    that serializes instances to a JSON file and deserializes JSON file to instances
    Attributes:
    __file_path: private attribute that have the path of the json file
    __objects: private attribute that contain the dic of instance
    """
    
    __file_path = "file.json"
    __objects = {}

    class_dict = {"BaseModel": BaseModel}
    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
       
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        """ print(self.__class__.__objects) """
        new_dict = {}
        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="UTF8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r", encoding="UTF8") as f:
                new_obj = json.load(f)
            for k, v in new_obj.items():
                obj = self.class_dict[v["__class__"]](**v)
                self.__objects[k] = obj
        except FileNotFoundError :
            pass