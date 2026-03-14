import unittest
from unittest.mock import patch

from src.api_source_interactive import ApiSourceInteractive

class TestApiSourceInteractive(unittest.TestCase):
    @patch("builtins.input", side_effect=["покушать", "поспать", "q"])
    def test_len_of_tasks(self, payloads):
        source = ApiSourceInteractive()
        tasks = source.get_tasks()
        self.assertEqual(len(tasks), 2)
