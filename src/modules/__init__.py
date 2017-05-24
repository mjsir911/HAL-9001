#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import importlib

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

module_names = [m[:-3] for m in
        os.listdir(os.path.dirname(os.path.abspath(__file__))) if m[-3:] ==
        '.py' and m != '__init__.py']

modules = {}
for module in module_names:
    modules[module] = importlib.import_module('.' + module, package=__name__)
    del globals()[module]
    del module

important = {}
for module in modules.values():
    important[module] = tuple(getattr(module, a) for a in getattr(module,
        '__all__', []))


"""
__all__ = []
for module in modules:
    module = importlib.import_module('.' + module, package=__name__)
    for important in getattr(module, '__all__', []):
        globals()[important] = getattr(module, important)
        __all__.append(important)
del module
del modules
"""
