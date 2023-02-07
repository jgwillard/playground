from typing import List
import unittest


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFindMinHeightTrees(self):
        self.assertEqual(
            self.sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]), [1]
        )
        self.assertEqual(
            self.sol.findMinHeightTrees(
                6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
            ),
            [3, 4],
        )


if __name__ == "__main__":
    unittest.main()
