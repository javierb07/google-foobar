import unittest
from solution import solution

class TestSum(unittest.TestCase):

    def test_solution(self):
        cases = [
           [19, 36],
           [0, 1]
        ]
        results = [
            1,
            3
        ]
        for case, result in zip(cases, results):
            self.assertEqual(solution(case[0], case[1]), result, "Should be " + str(result))

if __name__ == '__main__':
    unittest.main()