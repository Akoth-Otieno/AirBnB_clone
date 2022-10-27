#!/usr/bin/python3
"""The entry point to the command-line interpreter.
It implements:
    quit and EOF to exit the program
    help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
    a custom prompt: (hbnb)
    an empty line + ENTER shouldn’t execute anything
"""

import cmd

class HBNBCommand(cmd.Cmd):



if __name__ == '__main__':
    HBNBCommand().cmdloop()
