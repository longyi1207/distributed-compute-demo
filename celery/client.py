from tasks import process_task
from celery.result import AsyncResult

data_chunks = [f"Task-{i}" for i in range(10)]
task_ids = [process_task.delay(data) for data in data_chunks]

# Collect results
for task_id in task_ids:
    result = AsyncResult(task_id.id)
    print(f"Task {task_id.id} result: {result.get(timeout=10)}")
