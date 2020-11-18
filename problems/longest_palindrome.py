import unittest


class Solution:
    # TODO improve on O(n^3)
    def longestPalindrome(self, s: str) -> str:
        # let m be the length of the string
        m = len(s)
        for i in range(0, m):
            # let n be the size of the substring
            # start with the largest substring (n = m) and decrement
            n = m - i
            for j in range(0, m - n + 1):
                # iterate over every substring of size n in s
                substring = s[j:n + j]
                # if it's a palindrome return it, since we are iterating
                # from largest to smallest substring
                if Solution.isPalindrome(substring):
                    return substring
        return ''

    @staticmethod
    def isPalindrome(s: str):
        return s == s[::-1]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_longest_palindrome(self):
        self.assertEqual(self.sol.longestPalindrome('babad'), 'bab')
        self.assertEqual(self.sol.longestPalindrome('cbbd'), 'bb')
        self.assertEqual(self.sol.longestPalindrome('cbbdddbb'), 'bbdddbb')
        self.assertEqual(self.sol.longestPalindrome('babaddddd'), 'ddddd')
        self.assertEqual(self.sol.longestPalindrome('bbbbabad'), 'bbbb')
        self.assertEqual(self.sol.longestPalindrome('abcedf'), 'a')
        self.assertEqual(self.sol.longestPalindrome(''), '')
        self.assertEqual(self.sol.longestPalindrome('aacdefcaa'), 'aa')
        self.assertEqual(self.sol.longestPalindrome('cbcdcbedcbc'), 'bcdcb')


if __name__ == '__main__':
    unittest.main()
