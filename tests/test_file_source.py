from src.file_source import FileSource
import unittest
from unittest.mock import patch, mock_open

class TestFileSource(unittest.TestCase):
    def setUp(self):
        self.file_source = FileSource("tasks.json")

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.load")
    def test_get_tasks_returns_list_of_tasks(self, mock_json_load, mock_file):
        mock_json_load.return_value = [
            {"id": "1", "payload": "обработать заказ"},
            {"id": "2", "payload": "отправить уведомление"}
        ]

        tasks = self.file_source.get_tasks()

        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].payload, "обработать заказ")
        self.assertEqual(tasks[1].payload, "отправить уведомление")

    @patch("builtins.open")
    @patch("logging.error")
    def test_read_file_returns_none_when_file_not_found(self, mock_logging, mock_file):
        mock_file.side_effect = FileNotFoundError()

        result = self.file_source.read_file()

        self.assertIsNone(result)
        mock_logging.assert_called_once_with("file tasks.json not found\n")

    @patch.object(FileSource, "read_file")
    def test_get_tasks_returns_empty_list_when_read_file_returns_none(self, mock_read):
        mock_read.return_value = None

        tasks = self.file_source.get_tasks()

        self.assertEqual(tasks, [])
