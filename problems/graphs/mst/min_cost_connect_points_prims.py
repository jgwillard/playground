from typing import List
import unittest


class PriorityQueue(object):
    pass


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMinCostConnectPoints(self):
        self.assertEqual(
            self.sol.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]), 20
        )
        self.assertEqual(self.sol.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]), 18)
        self.assertEqual(
            self.sol.minCostConnectPoints([[-1000000, -1000000], [1000000, 1000000]]),
            4000000,
        )


if __name__ == "__main__":
    unittest.main()
