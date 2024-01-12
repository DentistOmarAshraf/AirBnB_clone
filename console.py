#!/usr/bin/env python3
import cmd
import sys
from models.__init__ import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    valid_classes = {"User": User, "State": State, "BaseModel": BaseModel,
                     "City": City, "Amenity": Amenity, "Place": Place,
                     "Review": Review}

    def help_help(self):
        """Overwrite of super class help def"""
        print('This is an Airbnb clone created using Python, OOP, and other concepts learned on ALX.')

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def help_quit(self):
        print('testtttt')
        print()

    def do_EOF(self, line):
        """Exit the program on EOF Style"""
        print()
        exit()

    def emptyline(self):
        """The program will perform no action when an empty line is entered."""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args = line.split(' ')

        if not args or not args[0]:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes.keys():
            print("** class doesn't exist **")
            return

        get_class = self.valid_classes[args[0]]
        var_class = get_class()
        var_class.save()
        print(var_class.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        args = line.split(' ')

        if not args or not args[0]:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes.keys():
            print("** class doesn't exist **")
            return

        if not args or len(args) < 2 or not args[1]:
            print("** instance id missing **")
            return

        dic_key = args[0] + '.' + args[1]

        all_objects = storage.all()

        if dic_key not in all_objects:
            print("** no instance found **")
            return

        print(all_objects.get(dic_key))

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split(' ')

        if not args or not args[0]:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes.keys():
            print("** class doesn't exist **")
            return

        if not args or len(args) < 2 or not args[1]:
            print("** instance id missing **")
            return

        dic_key = args[0] + '.' + args[1]

        if dic_key not in storage.all():
            print("** no instance found **")
            return

        del (storage.all()[dic_key])
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        args = line.split(' ')

        to_show = []

        if not args or not args[0]:
            for value in storage.all().values():
                to_show.append(str(value))
        elif args[0]:
            if args[0] not in self.valid_classes.keys():
                print("** class doesn't exist **")
                return

            for key, value in storage.all().items():
                if key.split('.')[0] == args[0]:
                    to_show.append(str(value))

        print(to_show)

    def do_update(self, line):
        args = line.split(' ')

        if not args or not args[0]:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes.keys():
            print("** class doesn't exist **")
            return

        if not args or len(args) < 2 or not args[1]:
            print("** instance id missing **")
            return

        dic_key = args[0] + '.' + args[1]

        if dic_key not in storage.all():
            print("** no instance found **")
            return

        if not args or len(args) < 3 or not args[2]:
            print("** attribute name missing **")
            return

        if not args or len(args) < 4 or not args[3]:
            print("** value missing **")
            return


if __name__ == '__main__':
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
