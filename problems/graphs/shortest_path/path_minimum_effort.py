import math
from typing import List
import unittest


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        num_cols = len(heights)
        num_rows = len(heights[0])
        # record minimum effort required to reach each cell
        minimum_effort: List[List[float]] = [[math.inf] * num_rows] * num_cols
        in_tree: List[List[bool]] = [[False] * num_rows] * num_cols

        x, y = (0, 0)
        minimum_effort[0][0] = 0
        # Dijkstra's algorithm
        while in_tree[x][y] == False:
            in_tree[0][0] = True
            # go through all nodes adjacent to the tree and update their
            # shortest distance to the tree (all have inf by default)

            # for each node adjacent to v:
            # weight = abs(heights[x][y] - heights[node_x][node_y])
            #   if dist[v] + weight < dist[node]:
            #       dist[node] = dist[v] + weight

            # go through all the nodes not in the tree and add the one
            # with the shortest distance to the tree

            # dist = math.inf
            # for i in range(num_rows):
            #   for j in range(num_cols):
            #       if not in_tree[i][j] and dist[i][j] < dist:
            #           dist = dist[i][j]
            #           x, y = i, j

        return int(minimum_effort[num_rows - 1][num_cols - 1])


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
