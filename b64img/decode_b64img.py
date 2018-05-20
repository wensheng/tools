#!/usr/bin/env python

import base64
import sys

if len(sys.argv)!=3:
    exit("Usage: %s input_file output_file"%sys.argv[0])

i = open(sys.argv[1])
t = i.read()
if ',' in t:
    h, t = t.split(',')
    print(h)

try:
    c = base64.b64decode(t)
except base64.binascii.Error:
    exit("invalid base64 file")

o = open(sys.argv[2],'wb')
o.write(c)
i.close()
o.close()
