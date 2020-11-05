#!/usr/bin/python3.8

import sys
import re

regex = '(.*?) - - \[(.*?)\] "(.*?)" (\d+|-) (\d+|-)'
for line in sys.stdin:
    line = re.match(regex, line).groups()
    print( line[0] + "\t1" )
