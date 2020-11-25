from typing import Optional
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# TODO improve this convoluted solution
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        out_list = ListNode()
        current_node = out_list

        while l1 and l2:
            if l1.val < l2.val:
                current_node.val = l1.val
                l1 = l1.next

            else:
                current_node.val = l2.val
                l2 = l2.next

            current_node.next = ListNode()
            if not l1 or not l2:
                break

            current_node = current_node.next

        if l1:
            current_node.next = l1
        elif l2:
            current_node.next = l2

        return out_list


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # NOTE this is a convenience method; it will pass incorrectly for
    # lists of different lengths
    def assertLinkedListEqual(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        if not l1 or not l2:
            return
        while l1 and l2:
            self.assertEqual(l1.val, l2.val)
            l1 = l1.next
            l2 = l2.next

    def testMergeTwoLists(self):
        self.assertLinkedListEqual(
            self.sol.mergeTwoLists(
                ListNode(1, ListNode(2, ListNode(4, None))),
                ListNode(1, ListNode(3, ListNode(4, None)))
            ),
            ListNode(1, ListNode(1, ListNode(
                2, ListNode(3, ListNode(4, ListNode(4, None))))))
        )

        self.assertLinkedListEqual(
            self.sol.mergeTwoLists(
                ListNode(1, ListNode(2, ListNode(4, None))),
                ListNode(1, ListNode(3, None))
            ),
            ListNode(1, ListNode(1, ListNode(
                2, ListNode(3, ListNode(4, None)))))
        )

        self.assertEqual(
            self.sol.mergeTwoLists(None, None),
            None
        )

        self.assertLinkedListEqual(
            self.sol.mergeTwoLists(
                None, ListNode(2, None)
            ),
            ListNode(2, None)
        )


if __name__ == '__main__':
    unittest.main()
