from typing import List
import unittest
from union_find import UnionFind


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        return uf.count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMethodName(self):
        self.assertEqual(self.sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]), 2)
        self.assertEqual(
            self.sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1
        )


if __name__ == "__main__":
    unittest.main()
