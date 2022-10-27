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


class HBNBCommand(cmd.Cmd):
    """HBNBCommand is the console for the airbnb clone.
    Attributes:
        prompt (str): The command prompt.
    """
     prompt = '(hbnb) '
     __file_path = 'file.json'






if __name__ == '__main__':
    HBNBCommand().cmdloop()
