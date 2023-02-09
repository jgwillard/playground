from typing import Dict, List, Deque
import unittest


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacency_list: Dict[int, List[int]] = {i: [] for i in range(n)}
        indegree: List[int] = [0 for _ in range(n)]
        leaves: List[int] = []

        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        for _, neighbors in adjacency_list.items():
            for neighbor in neighbors:
                indegree[neighbor] += 1

        for node, _ in enumerate(adjacency_list):
            if indegree[node] == 1:
                leaves.append(node)

        # a tree can have at most 2 centroid nodes, so we successively
        # trim leaves until only 2 or 1 nodes are left
        while len(adjacency_list) > 2:
            new_leaves = []
            # go through all current leaves and trim them, decrementing
            # the indegree of their neighbors
            for leaf in leaves:
                for neighbor in adjacency_list[leaf]:
                    indegree[neighbor] -= 1
                    # if a neighbor of a current leaf now has indegree 1
                    # then it is one of the new leaves
                    if indegree[neighbor] == 1:
                        new_leaves.append(neighbor)

                del adjacency_list[leaf]

            leaves = new_leaves

        return [node for node in adjacency_list.keys()]


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
