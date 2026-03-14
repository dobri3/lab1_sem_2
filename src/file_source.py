import json
from src.task import Task


class FileSource:
    def __init__(self, file_name):
        self.file_name = file_name
    def read_file(self):
        with open(self.file_name, "r", encoding="utf-8") as file_read:
            file = json.load(file_read)
        return file
    def get_tasks(self) -> list[Task]:
        tasks = []
        file = self.read_file()
        for i in file:
            id_get = i["id"]
            payload_get = i["payload"]
            task = Task(id_get, payload_get)
            tasks.append(task)
        return tasks


