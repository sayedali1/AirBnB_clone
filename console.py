#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place


"""
class for the console funs to test the our model
"""


class HBNBCommand(cmd.Cmd):
    """ consle class """
    prompt = "(hbnb)"

    """ 
        class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "Review": Review,
        "Amenity": Amenity,
        "City": City,
        "Place": Place
    } 
    """

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ exit the program when we press contrl-D """
        print()
        return True

    def emptyline(self):
        """ override the empty line """
        self.lastcmd = ""
        return super().emptyline()

    


if __name__ == "__main__":
    HBNBCommand().cmdloop()