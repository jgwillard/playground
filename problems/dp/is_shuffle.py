from functools import cache
import unittest


class Solution:
    def is_shuffle_top_down(self, x: str, y: str, z: str) -> bool:
        """
        Defines the following process for x = cat, y = dog, z = catdog
        s(3, 3) -> catdog, cat, dog AND z[6] == y[3]
        s(3, 2) -> catdo, cat, do AND z[5] == y[2]
        s(3, 1) -> catd, cat, d AND z[4] == y[1]
        s(3, 0) -> cat, cat, AND z[1..3] == x[1..3]
        """

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
        """
        A bottom up implementation of the above algorithm

        For x = 'cat', y = 'dog', z = 'catdog', this functon will create
        the following table:

        |      | ""   | D     | O     | G     |
        | ---- | ---- | ----- | ----- | ----- |
        | ""   | True | True  | True  | True  |
        | C    | True | False | False | False |
        | A    | True | False | False | False |
        | T    | True | True  | True  | True  |

        For x = 'cat', y = 'dog', z = 'dogcat', this functon will create
        the following table:

        |      | ""   | D     | O     | G    |
        | ---- | ---- | ----- | ----- | ---- |
        | ""   | True | True  | True  | True |
        | C    | True | False | False | True |
        | A    | True | False | False | True |
        | T    | True | False | False | True |

        The left column and top row are all initialized to true because
        it is vacuously the case that the empty string can be shuffled
        into any string and leave that string unchanged. For the other
        cells in the matrix, we check if the current letter in x matches
        the current letter in z;

        """
        n = len(x)
        m = len(y)
        s = [[False for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            s[i][0] = True

        for j in range(m + 1):
            s[0][j] = True

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s[i][j] = (s[i - 1][j] and z[i + j - 1] == x[i - 1]) or (
                    s[i][j - 1] and z[i + j - 1] == y[j - 1]
                )

        return s[n][m]


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
        self.assertTrue(self.sol.is_shuffle("cat", "dog", "dogcat"))
        self.assertTrue(self.sol.is_shuffle("cat", "dog", "cadogt"))
        self.assertTrue(self.sol.is_shuffle("cat", "dog", "cadotg"))
        self.assertFalse(self.sol.is_shuffle("cat", "dog", "caodtg"))


if __name__ == "__main__":
    unittest.main()
