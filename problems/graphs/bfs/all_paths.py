from typing import Deque, List
from collections import deque
import unittest


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        n = len(graph)
        target = n - 1

        # bfs
        valid_paths = []
        queue: Deque[List[int]] = deque()
        queue.append([0])

        while queue:
            # get current stack from queue
            path = queue.popleft()
            # check each vertex reachable from the last vertex in the
            # current path
            for v in graph[path[-1]]:
                # make a copy of the current path
                new_path = list(path)
                # add a node that is reachable from the last vertex in
                # the current path to the copy
                new_path.append(v)
                # put the new stack on the queue
                queue.append(new_path)
                # if the last vertex on the new path is the target, it
                # is a valid path
                if v == target:
                    valid_paths.append(queue[-1])

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
        self.assertListEqual(
            sorted(
                self.sol.allPathsSourceTarget(
                    [
                        [3, 1],
                        [4, 6, 7, 2, 5],
                        [4, 6, 3],
                        [6, 4],
                        [7, 6, 5],
                        [6],
                        [7],
                        [],
                    ]
                )
            ),
            sorted(
                [
                    [0, 3, 6, 7],
                    [0, 3, 4, 7],
                    [0, 3, 4, 6, 7],
                    [0, 3, 4, 5, 6, 7],
                    [0, 1, 4, 7],
                    [0, 1, 4, 6, 7],
                    [0, 1, 4, 5, 6, 7],
                    [0, 1, 6, 7],
                    [0, 1, 7],
                    [0, 1, 2, 4, 7],
                    [0, 1, 2, 4, 6, 7],
                    [0, 1, 2, 4, 5, 6, 7],
                    [0, 1, 2, 6, 7],
                    [0, 1, 2, 3, 6, 7],
                    [0, 1, 2, 3, 4, 7],
                    [0, 1, 2, 3, 4, 6, 7],
                    [0, 1, 2, 3, 4, 5, 6, 7],
                    [0, 1, 5, 6, 7],
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
