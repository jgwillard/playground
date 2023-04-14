from collections import defaultdict
from typing import Dict, List
import unittest


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points: Dict[int, int] = defaultdict(int)
        memo: Dict[int, int] = {}
        max_num = 0
        for num in nums:
            points[num] += num
            max_num = max(max_num, num)

        def dp(i: int) -> int:
            if i == 0:
                return 0
            if i == 1:
                return points[1]
            if i not in memo:
                memo[i] = max(points[i] + dp(i - 2), dp(i - 1))

            return memo[i]

        return dp(max_num)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testDeleteAndEarn(self):
        self.assertEqual(self.sol.deleteAndEarn([3, 4, 2]), 6)
        self.assertEqual(self.sol.deleteAndEarn([2, 2, 3, 3, 3, 4]), 9)


if __name__ == "__main__":
    unittest.main()
