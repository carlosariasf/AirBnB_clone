#!/usr/bin/python3
"""Unittest Console"""
import unittest
import os
import pep8
from console import HBNBCommand
from unittest.mock import create_autospec
from datetime import datetime


class test_HBNBCommand(unittest.TestCase):
    """ Test Console """

    @classmethod
    def setUpClass(cls):
        cls.m_stdin = create_autospec(os.sys.stdin)
        cls.m_stdout = create_autospec(os.sys.stdout)

    def create(self, server=None):
        """ create temp console"""
        return HBNBCommand(stdin=self.m_stdin, stdout=self.m_stdout)

    def _last_write(self, nr=None):
        """:return: last `n` output lines"""
        if nr is None:
            return self.m_stdout.write.call_args[0][0]
        return "".join(
            map(lambda c: c[0][0], self.m_stdout.write.call_args_list[-nr:]))

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

    def test_quit(self):
        """ test quit """
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))
        self.assertEqual(True, cli.onecmd("quit"))

    def test_create(self):
        """ test create """
        cli = self.create()
        self.assertFalse(cli.onecmd("create"))
        self.assertEqual("** class name missing **", self._last_write())

    def test_show(self):
        """ test show """
        cli = self.create()
        self.assertTrue("** class name missing **", cli.onecmd("show"))

    def test_destroy(self):
        """ test destroy """
        cli = self.create()
        self.assertTrue("** class name missing **", cli.onecmd("destroy"))

    def test_all(self):
        """ test update """
        cli = self.create()
        self.assertTrue("** class doesn't exist **", cli.onecmd("all My"))

    def test_update(self):
        """ test update """
        cli = self.create()
        self.assertTrue("** class name missing **", cli.onecmd("update"))

if __name__ == "__main__":
    unittest.main()
