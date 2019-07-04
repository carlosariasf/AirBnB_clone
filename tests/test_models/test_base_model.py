#!/usr/bin/python3
'''Unittest for base_model'''
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import pep8


class test_base_model(unittest.TestCase):
    '''Tests BaseModel class'''

    @classmethod
    def setUpClass(cls):
        '''set up before every test method'''
        cls.base1 = BaseModel()

    @classmethod
    def teardown(cls):
        '''remove test instances'''
        del cls.base1
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8_test_style(self):
        '''Pep8 style test'''
        pepe = pep8.StyleGuide(quiet=True)
        res = pepe.check_files(['models/base_model.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def test_docstring_test(self):
        '''Checks for docs'''
        for doc_fun in dir(BaseModel):
            self.assertIsNotNone(doc_fun.__doc__)

    def test_docstring_class_class(self):
        self.assertIsNotNone(BaseModel.__doc__)

    def test_check_if_hasattr(self):
        """Checks if the methods exists"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_isinstance(self):
        self.assertIsInstance(self.base1, BaseModel)

    def test_save(self):
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)
        self.an = self.base1.updated_at
        self.base1.save()
        self.des = self.base1.updated_at
        self.assertIsNot(self.an, self.des)

    def test_id_fun_test(self):
        """ test id functionality """
        self.assertEqual(str, type(self.base1.id))

    def test_created_at_fun_test(self):
        """ test created_at functionality"""
        self.assertEqual(datetime, type(self.base1.created_at))

    def test_updated_at_fun_test(self):
        """ test updated_at functionality"""
        self.assertEqual(datetime, type(self.base1.updated_at))

    def test_dictionary_test(self):
        '''Tests to_dict method'''
        test_dict = self.base1.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue('to_dict' in dir(self.base1))
        self.assertIsInstance(test_dict["created_at"], str)
        self.assertIsInstance(test_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()
