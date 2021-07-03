#!/bin/env python
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--kafka_host", dest='kafka_host', default='localhost')
parser.add_argument("--kafka_port", dest='kafka_port', default='19092')
parser.add_argument("--kafka_topic", dest='kafka_topic', default='devops_hashtag')
parser.add_argument("--kafka_consumer_group", dest="kafka_consumer_group", default="mygroup")

args = parser.parse_args()


