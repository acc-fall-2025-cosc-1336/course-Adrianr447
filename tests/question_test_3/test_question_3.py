import unittest
from src.question_3.question_3 import get_most_likely_ancestor_consensus


class TestQuestion3(unittest.TestCase):
    def test_sample(self):
        result = get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT")
        a, b, c = result
        self.assertEqual(a, 2)
        self.assertEqual(b, 4)
        self.assertEqual(c, 10)


if __name__ == "__main__":
    unittest.main()
