#!/usr/bin/env python3
import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    models_list = {"BaseModel": BaseModel}

    def do_create(self, line):
        """Create Instance"""
        if not line or len(line) == 0:
            print("** class name missing **")
            return
        if line not in self.models_list.keys():
            print("** class doesn't exist **")
            return
        obj = self.models_list[line]()
        obj.save()
        print(obj.id)
    
    def do_show(self, line):
        """Show Instance"""
        cmnd = line.split()
        if len(cmnd) == 0:
            print("** class name missing **")
            return
        if cmnd[0] not in self.models_list.keys():
            print("** class doesn't exist **")
            return
        if len(cmnd) == 1:
            print("** instance id missing **")
            return


    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line): 
        """Quit command to exit the program"""
        print()
        return True

    def help_help(self):
        """List available commands with "help" or detailed help with "help cmd"""
        pass
    
    def do_help(self, line):
        if len(line) == 0:
            print("")
            print(self.doc_header)
            for i in range(len(self.doc_header)):
                print(self.ruler, end="")
            print("")
            print("EOF  help  quit  create")
            print("")
        else:
            com = {"quit": self.do_quit, "EOF": self.do_EOF,
                   "help": self.help_help, "create": self.do_create,
                   "show": self.do_show}

            if line not in com or not com[line].__doc__:
                print("*** No help on {}".format(line))
            else:
                print(com[line].__doc__)
                print()

    def emptyline(self):
        """Do Nothing"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
