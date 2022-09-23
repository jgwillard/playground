from typing import Deque, List, Tuple
from collections import deque
import unittest


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rotten_oranges: List[Tuple[int, int]] = []
        fresh_oranges_count = 0
        minutes_elapsed = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges_count += 1

        def get_adjacent_squares(
            square: Tuple[int, int]
        ) -> List[Tuple[int, int]]:
            x, y = square
            ret: List[Tuple[int, int]] = []
            # top
            if y > 0:
                ret.append((x, y - 1))
            # right
            if x < m - 1:
                ret.append((x + 1, y))
            # bottom
            if y < n - 1:
                ret.append((x, y + 1))
            # left
            if x > 0:
                ret.append((x - 1, y))
            return ret

        queue: Deque[Tuple[int, int]] = deque(rotten_oranges)

        while queue:
            size = len(queue)
            if fresh_oranges_count == 0:
                break
            for i in range(size):
                square = queue.popleft()
                for x, y in get_adjacent_squares(square):
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh_oranges_count -= 1
                        queue.append((x, y))

            minutes_elapsed += 1

        return minutes_elapsed if fresh_oranges_count == 0 else -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testOrangesRotting(self):
        self.assertEqual(
            self.sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4
        )
        self.assertEqual(
            self.sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]), -1
        )
        self.assertEqual(self.sol.orangesRotting([[0, 2]]), 0)


if __name__ == "__main__":
    unittest.main()
