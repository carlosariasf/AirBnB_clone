#!/usr/bin/python3
"""Unittest Console"""
import unittest
import os
import pep8
from console import HBNBCommand
from unittest.mock import create_autospec
from datetime import datetime


class test_console(unittest.TestCase):
    """ Test Console """

    @classmethod
    def setUpClass(cls):
        cls.m_stdin = create_autospec(os.sys.stdin)
        cls.m_stdout = create_autospec(os.sys.stdout)

    @classmethod
    def tearDownClass(cls):
        """ teardown class """
        del cls.m_stdin
        del cls.m_stdout
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """ Pep8 test """
        pepr = pep8.StyleGuide(quiet=True)
        result = pepr.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep")

    def test_attrb(self):
        ''' test attr '''
        self.assertTrue(hasattr(HBNBCommand, "default"))
        self.assertTrue(hasattr(HBNBCommand, "do_EOF"))
        self.assertTrue(hasattr(HBNBCommand, "do_quit"))
        self.assertTrue(hasattr(HBNBCommand, "emptyline"))
        self.assertTrue(hasattr(HBNBCommand, "do_create"))
        self.assertTrue(hasattr(HBNBCommand, "do_show"))
        self.assertTrue(hasattr(HBNBCommand, "do_destroy"))
        self.assertTrue(hasattr(HBNBCommand, "do_all"))
        self.assertTrue(hasattr(HBNBCommand, "do_count"))
        self.assertTrue(hasattr(HBNBCommand, "do_update"))
        self.assertTrue(hasattr(HBNBCommand, "do_destroy"))
