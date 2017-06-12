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

def testBot():
        from HAL_9001.bot import Bot
        from HAL_9001.abc import Address, Ident
        addr = Address('irc.freenode.net', 6666)
        identy = Ident('hal', 'irc.freenode.net', 'hal')
        tmpdir = tempfile.gettempdir()

        return Bot(addr, identy, tmpdir)

class RFC1459_Case(unittest.TestCase):
    """
    TODO: auto-create
    https://tools.ietf.org/html/rfc1459
    """
    @classmethod
    def setUp(cls):
        cls.bot = testBot()

    def test_PASS(self):
        """
        parameters:  <password>
        """
        self.bot.command['PASS'](password)

    def test_NICK(self):
        """
        parameters:  <nickname> [ <hopcount> ]
        """
        self.bot.command['NICK'](nickname)

    def test_USER(self):
        """
        parameters:  <username> <hostname> <servername> <realname>
        """
        self.bot.command['USER'](username, hostname, servername, realname)

    def test_SERVER(self):
        """
        parameters:  <servername> <hopcount> <info>
        """
        self.bot.command['SERVER'](servername, hopcount, info)

    def test_OPER(self):
        """
        parameters:  <user> <password>
        """
        self.bot.command['OPER'](user, password)

    def test_QUIT(self):
        """
        parameters:  [<Quit message>]
        """
        self.bot.command['QUIT']()

    def test_SQUIT(self):
        """
        parameters:  <server> <comment>
        """
        self.bot.command['SQUIT'](server, comment)

    def test_JOIN(self):
        """
        parameters:  <channel>{,<channel>} [<key>{,<key>}]
        """
        self.bot.command['JOIN'](channel)

    def test_PART(self):
        """
        parameters:  <channel>{,<channel>}
        """
        self.bot.command['PART'](channel)

    def test_MODE(self):
        """
        parameters:
        """
        self.bot.command['MODE']()

    def test_TOPIC(self):
        """
        parameters:  <channel> [<topic>]
        """
        self.bot.command['TOPIC'](channel)

    def test_NAMES(self):
        """
        parameters:  [<channel>{,<channel>}]
        """
        self.bot.command['NAMES']()

    def test_LIST(self):
        """
        parameters:  [<channel>{,<channel>} [<server>]]
        """
        self.bot.command['LIST']()

    def test_INVITE(self):
        """
        parameters:  <nickname> <channel>
        """
        self.bot.command['INVITE'](nickname, channel)

    def test_KICK(self):
        """
        parameters:  <channel> <user> [<comment>]
        """
        self.bot.command['KICK'](channel, user)

    def test_VERSION(self):
        """
        parameters:  [<server>]
        """
        self.bot.command['VERSION']()

    def test_STATS(self):
        """
        parameters:  [<query> [<server>]]
        """
        self.bot.command['STATS']()

    def test_LINKS(self):
        """
        parameters:  [[<remote server>] <server mask>]
        """
        self.bot.command['LINKS'](server_mask)

    def test_TIME(self):
        """
        parameters:  [<server>]
        """
        self.bot.command['TIME']()

    def test_CONNECT(self):
        """
        parameters:  <target server> [<port> [<remote server>]]
        """
        self.bot.command['CONNECT'](target_server)

    def test_TRACE(self):
        """
        parameters:  [<server>]
        """
        self.bot.command['TRACE']()

    def test_ADMIN(self):
        """
        parameters:  [<server>]
        """
        self.bot.command['ADMIN']()

    def test_INFO(self):
        """
        parameters:  [<server>]
        """
        self.bot.command['INFO']()

    def test_PRIVMSG(self):
        """
        parameters:  <receiver>{,<receiver>} <text to be sent>
        """
        self.bot.command['PRIVMSG'](receiver, text_to_be_sent)

    def test_NOTICE(self):
        """
        parameters:  <nickname> <text>
        """
        self.bot.command['NOTICE'](nickname, text)

    def test_WHO(self):
        """
        parameters:  [<name> [<o>]]
        """
        self.bot.command['WHO']()

    def test_WHOIS(self):
        """
        parameters:  [<server>] <nickmask>[,<nickmask>[,...]]
        """
        self.bot.command['WHOIS'](nickmask)

    def test_WHOWAS(self):
        """
        parameters:  <nickname> [<count> [<server>]]
        """
        self.bot.command['WHOWAS'](nickname)

    def test_KILL(self):
        """
        parameters:  <nickname> <comment>
        """
        self.bot.command['KILL'](nickname, comment)

    def test_PING(self):
        """
        parameters:  <server1> [<server2>]
        """
        self.bot.command['PING'](server1)

    def test_PONG(self):
        """
        parameters:  <daemon> [<daemon2>]
        """
        self.bot.command['PONG'](daemon)

    def test_ERROR(self):
        """
        parameters:  <error message>
        """
        self.bot.command['ERROR'](error_message)

    def test_AWAY(self):
        """
        parameters:  [message]
        """
        self.bot.command['AWAY']()

    def test_REHASH(self):
        """
        parameters:  None
        """
        self.bot.command['REHASH']()

    def test_RESTART(self):
        """
        parameters:  None
        """
        self.bot.command['RESTART']()

    def test_SUMMON(self):
        """
        parameters:  <user> [<server>]
        """
        self.bot.command['SUMMON'](user)

    def test_USERS(self):
        """
        parameters:  [<server>]
        """
        self.bot.command['USERS']()

    def test_WALLOPS(self):
        """
        parameters:  Text to be sent to all operators currently online
        """
        self.bot.command['WALLOPS'](Text_to_be_sent_to_all_operators_currently_online)

    def test_USERHOST(self):
        """
        parameters:  <nickname>{<space><nickname>}
        """
        self.bot.command['USERHOST'](nickname)

    def test_ISON(self):
        """
        parameters:  <nickname>{<space><nickname>}
        """
        self.bot.command['ISON'](nickname)


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
