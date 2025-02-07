from celery import Celery
import time

# Connect Celery to Redis broker
app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

@app.task
def process_task(data):
    """Fake processing task on a worker node."""
    time.sleep(2)
    return f"Processed {data}"
