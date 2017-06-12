#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import tempfile
import os
import time
import collections

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
        if command and 'parameters:' in command[0].lower():
            p = ' '.join(command)
            p = p[p.find(':')+1:].strip()

            args = p
            if 'None' in args:
                args = []
            else:
                while '[' in args or ']' in args:
                    args = args[0:args.find('[')] + args[args.find(']')+1:]

                while '{' in args or '}' in args:
                    args = args[0:args.find('{')] + args[args.find('}')+1:]

                args = [a.strip().replace('<', '').replace('>', '').replace(
                    ' ', '_') for a in args.split('> <')]

        def wrapper(self):
            """
            parameters: {}
            """.format(p)
            self.bot.command[name](*args)

        attrs['test_{}'.format(name)] = wrapper

    def __new__(cls, name, bases, attrs):

        spec = name.replace('_Case', '')

        with open(
                '{}/{}_commands.list'.format(
                    __init__.__path__,
                    spec
                )) as fp:
            for line in fp.readlines():
                cls.process_command(attrs, line)


        return super().__new__(cls, name, bases, attrs)

class RFC1459_Case(unittest.TestCase, metaclass=RFC_Type):
    """
    TODO: auto-create
    https://tools.ietf.org/html/rfc1459
    """

    @classmethod
    def setUp(cls):
        cls.bot = testBot()

@unittest.skip("testing skipping")
class MessageCase(unittest.TestCase):
    def testSimpleModule(self):

        bot = testBot()

        class SaySomethingThenQuit():
            def __init__(self, bot):
                self.bot = bot
                self.channel = '#bot-test'
                self.spoken = False
            def __call__(self):
                if not self.spoken:
                    if self.channel not in self.bot.channels:
                        self.bot.channels.append(self.channel)
                    self.bot.command['PRIVMSG']('Hello world')
                    self.spoken = True
                else:
                    del self.bot.channels[
                            self.bot.channels.index(self.channel)
                            ] # remove chanel from channels
                    self.bot.everything.remove(self)

        bot.addMod(SaySomethingThenQuit)

        with self.subTest():
            self.assertEquals(len(bot.everything), 1)
            self.assertNotIn('#bot-test', bot.channels)

        with self.subTest():
            bot.step()
            self.assertEquals(len(bot.everything), 1)
            self.assertIn('#bot-test', bot.channels)

        with self.subTest():
            bot.step()
            self.assertEquals(len(bot.everything), 0)
            self.assertNotIn('#bot-test', bot.channels)

        time.sleep(1)
