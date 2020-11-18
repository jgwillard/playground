import unittest
from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_original = x
        if x < 0:
            return False
        digits: List[int] = []
        while x:
            digits.append(x % 10)
            x = x // 10

        x_reversed = 0
        multiplier = len(digits)-1
        for d in digits:
            x_reversed += d*(10**multiplier)
            multiplier -= 1

        return x_original == x_reversed


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_is_palindrome(self):
        self.assertTrue(self.sol.isPalindrome(121))
        self.assertTrue(self.sol.isPalindrome(31213))
        self.assertFalse(self.sol.isPalindrome(-121))
        self.assertFalse(self.sol.isPalindrome(122))


if __name__ == '__main__':
    unittest.main()
