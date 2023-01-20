from kafka import KafkaConsumer
import json

bootstrap_servers = ['localhost:9092']
topicName = 'stockWiseData'
consumer = KafkaConsumer(topicName,bootstrap_servers = bootstrap_servers)

try:
    for message in consumer:
        print (message.value.decode('utf-8'))
except KeyboardInterrupt:
    exit()