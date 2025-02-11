import ray
from task import process_task
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def dispatch_tasks():
    """Head node dispatches tasks to workers periodically"""
    
    try:
        while True:
            # Create a single task
            task_data = f"Task-{time.time()}"
            logging.info(f"Dispatching task: {task_data}")
            
            # Dispatch task
            future = process_task.remote(task_data)
            
            # Wait for result
            result = ray.get(future)
            logging.info(f"Task completed: {result}")
            
            time.sleep(5)  # Wait 5 seconds between tasks
            
    except KeyboardInterrupt:
        logging.info("Stopping task dispatcher...")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    logging.info("Initializing Ray...")
    ray.init()
    logging.info("Starting task dispatching...")
    dispatch_tasks()
