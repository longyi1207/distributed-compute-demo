from kafka import KafkaConsumer
import json
import time

consumer = KafkaConsumer(
    "tasks",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Worker listening for tasks...")

for message in consumer:
    task = message.value
    print(f"Processing {task['data']}...")
    time.sleep(2)  # Simulate processing delay
    print(f"Completed: {task['data']}")
