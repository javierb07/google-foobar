import unittest
from solution import solution

class TestSum(unittest.TestCase):

    def test_solution(self):
        cases = [
            [3, 1, 4, 1],
            [3, 1, 4, 1, 5, 9],
            [4, 4, 1, 1, 1, 3],
            [5, 5, 5, 7],
            [5, 4, 3, 1, 1],
            [0, 0, 3, 1, 1]
        ]
        results = [
            4311,
            94311,
            4431,
            555,
            4311,
            300
        ]
        for case, result in zip(cases, results):
            self.assertEqual(solution(case), result, "Should be " + str(result))

if __name__ == '__main__':
    unittest.main()