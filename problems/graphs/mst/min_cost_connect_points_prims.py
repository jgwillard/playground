from typing import List, Optional
import unittest


class MinPriorityQueue(object):
    def __init__(self):
        self.heap: List[int] = [0]
        self.count = 0

    def isEmpty(self) -> bool:
        return self.count == 0

    def _swap(self, i: int, j: int):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def _swim(self, k: int):
        while k > 1 and self.heap[k] < self.heap[k // 2]:
            self._swap(k, k // 2)
            k = k // 2

    def insert(self, x: int):
        self.count += 1
        self.heap.append(x)
        self._swim(self.count)

    def _sink(self, k: int):
        while k < self.count:
            j = 2 * k
            if j + 1 <= self.count and self.heap[j] > self.heap[j + 1]:
                j += 1
            if j <= self.count and not self.heap[k] < self.heap[j]:
                self._swap(j, k)
                k = j
            else:
                break

    def removeMin(self) -> Optional[int]:
        if self.isEmpty():
            return None
        self._swap(1, self.count)
        self.count -= 1
        top = self.heap.pop()
        self._sink(1)
        return top


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMinCostConnectPoints(self):
        self.assertEqual(
            self.sol.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]), 20
        )
        self.assertEqual(self.sol.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]), 18)
        self.assertEqual(
            self.sol.minCostConnectPoints([[-1000000, -1000000], [1000000, 1000000]]),
            4000000,
        )


if __name__ == "__main__":
    unittest.main()
