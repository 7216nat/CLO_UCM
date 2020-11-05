#!/usr/bin/python3.8

import sys
import re
import csv
from datetime import datetime

data = sys.stdin.readlines()
for line in list(csv.reader(data))[1:]:
	_type = line[3].strip()
	mass = line[4]
	if mass and float(mass) > 0:
		print(_type.lower() + '\t'+ mass)
