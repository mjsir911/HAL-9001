#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import tempfile
import time
import collections

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


class MessageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from HAL_9001.bot import Bot
        from HAL_9001.abc import Address, Ident
        addr = Address('irc.freenode.net', 6666)
        identy = Ident('hal', 'irc.freenode.net', 'hal')
        tmpdir = tempfile.gettempdir()
        cls.bot = Bot(addr, identy, tmpdir)
        class SaySomethingThenQuit():
            def __init__(self, bot):
                self.bot = bot
                self.channel = '#bot-test'
                self.spoken = False
            def __call__(self):
                if not self.spoken:
                    if self.channel not in self.bot.channels:
                        self.bot.channels.append(channel)
                    self.bot.command['PRIVMSG']('Hello world')
                    self.spoken = True
                else:
                    self.bot.everything.remove(self)

        cls.bot.everything.append(SaySomethingThenQuit(cls.bot))
        cls.bot()
        time.sleep(1)

    def testConfirmChannelConnection(self):
        assert '#bot-test' not in self.bot.everything

if __name__ == '__main__':
    unittest.main()
