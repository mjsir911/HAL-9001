#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import tempfile
import inspect
import os
import time
import collections
import internet

import __init__


__appname__     = ""
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "msirabel@gmail.com"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""
__all__         = []

def testBot():
        from HAL_9001.bot import Bot
        from HAL_9001.abc import Address, Ident
        addr = Address('irc.freenode.net', 6666)
        identy = Ident('hal', 'irc.freenode.net', 'hal')
        tmpdir = tempfile.gettempdir()

        return Bot(addr, identy, tmpdir)



class RFC_Type(type):
    @classmethod
    def process_command(cls, attrs, command):
        command = command.split()
        command = command[1:]

        name = command[0]
        command = command[1:]

        p = ''
        args = []
        sigerr = False
        sig = None
        if command and 'parameters:' in command[0].lower():
            p = ' '.join(command)
            p = p[p.find(':')+1:].strip()
        try:
            sig = internet.Bracketted.signature(p)
            """
            print('-' * 64)
            print(name)
            print('=' * 64)
            print(p)
            print('*' * 64)
            print(sig)
            print('-' * 64)
            """
        except ValueError as e:
            try:
                args = args[0], args[2], args[1]
                sig = inspect.Signature(args)
            except Exception:
                pass
        except Exception as e:
            pass

        def wrapper(self):
            """
            parameters: {}
            """.format(p)
            self.assertIn(name, self.bot.command.keys())
            if sig:
                self.assertEqual(inspect.signature(self.bot.command[name]), sig)
            self.bot.command[name](*args)

        wrapper.__name__ = 'test_{}'.format(name)
        attrs[wrapper.__name__] = wrapper

    def __new__(cls, name, bases, attrs):

        spec = name.replace('_Case', '')

        with open('{}/{}_commands.list'.format(__init__.__path__, spec)) as fp:
            for line in fp.readlines():
                cls.process_command(attrs, line)


        return super().__new__(cls, name, bases, attrs)

class RFC1459_Case(unittest.TestCase, metaclass=RFC_Type):
    """
    https://tools.ietf.org/html/rfc1459
    """

    @classmethod
    def setUp(cls):
        cls.bot = testBot()

class RFC2812_Case(unittest.TestCase, metaclass=RFC_Type):
    """
    https://tools.ietf.org/html/rfc2812
    """

    @classmethod
    def setUp(cls):
        cls.bot = testBot()
