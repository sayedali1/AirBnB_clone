#!/usr/bin/python3
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

    def __init__(self, *args, **kwargs):
        """
        initialition
        Attribures:
            my_number: model number
            name: model name
            id: model id
        """
        if kwargs is not None:
            if "id" in kwargs:
                self.id
        
    def __str__(self):
        """ string format of the model """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

""" if __name__ == '__main__':
    from base_model import BaseModel
    
    model = BaseModel()
    model.name = "sayed"
    model.my_number = 9
    print(model)
   
     """
