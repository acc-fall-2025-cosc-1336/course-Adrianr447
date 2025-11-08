import os
import sys

# ensure src is importable
tests_dir = os.path.dirname(__file__)
src_path = os.path.abspath(os.path.join(tests_dir, "..", "..", "..", "src"))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

import unittest
from src.homework.g_lists_and_tuples.lists import (
    get_lowest_list_value,
    get_highest_list_value,
)

class TestLists(unittest.TestCase):
    def test_get_lowest_list_value(self):
        data = [8, 10, 1, 50, 20]
        self.assertEqual(get_lowest_list_value(data), 1)

    def test_get_highest_list_value(self):
        data = [8, 10, 1, 50, 20]
        self.assertEqual(get_highest_list_value(data), 50)

if __name__ == "__main__":
    unittest.main()