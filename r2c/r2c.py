#!/bin/env python

"""
Author: Wensheng Wang (http://wensheng.com/)
license: WTFPL

This program change change rows to columns in a ASCII text file.
for example:
-----------
hello

world
!
-----------
will be converted to:
-----------
h w!
e o
l r
l l
o d
-----------

If you specify '-b', vertical bars will be added to non-empty line to fill up spaces, 
empty lines will still become empty columns, for example:
-----------
goodbye

world
-------------
will be converted to:
-----------
g w
o o
o r
d l
b d
y |
e |
-----------

By default, output will be printed to screen, use > to redirect output to a file.
If "-o filename" is specified, the output will be saved to the specified file.
"""

import sys
import os
from optparse import OptionParser

usage = "Usage: %prog [options] name"
parser = OptionParser(usage=usage)
parser.set_defaults(columns="",rows="1",delay_type=None)
parser.add_option("-b", "--bars", dest="bars", action="store_true", help="add bars")
parser.add_option("-o", "--output",   dest="ofile", help="output file name")

(coptions,cargs) = parser.parse_args()

if len(cargs) == 0:
    print "ERROR: Must supply file name." 
    sys.exit()

fname = cargs[0]

if coptions.ofile:
    ofile = open(coptions.ofile,'w')
else:
    ofile = sys.stdout

lines = [a[:-1] for a in file(fname).readlines()]

maxlen = max([len(line) for line in lines])

if coptions.bars:
    for i in range(len(lines)):
        if not lines[i]:
            lines[i]=" "*maxlen
        else:
            lines[i]="%s%s"%(lines[i],'|'*(maxlen-len(lines[i])))
else:
    lines = ["%s%s"%(line,' '*(maxlen-len(line))) for line in lines]

for i in range(maxlen):
    for j in lines:
        ofile.write(j[i])
    ofile.write('\n')

ofile.close()
