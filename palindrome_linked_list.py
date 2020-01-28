from typing import Optional, List
import unittest


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x: int, next: Optional['ListNode'] = None):
        self.val = x
        self.next = next

    def __repr__(self):
        node: Optional['ListNode'] = self
        digits: List[int] = []
        while node:
            digits.append(node.val)
            node = node.next
        return "->".join([str(digit) for digit in digits])


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        num = Solution.listToArr(head)
        return num == num[::-1]

    @staticmethod
    def listToArr(node: Optional[ListNode]) -> List[int]:
        number: List[int] = []
        while node:
            number.append(node.val)
            node = node.next
        return number


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_is_palindrome(self):
        self.assertTrue(self.sol.isPalindrome(
            ListNode(1, ListNode(2, ListNode(1, None)))))
        self.assertTrue(self.sol.isPalindrome(
            ListNode(3, ListNode(2, ListNode(3, None)))))
        self.assertTrue(self.sol.isPalindrome(
            ListNode(129, ListNode(129, None))))
        self.assertTrue(self.sol.isPalindrome(
            ListNode(-129, ListNode(-129, None))))
        self.assertFalse(self.sol.isPalindrome(
            ListNode(1, ListNode(2, ListNode(3, None)))))
        self.assertFalse(self.sol.isPalindrome(ListNode(1, ListNode(2, None))))


if __name__ == '__main__':
    unittest.main()
