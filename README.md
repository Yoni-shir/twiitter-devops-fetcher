# twitter-devops-fetcher
A simple docker compose based app which deploys a basic Kafka cluster, a Kafka producer which fetches tweets from twitter, and a Kafka consumer which consumes data from a topic and prints it to stdout. 

To orchestrate the application simply clone the repo and run the following commands:

```bash
cd twitter-devops-fetcher
sudo docker-compose up &
```

notice that it may take a few minutes for the application to write to stdout, unfortunately i was only able to make it print out the data in bulks. 