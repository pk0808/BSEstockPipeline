# BSEstockPipeline

Using the bsedata python library to make calls to BSE(Bombay Stock Exchange), and publish the requested data in form of JSON to kafka topics.

Steps:

1) Install bsedata python library .
2) Run the createTopic.py to create topics.
3) Run consumerAPI.py to consume data from topics.
4) Run producerAPI.py to trigger API calls to BSE and publish the returned data to Kafka topics.
