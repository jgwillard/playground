from typing import Dict, List, Tuple
import unittest


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        MAX_INT = 10 ** 6
        adjacency_list: Dict[int, List[Tuple[int, int]]] = {}
        for time in times:
            source, target, weight = time
            if source in adjacency_list:
                adjacency_list[source].append((target, weight))
            else:
                adjacency_list[source] = [(target, weight)]

        in_tree = [False] * (n + 1)
        dist = [MAX_INT] * (n + 1)

        # start from k
        v = k
        # distance from k to k is 0
        dist[v] = 0

        while not in_tree[v]:
            # we are adding v to the tree
            in_tree[v] = True

            # i is a node adjacent to v
            # we record the shortest distance from k to i by checking if
            # the weight of the edge v->i plus the distance from k to v
            # is less than the current shortest distance from k to i
            #
            # if it is, then we update the shortest distance from k to i
            # to be equal to the weight of v->i plus dist from k to v
            if v in adjacency_list:
                for edge in adjacency_list[v]:
                    i, weight = edge
                    if dist[v] + weight < dist[i]:
                        dist[i] = dist[v] + weight

            # we then add a node to the tree by iterating through all
            # and choosing the one with the shortest distance to the
            # tree
            # we know that this our path to this node is the shortest
            # possible one, because any other path would have to go
            # through a longer path first and then add another edge to
            # connect to the node, but we don't allow negative weights
            # so this would necessarily be a longer path
            min_dist = MAX_INT
            for i in range(n):
                if not in_tree[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    v = i

        head, *tail = dist
        return max(tail)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testNetworkDelayTime(self):
        self.assertEqual(
            self.sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2
        )
        self.assertEqual(self.sol.networkDelayTime([[1, 2, 1]], 2, 1), 1)
        # self.assertEqual(self.sol.networkDelayTime([[1, 2, 1]], 2, 2), -1)


if __name__ == "__main__":
    unittest.main()
