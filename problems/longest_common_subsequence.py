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
                    dp[i][j] = 1 + max(dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[n - 1][m - 1]


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


if __name__ == "__main__":
    unittest.main()
