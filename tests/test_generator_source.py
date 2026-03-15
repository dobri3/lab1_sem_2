import unittest
from unittest.mock import patch

from src.generator_source import GeneratorSource


class TestGeneratorSource(unittest.TestCase):

    @patch("random.randint")
    @patch("random.choice")
    def test_returns_specified_number_of_tasks(self, mock_choice, mock_randint):
        mock_randint.return_value = 2
        mock_choice.side_effect = ["обработать заказ", "отправить уведомление"]

        with patch("src.generator_source.uuid4") as mock_uuid:
            mock_uuid.side_effect = ["id1", "id2"]
            tasks = GeneratorSource().get_tasks()

        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].id, "id1")
        self.assertEqual(tasks[0].payload, "обработать заказ")
        self.assertEqual(tasks[1].id, "id2")
        self.assertEqual(tasks[1].payload, "отправить уведомление")

    @patch("random.randint")
    def test_can_return_different_numbers_of_tasks(self, mock_randint):
        mock_randint.side_effect = [1, 5]

        tasks1 = GeneratorSource().get_tasks()
        tasks2 = GeneratorSource().get_tasks()

        self.assertEqual(len(tasks1), 1)
        self.assertEqual(len(tasks2), 5)

    @patch("random.randint")
    def test_returns_different_ids_each_time(self, mock_randint):
        mock_randint.return_value = 3

        tasks = GeneratorSource().get_tasks()
        ids = [task.id for task in tasks]

        self.assertEqual(len(set(ids)), 3)  # все id разные
