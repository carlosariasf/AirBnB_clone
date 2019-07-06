#!/usr/bin/python3
""" UnitTest User """
import unittest
import os
import pep8
from models.amenity import Amenity
from datetime import datetime



class test_amenity(unittest.TestCase):
    '''Tests user from Base'''

    @classmethod
    def setUpClass(cls):
        ''' another comment '''
        cls.tmp = Amenity()

    @classmethod
    def tearDownClass(cls):
        ''' another comment '''
        del cls.tmp
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8(self):
        ''' another comment '''
        peptest = pep8.StyleGuide(quiet=True)
        exc = peptest.check_files(['models/amenity.py'])
        self.assertEqual(exc.total_errors, 0, "Fix pep")

    def test_docs(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_check_att(self):
        ''' another comment '''
        self.assertTrue(hasattr(Amenity, "name"))

    def test_save(self):
        ''' another comment '''
        self.tmp.save()
        self.assertNotEqual(self.tmp.created_at, self.tmp.updated_at)

    def test_id(self):
        """ another comment """
        self.assertEqual(str, type(self.tmp.id))

    def test_created_at(self):
        """ another comment """
        self.assertEqual(datetime, type(self.tmp.created_at))

    def test_updated_at(self):
        """ another comment """
        self.assertEqual(datetime, type(self.tmp.updated_at))

    def test_dic(self):
        ''' another test '''
        test_dic = self.tmp.to_dict()
        self.assertEqual(type(test_dic), dict)
        self.assertTrue('to_dict' in dir(self.tmp))

if __name__ == "__main__":
    unittest.main()
