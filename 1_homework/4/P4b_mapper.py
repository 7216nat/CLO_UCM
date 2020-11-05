#!/usr/bin/python3.8

import sys
import math
from datetime import datetime

for line in sys.stdin:
	key, value = line.split( '\t' )
	value = math.ceil(float(value))
	print(str(value)  + '\t'+ key)
