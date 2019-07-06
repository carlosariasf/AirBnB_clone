#!/usr/bin/python3
"""Unittest for FileStorage"""
import unittest
import os
import pep8
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class test_FileStorage(unittest.TestCase):
    """ Tests FileStorage """

    @classmethod
    def setUpClass(cls):
        """set up before every test method"""
        cls.obj_tmp = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """remove test instances"""
        del cls.obj_tmp
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8(self):
        """ another comment """
        pep_test = pep8.StyleGuide(quiet=True)
        exc = pep_test.check_files(['models/engine/file_storage.py'])
        self.assertEqual(exc.total_errors, 0, "Fix Style")

    def test_check_attr(self):
        """ another comment """
        self.assertTrue(hasattr(models.storage, "_FileStorage__file_path"))
        self.assertTrue(type(self.obj_tmp._FileStorage__file_path) is str)

    def test_all(self):
        """ another comment """
        dict_tmp = self.obj_tmp.all()
        self.assertIsInstance(dict_tmp, dict)
        self.assertIs(dict_tmp, self.obj_tmp._FileStorage__objects)

    def test_reload(self):
        """ another comment """
        self.assertIsNotNone(FileStorage.reload)
        try:
            os.remove("file.json")
        except BaseException:
            pass
        with open("file.json", "w") as writer:
            writer.write("{}")
        with open("file.json", "r") as reader:
            for i in reader:
                self.assertEqual(i, "{}")
        self.assertIs(self.obj_tmp.reload(), None)

    def test_new(self):
        """ another comment """
        dict_tmp = self.obj_tmp.all()
        new = BaseModel()
        tmp = "{}.{}".format(type(new).__name__, new.id)
        self.assertTrue(tmp in dict_tmp.keys())

    def test_save(self):
        """ another comment """
        self.assertIsNotNone(FileStorage.save)
        self.obj_tmp.save()
        with open("file.json", 'r') as reader:
            string = reader.readlines()
        try:
            os.remove("file.json")
        except BaseException:
            pass
        self.obj_tmp.save()
        with open("file.json", 'r') as reader:
            string2 = reader.readlines()
        self.assertEqual(string, string2)
        self.assertTrue(os.path.exists("file.json"))

if __name__ == "__main__":
    unittest.main()
