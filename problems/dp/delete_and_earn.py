from collections import defaultdict
from typing import Dict, List
import unittest


class Solution:
    # NOTE this problem is only a very slight variation on house robber:
    # the algorithm is identical except for some preparatory work to
    # create the necessary data structures
    def deleteAndEarnTopDown(self, nums: List[int]) -> int:
        # defaultdict will always default to 0, so we can iterate over
        # all numbers without key errors (unlike house robber, the data
        # will not necessarily contain all numbers 0-n)
        points: Dict[int, int] = defaultdict(int)
        memo: Dict[int, int] = {}
        # we track the highest number in the array since we are not just
        # given a list of values; we have to construct a dictionary and
        # we have to start processing its highest value
        max_num = 0
        for num in nums:
            points[num] += num
            max_num = max(max_num, num)

        def dp(i: int) -> int:
            if i == 0:
                # in the house robber algo we would return points[0],
                # but here we are given that points[0] would always be
                # worth 0 points
                return 0
            if i == 1:
                # similarly, in house robber, we would return the max of
                # points[0] and points[1], but since we are given that
                # points[0] is worth 0, we know that points[1] will be
                # less than or equal to it
                return points[1]
            if i not in memo:
                memo[i] = max(points[i] + dp(i - 2), dp(i - 1))

            return memo[i]

        return dp(max_num)

    def deleteAndEarn(self, nums: List[int]) -> int:
        points: Dict[int, int] = defaultdict(int)

        max_num = 0
        for num in nums:
            points[num] += num
            max_num = max(max_num, num)

        dp = [0] * (max_num + 1)
        dp[0] = 0
        dp[1] = points[1]

        for i in range(2, max_num + 1):
            dp[i] = max(points[i] + dp[i - 2], dp[i - 1])

        return dp[max_num]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testDeleteAndEarn(self):
        self.assertEqual(self.sol.deleteAndEarn([3, 4, 2]), 6)
        self.assertEqual(self.sol.deleteAndEarn([2, 2, 3, 3, 3, 4]), 9)


if __name__ == "__main__":
    unittest.main()
