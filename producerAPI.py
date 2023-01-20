from bsedata.bse import BSE
from kafka import KafkaProducer
import json

#initialization of BSE object
b = BSE()

#kafka configration, KafkaProducer initialization
bootstrap_servers = ['localhost:9092']
topicName = 'stockWiseData'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

#gets the keys(of stockId) from DICT returned from stocks in BSE
stockCodelist = b.getScripCodes().keys()

for stockId in stockCodelist:
    stockData = b.getQuote(stockId)
    #Check if the stockID is currently being traded or not
    if len(stockData) > 0:
        #stock data being published to kafka topic
        producer.send(topicName,json.dumps(stockData).encode('utf-8'))