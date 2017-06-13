#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import inspect
import os
import html

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

standards = (1459, 2812)
url = 'https://tools.ietf.org/html/rfc{}'

for s_num in standards:
    path = '{}/RFC{}_commands.list'.format(__init__.__path__, s_num)
    if not os.path.exists(path):
        with open(path, 'w') as fp:
            r =  requests.get(url.format(s_num))
            lines = r.text.split('\n')
            for i, line in enumerate(lines):
                if 'command:' in line.lower():
                        fp.write(html.unescape(' '.join(w.strip() for w in lines[i:i+2])))
                        fp.write('\n')

"""
test_command = ['Command: PRIVMSG',
'Parameters: &lt;receiver&gt;{,&lt;receiver&gt;} &lt;text to be sent&gt;']
process_command(test_command)
"""

import collections

def flatten(l):
    t = []
    for sl in l:
        if isinstance(sl, collections.abc.Iterable):
            t.extend(flatten(sl))
        else:
            t.append(sl)
    return tuple(t)

class Bracketted():
    bracket_map  = {'<': '>', '{': '}', '[': ']'}
    def __init__(self, contents, bracket):
        self.bracket  = bracket
        self.contents = contents

    @classmethod
    def splitstr(cls, string):
        brack = min([string.find(b) for b in cls.bracket_map if string.find(b) !=
                -1])
        first = string[brack: string.find( cls.bracket_map[string[brack]]) + 1]

        string = string.replace(first, '', 1).strip()

        if string == '[]':
            string = []
        """
        print('ostring:', string)
        print('fbrack:', brack)
        print('first:', first)
        print('string:', string)
        print(type(string))
        #print(string, first)
        """
        if not string:
            return cls.fromstr(first)
        if not first:
            return cls.fromstr(string)

        return flatten([cls.fromstr(first), cls.splitstr(string)])

    @classmethod
    def fromstr(cls, string):
        string = string.strip()
        string = string.replace(',', '')
        if not string:
            return
        if string[-1] == cls.bracket_map[string[0]]:
            inside = string[1: -1]
            inside_brackets = [inside.find(b) for b in cls.bracket_map if
                    inside.find(b) != -1]
            if len(inside_brackets) == 0:
                return cls(inside, string[0])
            else:
                return cls(cls.splitstr(inside), string[0])
        else:
            return cls.splitstr(string)

    def parametrize(self, kind=inspect.Parameter.POSITIONAL_ONLY, uniques=None):
        if uniques is None:
            uniques = {}
        if self.contents in uniques:
            uniques[self.contents] += 1
            self.contents += '1'
        else:
            uniques[self.contents] = 0
        if self.bracket == '[':
            kind = inspect.Parameter.KEYWORD_ONLY
        elif self.bracket == '{':
            if kind == inspect.Parameter.POSITIONAL_ONLY:
                kind = inspect.Parameter.VAR_POSITIONAL
            elif kind == inspect.Parameter.KEYWORD_ONLY:
                kind = inspect.Parameter.VAR_KEYWORD
            else:
                print('WARNING,', kind)
        if isinstance(self.contents, str):
            return inspect.Parameter(self.contents.replace(' ', '_'), kind)
        elif isinstance(self.contents, collections.abc.Iterable):
            return [each.parametrize(kind, uniques) for each in self.contents]
        elif isinstance(self.contents, type(self)):
            return self.contents.parametrize(kind, uniques)


    def __repr__(self):
        if isinstance(self.contents, str):
            return self.bracket + self.contents + self.bracket_map[self.bracket]
        elif isinstance(self.contents, collections.abc.Iterable):
            return self.bracket + ' '.join(str(b) for b in self.contents) + self.bracket_map[self.bracket]
        else:
            return self.bracket + str(self.contents) + self.bracket_map[self.bracket]
