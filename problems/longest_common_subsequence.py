import unittest


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        def dp(i: int, j: int) -> int:

            if i < 0 or j < 0:
                return 0

            if text1[i] == text2[j]:
                return 1 + dp(i - 1, j - 1)

            return max(dp(i, j - 1), dp(i - 1, j))

        # right to left
        return dp(n - 1, m - 1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testLongestCommonSubsequence(self):
        self.assertEqual(self.sol.longestCommonSubsequence("abcde", "ace"), 3)
        self.assertEqual(self.sol.longestCommonSubsequence("abc", "abc"), 3)
        self.assertEqual(self.sol.longestCommonSubsequence("abc", "def"), 0)


if __name__ == "__main__":
    unittest.main()
