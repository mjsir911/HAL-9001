#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import typing

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

Address = typing.NamedTuple("Address", [('host', str), ('port', int)])
Address.__doc__ = """ Named tuple for server addresses """

Ident = typing.NamedTuple("Ident", [('ident', str), ('host', str), ('realname',
    str)])
Ident.__doc__ = """ Named tuple for identities """
