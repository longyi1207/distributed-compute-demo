import ray
import time

@ray.remote
def process_task(data):
    """Fake processing task on a worker node."""
    time.sleep(2)
    return f"Processed {data}"