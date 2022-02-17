from collections import defaultdict
from typing import DefaultDict, List
import unittest

from union_find import UnionFind


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        for pair in pairs:
            uf.union(pair[0], pair[1])
        # now we have the indices organized into connected components
        connected_components: DefaultDict[int, List[str]] = defaultdict(list)
        for i in range(n):
            connected_components[uf.find(i)].append(s[i])
        # we need to sort each connected component alphabetically
        for root, chars in connected_components.items():
            connected_components[root] = sorted(chars)
        # now we can iterate through the string, find the root of each
        # index, and put the highest ranked element in that component
        # at that index
        smallest_str = []
        for i in range(n):
            smallest_str.append(connected_components[uf.find(i)].pop(0))

        return "".join(smallest_str)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testSmallestStringWithSwaps(self):
        self.assertEqual(
            self.sol.smallestStringWithSwaps("dcab", [[0, 3], [1, 2]]), "bacd"
        )
        self.assertEqual(
            self.sol.smallestStringWithSwaps("dcab", [[0, 3], [1, 2], [0, 2]]), "abcd"
        )
        self.assertEqual(
            self.sol.smallestStringWithSwaps("cba", [[0, 1], [1, 2]]), "abc"
        )


if __name__ == "__main__":
    unittest.main()
