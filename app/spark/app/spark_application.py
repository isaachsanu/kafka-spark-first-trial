from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 pyspark-shell'

# # Create a SparkContext
# sc = SparkContext(appName="SparkStreamingApp")
# # Create a StreamingContext with a batch interval of 1 second
# ssc = StreamingContext(sparkContext=sc, batchDuration=1)

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