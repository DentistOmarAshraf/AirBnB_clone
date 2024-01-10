import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def help_help(self):
        print('This is an Airbnb clone created using Python, OOP, and other concepts learned on ALX.')

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program on EOF Mode"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
