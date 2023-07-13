#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""
This module (called BaseModel) to take care of the initialization,
serialization and deserialization of your future instances
"""


class BaseModel:
    """
    this class defines all common attributes/methods for other classes

    Attributes:
        id (str) : public ,generate unique id
        create_at : assign with the current datetime
    """

    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """
        initialition
        Attribures:
            my_number: model number
            name: model name
            id: model id
        """
        if kwargs:
            if "my_number" in kwargs:
                self.my_number = kwargs["my_number"]
            if "name" in kwargs:
                self.name = kwargs["name"]
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"],'%Y-%m-%dT%H:%M:%S.%f')
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"],'%Y-%m-%dT%H:%M:%S.%f')
        else:
            
            self.id = self.id
            self.created_at = self.created_at   
            self.updated_at = self.updated_at
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
        
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance:"""
        obj_dict = self.__dict__.copy()
        
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """ string format of the model """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id,
                                         self.__dict__)

    