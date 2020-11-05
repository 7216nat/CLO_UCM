#!/usr/bin/python3.8

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    if sys.argv[1] in line:
        print (line)
