from confluent_kafka import Consumer, KafkaException

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['my_topic'])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                continue
            else:
                print(f"Consumer error: {msg.error()}")
                break
        print(f"Received message: {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    pass

consumer.close()
