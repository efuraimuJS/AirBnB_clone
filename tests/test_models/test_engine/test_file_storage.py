#!/usr/bin/python3
"""Unittest module for the FileStorage class."""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import json
import os

class TestFileStorage(unittest.TestCase):
    """Test Cases for the FileStorage class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def test_5_instantiation(self):
        """Tests instantiation of storage class."""
        self.assertEqual(type(storage).__name__, "FileStorage")
    
    def test_3_init_no_args(self):
        """Tests __init__ with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), msg)

    def test_3_init_many_args(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        msg = "object() takes no parameters"
        self.assertEqual(str(e.exception), msg)
    
    def test_5_attributes(self):
        """Tests class attributes."""
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})
    
    def help_test_all(self, classname):
        """Helper tests all() method for classname."""
        self.resetStorage()
        self.assertEqual(storage.all(), {})

        o = storage.classes()[classname]()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], o)
    
    def test_5_all_base_model(self):
        """Tests all() method for BaseModel."""
        self.help_test_all("BaseModel")

    def test_5_all_user(self):
        """Tests all() method for User."""
        self.help_test_all("User")

    def test_5_all_state(self):
        """Tests all() method for State."""
        self.help_test_all("State")

    def test_5_all_city(self):
        """Tests all() method for City."""
        self.help_test_all("City")

    def test_5_all_amenity(self):
        """Tests all() method for Amenity."""
        self.help_test_all("Amenity")

    def test_5_all_place(self):
        """Tests all() method for Place."""
        self.help_test_all("Place")

    def test_5_all_review(self):
        """Tests all() method for Review."""
        self.help_test_all("Review")
    
