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
    prompt = "(hbnb) "

    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "Review": Review,
        "Amenity": Amenity,
        "City": City,
        "Place": Place
    }

    def do_create(self, line):
        """ create new obj """
        if not line:
            print("** class name missing **")
            return
        try:
            obj = eval(line)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        line_args = line.split()
        if not line_args:
            print("** class name missing **")
            return

        class_name = line_args[0]
        if class_name not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        obj_id = line_args[1]
        try:
            obj = storage.all().get(f"{class_name}.{obj_id}")
            if obj:
                print(obj)
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """ destroy obj """
        line_args = line.split()
        if not line_args:
            print("** class name missing **")
            return
        class_name = line_args[0]
        if class_name not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        obj_id = line_args[1]
        try:
            obj = storage.all().get(f"{class_name}.{obj_id}")
            if obj:
                del storage.all()[f"{class_name}.{obj_id}"]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        objects = storage.all()

        if not line:
            print([str(obj) for obj in objects.values()])
        else:
            if line not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects.values()
                       if obj.__class__.__name__ == line])

    def do_count(self, line):
        """Prints the number of instances of a class"""
        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        if class_name not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        objects = storage.all(class_name)
        count = len(objects)
        print(count)

    def do_update(self, line):
        """Update if given exact object, exact attribute"""
        args = line.split()

        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        obj_id = args[1]
        if obj_id == "":
            print("** instance id missing **")
            return
        attr_name = args[2]
        if attr_name == "":
            print("** attribute name missing **")
            return
        attr_value = args[3]
        if attr_value == "":
            print("** value missing **")

        obj = storage.all().get(f"{class_name}.{obj_id}")
        if obj:
            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            print("** no instance found **")

    def default(self, line):
        if "." in line:
            args = line.split(".")
        else:
            return super().default(line)

        if "all" in args[1]:
            self.do_all(args[0])
        elif "count" in args[1]:
            self.do_count(args[0])
        elif "show" in args[1]:
            id = args[1].split("\"")[1]
            self.do_show(args[0] + " " + id)
        elif "destroy" in args[1]:
            id = args[1].split("\"")[1]
            self.do_show(args[0] + " " + id)
        elif "update" in args[1]:
            attrs = args[1].split("\"")
            id = attrs[1]
            key = attrs[3]
            value = attrs[5]
            self.do_update(args[0] + " " + id + " " + key + " " + value)
        else:
            return super().default(line)

    def emptyline(self):
        """ override the empty line """
        self.lastcmd = ""
        return super().emptyline()

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ exit the program when we press contrl-D """
        print("\n")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
