#!/usr/bin/python3
"""Implements an entry point for the command line interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class_names = ["BaseModel", "User", "State", "City", "Place", "Amenity",
               "Review"]


class HBNBCommand(cmd.Cmd):
    """Uses the cmd module to implement a command interpreter.

    Attributes:
        prompt(str): a custom prompt.
    """

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exits the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def emptyline(self):
        return

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it & prints the id"""
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in class_names:
            print("** class doesn't exist **")
        else:
            x = eval(arg_list[0])()
            print(x.id)
            storage.save()

    def do_show(self, arg):
        """Prints the str rep of an instance based on the class name and id"""
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in class_names:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            obj_key = arg_list[0] + "." + arg_list[1]
            if obj_key in storage.all():
                print(storage.all()[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        The change is saved to the into the JSON file.
        """
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in class_names:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            obj_key = arg_list[0] + "." + arg_list[1]
            if obj_key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[obj_key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        arg_list = arg.split()
        if len(arg_list) > 0:
            if arg_list[0] not in class_names:
                print("** class doesn't exist **")
                return
        inst_list = []
        for obj in storage.all().values():
            inst_list.append(obj.__str__())
        print("{}".format(inst_list))

    def do_update(self, arg):
        """Updates/adds an instance attribute based on the class name and id"""
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        elif arg_list[0] not in class_names:
            print("** class doesn't exist **")
            return False
        elif len(arg_list) == 1:
            print("** instance id missing **")
            return False

        obj_key = arg_list[0] + "." + arg_list[1]
        if obj_key not in storage.all():
            print("** no instance found **")
            return False
        elif len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        elif len(arg_list) == 3:
            print("** value missing **")
            return False
        else:
            attr = arg_list[2]
            val = type(attr)(arg_list[3])
            for key in storage.all():
                if key == obj_key:
                    setattr(storage.all()[key], arg_list[2], val)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
