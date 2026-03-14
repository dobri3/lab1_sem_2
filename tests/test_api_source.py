import unittest

from src.api_source import ApiSource

class TestApiSource(unittest.TestCase):
    def test_output(self):
        source = ApiSource()
        tasks = source.get_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].payload, "обработать заказ")
        self.assertEqual(tasks[1].payload, "отправить уведомление")