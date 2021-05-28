from pyspark import SparkConf, SparkContext
import string
import sys

conf = SparkConf().setMaster('local').setAppName('P1_spark')
sc = SparkContext(conf = conf)
word = sys.argv[1]

RDDvar = sc.textFile("input.txt")

aggreg1 = RDDvar.filter(lambda line: word in line.lower()).collect()

for line in aggreg1:
    print line
