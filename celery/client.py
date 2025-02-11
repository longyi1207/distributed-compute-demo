from tasks import process_task
from celery.result import AsyncResult
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def dispatch_tasks():
    """Dispatch tasks to workers periodically"""
    
    try:
        while True:
            # Create a single task
            task_data = f"Task-{time.time()}"
            logging.info(f"Dispatching task: {task_data}")
            
            # Dispatch task
            task = process_task.delay(task_data)
            
            # Wait for result
            result = AsyncResult(task.id)
            logging.info(f"Task {task.id} result: {result.get(timeout=10)}")
            
            time.sleep(5)  # Wait 5 seconds between tasks
            
    except KeyboardInterrupt:
        logging.info("Stopping task dispatcher...")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    logging.info("Starting task dispatching...")
    dispatch_tasks()
