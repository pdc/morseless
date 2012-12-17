#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import re
import json

alphanumeric_pattern = re.compile(r"""
    ^\|  \s
    \{\{Audio-nohelp\|.* \s morse \s code\.ogg\|
    (?P<char>[A-Z0-9])
    \}\} \s  \|\| \s '''
    (?P<morse>(?:·|&nbsp;|–)+)
    ''' \s*
    """, re.VERBOSE)
punctuation_pattern = re.compile(r"""
    ^\|  \s
    \[\[.*?\]\] \s \[
    (?P<char>.)
    \]  \s  \|\| \s '''
    (?P<morse>(?:·|&nbsp;|–)+)
    ''' \s*
    """, re.VERBOSE)

data_dir = os.path.dirname(__file__)
data_file = os.path.join(data_dir, 'wikipedia-table.txt')
to_morse = {}
from_morse = {}
with open(data_file, 'rt') as strm:
    for line in strm:
        for pattern in [alphanumeric_pattern, punctuation_pattern]:
            m = pattern.match(line)
            if m:
                char = m.group('char')
                morse = m.group('morse').replace('&nbsp;', '').replace('·', '.').replace('–', '-')
                to_morse[char] = morse
                from_morse[morse] = char

out_file = os.path.join(data_dir, 'to-morse.json')
with open(out_file, 'wb') as strm:
    json.dump(to_morse, strm, indent=4)
    print 'Wrote JSON to ', out_file

out_file = os.path.join(data_dir, 'from-morse.json')
with open(out_file, 'wb') as strm:
    json.dump(from_morse, strm, indent=4)
    print 'Wrote JSON to ', out_file