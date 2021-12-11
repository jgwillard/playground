from functools import lru_cache
from typing import Dict, List
import unittest
from timeit import timeit


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

    def maximumScoreAutoMemoized(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)

        # lru_cache from functools automatically memoizes the function
        @lru_cache(2000)
        def dp(i: int, left: int) -> int:
            if i == m:
                return 0

            right = n - 1 - (i - left)

            return max(
                multipliers[i] * nums[left] + dp(i + 1, left + 1),
                multipliers[i] * nums[right] + dp(i + 1, left),
            )

        return dp(0, 0)

    def maximumScoreBottomUp(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)

        dp: Dict[int, Dict[int, int]] = {i: {} for i in range(0, m + 1)}

        # base case: explicitly set row m to have all 0 values, because
        # on the first iteration of the loop where i == m - 1, we check
        # each value of dp[i - 1] == dp[m], in which case there are no
        # more operations so nothing to add to the score
        dp[m] = {i: 0 for i in range(0, m + 1)}

        for i in reversed(range(0, m)):
            # in an iteration i, the left index has a maximum of i
            # possible values if we always choose the leftmost number
            # (the left index can increase by at most 1 per iteration)
            # this loop iterates over all possible left-index values for
            # the current value of i
            for left in reversed(range(0, i + 1)):

                right = n - 1 - (i - left)

                dp[i][left] = max(
                    multipliers[i] * nums[left] + dp[i + 1][left + 1],
                    multipliers[i] * nums[right] + dp[i + 1][left],
                )

        return dp[0][0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMaximumScore(self):
        self.assertEqual(self.sol.maximumScore([1, 2, 3], [3, 2, 1]), 14)
        self.assertEqual(
            self.sol.maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]), 102
        )

    def testMaximumScoreAutoMemoized(self):
        self.assertEqual(self.sol.maximumScoreAutoMemoized([1, 2, 3], [3, 2, 1]), 14)
        self.assertEqual(
            self.sol.maximumScoreAutoMemoized(
                [-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]
            ),
            102,
        )

    def testMaximumScoreBottomUp(self):
        self.assertEqual(self.sol.maximumScoreBottomUp([1, 2, 3], [3, 2, 1]), 14)
        self.assertEqual(
            self.sol.maximumScoreBottomUp([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]),
            102,
        )


if __name__ == "__main__":
    sol = Solution()
    # NOTE manual memo beats lru_cache handily and bottom up beats both
    print(timeit(lambda: sol.maximumScore([1, 2, 3], [3, 2, 1])), 1000)
    print(timeit(lambda: sol.maximumScoreAutoMemoized([1, 2, 3], [3, 2, 1])), 1000)
    print(timeit(lambda: sol.maximumScoreBottomUp([1, 2, 3], [3, 2, 1])), 1000)
    unittest.main()
