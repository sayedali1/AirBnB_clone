#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
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
