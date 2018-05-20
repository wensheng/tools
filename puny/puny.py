#!/usr/bin/env python3

import re
import sys

name, tld = re.split(r'[\.。]', sys.argv[1])
print("xn--%s.xn--%s" % (name.encode("punycode").decode(),
                         tld.encode("punycode").decode()))
