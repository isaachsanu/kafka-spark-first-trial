from confluent_kafka.admin import AdminClient, NewTopic

def create_topic():
    admin_client = AdminClient({'bootstrap.servers': 'kafka:9092'})
    topic = NewTopic("your_topic_name", num_partitions=1, replication_factor=1)
    admin_client.create_topics([topic])

if __name__ == "__main__":
    create_topic()
