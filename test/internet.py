#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
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

standards = (1459,)
url = 'https://tools.ietf.org/html/rfc{}'

for s_num in standards:
    with open('{}/RFC{}_commands.list'.format(__init__.path, s_num), 'w') as fp:
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
