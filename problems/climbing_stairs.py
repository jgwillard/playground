from typing import Dict
import unittest
import timeit


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # dp is a list such that dp[i] contains the number of ways to
        # reach the ith step
        dp = [0] * (n + 1)
        # base cases: you can reach the first step only by taking one
        # step, you can reach the second by taking one or two steps
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            # you can get to step i by taking one step from step i - 1
            # or by taking two steps from step i - 2
            # so the number of ways to get to step i is the number of
            # ways to get to step i - 1 plus the number of ways to get
            # to step i - 2
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairsTopDown(self, n: int) -> int:
        memo: Dict[int, int] = {}

        def dp(i: int) -> int:
            if i <= 2:
                return i

            if i not in memo:
                memo[i] = dp(i - 1) + dp(i - 2)

            return memo[i]

        return dp(n)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testclimbStairs(self):
        self.assertEqual(self.sol.climbStairs(1), 1)
        self.assertEqual(self.sol.climbStairs(2), 2)
        self.assertEqual(self.sol.climbStairs(3), 3)
        self.assertEqual(self.sol.climbStairs(4), 5)
        self.assertEqual(self.sol.climbStairs(10), 89)

    def testclimbStairsTopDown(self):
        self.assertEqual(self.sol.climbStairsTopDown(1), 1)
        self.assertEqual(self.sol.climbStairsTopDown(2), 2)
        self.assertEqual(self.sol.climbStairsTopDown(3), 3)
        self.assertEqual(self.sol.climbStairsTopDown(4), 5)
        self.assertEqual(self.sol.climbStairsTopDown(10), 89)


if __name__ == "__main__":
    sol = Solution()
    # TODO why is the difference between top down and bottom up not a
    # constant factor? What is the complexity of the number of procedure
    # calls in the top down implementation?
    print(timeit.timeit(lambda: sol.climbStairs(5)))
    print(timeit.timeit(lambda: sol.climbStairsTopDown(5)))
    print(timeit.timeit(lambda: sol.climbStairs(10)))
    print(timeit.timeit(lambda: sol.climbStairsTopDown(10)))
    unittest.main()
