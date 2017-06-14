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

if __name__ == '__main__':
    def vprint(*args, **kwargs):
        print(*args, **kwargs)
else:
    def vprint(*args, **kwargs):
        pass


def testBot(**kwargs):
        from HAL_9001.bot import Bot
        from HAL_9001.abc import Address, Ident
        addr = Address('irc.freenode.net', 6666)
        identy = Ident('hal', 'irc.freenode.net', 'hal')
        tmpdir = tempfile.gettempdir()

        return Bot(addr, identy, tmpdir, **kwargs)



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
            vprint('-' * 64)
            vprint(name)
            vprint('=' * 64)
            vprint(p)
            vprint('*' * 64)
            vprint(sig)
            vprint([i.kind for i in sig.parameters.values()])
            vprint('-' * 64)
        except Exception as e:
            vprint('error')
            vprint(name)
            def wrapper(self):
                self.fail('name: {}, param: {}, err: {}'.format(name, p,
                'error'))
        else:
            def wrapper(self):
                """
                parameters: {}
                """.format(p)
                self.assertIn(name, self.bot.command.keys())
                if sig:
                    self.assertEqual(inspect.signature(self.bot.command[name]), sig)
                args, kwargs = sig.default()
                with self.subTest(args=args, kwargs=kwargs):
                    self.bot.command[name](*args, **kwargs)

        wrapper.__name__ = 'test_{}'.format(name)
        attrs[wrapper.__name__] = wrapper

    def __new__(cls, name, bases, attrs):

        spec = name.replace('_Case', '')

        with internet.get_standard(spec) as fp:
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

'''
class RFC2812_Case(unittest.TestCase, metaclass=RFC_Type):
    """
    https://tools.ietf.org/html/rfc2812
    """

    @classmethod
    def setUp(cls):
        cls.bot = testBot()
'''

class Custom_Case(unittest.TestCase):

    def testC(self):
        from HAL_9001.bot import Command_Dict
        custom_command_dict = Command_Dict()

        name = 'chanserv'
        @custom_command_dict.something(name)  # TODO: change name
        def chan_command(self, msg):
            return self['PRIVMSG']('chanserv', msg)

        bot = testBot(dict=custom_command_dict)
        self.assertIn(name, self.bot.command.keys())
        self.bot.command[name]('help')
