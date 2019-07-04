#!/usr/bin/python3
"""CLI command line interface for hbnb project
"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Airbnb clone CLI command line
    """
    prompt = "(hbnb) "
    clss = {
            "BaseModel": BaseModel,
            "User": User}

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

    def do_create(self, arg):
        """Create new instance from class
        """
        if len(arg) is 0:
            print("** class name missing **")
        elif self.clss.get(arg) is None:
            print("** class doesn't exist **")
        else:
            new = self.clss.get(arg)()
            new.save()
            print(new.id)

    def do_show(self, args):
        """Print stored objects by id
        """
        cmd_args = args.split(" ")
        if len(cmd_args[0]) is 0:
            print("** class name missing **")
        elif self.clss.get(cmd_args[0]) is None:
            print("** class doesn't exist **")
        elif len(cmd_args) is 1:
            print("** instance id missing **")
        else:
            all_obj = storage.all()
            if str(cmd_args[0]) + '.' + str(cmd_args[1]) in all_obj.keys():
                print(all_obj[str(cmd_args[0]) + '.' + str(cmd_args[1])])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Delete stored objects by id
        """
        cmd_args = args.split(" ")
        if len(cmd_args[0]) is 0:
            print("** class name missing **")
        elif self.clss.get(cmd_args[0]) is None:
            print("** class doesn't exist **")
        elif len(cmd_args) is 1:
            print("** instance id missing **")
        else:
            all_obj = storage.all()
            if str(cmd_args[0]) + '.' + str(cmd_args[1]) in all_obj.keys():
                storage.remove(str(cmd_args[0]) + '.' + str(cmd_args[1]))
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all items
        """
        all_obj = storage.all()
        listn = []
        if len(arg) is 0:
            for key, value in all_obj.items():
                listn.append(str(value))
            if len(listn) is 0:
                pass
            else:
                print(listn)
        elif self.clss.get(arg) is None:
            print("** class doesn't exist **")
        else:
            for key, value in all_obj.items():
                if arg in key:
                    listn.append(str(value))
            if len(listn) is 0:
                pass
            else:
                print(listn)

    def do_update(self, args):
        """Update or add new attribute to object
        """
        cmd_args = args.split(" ")
        if len(cmd_args[0]) is 0:
            print("** class name missing **")
        elif self.clss.get(cmd_args[0]) is None:
            print("** class doesn't exist **")
        elif len(cmd_args) is 1:
            print("** instance id missing **")
        else:
            all_obj = storage.all()
            if str(cmd_args[0]) + '.' + str(cmd_args[1]) in all_obj.keys():
                if len(cmd_args) is 2:
                    print("** attribute name missing **")
                else:
                    tmp = str(all_obj[str(
                        cmd_args[0]) + '.' + str(cmd_args[1])])
                    if len(cmd_args) is 3:
                        print("** value missing **")
                    else:
                        storage.update_attr(
                                str(cmd_args[0]) + '.' + str(cmd_args[1]),
                                str(cmd_args[2]).replace('"', ''),
                                str(cmd_args[3]).replace('"', ''))
            else:
                print("** no instance found **")

if __name__ == '__main__':
    hbnb = HBNBCommand()
    hbnb.cmdloop()
