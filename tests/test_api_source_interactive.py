import unittest
from unittest.mock import patch

from src.api_source_interactive import ApiSourceInteractive


class TestApiSourceInteractive(unittest.TestCase):
    @patch("builtins.input", side_effect=["покушать", "поспать", "q"])
    def test_len_of_tasks(self, payloads):
        source = ApiSourceInteractive()
        tasks = source.get_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].payload, "покушать")
        self.assertEqual(tasks[1].payload, "поспать")

    @patch("builtins.input", side_effect=["q"])
    def test_empty_input(self, payloads):
        source = ApiSourceInteractive()
        tasks = source.get_tasks()
        self.assertEqual(len(tasks), 0)
