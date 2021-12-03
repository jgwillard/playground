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


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMethodName(self):
        self.assertEqual(self.sol.tribonacci(1), 1)
        self.assertEqual(self.sol.tribonacci(2), 1)
        self.assertEqual(self.sol.tribonacci(3), 2)
        self.assertEqual(self.sol.tribonacci(4), 4)
        self.assertEqual(self.sol.tribonacci(25), 1389537)


if __name__ == "__main__":
    unittest.main()
