#!/usr/bin/env ash

python ./producer.py --consumer_key=$CONSUMER_KEY --consumer_secret=$CONSUMER_SECRET --kafka_host=$KAFKA_HOST --kafka_port=$KAFKA_PORT  --kafka_topic=$KAFKA_TOPIC
