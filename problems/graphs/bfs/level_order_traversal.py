from collections import deque
from typing import List, Optional
import unittest


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:

        if not root:
            return []

        ret: List[List[int]] = []
        queue = deque([root])

        counter: int = 0
        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                # add values to level list
                if node.val is not None:
                    if counter >= len(ret):
                        ret.append([])
                    ret[counter].append(node.val)

                if node.children is not None:
                    for child in node.children:
                        queue.append(child)

                # check if we're at the end of a level and if we are,
                # increment the counter
                if i == size - 1:
                    counter += 1

        return ret


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testLevelOrder(self):
        self.assertEqual(
            self.sol.levelOrder(
                Node(1, [Node(2, [Node(4), Node(5)]), Node(3, [Node(6), Node(7)])])
            ),
            [[1], [2, 3], [4, 5, 6, 7]],
        )
        self.assertEqual(
            self.sol.levelOrder(
                Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
            ),
            [[1], [3, 2, 4], [5, 6]],
        )
        self.assertEqual(
            self.sol.levelOrder(
                Node(1, [Node(10, [Node(5), Node(0)]), Node(3, [Node(6)])])
            ),
            [[1], [10, 3], [5, 0, 6]],
        )


if __name__ == "__main__":
    unittest.main()
