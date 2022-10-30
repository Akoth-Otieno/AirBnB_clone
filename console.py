#!/usr/bin/python3
"""The entry point to the command-line interpreter - cnsole for the airbnb clone.
It implements:
   - quit and EOF to exit the program
   - help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
   - a custom prompt: (hbnb)
   - an empty line + ENTER shouldn’t execute anything
"""

import cmd
import sys
import argparser
from from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import os.path
import json
import shlex

class HBNBCommand(cmd.Cmd):
    """HBNBCommand is the console for the airbnb clone.
    Attributes:
        prompt (str): The command prompt.
    """
     prompt = '(hbnb) '
     __file_path = 'file.json'

     def do_quit(self, inp):
        '''do_quit - Quit command to exit the program'''
        return True

    def emptyline(self):
        '''emptyline - do nothing'''
        pass

    def do_EOF(self, inp):
        '''do_EOF - Quit command to exit the program'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
