from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

# Create a Spark Streaming context
ssc = StreamingContext(sparkContext, 1)

# Connect to Kafka and create a DStream
kafkaParams = {"metadata.broker.list": "kafka:9092"}
topics = ["your_topic_name"]
kafkaStream = KafkaUtils.createDirectStream(ssc, topics, kafkaParams)

# Process the Kafka stream
kafkaStream.foreachRDD(lambda rdd: print(rdd.collect()))

# Start the streaming context
ssc.start()
ssc.awaitTermination()
