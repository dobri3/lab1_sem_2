from uuid import uuid4

from src.task import Task


class ApiSource:
    def get_tasks(self) -> list[Task]:
        """
        функция имитирующая получение таска через API
        :return: list[Task]
        """
        return [
            Task(str(uuid4()), "обработать заказ"),
            Task(str(uuid4()), "отправить уведомление"),
        ]
