#!/bin/env python
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--consumer_key", dest='consumer_key', default='f9QNd2fICv8Sakm69ObbVOR8J')
parser.add_argument("--consumer_secret", dest='consumer_secret', default='ijHUZlrBGJIqPSzTn8GA5xvOuEfGUvJCtYiO1bS21rgqePasgV')
parser.add_argument("--kafka_host", dest='kafka_host', default='localhost')
parser.add_argument("--kafka_port", dest='kafka_port', default='19092')
parser.add_argument("--kafka_topic", dest='kafka_topic', default='devops_hashtag')

args = parser.parse_args()


