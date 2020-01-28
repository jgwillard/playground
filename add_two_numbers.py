from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return Solution.numberToList(
            Solution.listToNumber(l1) + Solution.listToNumber(l2))

    @staticmethod
    def listToNumber(l: Optional[ListNode]) -> int:
        number: str = ''
        while l:
            number += str(l.val)
            l = l.next
        return int(number[::-1])

    @staticmethod
    def numberToList(num: int) -> ListNode:
        prev_node = None
        for nu in str(num):
            l = ListNode(int(nu))
            if prev_node:
                l.next = prev_node
            prev_node = l
        return l
