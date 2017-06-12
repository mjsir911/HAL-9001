#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

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

standards = (1459,)
url = 'https://tools.ietf.org/html/rfc{}'

pyth_str = '''def test_{cmd}(self):
    """
    parameters: {params}
    """
    self.bot.command['{cmd}']({args})
'''
def process_command(command):
    cmd = command[0].split()
    cmd = cmd[1]
    p = ''
    args = []
    if 'parameters:' in command[1].lower():
        p = command[1]
        p = p[p.find(':')+1:]
        p = p.replace('&lt;', '<')
        p = p.replace('&gt;', '>')
        args = p
        if 'None' in args:
            args = []
        else:
            while '[' in args or ']' in args:
                args = args[0:args.find('[')] + args[args.find(']')+1:]
            while '{' in args or '}' in args:
                args = args[0:args.find('{')] + args[args.find('}')+1:]
            args = [a.strip().replace('<', '').replace('>', '').replace(' ', '_') for a in args.split('> <')]
    print(pyth_str.format(cmd=cmd, params=p, args=', '.join(args)))
    return cmd

for s_num in standards:
    r =  requests.get(url.format(s_num))
    lines = r.text.split('\n')
    for i, line in enumerate(lines):
        if 'command: ' in line.lower():
            process_command(lines[i:i+2])
"""
test_command = ['Command: PRIVMSG',
'Parameters: &lt;receiver&gt;{,&lt;receiver&gt;} &lt;text to be sent&gt;']
process_command(test_command)
"""
