from typing import List
import unittest


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        def dp(i, day):
            pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMinDifficulty(self):
        self.assertEqual(self.sol.minDifficulty([6, 5, 4, 3, 2, 1], 2), 2)
        self.assertEqual(self.sol.minDifficulty([9, 9, 9], 4), -1)
        self.assertEqual(self.sol.minDifficulty([1, 1, 1], 3), 3)


if __name__ == "__main__":
    unittest.main()
