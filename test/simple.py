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
    def testSimpleModule(self):
        from HAL_9001.bot import Bot
        from HAL_9001.abc import Address, Ident
        addr = Address('irc.freenode.net', 6666)
        identy = Ident('hal', 'irc.freenode.net', 'hal')
        tmpdir = tempfile.gettempdir()
        bot = Bot(addr, identy, tmpdir)
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
                    del self.bot.channels[
                            self.bot.channels.index(self.channel)
                            ] # remove chanel from channels
                    self.bot.everything.remove(self)

        bot.addMod(SaySomethingThenQuit)

        self.assertEquals(len(bot.everything), 1)
        self.assertNotIn('#bot-test', bot.channels)

        bot.step()

        self.assertEquals(len(bot.everything), 1)
        self.assertIn('#bot-test', self.bot.channels)

        bot.step()

        self.assertEquals(len(bot.everything), 0)
        self.assertNotIn('#bot-test', self.bot.channels)

        time.sleep(1)



if __name__ == '__main__':
    unittest.main()
