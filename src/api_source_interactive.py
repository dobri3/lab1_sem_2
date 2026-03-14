from uuid import uuid4

from src.task import Task


class ApiSourceInteractive:
    def get_tasks(self) ->list[Task]:
        tasks = []
        while ((f:=input("Введите название задачи (press q to quit) :"))!= "q"):
            task = Task(str(uuid4()), f)
            tasks.append(task)
        return tasks

