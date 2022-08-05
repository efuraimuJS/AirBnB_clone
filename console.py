#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""
    
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exits the program.
        """
        return True
    
    def do_EOF(self, line):
        """Handles End Of File character.
        """
        print()
        return True
    
    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)
    
    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass
    
    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel"""

        if line == "" or line is None:
            print("** class name missing **")
        
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)
    
    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id. 
            Ex: $ show BaseModel 1234-1234-1234.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])
    
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file). 
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        if line == ""or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()
        
    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all."""
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                l = [str(obj) for key, obj in storage.all().items()
                        if type(obj).__name__ == words[0]]
                print(l)
        
        else:
            l = [str(obj) for key, obj in storage.all().items()]

                







if __name__ == '__main__':
    HBNBCommand().cmdloop()

