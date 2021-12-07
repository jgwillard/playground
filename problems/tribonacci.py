from typing import Dict
import unittest


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        # dp is a list such that dp[i] contains the ith tribonacci num
        dp = [0] * (n + 1)
        # base cases
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            # each subsequent tribonacci number is the sum of the three
            # preceding tribonacci numbers
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]

    def tribonacciTopDown(self, n: int) -> int:
        memo: Dict[int, int] = {}

        def dp(i: int) -> int:
            if i <= 1:
                return i
            if i == 2:
                return 1

            if i not in memo:
                memo[i] = dp(i - 1) + dp(i - 2) + dp(i - 3)

            return memo[i]

        return dp(n)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testTribonacci(self):
        self.assertEqual(self.sol.tribonacci(1), 1)
        self.assertEqual(self.sol.tribonacci(2), 1)
        self.assertEqual(self.sol.tribonacci(3), 2)
        self.assertEqual(self.sol.tribonacci(4), 4)
        self.assertEqual(self.sol.tribonacci(25), 1389537)

    def testTribonacciTopDown(self):
        self.assertEqual(self.sol.tribonacciTopDown(1), 1)
        self.assertEqual(self.sol.tribonacciTopDown(2), 1)
        self.assertEqual(self.sol.tribonacciTopDown(3), 2)
        self.assertEqual(self.sol.tribonacciTopDown(4), 4)
        self.assertEqual(self.sol.tribonacciTopDown(25), 1389537)


if __name__ == "__main__":
    unittest.main()
