#!/usr/bin/env python3
"""THE CONSOLE"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Console Class"""

    prompt = "(hbnb) "
    models_list = {"User": User, "State": State, "BaseModel": BaseModel,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
    data = models.storage.all()

    def do_create(self, line):
        """Create Instance => Usage: Create <ClassName>"""
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
        """Show Instance => Usage: show <ClassName> <id>"""
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

        inst_key = cmnd[0] + '.' + cmnd[1]

        if inst_key not in self.data.keys():
            print("** no instance found **")
            return

        print(self.data[inst_key])

    def do_destroy(self, line):
        """Delete instance => Usage: destroy <ClassName> <id>"""
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
        inst_key = cmnd[0] + '.' + cmnd[1]
        if inst_key not in self.data.keys():
            print("** no instance found **")
        del(self.data[inst_key])
        models.storage.save()

    def do_all(self, line):
        """Print all instance => Usage: all || all <ClassName>"""
        if not line or len(line) == 0:
            print([obj.__str__() for obj in self.data.values()])
            return
        if line not in self.models_list:
            print("** class doesn't exist **")
            return
        ls = []
        for obj in self.data.values():
            if line == obj.to_dict()['__class__']:
                ls.append(obj.__str__())
        print(ls)

    def do_update(self, line):
        """Update Instance => Usage: update <ClassName> <id> <attr> <value>"""
        if not line or len(line) == 0:
            print("** class name missing **")
            return

        cmnd = line.split()

        if cmnd[0] not in self.models_list.keys():
            print("** class doesn't exist **")
            return
        if len(cmnd) == 1:
            print("** instance id missing **")
            return
        inst_key = cmnd[0] + '.' + cmnd[1]
        if inst_key not in self.data.keys():
            print("** instance id missing **")
            return
        if len(cmnd) == 2:
            print("** attribute name missing **")
            return
        if len(cmnd) == 3:
            print("** value missing **")
            return
        # This Block is not in Task from here
        forbid = ['id', 'created_at', 'updated_at']
        if cmnd[2] in forbid:
            print("** Attribute Immutable Can't Change **")
            return
        # to here

        setattr(self.data[inst_key], cmnd[2], cmnd[3].strip('"'))
        models.storage.save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print()
        return True

    def help_help(self):
        """List available commands with """
        pass

    def do_help(self, line):
        if len(line) == 0:
            print("\n" + self.doc_header)
            print(len(self.doc_header) * self.ruler)
            print("EOF  help  quit  create  show  destroy  all  update\n")

        else:
            com = {"quit": self.do_quit, "EOF": self.do_EOF,
                   "help": self.help_help, "create": self.do_create,
                   "show": self.do_show, "destroy": self.do_destroy,
                   "all": self.do_all, "update": self.do_update}

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
