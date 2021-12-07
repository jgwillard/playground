from typing import Dict, List
import unittest


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # we are trying to get to step n (top of stairs)
        n = len(cost)
        # dp is a list such that dp[i] contains the minimum cost of
        # reaching the ith step
        dp = [0] * n
        # base cases:
        # since we can reach steps 0 and 1 without touching a previous
        # step, they cost nothing additional
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            # for each subsequent stair, we can reach it from step i - 1
            # or step i - 2, so we should choose whichever costs less
            # and add the cost of the current step
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        # top of stairs has no additonal cost
        return min(dp[n - 1], dp[n - 2])

    def minCostClimbingStairsTopDown(self, cost: List[int]) -> int:
        n = len(cost)
        memo: Dict[int, int] = {}

        def dp(i: int) -> int:
            if i <= 1:
                return cost[i]

            if i not in memo:
                memo[i] = cost[i] + min(dp(i - 1), dp(i - 2))

            return memo[i]

        return min(dp(n - 1), dp(n - 2))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMinCostClimbingStairs(self):
        self.assertEqual(self.sol.minCostClimbingStairs([1, 2]), 1)
        self.assertEqual(self.sol.minCostClimbingStairs([3, 2]), 2)
        self.assertEqual(self.sol.minCostClimbingStairs([10, 15, 20]), 15)
        self.assertEqual(
            self.sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6
        )

    def testMinCostClimbingStairsTopDown(self):
        self.assertEqual(self.sol.minCostClimbingStairsTopDown([1, 2]), 1)
        self.assertEqual(self.sol.minCostClimbingStairsTopDown([3, 2]), 2)
        self.assertEqual(self.sol.minCostClimbingStairsTopDown([10, 15, 20]), 15)
        self.assertEqual(
            self.sol.minCostClimbingStairsTopDown([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]),
            6,
        )


if __name__ == "__main__":
    unittest.main()
