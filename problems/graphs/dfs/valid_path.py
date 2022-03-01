from typing import Dict, List
import unittest


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        """
        Given a graph of n vertices and a list of edges, return true if
        there is a valid path between source and destination, else false
        """
        adjacency_list: Dict[int, List[int]] = {i: [] for i in range(0, n)}
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])

        # dfs
        processed = [False] * n
        vertex_stack: List[int] = [source]

        while vertex_stack:
            # get current node
            node = vertex_stack.pop()

            # check if we have reached destination
            if node == destination:
                return True

            # add adjacent unprocessed nodes to stack
            for v in adjacency_list[node]:
                if not processed[v]:
                    vertex_stack.append(v)

            # mark current node as processed
            processed[node] = True

        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testValidPath(self):
        self.assertEqual(self.sol.validPath(1, [], 0, 0), True)
        self.assertEqual(self.sol.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2), True)
        self.assertEqual(
            self.sol.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5), False
        )


if __name__ == "__main__":
    unittest.main()
