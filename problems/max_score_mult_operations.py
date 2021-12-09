from typing import Dict, List
import unittest


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        memo: Dict[int, Dict[int, int]] = {}

        # i is the number of iterations, left is the left index
        def dp(i: int, left: int) -> int:
            # base case: there are no more operations
            if i == m:
                return 0

            # right is the right index
            right = n - 1 - (i - left)

            # choose the max between
            # the score so far plus multipliers[i] * nums[left]
            # (if so, increment left explicitly)
            # and
            # the score so far plus multipliers[i] * nums[right]
            # (if so, right is decremented implicitly when i is incremented)
            if i not in memo:
                memo[i] = {}
            if left not in memo[i]:
                memo[i][left] = max(
                    multipliers[i] * nums[left] + dp(i + 1, left + 1),
                    multipliers[i] * nums[right] + dp(i + 1, left),
                )

            return memo[i][left]

        return dp(0, 0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMaximumScore(self):
        self.assertEqual(self.sol.maximumScore([1, 2, 3], [3, 2, 1]), 14)
        self.assertEqual(
            self.sol.maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]), 102
        )


if __name__ == "__main__":
    unittest.main()
