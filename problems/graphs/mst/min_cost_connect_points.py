from typing import Dict, List, Tuple
import unittest


class UnionFind(object):
    def __init__(self, n: int):
        self.root = [i for i in range(n)]
        self.count = n
        self.height = [1] * n

    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        return self.find(self.root[x])

    def union(self, x: int, y: int):
        i = self.find(x)
        j = self.find(y)

        if i == j:
            return

        # the root of the taller tree becomes the root of the shorter
        # tree so that it does not grow by a level
        if self.height[i] > self.height[j]:
            self.root[j] = i
            self.height[i] += self.height[j]
        else:
            self.root[i] = j
            self.height[j] += self.height[i]

        self.count -= 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        points_dict: Dict[Tuple[int, int], int] = {}
        # edges are 3-tuples of two points and the distance between them
        edges: List[Tuple[List[int], List[int], int]] = []
        for i in range(n):
            x_i, y_i = points[i]
            points_dict[(x_i, y_i)] = i
            for j in range(i + 1, n):
                x_j, y_j = points[j]
                edges.append((points[i], points[j], abs(x_i - x_j) + abs(y_i - y_j)))

        uf = UnionFind(len(edges))
        # sort edges by Manhattan distance
        edges_sorted = sorted(edges, key=lambda edge: edge[2])
        total_distance = 0
        for edge in edges_sorted:
            point_a, point_b, distance = edge
            x_i, y_i = point_a
            x_j, y_j = point_b
            if not uf.connected(points_dict[(x_i, y_i)], points_dict[(x_j, y_j)]):
                uf.union(points_dict[(x_i, y_i)], points_dict[(x_j, y_j)])
                total_distance += distance
            if uf.count == 1:
                break

        return total_distance


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMinCostConnectPoints(self):
        self.assertEqual(
            self.sol.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]), 20
        )
        self.assertEqual(self.sol.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]), 18)


if __name__ == "__main__":
    unittest.main()
