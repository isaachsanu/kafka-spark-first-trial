from pyspark import SparkContext
from pyspark.sql import SparkSession

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1 pyspark-shell'

spark = SparkSession \
    .builder \
    .appName("SparkStreamingApp") \
    .getOrCreate()

df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka:9092") \
  .option("subscribe", "your_topic_name") \
  .load()

# # Start the streaming context
# ssc.start()
# ssc.awaitTermination()

# Write the streaming data to the console
query = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Wait for the query to terminate
query.awaitTermination()