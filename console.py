#!/usr/bin/python3
"""
Entry to command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Entry to command interpreter
    """
    prompt = "(hbnb)"

    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "Review": Review,
        "Amenity": Amenity,
        "City": City,
        "Place": Place
    }

    def do_EOF(self, line):
        """Exit on Ctrl-D"""
        print()
        return True

    def do_quit(self, line):
        """Exit on quit"""
        return True

    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""
        pass

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
        if class_name not in class_dict:
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
        if class_name not in class_dict:
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
            if line not in class_dict:
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
        if class_name not in class_dict:
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
        if class_name not in class_dict:
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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
