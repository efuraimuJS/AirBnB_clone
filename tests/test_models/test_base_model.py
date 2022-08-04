#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid

class TestBaseModel(unittest.TestCase):
    """Test Cases for the BaseModel class."""
    
    def setUp(self):
        """Sets up test methods."""
        pass