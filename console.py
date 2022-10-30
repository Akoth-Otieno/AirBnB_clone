#!/usr/bin/python3
"""The entry point to the console for the airbnb clone.
It implements:
   - quit and EOF to exit the program
   - help
   - a custom prompt: (hbnb)
   - an empty line + ENTER shouldn’t execute anything
"""

import cmd
import sys
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
