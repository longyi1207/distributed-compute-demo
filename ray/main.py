import ray
import time

# Start Ray in head mode
ray.init(address="ray-head:6379") # This connects to an existing Ray cluster

@ray.remote
def process_task(data):
    """Fake processing task on a worker node."""
    time.sleep(2)
    return f"Processed {data}"

def main():
    """Head node dispatches tasks to workers"""
    data_chunks = [f"Task-{i}" for i in range(10)]
    
    # Dispatch tasks
    futures = [process_task.remote(data) for data in data_chunks]
    
    # Collect results
    results = ray.get(futures)

    print("All tasks completed:")
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
