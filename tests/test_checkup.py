import unittest

from src.api_source import ApiSource
from src.main import checkup

class WrongSource:
    ...

class CheckupTest(unittest.TestCase):
    def test_wrong_type_of_source(self):
        result = checkup(WrongSource())
        self.assertFalse(result)
    def test_wrong_compatibility(self):
        result = checkup(WrongSource())
        self.assertFalse(result)
    def test_right_source(self):
        result = checkup(ApiSource())
        self.assertTrue(result)
    




