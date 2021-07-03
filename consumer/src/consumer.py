from kafka import KafkaConsumer, errors
from config.conf import *
from time import sleep


def try_creating_kafka_consumer(broker, broker_port, topic, consumer_group):
        retries = 6
        for i in range(retries):
            try:
                return KafkaConsumer(topic, group_id=consumer_group, bootstrap_servers=[f'{broker}:{broker_port}'])
            except errors.NoBrokersAvailable:
                sleep(10)
        raise errors.NoBrokersAvailable


if __name__ == '__main__':

    kafka_host = args.kafka_host
    kafka_port = args.kafka_port
    kafka_topic = args.kafka_topic
    kafka_consumer_group = args.kafka_consumer_group

    consumer = try_creating_kafka_consumer(kafka_host, kafka_port, kafka_topic, kafka_consumer_group)
    for message in consumer:
        print(message.value.decode('utf-8'))


