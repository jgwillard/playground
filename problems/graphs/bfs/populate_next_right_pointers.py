from collections import deque
from typing import Deque, Optional
import unittest


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        next: Optional["Node"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        return f"NODE(val: {self.val}, left: {self.left}, right: {self.right}, next: {self.next})"

    def __repr__(self):
        return self.__str__()


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:

        if not root:
            return None

        queue: Deque[Node] = deque([root])

        while queue:
            size = len(queue)
            print("outer loop")
            for i in range(size):
                print(i)
                node = queue.popleft()

                if i < size - 1:
                    print("setting next")
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testConnect(self):
        print(
            self.sol.connect(
                Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
            ),
        )


if __name__ == "__main__":
    unittest.main()
