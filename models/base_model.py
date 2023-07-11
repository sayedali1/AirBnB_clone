"""#!/usr/bin/python3"""
import uuid
from datetime import datetime

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
    create_at = datetime.now()
    update_at = datetime.now()

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
            if "create_at" in kwargs:
                self.create_at = kwargs["create_at"]
            if "update_at" in kwargs:
                self.update_at = kwargs["update_at"]
        else:
            self.id = self.__class__.id
            self.create_at = self.__class__.create_at
    
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.update_at - datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance:"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['create_at'] = self.create_at.isoformat()
        obj_dict['update_at'] = self.update_at.isoformat()
        return obj_dict

    def __str__(self):
        """ string format of the model """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id,
                                         self.__dict__)

    
if __name__ == '__main__':

    from base_model import BaseModel

    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89

    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
