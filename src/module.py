#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import hashlib
import importlib
import sys

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


mdir = 'modules'
mods = [m[:-3] for m in os.listdir(mdir) if m[-3:] == '.py']
def module_manager(mdir, mods):
    oldpath = sys.path
    sys.path = [mdir]
    imported = [importlib.import_module(m) for m in mods]
    sys.path = oldpath
    z = []
    for imp in imported:
        if not getattr(imp, '__all__', False):
            continue
        z.extend(getattr(imp, name) for name in imp.__all__)
    return z

class Update_Keeper():
    def __init__(self, module_directory):
        self.mdir = os.path.abspath(module_directory)
        self.hashes = {}
        self()

    @property
    def modules(self):
        return [m[:-3] for m in os.listdir(self.mdir) if m[-3:] == '.py']

    @property
    def i_modules(self):
        return dict((m.__name__, m) for m in self.hashes)


    @staticmethod
    def get_important(module):
        if not getattr(module, '__all__', False):
            return []
        else:
            return [getattr(module, name) for name in module.__all__]

    def get_module_hash(self, mod_name):
        path = '{}/{}.py'.format(self.mdir, mod_name)
        d = hashlib.md5()
        with open(path, 'rb') as f:
            buf = True
            while buf:
                buf = f.read(128)
                d.update(buf)
        return d.hexdigest()

    def get_module(self, mod_name):
        oldpath = sys.path
        sys.path = [self.mdir]
        m_mod = self.i_modules.get(mod_name, False)
        m_hash = self.get_module_hash(mod_name)
        if not m_mod:
            imported = importlib.import_module(mod_name)
        elif m_hash != self.hashes.get(m_mod, False):
            imported = importlib.reload(m_mod)
        else:
            imported = m_mod
        sys.path = oldpath
        return {imported: m_hash}


    def __iter__(self):
        self()
        for module in self.hashes:
            for item in self.get_important(module):
                yield item

    def __call__(self):
        for mod in self.modules:
            self.hashes.update(self.get_module(mod))
