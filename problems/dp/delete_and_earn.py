from typing import List
import unittest


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testDeleteAndEarn(self):
        self.assertEqual(self.sol.deleteAndEarn([3, 4, 2]), 6)
        self.assertEqual(self.sol.deleteAndEarn([2, 2, 3, 3, 3, 4]), 9)


if __name__ == "__main__":
    unittest.main()
