#!/usr/bin/env ash

python ./consumer.py --kafka_host=$KAFKA_HOST --kafka_port=$KAFKA_PORT  --kafka_topic=$KAFKA_TOPIC --kafka_consumer_group=$KAFKA_CONSUMER_GROUP
