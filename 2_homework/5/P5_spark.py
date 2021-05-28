from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import string
import csv

conf = SparkConf().setMaster('local').setAppName('P5_spark')
sc = SparkContext(conf = conf)
spark = SparkSession(sc)

# Nombres de las columnas 
schemaString = ['name','id', 'nametype','recclass','mass','fall','year','reclat','reclong', 'Geolocation']

# darles tipo a las columnas
fields = [StructField(fieldname, StringType(), True) for fieldname in schemaString]

# especificamente mass tiene que ser del tipo double
fields[4] = StructField('mass', DoubleType(), True)

# asigno schema a los datos
schema = StructType(fields)
df = spark.read.schema(schema).csv("Meteorite_Landings.csv")

# selecciono las dos clases que me interesan
df = df.select('recclass', 'mass')

# drop filas con null
df = df.dropna()

# filtro de masas invalidas
df = df.filter(df.mass > 0)

# agrupar por recclass y calcula la media, y un sort
df = df.groupby('recclass').mean('mass').sort('recclass').show()
