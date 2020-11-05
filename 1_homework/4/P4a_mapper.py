#!/usr/bin/python3.8

import sys
import re
import csv
from datetime import datetime

data = sys.stdin.readlines()
for line in list(csv.reader(data))[1:]:
	_id = line[1]
	rate = line[2]
	print(_id + '\t'+ rate)
