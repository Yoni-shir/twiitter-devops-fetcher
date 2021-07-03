from kafka import KafkaConsumer, errors
from config.conf import *
from time import sleep
import logging


def try_creating_kafka_consumer(broker, broker_port, topic, consumer_group):
    """
    retries creation of kafka consumer connections until it succeeds or times out

    :parameter str broker: dns or if of a kafka broker in the desired Kafka cluster
    :parameter int broker_port: the listening port of the Kafka broker
    :parameter str topic: topic name to consume from
    :parameter str consumer_group: consumer group name

    :returns: KafkaConsumer object
    """
    retries = 8
    for i in range(retries):
        try:
            return KafkaConsumer(topic, group_id=consumer_group, bootstrap_servers=[f'{broker}:{broker_port}'])
        except errors.NoBrokersAvailable:
            logging.error("attempt number: " + str(i + 1) + " broker: " + broker + ":" + str(broker_port))
            sleep(10)
    raise errors.NoBrokersAvailable


if __name__ == '__main__':

    # Initializing parameters from argparse
    kafka_host = args.kafka_host
    kafka_port = args.kafka_port
    kafka_topic = args.kafka_topic
    kafka_consumer_group = args.kafka_consumer_group

    # creating KafkaConsumer object
    consumer = try_creating_kafka_consumer(kafka_host, kafka_port, kafka_topic, kafka_consumer_group)

    for message in consumer:
        print("reading from kafka: " + message.value.decode('utf-8'))
