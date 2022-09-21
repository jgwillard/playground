from typing import List
import unittest


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFindCheapestPrice(self):
        self.assertEqual(
            self.sol.findCheapestPrice(
                4,
                [
                    [0, 1, 100],
                    [1, 2, 100],
                    [2, 0, 100],
                    [1, 3, 600],
                    [2, 3, 200],
                ],
                0,
                3,
                1,
            ),
            700,
        )
        self.assertEqual(
            self.sol.findCheapestPrice(
                2, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1
            ),
            200,
        )
        self.assertEqual(
            self.sol.findCheapestPrice(
                3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0
            ),
            500,
        )


if __name__ == "__main__":
    unittest.main()
