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








if __name__ == '__main__':
    HBNBCommand().cmdloop()

