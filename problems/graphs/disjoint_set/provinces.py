from typing import List
import unittest
from union_find import UnionFind


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(0, n):
            for j in range(i, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        return uf.count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFindCircleNum(self):
        self.assertEqual(self.sol.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
        self.assertEqual(self.sol.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3)


if __name__ == "__main__":
    unittest.main()
