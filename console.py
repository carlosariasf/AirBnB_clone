#!/usr/bin/python3
"""CLI command line interface for hbnb project
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Airbnb clone CLI command line
    """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exit with EOF
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Modify behavior of native method
        """
        pass

if __name__ == '__main__':
    hbnb = HBNBCommand()
    hbnb.cmdloop()
