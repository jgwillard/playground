from collections import deque
from typing import Deque, Dict, List, Tuple
import unittest


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        MAX_INT = 10**4 + 1
        # dict of edges from a node -- node: [(node, weight)]
        adjacency_list: Dict[int, List[Tuple[int, int]]] = {}
        for flight in flights:
            source, target, weight = flight
            if source in adjacency_list:
                adjacency_list[source].append((target, weight))
            else:
                adjacency_list[source] = [(target, weight)]

        dist = [MAX_INT] * (n + 1)
        queue: Deque[int] = deque()

        queue.append(src)
        # distance from k to k is 0
        dist[src] = 0
        # can only go k + 1 hops away from src
        hops = 0

        while queue:
            size = len(queue)
            # we have exceeded max number of stops so exit loop
            if hops > k:
                break

            for i in range(size):
                v = queue.popleft()
                if v in adjacency_list:
                    for edge in adjacency_list[v]:
                        # i is a node adjacent to v
                        j, weight = edge
                        queue.append(j)

                        if dist[v] + weight < dist[j]:
                            # on first discovery of i, dist[i] = MAX_INT, so
                            # this will be updated to the weight of the outgoing
                            # edge from src to i
                            # on subsequent iterations, we only update if the
                            # total weight from src to v + the weight from v to
                            # i is less than our previously recorded weight from
                            # src to i
                            dist[j] = dist[v] + weight

            hops += 1

        return dist[dst] if dist[dst] != MAX_INT else -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testFindCheapestPrice(self):
        self.assertEqual(
            self.sol.findCheapestPrice(
                4,
                [
                    [0, 1, 100],
                    [1, 2, 100],
                    [2, 0, 100],
                    [1, 3, 600],
                    [2, 3, 200],
                ],
                0,
                3,
                0,
            ),
            -1,
        )
        self.assertEqual(
            self.sol.findCheapestPrice(
                4,
                [
                    [0, 1, 100],
                    [1, 2, 100],
                    [2, 0, 100],
                    [1, 3, 600],
                    [2, 3, 200],
                ],
                0,
                3,
                1,
            ),
            700,
        )
        self.assertEqual(
            self.sol.findCheapestPrice(
                4,
                [
                    [0, 1, 100],
                    [1, 2, 100],
                    [2, 0, 100],
                    [1, 3, 600],
                    [2, 3, 200],
                ],
                0,
                3,
                2,
            ),
            400,
        )
        self.assertEqual(
            self.sol.findCheapestPrice(
                2, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1
            ),
            200,
        )
        self.assertEqual(
            self.sol.findCheapestPrice(
                3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0
            ),
            500,
        )
        self.assertEqual(
            self.sol.findCheapestPrice(
                5,
                [
                    [4, 1, 1],
                    [1, 2, 3],
                    [0, 3, 2],
                    [0, 4, 10],
                    [3, 1, 1],
                    [1, 4, 3],
                ],
                2,
                1,
                1,
            ),
            -1,
        )
        self.assertEqual(
            self.sol.findCheapestPrice(
                4,
                [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]],
                0,
                3,
                1,
            ),
            6,
        )


if __name__ == "__main__":
    unittest.main()
