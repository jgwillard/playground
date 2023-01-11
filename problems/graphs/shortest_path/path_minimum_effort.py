import math
from typing import List, Tuple
import unittest


class Solution:
    @staticmethod
    def _get_adjacent_nodes(
        x: int, y: int, num_cols: int, num_rows: int
    ) -> List[Tuple[int, int]]:
        nodes: List[Tuple[int, int]] = []
        if x > 0:
            nodes.append((x - 1, y))
        if y > 0:
            nodes.append((x, y - 1))
        if x < num_cols - 1:
            nodes.append((x + 1, y))
        if y < num_rows - 1:
            nodes.append((x, y + 1))
        return nodes

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        num_cols = len(heights)
        num_rows = len(heights[0])
        # record minimum effort required to reach each cell
        min_effort: List[List[float]] = [
            [math.inf for j in range(num_rows)] for i in range(num_cols)
        ]
        in_tree: List[List[bool]] = [
            [False for j in range(num_rows)] for i in range(num_cols)
        ]

        x, y = (0, 0)
        min_effort[0][0] = 0

        # Dijkstra's algorithm
        while in_tree[x][y] == False:
            # mark curent node as visited and iterate over adjacent nodes
            in_tree[x][y] = True
            adjacent_nodes = self._get_adjacent_nodes(x, y, num_cols, num_rows)
            for i, j in adjacent_nodes:
                # min_effort is the maximum absolute difference in
                # heights between two consecutive cells in a path
                # therefore, we just want the min of the currently
                # recorded maximum height on this path and the current
                # difference (cost)
                # NOTE: this differs slightly from vanilla Dijkstra's
                # algorithm in that the cost function only tracks the
                # highest-weighted edge in the path, rather than the
                # total path weight, i.e.
                # min(min_effort[adj_x][adj_y], min_effort[x][y] + cost)
                cost = abs(heights[x][y] - heights[i][j])
                # either the current cost is the highest encountered, or
                # the cost of the path is the previous highest cost
                max_difference = max(min_effort[x][y], cost)
                # if the max difference encountered on the current path
                # is lower than for previously explored paths, update
                min_effort[i][j] = min(min_effort[i][j], max_difference)

            # go through all the nodes not in the tree and add the one
            # with the shortest distance to the tree (can be sped up by
            # priority queue)
            dist: float = math.inf
            for i in range(num_cols):
                for j in range(num_rows):
                    if not in_tree[i][j] and min_effort[i][j] <= dist:
                        dist = min_effort[i][j]
                        x, y = i, j

        return int(min_effort[num_cols - 1][num_rows - 1])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMinimumEffortPath(self):
        self.assertEqual(
            self.sol.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]), 2
        )
        self.assertEqual(
            self.sol.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]), 1
        )
        self.assertEqual(
            self.sol.minimumEffortPath(
                [
                    [1, 2, 1, 1, 1],
                    [1, 2, 1, 2, 1],
                    [1, 2, 1, 2, 1],
                    [1, 2, 1, 2, 1],
                    [1, 1, 1, 2, 1],
                ]
            ),
            0,
        )
        self.assertEqual(
            self.sol.minimumEffortPath([[1, 10, 6, 7, 9, 10, 4, 9]]), 9
        )


if __name__ == "__main__":
    unittest.main()
