import tweepy
from kafka import KafkaProducer, errors
from time import sleep
import re
from json import dumps
from config.conf import *
import logging


def try_creating_kafka_producer(broker, broker_port):
    """
    retries creation of kafka producer connections until it succeeds or times out

    :parameter str broker: dns or if of a kafka broker in the desired Kafka cluster
    :parameter int broker_port: the port listening port of the Kafka broker

    :returns: KafkaProducer object
    """
    retries = 6
    for i in range(retries):
        try:
            return KafkaProducer(bootstrap_servers=[f'{broker}:{broker_port}'], value_serializer=lambda x: dumps(x).encode('utf-8'))
        except errors.NoBrokersAvailable:
            logging.error("attempt number: " + str(i+1) + " broker: " + broker + ":" + str(broker_port))
            sleep(10)
    raise errors.NoBrokersAvailable


if __name__ == '__main__':

    # Initializing parameters from argparse
    kafka_host = args.kafka_host
    kafka_port = args.kafka_port
    consumer_key = args.consumer_key
    consumer_secret = args.consumer_secret
    kafka_topic = args.kafka_topic

    # creating KafkaProducer object
    producer = try_creating_kafka_producer(kafka_host, kafka_port)

    # Twitter API authentication
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    for tweet in tweepy.Cursor(api.search, q="#devops", lang="en").items():
        data = {"tweet_content": tweet.text.lower(),
                "user": tweet.user.name,
                "tweet_id": tweet.id,
                "tweet_hashtags": re.findall("#([a-zA-Z0-9_]{1,50})", tweet.text)}
        producer.send(topic=kafka_topic, value=data)
        sleep(3)

    producer.flush()

