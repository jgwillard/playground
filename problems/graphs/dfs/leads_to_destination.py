from typing import List
import unittest


class Solution:
    def leadsToDestination(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adjacency_list: List[List[int]] = [[] for _ in range(n)]
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])

        discovered = [False] * n
        stack: List[int] = [source]

        while stack:
            node = stack.pop()

            # import pdb

            # pdb.set_trace()
            for neighbor in adjacency_list[node]:
                # if cycle is created return false (check for backedges
                # and selfedges)
                if neighbor in stack or neighbor == node:
                    return False

                # append all reachable nodes to the stack
                if adjacency_list[neighbor]:
                    for next_node in adjacency_list[neighbor]:
                        stack.append(next_node)
                # if no nodes are reachable, make sure node is
                # destination
                elif node != destination:
                    return False

        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testLeadsToDestination(self):
        self.assertFalse(self.sol.leadsToDestination(3, [[0, 1], [0, 2]], 0, 2))
        self.assertFalse(
            self.sol.leadsToDestination(
                4, [[0, 1], [0, 3], [1, 2], [2, 1]], 0, 3
            )
        )
        self.assertTrue(
            self.sol.leadsToDestination(
                4, [[0, 1], [0, 2], [1, 3], [2, 3]], 0, 3
            )
        )
        self.assertFalse(self.sol.leadsToDestination(2, [[0, 1], [1, 1]], 0, 1))
        self.assertTrue(self.sol.leadsToDestination(2, [[0, 1]], 0, 1))


if __name__ == "__main__":
    unittest.main()
