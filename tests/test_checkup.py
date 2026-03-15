import unittest
from unittest.mock import patch
from src.main import checkup
from src.task_source import TaskSource


class FakeSource(TaskSource):
    def get_tasks(self):
        return []


class TestCheckup(unittest.TestCase):

    @patch("src.main.logger")
    def test_checkup_valid_source(self, mock_logger):
        source = FakeSource()

        result = checkup(source)

        self.assertTrue(result)
        mock_logger.error.assert_not_called()

    @patch("src.main.logger")
    def test_checkup_invalid_source(self, mock_logger):
        source = "not_a_source"

        result = checkup(source)

        self.assertFalse(result)
        mock_logger.error.assert_called_once()
