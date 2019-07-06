#!/usr/bin/python3
"""Unittest for base_model"""
import unittest
import os
import pep8
from models.base_model import BaseModel
from datetime import datetime


class Test_b_model(unittest.TestCase):
    """Tests BaseModel """

    @classmethod
    def setUpClass(cls):
        """First class setup"""
        cls.bs = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """ teardown class """
        del cls.bs
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """ Pep8 test """
        pepr = pep8.StyleGuide(quiet=True)
        result = pepr.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix Style")

    def test_attrb(self):
        ''' test attr '''
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_save(self):
        ''' test save '''
        self.bs.save()
        self.assertNotEqual(self.bs.created_at, self.bs.updated_at)
        self.tmp = self.bs.updated_at
        self.bs.save()
        self.desc = self.bs.updated_at
        self.assertIsNot(self.tmp, self.desc)

    def test_isinstance(self):
        self.assertIsInstance(self.bs, BaseModel)

    def test_dict(self):
        ''' test dict '''
        test_dict = self.bs.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue('to_dict' in dir(self.bs))
        self.assertIsInstance(test_dict["created_at"], str)
        self.assertIsInstance(test_dict["updated_at"], str)    

    def test_id(self):
        ''' test id '''
        self.assertEqual(str, type(self.bs.id))

    def test_created_at(self):
        ''' test created_at '''
        self.assertEqual(datetime, type(self.bs.created_at))

    def test_updated_at(self):
        ''' test updated_at '''
        self.assertEqual(datetime, type(self.bs.updated_at))

if __name__ == "__main__":
        unittest.main()
