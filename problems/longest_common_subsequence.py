import unittest


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        # n rows, m columns
        dp = [[0] * m for _ in range(0, n)]

        for i in range(0, n):
            for j in range(0, m):
                if text1[i] == text2[j]:
                    # if we match, both i and j are decremented
                    # if we took the max of decrementing either i or j
                    # we would double count some letters
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # if we don't match, we take try decrementing i and
                    # j separately and take the max result between them
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[n - 1][m - 1]

    def longestCommonSubsequenceTopDown(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            elif text1[i] == text2[j]:
                return 1 + dp(i - 1, j - 1)
            else:
                return max(dp(i - 1, j), dp(i, j - 1))

        return dp(n - 1, m - 1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testLongestCommonSubsequence(self):
        self.assertEqual(self.sol.longestCommonSubsequence("abcde", "ace"), 3)
        self.assertEqual(self.sol.longestCommonSubsequence("abc", "abc"), 3)
        self.assertEqual(self.sol.longestCommonSubsequence("abc", "def"), 0)
        self.assertEqual(self.sol.longestCommonSubsequence("abcd", "def"), 1)
        self.assertEqual(self.sol.longestCommonSubsequence("abc", "cdef"), 1)
        self.assertEqual(self.sol.longestCommonSubsequence("mbsbinin", "jmjkbkjkv"), 2)
        self.assertEqual(self.sol.longestCommonSubsequence("bsbininm", "jmjkbkjkv"), 1)
        self.assertEqual(self.sol.longestCommonSubsequence("bsbminin", "jmjkbkjkv"), 1)

    def testLongestCommonSubsequenceTopDown(self):
        self.assertEqual(self.sol.longestCommonSubsequenceTopDown("abcde", "ace"), 3)
        self.assertEqual(self.sol.longestCommonSubsequenceTopDown("abc", "abc"), 3)
        self.assertEqual(self.sol.longestCommonSubsequenceTopDown("abc", "def"), 0)
        self.assertEqual(self.sol.longestCommonSubsequenceTopDown("abcd", "def"), 1)
        self.assertEqual(self.sol.longestCommonSubsequenceTopDown("abc", "cdef"), 1)
        self.assertEqual(
            self.sol.longestCommonSubsequenceTopDown("mbsbinin", "jmjkbkjkv"), 2
        )
        self.assertEqual(
            self.sol.longestCommonSubsequenceTopDown("bsbininm", "jmjkbkjkv"), 1
        )
        self.assertEqual(
            self.sol.longestCommonSubsequenceTopDown("bsbminin", "jmjkbkjkv"), 1
        )


if __name__ == "__main__":
    unittest.main()
