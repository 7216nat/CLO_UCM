#!/usr/bin/python3.8

import sys
import re
import csv
from datetime import datetime

data = sys.stdin.readlines()
for line in list(csv.reader(data))[1:]:
	date = line[0]
	price = line[4]
	print(date + '\t'+ price)
	#datetime(int(date[0]),int(date[1]),int(date[2])).strftime("%Y-%m-%d")
