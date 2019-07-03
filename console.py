#!/usr/bin/python3
"""CLI command line interface for hbnb project
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Airbnb clone CLI command line
    """
    def do_EOF(self, line):
        """Exit with EOF
        """
        return True

    def do_quit(self, args):
        """Quit command to exit the program
        """
        raise SystemExit

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
