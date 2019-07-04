i#!/usr/bin/python3
'''Unittest for base_model'''
import unittest
import os
import pep8
from models.base_model import BaseModel
from datetime import datetime


class Test_b_model(unittest.TestCase):
    '''Tests BaseModel'''

    @classmethod
    def set_up_class(cls):
        '''set up class method'''
        cls.bs = BaseModel()

    @classmethod
    def set_down_class(cls):
        '''set down class'''
        del cls.bs
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def docstring_test(self):
        '''validate for docs'''
        for doc_fun in dir(BaseModel):
            self.assertIsNotNone(doc_fun.__doc__)

    def pep8_test(self):
        '''Pep8 test'''
        pep_ = pep8.StyleGuide(quiet=True)
        result = pep_.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix Style")

    def check_if_hasattr_test(self):
        """Checks if the methods exists"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def docstring_class(self):
        self.assertIsNotNone(BaseModel.__doc__)

    def save_test(self):
        self.bs.save()
        self.assertNotEqual(self.bs.created_at, self.bs.updated_at)
        self.aa = self.bs.updated_at
        self.bs.save()
        self.desc = self.bs.updated_at
        self.assertIsNot(self.aa, self.desc)

    def isinstance_test(self):
        self.assertIsInstance(self.bs, BaseModel)

    def dictionary_test(self):
        '''Tests dict method'''
        test_dicty = self.bs.to_dict()
        self.assertEqual(type(test_dicty), dict)
        self.assertTrue('to_dict' in dir(self.bs))
        self.assertIsInstance(test_dicty["created_at"], str)
        self.assertIsInstance(test_dicty["updated_at"], str)    

    def id_fun_test(self):
        """ test id """
        self.assertEqual(str, type(self.bs.id))

    def created_at_fun_test(self):
        """ test created_at functionality"""
        self.assertEqual(datetime, type(self.bs.created_at))

    def updated_at_fun_test(self):
        """ test updated_at functionality"""
        self.assertEqual(datetime, type(self.bs.updated_at))

if __name__ == "__main__":
    unittest.main()
