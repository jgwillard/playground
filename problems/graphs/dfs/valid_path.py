from typing import List
import unittest


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testValidPath(self):
        self.assertEqual(self.sol.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2), True)
        self.assertEqual(
            self.sol.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5), False
        )


if __name__ == "__main__":
    unittest.main()
