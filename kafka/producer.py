from kafka import KafkaProducer
import json
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_producer():
    """Create a Kafka producer with retry logic"""
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers="kafka:9092",
                value_serializer=lambda v: json.dumps(v).encode("utf-8")
            )
            logging.info("Connected to Kafka successfully.")
            return producer
        except Exception as e:
            logging.error(f"Failed to connect to Kafka: {e}. Retrying in 5 seconds...")
            time.sleep(5)

def dispatch_tasks():
    """Dispatch tasks to Kafka topic periodically"""
    
    producer = create_producer()
    
    try:
        while True:
            # Create a single task
            task = {"task_id": int(time.time()), "data": f"Task-{time.time()}"}
            logging.info(f"Dispatching task: {task}")
            
            # Send task to Kafka
            producer.send("tasks", task)
            
            time.sleep(5)  # Wait 5 seconds between tasks
            
    except KeyboardInterrupt:
        logging.info("Stopping task dispatcher...")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        producer.close()

if __name__ == "__main__":
    logging.info("Starting task dispatching...")
    dispatch_tasks()
