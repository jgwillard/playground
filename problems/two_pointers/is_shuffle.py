import unittest


class Solution:
    def is_shuffle(self, x: str, y: str, z: str) -> bool:
        # n = len(u)
        # i = 0
        # j = 0
        # for k in range(n):
        #     if i < len(x) and z[k] == x[i]:
        #         i += 1
        #     elif j < len(y) and z[k] == y[j]:
        #         j += 1
        #     else:
        #         return False

        # return True
        n = len(x)
        m = len(y)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(n):
            dp[i + 1][m] = z[i + m] == x[i]
        for j in range(m):
            dp[n][j + 1] = z[j + n] == y[j]
        print(dp)
        return dp[n][m]


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
        # self.assertTrue(self.sol.is_shuffle("ss", "o", "sos"))
        # self.assertTrue(self.sol.is_shuffle("sos", "", "sos"))
        # self.assertTrue(self.sol.is_shuffle("", "sos", "sos"))
        self.assertTrue(self.sol.is_shuffle("cat", "dog", "catdog"))
        # self.assertTrue(self.sol.is_shuffle("cat", "dog", "cadogt"))
        # self.assertTrue(self.sol.is_shuffle("cat", "dog", "cadotg"))
        # self.assertFalse(self.sol.is_shuffle("cat", "dog", "caodtg"))


if __name__ == "__main__":
    unittest.main()
