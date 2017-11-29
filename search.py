#!/usr/bin/env python3
import  os,sys, re

part=sys.argv[1]
file=open(os.path.expanduser('~/Cisco/price.txt'))

rgx=re.compile(part, re.I)
for line in file:
	if re.search(rgx, line):
		print(line)
file.close()
