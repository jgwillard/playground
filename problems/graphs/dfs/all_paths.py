from typing import Dict, List
import unittest


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        n = len(graph)
        target = n - 1

        # dfs
        valid_paths = []
        stack: List[List[int]] = [[0]]

        while stack:
            path = stack.pop()
            for v in graph[path[-1]]:
                new_path = list(path)
                new_path.append(v)
                stack.append(new_path)
                if v == target:
                    valid_paths.append(stack[-1])

        return valid_paths


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMethodName(self):
        self.assertListEqual(
            sorted(self.sol.allPathsSourceTarget([[1, 2], [3], [3], []])),
            sorted([[0, 1, 3], [0, 2, 3]]),
        )
        self.assertListEqual(
            sorted(self.sol.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []])),
            sorted([[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]),
        )


if __name__ == "__main__":
    unittest.main()
