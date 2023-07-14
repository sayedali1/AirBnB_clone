#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_create(self, line):
        if line == "":
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_delete(self, line):
        line_args = line.split(" ")
        if line_args[0] == "":
            print("** class name missing **")
        elif line[0] != "BaseModel":
            print("** class doesn't exist **")
        elif line[1] == "":
            print("** instance id missing **")
        key = "{}.{}".format(line[0], line[1]) 
        if  key not in storage.all().keys():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()
    
    def do_update(self, line):
        """Update if given exact object, exact attribute"""
        args = line.split(" ")
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
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
