from typing import Dict, List, Deque
from collections import deque
import unittest


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacency_list: Dict[int, List[int]] = [[] for _ in range(n)]
        indegree: List[int] = [0 for _ in range(n)]
        leaf_nodes_queue: Deque[int] = deque()

        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        for _, neighbors in enumerate(adjacency_list):
            for neighbor in neighbors:
                indegree[neighbor] += 1

        for node, _ in enumerate(adjacency_list):
            if indegree[node] == 1:
                leaf_nodes_queue.append(node)

        while leaf_nodes_queue:
            node = leaf_nodes_queue.popleft()
            for neighbor in adjacency_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 1:
                    leaf_nodes_queue.append(neighbor)

            del adjacency_list[node]

            # TODO check if the two nodes in adjacency list point to each other
            if len(adjacency_list) == 2:
                return [node for node, _ in enumerate(adjacency_list)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFindMinHeightTrees(self):
        self.assertEqual(
            self.sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]), [1]
        )
        self.assertEqual(
            self.sol.findMinHeightTrees(
                6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
            ),
            [3, 4],
        )


if __name__ == "__main__":
    unittest.main()
