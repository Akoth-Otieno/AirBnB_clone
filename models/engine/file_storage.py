#!/usr/bin/python3
''' 
Custom FileStorage Class.
'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os.path

class FileStorage:
    '''
    Represents a storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    '''
    def __init__(self):
        '''INitializes File Storage Instances.'''
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        '''returns all objects.'''
        return (self.__objects)

    def new(self, obj):
        '''creates new objects.'''
        new_id = getattr(obj, 'id')
        self.__objects[obj.to_dict()['__class__'] + '.' + new_id] = obj
    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = FileStorage.__objects
        obj_dict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)
    
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
