from typing import List
import unittest
from union_find import UnionFind


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        logs_sorted = sorted(logs, key=lambda log: log[0])
        for log in logs_sorted:
            uf.union(log[1], log[2])
            if uf.count == 1:
                return log[0]
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMethodName(self):
        self.assertEqual(
            self.sol.earliestAcq(
                [
                    [20190101, 0, 1],
                    [20190104, 3, 4],
                    [20190107, 2, 3],
                    [20190211, 1, 5],
                    [20190224, 2, 4],
                    [20190301, 0, 3],
                    [20190312, 1, 2],
                    [20190322, 4, 5],
                ],
                6,
            ),
            20190301,
        )
        self.assertEqual(
            self.sol.earliestAcq(
                [[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]],
                4,
            ),
            3,
        )


if __name__ == "__main__":
    unittest.main()
