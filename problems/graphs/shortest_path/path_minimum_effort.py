import math
from typing import List
import unittest


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        num_cols = len(heights)
        num_rows = len(heights[0])
        # record minimum effort required to reach each cell
        minimum_effort: List[List[float]] = [[math.inf] * num_rows] * num_cols
        visited: List[List[bool]] = [[False] * num_rows] * num_cols

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
