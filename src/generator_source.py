import random
from uuid import uuid4

from src.constants import TASK_NAMES
from src.task import Task

class GeneratorSource:
    def get_tasks(self) -> list[Task]:
        tasks = []
        i = random.randint(1,5)
        for k in range(i):
            id = str(uuid4())
            payload = random.choice(TASK_NAMES)
            task = Task(id, payload)
            tasks.append(task)
        return tasks