from pyspark import SparkConf, SparkContext
import string
import sys
import re

regex = '(.*?) - - \[(.*?)\] "(.*?)" (\d+|-) (\d+|-)'

conf = SparkConf().setMaster('local').setAppName('P1_spark')
sc = SparkContext(conf = conf)

RDDvar = sc.textFile("access_log")

# un Pattern Match con regex
RDDvar = RDDvar.map(lambda line: re.match(regex, line).groups())

# selecciono la primera coincidencia del patron 
result = RDDvar.map(lambda word: (word[0],1))

aggreg1 = result.reduceByKey(lambda a, b: a+b).collect()

for line in aggreg1:
    print line
