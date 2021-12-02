from typing import List
import unittest


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp is a list such that dp[i] contains the maximum amount of
        # money that a robber can have taken when he arrives at house i
        dp = [0] * (n + 1)
        # if there is one house, the robber can only rob that house
        dp[0] = nums[0]
        if n == 1:
            return dp[0]
        # if there are two houses, the robber should rob whichever house
        # has more money
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # at house i, a robber will either be able to rob house i or
            # house i - 1, but not both, so he must choose the maximum
            # between the money in house i plus the maximum amount of
            # money that the robber can have taken at house i - 2, or
            # just the maximum amount of money taken at house i - 1
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[n - 1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testRob(self):
        self.assertEqual(self.sol.rob([]), 0)
        self.assertEqual(self.sol.rob([0]), 0)
        self.assertEqual(self.sol.rob([0, 1]), 1)
        self.assertEqual(self.sol.rob([1, 2, 3, 1]), 4)
        self.assertEqual(self.sol.rob([2, 7, 9, 3, 1]), 12)
        self.assertEqual(self.sol.rob([1, 2, 3, 1, 4, 28, 137, 2, 18]), 163)


if __name__ == "__main__":
    unittest.main()
