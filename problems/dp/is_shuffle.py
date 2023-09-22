from functools import cache
import unittest


class Solution:
    def is_shuffle_top_down(self, x: str, y: str, z: str) -> bool:

        # defines the following process for x = cat, y = dog, z = catdog
        # s(3, 3) -> catdog, cat, dog AND z[6] == y[3]
        # s(3, 2) -> catdo, cat, do AND z[5] == y[2]
        # s(3, 1) -> catd, cat, d AND z[4] == y[1]
        # s(3, 0) -> cat, cat, AND z[1..3] == x[1..3]
        @cache
        def s(i, j):
            if i == 0:
                return y[0:j] == z[0 : i + j]
            if j == 0:
                return x[0:i] == z[0 : i + j]
            return (s(i - 1, j) and z[i + j - 1] == x[i - 1]) or (
                s(i, j - 1) and z[i + j - 1] == y[j - 1]
            )

        return s(len(x), len(y))

    def is_shuffle(self, x: str, y: str, z: str):
        n = len(x)
        m = len(y)
        s = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            s[0][i] = True

        for j in range(m):
            s[j][0] = True

        for i in range(1, n):
            for j in range(1, m):
                print(i, j)
                s[i][j] = (s[i - 1][j] and z[i + j - 1] == x[i - 1]) or (
                    s[i][j - 1] and z[i + j - 1] == y[j - 1]
                )

        print(s)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_is_shuffle(self):
        self.assertTrue(
            self.sol.is_shuffle("chocolate", "chips", "cchocohilaptes")
        )
        self.assertFalse(
            self.sol.is_shuffle("chocolate", "chips", "chocochilatspe")
        )
        self.assertTrue(self.sol.is_shuffle("ss", "o", "sos"))
        self.assertTrue(self.sol.is_shuffle("sos", "", "sos"))
        self.assertTrue(self.sol.is_shuffle("", "sos", "sos"))
        self.assertTrue(self.sol.is_shuffle("cat", "cat", "catcat"))
        self.assertTrue(self.sol.is_shuffle("cat", "dog", "catdog"))
        self.assertTrue(self.sol.is_shuffle("cat", "dog", "cadogt"))
        self.assertTrue(self.sol.is_shuffle("cat", "dog", "cadotg"))
        self.assertFalse(self.sol.is_shuffle("cat", "dog", "caodtg"))


if __name__ == "__main__":
    unittest.main()
