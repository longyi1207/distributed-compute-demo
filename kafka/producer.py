from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Send tasks
for i in range(10):
    task = {"task_id": i, "data": f"Task-{i}"}
    producer.send("tasks", task)
    print(f"Sent: {task}")
    time.sleep(1)  # Simulate delay

producer.close()
