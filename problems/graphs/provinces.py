from typing import List
import unittest


class UnionFind(object):
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.count = size

    def find(self, x: int) -> int:
        while self.root[x] != x:
            x = self.root[x]
        return x

    def union(self, x: int, y: int):
        i = self.find(x)
        j = self.find(y)
        if i != j:
            self.root[i] = j
            self.count -= 1

    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)


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
