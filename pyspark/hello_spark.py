# Pyspark starts with initializing a sparkSession 

from pyspark.sql import SparkSession, Row
from datetime import datetime, date 
import pandas as pd 

spark = SparkSession.builder.getOrCreate()

# Create a data frame from a list of rows 
df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=2., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=3, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])

print(df)