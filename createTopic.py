from kafka.admin import KafkaAdminClient, NewTopic
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092")

topic_list = []
topic_list.append(NewTopic(name="stockWiseData", num_partitions=4, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)