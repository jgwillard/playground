from typing import List
import unittest


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # the matrix is size m x n where m = height = len(matrix) and
        # n = width = len(matrix[0]) (we are given that m, n >= 1)
        # each element in the matrix is "0" or "1"; we are to find the
        # size of the largest square in the matrix comprising all 1's
        m = len(matrix)
        n = len(matrix[0])
        maximal_square_side = 0

        memo = [[0] * (n + 1) for _ in range(0, m + 1)]

        def dp(i: int, j: int) -> int:
            # find the length of the side of the maximum square starting
            # at matrix[i][j] by recursively checking each of its
            # neighbors to the right, bottom right, and bottom, and
            # adding 1 to the minimum of each of those calls so that if
            # each is a 1, the length of a side of the maximal square is
            # at least 2, but if any is a 0, the length of the side is 1
            if i >= m:
                return 0
            if j >= n:
                return 0
            if matrix[i][j] == "0":
                return 0
            if not memo[i][j]:
                memo[i][j] = 1 + min(dp(i, j + 1), dp(i + 1, j + 1), dp(i + 1, j))
            return memo[i][j]

        for i in range(0, m):
            for j in range(0, n):
                square_size = dp(i, j)
                if square_size > maximal_square_side:
                    maximal_square_side = square_size
        return maximal_square_side ** 2


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMaximalSquare(self):
        self.assertEqual(self.sol.maximalSquare([["0"]]), 0)
        self.assertEqual(self.sol.maximalSquare([["1"]]), 1)
        self.assertEqual(self.sol.maximalSquare([["0", "1"], ["1", "0"]]), 1)
        self.assertEqual(
            self.sol.maximalSquare(
                [
                    ["1", "0", "1", "0", "0"],
                    ["1", "0", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "0", "0", "1", "0"],
                ]
            ),
            4,
        )
        self.assertEqual(
            self.sol.maximalSquare(
                [
                    ["1", "0", "1", "0", "0"],
                    ["1", "0", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "0", "1", "1", "1"],
                ]
            ),
            9,
        )
        self.assertEqual(
            self.sol.maximalSquare(
                [
                    ["1", "1", "1", "1", "1", "1", "1", "1"],
                    ["1", "1", "1", "1", "1", "1", "1", "0"],
                    ["1", "1", "1", "1", "1", "1", "1", "0"],
                    ["1", "1", "1", "1", "1", "0", "0", "0"],
                    ["0", "1", "1", "1", "1", "0", "0", "0"],
                ],
            ),
            16,
        )


if __name__ == "__main__":
    unittest.main()
