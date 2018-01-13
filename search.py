#!/usr/bin/env python3
import os
import sys
import re
version = 2.0

part = sys.argv[1]
file = open(os.path.expanduser('~/Cisco/price.txt'))

rgx = re.compile(part, re.I)
for line in file:
    if re.search(rgx, line):
        print(line)
file.close()
