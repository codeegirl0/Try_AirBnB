#!/usr/bin/python3
"""The HBnB console file."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def reparsing(arg):
    crl_brc = re.search(r"\{(.*?)\}", arg)
    brackts = re.search(r"\[(.*?)\]", arg)
    if crl_brc is None:
        if brackts is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexing = split(arg[:brackts.span()[0]])
            retling = [i.strip(",") for i in lexing]
            retling.append(brackts.group())
            return retling
    else:
        lexing = split(arg[:crl_brc.span()[0]])
        retling = [i.strip(",") for i in lexing]
        retling.append(crl_brc.group())
        return retling


class HBNBCommand(cmd.Cmd):
    """the command hbnb interpreter.
    Attributes:
        prompt (str): The prompt in cmd.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def handleemptyline(self):
        """nothing when empty line."""
        pass

    def default(self, arg):
        """show if invalid cmd"""
        argdict = {
            "all": self.do_theall,
            "show": self.do_theshowing,
            "destroy": self.do_thedestroying,
            "count": self.do_counting,
            "update": self.do_theupdate
        }
        matchings = re.search(r"\.", arg)
        if matchings is not None:
            myargll = [arg[:matchings.span()[0]], arg[matchings.span()[1]:]]
            matchings = re.search(r"\((.*?)\)", myargll[1])
            if matchings is not None:
                command = [myargll[1][:matchings.span()[0]], matchings.group()[1:-1]]
                if command[0] in argdict.keys():
                    calling = "{} {}".format(myargll[0], command[1])
                    return argdict[command[0]](calling)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_thequiting(self, arg):
        """exit program."""
        return True

    def do_sigEOF(self, arg):
        """EOF signal for exiting."""
        print("")
        return True

    def do_thecreating(self, arg):
        """Usage: creating <class>
        Creating the class with id.
        """
        myargll = reparsing(arg)
        if len(myargll) == 0:
            print("** class name missing **")
        elif myargll[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(myargll[0])().id)
            storage.save()

    def do_theshowing(self, arg):
        """Usage: showing class id or class show
        showing the string of a id.
        """
        myargll = reparsing(arg)
        myobjdictt = storage.all()
        if len(myargll) == 0:
            print("** class name missing **")
        elif myargll[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(myargll) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(myargll[0], myargll[1]) not in myobjdictt:
            print("** no instance found **")
        else:
            print(myobjdictt["{}.{}".format(myargll[0], myargll[1])])

    def do_thedestroying(self, arg):
        """Usage: remove class id or cls.destroy(<id>)
        remove a class inst id."""
        myargll = reparsing(arg)
        myobjdictt = storage.all()
        if len(myargll) == 0:
            print("** class name missing **")
        elif myargll[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(myargll) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(myargll[0], myargll[1]) not in myobjdictt.keys():
            print("** no instance found **")
        else:
            del myobjdictt["{}.{}".format(myargll[0], myargll[1])]
            storage.save()

    def do_theall(self, arg):
        """Usage: all or all class
        show string  of all class.
        all instantiated obj."""
        myargll = reparsing(arg)
        if len(myargll) > 0 and myargll[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            myobjl = []
            for obj in storage.all().values():
                if len(myargll) > 0 and myargll[0] == obj.__class__.__name__:
                    myobjl.append(obj.__str__())
                elif len(myargll) == 0:
                    myobjl.append(obj.__str__())
            print(myobjl)

    def do_counting(self, arg):
        """Usage: count class
        return number inst class."""
        myargll = reparsing(arg)
        count = 0
        for obj in storage.all().values():
            if myargll[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_theupdate(self, arg):
        """Usage: update class id
        Update id instance
        a attr of pair or dict."""
        myargll = reparsing(arg)
        myobjdictt = storage.all()

        if len(myargll) == 0:
            print("** class name missing **")
            return False
        if myargll[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(myargll) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(myargll[0], myargll[1]) not in myobjdictt.keys():
            print("** no instance found **")
            return False
        if len(myargll) == 2:
            print("** attribute name missing **")
            return False
        if len(myargll) == 3:
            try:
                type(eval(myargll[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(myargll) == 4:
            obj = myobjdictt["{}.{}".format(myargll[0], myargll[1])]
            if myargll[2] in obj.__class__.__dict__.keys():
                valuttp = type(obj.__class__.__dict__[myargll[2]])
                obj.__dict__[myargll[2]] = valuttp(myargll[3])
            else:
                obj.__dict__[myargll[2]] = myargll[3]
        elif type(eval(myargll[2])) == dict:
            obj = myobjdictt["{}.{}".format(myargll[0], myargll[1])]
            for n, p in eval(myargll[2]).items():
                if (n in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[n]) in {str, int, float}):
                    valuttp = type(obj.__class__.__dict__[n])
                    obj.__dict__[n] = valuttp(p)
                else:
                    obj.__dict__[n] = p
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
