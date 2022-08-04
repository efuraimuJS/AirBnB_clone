#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os

class FileStorage:
    """Class for serializtion and deserialization of base classes."""
    __file_path = "file.json"
    __objects = {}
    
    def all(self): 
        """returns the dictionary __objects"""
        # TODO: should this be a copy()?
        return FileStorage.__objects

    def new(self, obj): 
        """sets in __objects the obj with key <obj class name>.id"""
        # TODO: should these be more precise specifiers?
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self): 
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self): 
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; 
            otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        if not os.path.isfile(FileStorage.__file_path)
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v) for k, v in obj_dict.items()}
            # TODO: should this overwrite or insert?
            FileStorage.__objects = obj_dict



    
