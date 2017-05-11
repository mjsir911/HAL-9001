#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import irc.client
import module

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

class ModuleBot(irc.client.SimpleIRCClient):
    def __init__(self, module_updater, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mod_update = module_updater
    def _dispatcher(self, connection, event):
        for mod in self.mod_update:
            mod(self, connection, event)

z = ModuleBot(module.Update_Keeper(module.mdir))
z.connect('irc.freenode.org', 6666, 'test')
z.start()

__all__ = ['ModuleBot']
