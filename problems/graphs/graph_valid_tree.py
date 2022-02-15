from typing import List
import unittest
from union_find import UnionFind


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for edge in edges:
            if uf.connected(edge[0], edge[1]):
                return False
            uf.union(edge[0], edge[1])
        return uf.count == 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testValidTree(self):
        self.assertEqual(self.sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True)
        self.assertEqual(
            self.sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False
        )


if __name__ == "__main__":
    unittest.main()
