from kafka import KafkaConsumer
import json
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_consumer():
    """Create a Kafka consumer with retry logic"""
    while True:
        try:
            consumer = KafkaConsumer(
                "tasks",
                bootstrap_servers="kafka:9092",
                value_deserializer=lambda m: json.loads(m.decode("utf-8"))
            )
            logging.info("Connected to Kafka successfully.")
            return consumer
        except Exception as e:
            logging.error(f"Failed to connect to Kafka: {e}. Retrying in 5 seconds...")
            time.sleep(5)

def consume_tasks():
    """Consume tasks from Kafka topic"""
    
    consumer = create_consumer()
    
    logging.info("Worker listening for tasks...")
    
    try:
        for message in consumer:
            task = message.value
            logging.info(f"Processing {task['data']}...")
            time.sleep(2)  # Simulate processing delay
            logging.info(f"Completed: {task['data']}")
            
    except KeyboardInterrupt:
        logging.info("Stopping task consumer...")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        consumer.close()

if __name__ == "__main__":
    logging.info("Starting task consumption...")
    consume_tasks()
