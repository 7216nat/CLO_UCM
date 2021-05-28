from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import year
import string
import csv

conf = SparkConf().setMaster('local').setAppName('P3_spark')
sc = SparkContext(conf = conf)
spark = SparkSession(sc)

df = spark.read.options(header='true').csv("GOOGLE.csv")

# cast de StringType a DoubleType para la columna Close
df = df.withColumn("Close", df["Close"].cast(DoubleType()))

# sustituyo la columna de fecha por su año
df = df.withColumn("Date", year(df["Date"]))

# selecciono solamente las columnas Date y Close
df = df.select('Date', 'Close')

# drop de las filas con null
df = df.dropna()

# agrupar por Date y calculo su media
df = df.groupby('Date').mean('Close').sort('Date').show()




