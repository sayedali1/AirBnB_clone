#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
  
    def do_create(self, line):
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
        try:
            class_name = line_args[0]
            obj_id = line_args[1]
            obj = storage.all().get(f"{class_name}.{obj_id}")
            if obj:
                print(obj)
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")    
    
    def do_destroy(self, line):
        line_args = line.split()
        if not line_args:
            print("** class name missing **")
            return
        try:
            class_name = line_args[0]
            obj_id = line_args[1]
            obj = storage.all().get(f"{class_name}.{obj_id}")
            if obj:
                del storage.all()[f"{class_name}.{obj_id}"]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        objects = storage.all()
        if not line:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                class_name = line
                print([str(obj) for obj in objects.values() if obj.__class__.__name__ == class_name])
            except NameError:
                print("** class doesn't exist **")
 
    def do_update(self, line):
        """Update if given exact object, exact attribute"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            obj_id = args[1]
            attr_name = args[2]
            attr_value = args[3]
            obj = storage.all().get(f"{class_name}.{obj_id}")
            if obj:
                setattr(obj, attr_name, attr_value)
                obj.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")
        

    def emptyline(self):
        """ override the empty line """
        self.lastcmd = ""
        return super().emptyline()
    def do_quit(self,line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ exit the program when we press contrl-D """
        print("\n")
        return True
   
       
if __name__ == "__main__":
    HBNBCommand().cmdloop()
