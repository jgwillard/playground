from typing import Dict, List
import unittest


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        For an integer array coins representing coins of different
        denominations and an integer amount representing a total amount
        of money, return the fewest number of coins that you need to
        make up that amount. If that amount of money cannot be made up
        by any combination of the coins, return -1.
        """
        memo: Dict[int, int] = {}

        # for a given amount, the minimum number of coins to make that
        # amount is equal to 1 plus the minimum number of coins to make
        # that amount less the value of the last coin:
        # F(a) = 1 + F(a - c)
        # the rub is that we don't know that value of the last coin, so
        # we have to try them all (note that a greedy algorithm won't
        # work here; for a counterexample consider denominations 4, 7
        # and a total amount of 12)
        def dp(remaining: int):

            if remaining == 0:
                return 0
            if remaining < 1:
                return -1

            if remaining not in memo:
                min_cost = float("inf")
                # for each denomination of coin, calculate the minimum
                # number of coins needed to make the amount less the
                # value of that denomination
                for coin in coins:
                    cost = dp(remaining - coin)
                    # if cost was -1, then no valid solution was found in
                    # the above call's subtree
                    if cost != -1:
                        min_cost = min(cost + 1, min_cost)

                # if min_cost is still inf after the loop, no valid
                # solution was found in the subtree of any calls in the
                # loop
                memo[remaining] = min_cost if min_cost != float("inf") else -1

            return memo[remaining]

        return dp(amount)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcoinChange(self):
        self.assertEqual(self.sol.coinChange([1, 2, 5], 11), 3)
        self.assertEqual(self.sol.coinChange([2], 3), -1)
        self.assertEqual(self.sol.coinChange([1], 0), 0)


if __name__ == "__main__":
    unittest.main()
