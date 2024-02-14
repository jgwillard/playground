import math
from typing import List
import unittest


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if n < d:
            return -1

        hardestJobRemaining = [0] * n
        hardest = 0
        for i in range(n - 1, -1, -1):
            hardest = max(hardest, jobDifficulty[i])
            hardestJobRemaining[i] = hardest

        memo = {i: {} for i in range(n)}

        def dp(i, day):
            print(i, day)
            if day == d:
                return hardestJobRemaining[i]
                # hardest = 0
                # for j in range(i, n):
                #     hardest = max(hardest, jobDifficulty[j])
                # return hardest

            best = math.inf
            hardest = 0
            if memo.get(i) is None or memo.get(i).get(day) is None:
                for j in range(i, n - d - day):
                    hardest = max(hardest, jobDifficulty[j])
                    best = min(best, hardest + dp(j + 1, day + 1))

                memo[i][day] = best

            return memo[i][day]

        ret = dp(0, 1)
        print(memo)
        return ret


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMinDifficulty(self):
        self.assertEqual(self.sol.minDifficulty([6, 5, 4, 3, 2, 1], 2), 7)
        self.assertEqual(self.sol.minDifficulty([9, 9, 9], 4), -1)
        self.assertEqual(self.sol.minDifficulty([1, 1, 1], 3), 3)


if __name__ == "__main__":
    unittest.main()
