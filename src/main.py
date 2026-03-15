import logging

from src.api_source import ApiSource
from src.api_source_interactive import ApiSourceInteractive
from src.file_source import FileSource
from src.generator_source import GeneratorSource
from src.task_source import TaskSource
from src.config import LOGGING_CONFIG
import logging.config

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

SOURCES: dict[str, TaskSource] = {
    "API": ApiSource(),
    "API interact": ApiSourceInteractive(),
    "file": FileSource("test_file.json"),
    "generator": GeneratorSource(),
}


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    ids = []

    while (
        f := input(
            "введите тип источника:\nAPI\nAPI interact\nfile\ngenerator\nor q to quit\n"
        )
    ) != "q":
        source: TaskSource | None = SOURCES.get(f)
        if source is None:
            logger.error(f"неизвестный тип источника: {f}")
            continue
        if not checkup(source):
            continue
        print("\n")
        tasks = source.get_tasks()
        for task in tasks:
            if task.id not in ids:
                ids.append(task.id)
                logger.info(f"{task} успешно обработан\n")
            else:
                logger.error(f"id {task.id} уже существует")


def checkup(source) -> bool:
    """
    функция для проверки совместимости источника с TaskSource
    :return: bool
    """
    if not isinstance(source, TaskSource):
        logger.error(f"источник {source} несовместим с TaskSource\n")
        return False
    return True


if __name__ == "__main__":
    main()
