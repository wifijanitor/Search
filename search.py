#!/usr/bin/env python3
import  sys, re

part=sys.argv[1]
file=open("/Cisco/price.txt", 'rt')

rgx=re.compile(part, re.I)
for line in file:
	if re.search(rgx, line):
		print(line)
