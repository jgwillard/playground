from typing import List
import unittest


class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: List[int], pipes: List[List[int]]
    ) -> int:
        # add virtual node and connect it to each house with cost of
        # building a well in that house as its weight by appending
        # it to the pipes array

        # sort the pipes array by weight

        # for each pipe in pipes check if they are already connected via
        # UnionFind.connected

        # if they are not connected, connect them via UnionFind.union
        # and add the cost of the pipe to a counter

        # check if UnionFind.count == 1 and if it does exit loop

        # return cost counter
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.assertEqual(
            self.sol.minCostToSupplyWater(3, [1, 2, 2], [[1, 2, 1], [2, 3, 1]]), 3
        )
        self.assertEqual(
            self.sol.minCostToSupplyWater(2, [1, 1], [[1, 2, 1], [1, 2, 2]]), 2
        )

    def testMinCostToSupplyWater(self):
        pass


if __name__ == "__main__":
    unittest.main()
