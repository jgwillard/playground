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
        if x < num_rows - 1:
            nodes.append((x + 1, y))
        if y < num_cols - 1:
            nodes.append((x, y + 1))
        return nodes

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        num_cols = len(heights)
        num_rows = len(heights[0])
        # record minimum effort required to reach each cell
        min_effort: List[List[float]] = [
            [math.inf for j in range(num_cols)] for i in range(num_rows)
        ]
        in_tree: List[List[bool]] = [
            [False for j in range(num_cols)] for i in range(num_rows)
        ]

        x, y = (0, 0)
        min_effort[0][0] = 0

        # Dijkstra's algorithm
        while in_tree[x][y] == False:
            # mark curent node as visited and iterate over adjacent nodes
            in_tree[x][y] = True
            adjacent_nodes = self._get_adjacent_nodes(x, y, num_cols, num_rows)
            for adj_x, adj_y in adjacent_nodes:
                weight = abs(heights[x][y] - heights[adj_x][adj_y])
                # min_effort is the maximum absolute difference in
                # heights between two consecutive cells
                # therefore, we just want the max of the currently
                # recorded maximum height on this path and the current
                # difference (weight)
                if min_effort[adj_x][adj_y] > min_effort[x][y] + weight:
                    min_effort[adj_x][adj_y] = min_effort[x][y] + weight

            # go through all the nodes not in the tree and add the one
            # with the shortest distance to the tree (can be sped up by
            # priority queue)
            dist: float = math.inf
            for i in range(num_rows):
                for j in range(num_cols):
                    if not in_tree[i][j] and min_effort[i][j] <= dist:
                        dist = min_effort[i][j]
                        x, y = i, j

        print(min_effort)
        return int(min_effort[num_rows - 1][num_cols - 1])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMinimumEffortPath(self):
        self.assertEqual(
            self.sol.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]), 2
        )
        self.assertEqual(
            self.sol.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]), 5
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


if __name__ == "__main__":
    unittest.main()
