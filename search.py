#!/usr/bin/env python
from sys import argv
import re

script, part=argv
file=open("/Cisco/price.txt", 'rt')

rgx=re.compile(part, re.I)
for line in file:
	if re.search(rgx, line):
		print(line)