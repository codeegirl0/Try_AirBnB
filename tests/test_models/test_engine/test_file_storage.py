#!/usr/bin/python3
"""All unittests for file_storage.
All Unittest class:
    Testfile_storageinst
    TestStorage_meths
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review


class Testfile_storageinst(unittest.TestCase):
    """testing FileStorage class."""

    def test_FileStorage_with_out_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_filepath_in_private_string(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objs_in_private_dictionary(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializing(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestStorage_meths(unittest.TestCase):
    """testing methods of file storage."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bss = BaseModel()
        us = User()
        sta = State()
        plc = Place()
        ctt = City()
        amn = Amenity()
        rww = Review()
        models.storage.new(bss)
        models.storage.new(us)
        models.storage.new(sta)
        models.storage.new(plc)
        models.storage.new(ctt)
        models.storage.new(amn)
        models.storage.new(rww)
        self.assertIn("BaseModel." + bss.id, models.storage.all().keys())
        self.assertIn(bss, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + sta.id, models.storage.all().keys())
        self.assertIn(sta, models.storage.all().values())
        self.assertIn("Place." + plc.id, models.storage.all().keys())
        self.assertIn(plc, models.storage.all().values())
        self.assertIn("City." + ctt.id, models.storage.all().keys())
        self.assertIn(ctt, models.storage.all().values())
        self.assertIn("Amenity." + amn.id, models.storage.all().keys())
        self.assertIn(amn, models.storage.all().values())
        self.assertIn("Review." + rww.id, models.storage.all().keys())
        self.assertIn(rww, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        bss = BaseModel()
        us = User()
        sta = State()
        plc = Place()
        ctt = City()
        amn = Amenity()
        rww = Review()
        models.storage.new(bss)
        models.storage.new(us)
        models.storage.new(sta)
        models.storage.new(plc)
        models.storage.new(ctt)
        models.storage.new(amn)
        models.storage.new(rww)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bss.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + sta.id, save_text)
            self.assertIn("Place." + plc.id, save_text)
            self.assertIn("City." + ctt.id, save_text)
            self.assertIn("Amenity." + amn.id, save_text)
            self.assertIn("Review." + rww.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bss = BaseModel()
        us = User()
        sta = State()
        plc = Place()
        ctt = City()
        amn = Amenity()
        rww = Review()
        models.storage.new(bss)
        models.storage.new(us)
        models.storage.new(sta)
        models.storage.new(plc)
        models.storage.new(ctt)
        models.storage.new(amn)
        models.storage.new(rww)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bss.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + sta.id, objs)
        self.assertIn("Place." + plc.id, objs)
        self.assertIn("City." + ctt.id, objs)
        self.assertIn("Amenity." + amn.id, objs)
        self.assertIn("Review." + rww.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
