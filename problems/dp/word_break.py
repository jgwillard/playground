from typing import List
import unittest


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testWordBreak(self):
        self.assertEqual(self.sol.wordBreak("leetcode", ["leet", "code"]), True)
        self.assertEqual(
            self.sol.wordBreak("abcdef", ["abcde", "ef", "abc", "a", "d"]), True
        )
        self.assertEqual(
            self.sol.wordBreak("applepenapple", ["apple", "pen"]), True
        )
        self.assertEqual(
            self.sol.wordBreak(
                "catsandog", ["cats", "dog", "sand", "and", "cat"]
            ),
            False,
        )


if __name__ == "__main__":
    unittest.main()
