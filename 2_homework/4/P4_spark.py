from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import string
import csv

conf = SparkConf().setMaster('local').setAppName('P4_spark')
sc = SparkContext(conf = conf)
spark = SparkSession(sc)

df = spark.read.options(header='true').csv("ratings.csv")

# cast de las columnas que me interesan
df = df.withColumn("rating", df["rating"].cast(DoubleType()))
df = df.withColumn("movieId", df["movieId"].cast(IntegerType()))

# seleciono las dos columnas
df = df.select('movieId', 'rating')

# hacer un drop de aquellas filas que tengan un null
df = df.dropna()

# agrupar por id y hacer la media
df = df.groupby('movieId').mean('rating')

# sort por la valoracion
df.orderBy('avg(rating)').show()

