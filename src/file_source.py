import json
import logging.config
from src.config import LOGGING_CONFIG
from src.task import Task

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


class FileSource:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        """
        функция для чтения списка тасков из файла json
        :return: file|FileNotFoundError|JSONDecodeError
        """
        try:
            with open(self.file_name, "r", encoding="utf-8") as file_read:
                file = json.load(file_read)
            return file
        except FileNotFoundError:
            logger.error(f"file {self.file_name} not found\n")

        except json.JSONDecodeError:
            logger.error(f"file {self.file_name} has invalid JSON\n")

    def get_tasks(self) -> list[Task]:
        """
        функция для получения списка тасков из файла json
        :return: list[Task]
        """
        tasks = []
        file = self.read_file()
        if file is None:
            return []
        for i in file:
            id_get = i["id"]
            payload_get = i["payload"]
            task = Task(id_get, payload_get)
            tasks.append(task)
        return tasks
