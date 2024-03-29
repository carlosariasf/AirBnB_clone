#!/usr/bin/python3
"""CLI command line interface for hbnb project
"""


import cmd
import re
import math
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Airbnb clone CLI command line
    """
    prompt = "(hbnb) "
    clss = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review}

    def default(self, args):
        """called on an input line when the command prefix is not recognized
        """
        cmd_args = re.split('[.,(){}":\' ]', args)
        cmd_args = list(filter(None, cmd_args))
        if self.clss.get(cmd_args[0]):
            cls = cmd_args[1]
            leng = len(cmd_args)
            if leng is 2:
                run = getattr(self, "do_" + cls)
                run(cmd_args[0])
            elif leng is 3:
                run = getattr(self, "do_" + cls)
                run(cmd_args[0] + " " + cmd_args[2])
            elif leng is 4:
                run = getattr(self, "do_" + cls)
                run(cmd_args[0] + " " + cmd_args[2] + ' ' + cmd_args[3])
            elif leng is 5:
                run = getattr(self, "do_" + cls)
                run(cmd_args[0] + ' ' + cmd_args[2] + ' ' + cmd_args[3] +
                    ' ' + cmd_args[4])
            elif leng >= 6 and cls == "update":
                fval = 3
                lengf = int(math.ceil((leng - 3) / 2))
                run = getattr(self, "do_" + cls)
                if leng % 2 == 0:
                    for i in range(lengf):
                        if i != lengf - 1:
                            run(cmd_args[0] + ' ' + cmd_args[2] + ' ' +
                                cmd_args[fval] + ' ' + cmd_args[fval+1])
                            fval += 2
                        else:
                            run(cmd_args[0] + ' ' + cmd_args[2] + ' ' +
                                cmd_args[fval])
                else:
                    for i in range(lengf):
                        run(cmd_args[0] + ' ' + cmd_args[2] + ' ' +
                            cmd_args[fval] + ' ' + cmd_args[fval+1])
                        fval += 2

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

    def do_count(self, arg):
        """Call counter
        """
        storage.counter(arg)

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
