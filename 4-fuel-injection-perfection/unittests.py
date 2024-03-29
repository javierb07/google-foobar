import unittest
from solution import solution

class TestSum(unittest.TestCase):

    def test_solution(self):
        cases = [
            "4",
            "15"
        ]
        results = [
            2,
            5
        ]
        for case, result in zip(cases, results):
            self.assertEqual(solution(case), result, "Should be " + str(result))

if __name__ == '__main__':
    unittest.main()