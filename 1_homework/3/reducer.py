#!/usr/bin/python3.8

import sys
import re
previous = None
sum = 0
count = 0

for line in sys.stdin:
    key, value = line.split( '\t' )
    key = re.split('-', key)[0]
    
    if key != previous:
        if previous is not None:
            print (str(sum/count) + '\t' + previous)
        previous = key
        sum = 0
        count = 0
    
    sum = sum + float( value )
    count += 1

print (str(sum/count) + '\t' + previous)
