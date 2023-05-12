import unittest


class Solution:
    def is_shuffle(self, s: str, t: str, u: str) -> bool:
        # n = len(u)
        # i = 0
        # j = 0
        # for k in range(n):
        #     if i < len(s) and u[k] == s[i]:
        #         i += 1
        #     elif j < len(t) and u[k] == t[j]:
        #         j += 1
        #     else:
        #         return False

        # return True
        dp = [[False] * (len(s) + 1) for _ in range(len(t) + 1)]
        dp[0][1] = s[0] == u[0]
        dp[1][0] = t[0] == u[0]
        print(dp)
        for i in range(1, len(s)):
            for j in range(1, len(t)):
                dp[i][j] = (s[i] == u[i + j] and dp[i - 1][j]) or (
                    t[j] == u[i + j] and dp[i][j - 1]
                )

        print(dp)
        return dp[len(s)][len(t)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_is_shuffle(self):
        # self.assertTrue(
        #     self.sol.is_shuffle("chocolate", "chips", "cchocohilaptes")
        # )
        # self.assertFalse(
        #     self.sol.is_shuffle("chocolate", "chips", "chocochilatspe")
        # )
        self.assertTrue(self.sol.is_shuffle("cat", "dog", "catdog"))
        self.assertTrue(self.sol.is_shuffle("cat", "dog", "cadogt"))
        self.assertTrue(self.sol.is_shuffle("cat", "dog", "cadotg"))
        self.assertFalse(self.sol.is_shuffle("cat", "dog", "caodtg"))


if __name__ == "__main__":
    unittest.main()
