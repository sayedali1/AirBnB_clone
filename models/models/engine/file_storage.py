#!/usr/bin/python3
import json
""" 
model to covert dict to a json and store in file
"""


class FileStorge:
    """  
    that serializes instances to a JSON file and deserializes JSON file to instances
    Attributes:
    __file_path: private attribute that have the path of the json file
    __objects: private attribute that contain the dic of instance
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__class__.__objects

    def new(self, obj):
        """ sets in __objects """
        self.__class__.__objects[obj.__class__.__name__.id] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        with open(self.__class__.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(self.__class__.__objects))

    def reload(self):
        """ deserializes the JSON file to __objects """
        with open(self.__class__.__file_path, "r", encoding="utf-8") as f:
            self.__class__.__objects = json.loads(f)
