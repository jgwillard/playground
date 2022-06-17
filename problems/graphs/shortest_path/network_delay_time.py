from typing import List
import unittest


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testNetworkDelayTime(self):
        self.assertEqual(
            self.sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2
        )
        self.assertEqual(self.sol.networkDelayTime([[1, 2, 1]], 2, 1), 1)
        self.assertEqual(self.sol.networkDelayTime([[1, 2, 1]], 2, 2), -1)


if __name__ == "__main__":
    unittest.main()
