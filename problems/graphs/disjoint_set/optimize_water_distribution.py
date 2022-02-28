from typing import List
import unittest

from union_find import UnionFind


class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: List[int], pipes: List[List[int]]
    ) -> int:
        # union find has size = n + 1 to accout for the virtual node
        uf = UnionFind(n + 1)
        total_cost = 0

        # add virtual node and connect it to each house with cost of
        # building a well in that house as its weight by appending
        # it to the pipes array
        for i, cost in enumerate(wells):
            pipes.append([n + 1, i + 1, cost])

        # sort the pipes array by weight ascending (Kruskal's algorithm)
        pipes_sorted = sorted(pipes, key=lambda pipe: pipe[2])

        for i, pipe in enumerate(pipes_sorted):

            # if all houses are connected we are done
            if uf.count == 1:
                break

            # if the houses connected by the pipe with the lowest weight
            #  are not connected, connect them via UnionFind.union and
            # add the cost of the pipe to total
            if not uf.connected(pipe[0] - 1, pipe[1] - 1):
                uf.union(pipe[0] - 1, pipe[1] - 1)
                total_cost += pipe[2]

        return total_cost


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
