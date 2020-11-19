from typing import List
import unittest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_strs = len(strs)
        if len_strs == 0:
            return ''
        out = ''
        i = 0
        while True:
            try:
                current_char = strs[0][i]
                for j in range(1, len_strs):
                    if strs[j][i] != current_char:
                        return out
                out += current_char
                i += 1
            except IndexError:
                return out


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_longest_common_prefix(self):
        self.assertEqual(self.sol.longestCommonPrefix(
            ['', '', '']), '')
        self.assertEqual(self.sol.longestCommonPrefix(
            ['sun', 'speed', 'sand']), 's')
        self.assertEqual(self.sol.longestCommonPrefix(
            ['flower', 'flow', 'flight']), 'fl')
        self.assertEqual(self.sol.longestCommonPrefix(
            ['dog', 'racecar', 'car']), '')
        self.assertEqual(self.sol.longestCommonPrefix(
            ['Dampf', 'Dampfschifffahrt', 'Dampfbad']), 'Dampf')
        self.assertEqual(self.sol.longestCommonPrefix(
            ['fun', 'fun', 'fun']), 'fun')


if __name__ == '__main__':
    unittest.main()
