#!/usr/bin/python3
'''Unittest FileStorage'''
import os
import pep8
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class FileStorage(unittest.TestCase):
    '''Tests FileStorage'''

    @classmethod
    def set_up_class(cls):
        '''set up method'''
        cls.fil = FileStorage()

    @classmethod
    def set_down(cls):
        '''set down method'''
        del cls.fil
        try:
            os.remove("file.json")
        except bseException:
            pass

    def pep8_test(self):
        '''Pep8 test'''
        pep_ = pep8.StyleGuide(quiet=True)
        result = pep_.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Fix Style")
    
    def new_test(self):
        dicty = self.fil.all()
        bs = BaseModel()
        kk = "{}.{}".format(type(bs).__name__, bs.id)
        self.assertTrue(kk in dicty.keys())
    
    def all_test(self):
        dicty = self.fil.all()
        self.assertIsInstance(dicty, dict)
        self.assertIs(dicty, self.fil._FileStorage__objects)
    
    def check_if_hasattr_test(self):
        """Checks methods exists"""
        self.assertTrue(hasattr(models.storage, "_FileStorage__file_path"))
        self.assertTrue(type(self.fil._FileStorage__file_path) is str)

    def save_test(self):
        self.assertIsNotNone(FileStorage.save)
        self.fil.save()
        with open("file.json", 'r') as reader:
            string = reader.readlines()

        try:
            os.remove("file.json")
        except BaseException:
            pass

        self.fil.save()

        with open("file.json", 'r') as reader:
            string2 = reader.readlines()

        self.assertEqual(string, string2)
        self.assertTrue(os.path.exists("file.json"))

    def reload_test(self):
        self.assertIsNotNone(FileStorage.reload)
        try:
            os.remove("file.json")
        except BaseException:
            pass
        with open("file.json", "w") as writer:
            writer.write("{}")
        with open("file.json", "r") as reader:
            for l in reader:
                self.assertEqual(l, "{}")
        self.assertIs(self.fil.reload(), None)

if __name__ == "__main__":
    unittest.main()
