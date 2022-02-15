from typing import List
import unittest


class UnionFind(object):
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.count = size
        self.weight = [1] * size

    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        # path compression: if the examined node is not a root, set its
        # parent to be the root so that future lookups take O(1) time
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        i = self.find(x)
        j = self.find(y)
        if i == j:
            return
        if self.weight[i] < self.weight[j]:
            self.root[i] = j
            self.weight[j] += self.weight[i]
        else:
            self.root[j] = i
            self.weight[i] += self.weight[j]

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
