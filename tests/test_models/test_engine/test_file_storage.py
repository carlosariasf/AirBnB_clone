#!/usr/bin/python3
'''Unittest for FileStorage'''
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import pep8


class test_FileStorage(unittest.TestCase):
    '''Tests FileStorage class'''

    @classmethod
    def setUpClass(cls):
        '''set up before every test method'''
        cls.files1 = FileStorage()

    @classmethod
    def teardown(cls):
        '''remove test instances'''
        del cls.files1
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_check_if_hasattr(self):
        """Checks if the methods exists"""
        self.assertTrue(hasattr(models.storage, "_FileStorage__file_path"))
        self.assertTrue(type(self.files1._FileStorage__file_path) is str)

    def test_pep8_test_style(self):
        '''Pep8 style test'''
        pepe = pep8.StyleGuide(quiet=True)
        res = pepe.check_files(['models/engine/file_storage.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def test_all(self):
        s_dict = self.files1.all()
        self.assertIsInstance(s_dict, dict)
        self.assertIs(s_dict, self.files1._FileStorage__objects)

    def test_new(self):
        s_dict = self.files1.all()
        bas = BaseModel()
        kk = "{}.{}".format(type(bas).__name__, bas.id)
        self.assertTrue(kk in s_dict.keys())

    def test_save(self):
        self.assertIsNotNone(FileStorage.save)
        self.files1.save()
        with open("file.json", 'r') as reader:
            string = reader.readlines()

        try:
            os.remove("file.json")
        except BaseException:
            pass

        self.files1.save()

        with open("file.json", 'r') as reader:
            string2 = reader.readlines()

        self.assertEqual(string, string2)
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
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
        self.assertIs(self.files1.reload(), None)

if __name__ == "__main__":
    unittest.main()
