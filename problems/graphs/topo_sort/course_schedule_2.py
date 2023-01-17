from collections import deque
from typing import Deque, List
import unittest


class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list: List[List[int]] = [[] for _ in range(n)]
        indegree: List[int] = [0 for n in range(n)]
        indegree_zero_queue: Deque[int] = deque()
        sorted_list: List[int] = []

        for a, b in prerequisites:
            adjacency_list[b].append(a)

        for node, neighbors in enumerate(adjacency_list):
            # compute the indegree for each node
            for neighbor in neighbors:
                indegree[neighbor] += 1

        for node, _ in enumerate(adjacency_list):
            # enqueue any nodes with indegree of 0
            if indegree[node] == 0:
                indegree_zero_queue.append(node)

        while indegree_zero_queue:
            # remove node from queue and add to sorted list
            node = indegree_zero_queue.popleft()
            sorted_list.append(node)
            # iterate over all that node's neighbors and decrement their
            # indegree count
            for neighbor in adjacency_list[node]:
                indegree[neighbor] -= 1
                # if any neighbors indegree count is now 0, enqueue it
                if indegree[neighbor] == 0:
                    indegree_zero_queue.append(neighbor)

        return sorted_list


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFindOrder(self):
        self.assertEqual(self.sol.findOrder(2, [[1, 0]]), [0, 1])
        self.assertEqual(
            self.sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
            [0, 1, 2, 3],  # or [0,2,1,3]
        )
        self.assertEqual(self.sol.findOrder(1, []), [0])


if __name__ == "__main__":
    unittest.main()
