#!/usr/bin/env python3

import time
import os
import logging
import json

import requests
import kafka
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import pandas as pd


# Configure logging to display messages at INFO level and above
LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')
logging.basicConfig(level=LOGGING_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S')
#KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'stock_prices')
# Set Kafka related logs to WARNING to reduce output verbosity
logging.getLogger('kafka').setLevel(LOGGING_LEVEL)

# Constants
CSV_FILE_PATH = os.getenv('CSV_FILE_PATH', '/app/yellow_tripdata_2019-01.csv')
CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', '100'))


KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'taxi_data')
KAFKA_SERVER = os.getenv('KAFKA_SERVER', 'kafka_broker:29092')
MAX_RETRIES = int(os.getenv('KAFKA_MAX_RETRIES', '5'))
RETRY_DELAY = int(os.getenv('KAFKA_RETRY_DELAY', '2'))

# Log the config variables
logging.info(f'Kafka-Python package version: {kafka.__version__}')


logging.info(f"KAFKA_SERVER: {KAFKA_SERVER}, KAFKA_TOPIC: {KAFKA_TOPIC}")

# Initialize Kafka producer
def create_producer(server):
    return KafkaProducer(
        bootstrap_servers=[server],
        retries=5,
        retry_backoff_ms=1000,
        request_timeout_ms=30000,
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )

for attempt in range(MAX_RETRIES):
    try:
        logging.info(f"Attempting to connect to Kafka broker: {KAFKA_SERVER}, Attempt: {attempt + 1}")
        producer = create_producer(KAFKA_SERVER)
        logging.info("Successfully connected to Kafka broker.")
        break  # Exit the loop on successful connection
    except NoBrokersAvailable as e:
        logging.error(f"Connection attempt {attempt + 1} failed: {str(e)}")
        if attempt < MAX_RETRIES - 1:
            logging.info(f"Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)
        else:
            logging.error("Exhausted all retries. Failed to connect to Kafka broker.")
            raise


# Rest of the producer code
logging.info(f"Producer config: {producer.config}")

def fetch_stock_data_from_csv(file_path, chunk_size):
    try:
        chunk_iter = pd.read_csv(file_path, chunksize=chunk_size)
        return chunk_iter
    except Exception as err:
        logging.error(f'An error occurred while reading CSV file: {err}')
        return None


# Main loop
chunk_iter = fetch_stock_data_from_csv(CSV_FILE_PATH, CHUNK_SIZE)

if chunk_iter:
    while True:
        try:
            for chunk in chunk_iter:
                for _, row in chunk.iterrows():
                    stock_data = row.to_dict()  # Convert each row to dictionary
                    try:
                        producer.send(KAFKA_TOPIC, value=stock_data)
                        logging.info(f"Sent data to Kafka: {stock_data}")
                    except Exception as e:
                        logging.error(f"An error occurred while sending data to Kafka: {e}")

                time.sleep(60)  # Sleep to simulate real-time data

            chunk_iter = fetch_stock_data_from_csv(CSV_FILE_PATH, CHUNK_SIZE)  # Restart when finished

        except StopIteration:
            logging.info("Finished reading the CSV file.")
            break
