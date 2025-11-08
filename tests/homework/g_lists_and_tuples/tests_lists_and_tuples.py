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
    get_p_distance,
    get_p_distance_matrix,
)

class TestLists(unittest.TestCase):
    def test_get_lowest_list_value(self):
        data = [8, 10, 1, 50, 20]
        self.assertEqual(get_lowest_list_value(data), 1)

    def test_get_highest_list_value(self):
        data = [8, 10, 1, 50, 20]
        self.assertEqual(get_highest_list_value(data), 50)

class Test_Config(unittest.TestCase):

    def test_p_distance(self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']
        self.assertEqual(get_p_distance(list1, list2), 0.4)

    def test_get_p_distance_matrix(self):
        data = [
            ['T','T','T','C','C','A','T','T','T','A'],
            ['G','A','T','T','C','A','T','T','T','C'],
            ['T','T','T','C','C','A','T','T','T','T'],
            ['G','T','T','C','C','A','T','T','T','A'],
        ]
        expected = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0],
        ]
        self.assertEqual(get_p_distance_matrix(data), expected)

if __name__ == "__main__":
    unittest.main()