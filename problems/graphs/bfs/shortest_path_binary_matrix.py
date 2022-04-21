from collections import deque
from typing import List, Deque, Tuple
import unittest


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # [    j  j+1 j+2
        # i   [0,  0,  0],
        # i+1 [0,  0,  0],
        # i+2 [0,  0,  0],
        # ]

        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        target = (n - 1, n - 1)

        if target == (0, 0):
            return 1

        adjacency_list: List[List[List[Tuple[int, int]]]] = []

        for i in range(n):
            adjacency_list.append([])
            for j in range(n):
                adjacency_list[i].append([])

                if grid[i][j] == 0:
                    # right
                    if j + 1 < n and grid[i][j + 1] == 0:
                        adjacency_list[i][j].append((i, j + 1))
                    # bottom right
                    if i + 1 < n and j + 1 < n and grid[i + 1][j + 1] == 0:
                        adjacency_list[i][j].append((i + 1, j + 1))
                    # bottom
                    if i + 1 < n and grid[i + 1][j] == 0:
                        adjacency_list[i][j].append((i + 1, j))
                    # bottom left
                    if i + 1 < n and j - 1 > -1 and grid[i + 1][j - 1] == 0:
                        adjacency_list[i][j].append((i + 1, j - 1))
                    # left
                    if j - 1 > -1 and grid[i][j - 1] == 0:
                        adjacency_list[i][j].append((i, j - 1))
                    # top left
                    if j - 1 > -1 and i - 1 > -1 and grid[i - 1][j - 1] == 0:
                        adjacency_list[i][j].append((i - 1, j - 1))
                    # top
                    if i - 1 > -1 and grid[i - 1][j] == 0:
                        adjacency_list[i][j].append((i - 1, j))
                    # top right
                    if i - 1 > -1 and j + 1 < n and grid[i - 1][j + 1] == 0:
                        adjacency_list[i][j].append((i - 1, j + 1))

        queue: Deque[List[Tuple[int, int]]] = deque([[(0, 0)]])

        while queue:
            path = queue.popleft()

            i, j = path[-1]
            for v in adjacency_list[i][j]:
                new_path = list(path)
                new_path.append(v)
                queue.append(new_path)
                if v == target:
                    return len(queue[-1])

        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testShortestPathBinaryMatrix(self):
        self.assertEqual(self.sol.shortestPathBinaryMatrix([[0, 1], [1, 0]]), 2)
        self.assertEqual(
            self.sol.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]), 4
        )
        self.assertEqual(
            self.sol.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]), -1
        )
        self.assertEqual(
            self.sol.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 1]]), -1
        )
        self.assertEqual(
            self.sol.shortestPathBinaryMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 4
        )
        self.assertEqual(
            self.sol.shortestPathBinaryMatrix(
                [
                    [0, 1, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 0, 0, 0, 0, 0],
                    [0, 1, 0, 1, 1, 1, 1, 0],
                    [0, 1, 0, 1, 1, 1, 1, 0],
                    [0, 1, 1, 0, 0, 1, 1, 0],
                    [0, 1, 1, 1, 1, 0, 1, 0],
                    [0, 0, 0, 0, 0, 1, 1, 0],
                    [1, 1, 1, 1, 1, 1, 1, 0],
                ]
            ),
            25,
        )


if __name__ == "__main__":
    unittest.main()
