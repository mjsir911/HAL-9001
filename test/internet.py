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
url = 'https://tools.ietf.org/html/{}'

def get_standard(s_name):
    path = '{}/{}.list'.format(__init__.__path__, s_name)
    if not os.path.exists(path):
        print('file not found, downloading')
        r = requests.get(url.format(s_name))
        if r.status_code is not 200:
            raise Exception(r.status_code)
        lines = r.text.split('\n')
        with open(path, 'w') as fp:
            for i, line in enumerate(lines):
                if 'command:' in line.lower():
                    fp.write(html.unescape(' '.join(w.strip() for w in lines[i:i+2])))
                    fp.write('\n')
    return open(path, 'r')

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

class Signature(inspect.Signature):
    def __eq__(self, other):
        return all(p.kind == o.kind for p, o in zip(self.parameters.values(),
            other.parameters.values()))


class Bracketted():
    bracket_map  = {'<': '>', '{': '}', '[': ']'}

    @classmethod
    def find_complementary_brackets(cls, string, index):
        fbrack = string[index], index + 1
        count = 0
        for i, c in enumerate(string[fbrack[1]:]):
            if c == fbrack[0]:
                count += 1
            elif c == cls.bracket_map[fbrack[0]]:
                if count:
                    count -= 1
                else:
                    lbrack = c, i + fbrack[1]
        return lbrack

    @classmethod
    def lowest_bracket(cls, string):
        for i, c in enumerate(string):
            if c in cls.bracket_map:
                return c, i
        return ('', -1)

    def __init__(self, full_params):
        full_params = full_params.replace(',', '')
        bracket = self.lowest_bracket(full_params)
        if bracket[1] < 0:
            self.bracket = '<'
            self.contents = full_params
        else:
            params = full_params[bracket[1] + 1:
                    self.find_complementary_brackets(full_params, bracket[1])[1]]

            if self.lowest_bracket(params)[1] >= 0:
                params = self.split(params)

            self.bracket = bracket[0]
            self.contents = params

    @classmethod
    def split(cls, string):
        string = string.strip()
        string = string.replace('<space>', ' ')
        fbrack = cls.lowest_bracket(string)
        if fbrack[1] < 0:
            return (cls(string),)

        lbrack = cls.find_complementary_brackets(string, fbrack[1])

        first = cls(string[fbrack[1]: lbrack[1] + 1].strip())
        rest = string[:fbrack[1]] + string[lbrack[1] + 1:].strip()
        if rest:
            return (first,) + cls.split(rest)
        return (first,)
    def parametrize(self, maximum=0, uniques=None):

        enum = inspect._ParameterKind

        if uniques is None:
            uniques = {}
        if self.contents in uniques:
            uniques[self.contents] += 1
            self.contents += '1'
        else:
            uniques[self.contents] = 0
        if self.bracket == '[':
            if maximum < 2:
                maximum = 1
            else:
                maximum = 3
        elif self.bracket == '{':
            if maximum <= 2:
                maximum = 2
            else:
                maximum = 4

        if maximum < 2:
            kind = inspect.Parameter.POSITIONAL_OR_KEYWORD
        elif maximum == 2:
            kind = inspect.Parameter.VAR_POSITIONAL
        elif 2 < maximum < 4:
            kind = inspect.Parameter.KEYWORD_ONLY
        elif maximum == 4:
            kind = inspect.Parameter.VAR_KEYWORD
        else:
            print(maximum, 'hi')

        if isinstance(self.contents, str):
            return maximum, inspect.Parameter(self.contents.replace(' ', '_'), kind)
        elif isinstance(self.contents, collections.abc.Iterable):
            z = []
            for each in self.contents:
                maximum, p = each.parametrize(maximum, uniques)
                z.append(p)
            return maximum, z

    @classmethod
    def signature(cls, string):
        if string == 'None' or not string:
            return Signature()
        z = cls.split(string)

        uniques = {}
        args = []
        maximum = 0
        for i in z:
            maximum, p = i.parametrize(maximum=maximum, uniques=uniques)
            args.append(p)
        args = flatten(args)
        return Signature(args)


    def __repr__(self):
        if isinstance(self.contents, str):
            return self.bracket + self.contents + self.bracket_map[self.bracket]
        elif isinstance(self.contents, collections.abc.Iterable):
            return self.bracket + ' '.join(str(b) for b in self.contents) + self.bracket_map[self.bracket]
        else:
            return self.bracket + str(self.contents) + self.bracket_map[self.bracket]
