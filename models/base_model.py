#!/usr/bin/python3
import uuid
from datetime import datetime
import models

"""
This module (called BaseModel) to take care of the initialization,
serialization and deserialization of your future instances
"""


class BaseModel():
    """this class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
        initialition

        Attribures:
            created_at
            id: model id
            updated_at
        """
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ string format of the model """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance:
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
