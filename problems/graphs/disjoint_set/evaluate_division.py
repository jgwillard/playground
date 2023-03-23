from typing import Dict, List
import unittest


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        # build graph out of equations list
        # ex: {
        #       'a': { 'b': 2.0 },
        #       'b': { 'a': 0.5, 'c': 3.0 },
        #       'c' { 'b': 0.33 }
        # }
        graph: Dict[str, Dict[str, float]] = {}
        for i, val in enumerate(values):
            x, y = equations[i]
            x_adj_list = graph.setdefault(x, {})
            y_adj_list = graph.setdefault(y, {})
            x_adj_list[y] = val
            y_adj_list[x] = 1 / val

        print(graph)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testCalcEquation(self):
        self.assertEqual(
            self.sol.calcEquation(
                [["a", "b"], ["b", "c"]],
                [2.0, 3.0],
                [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            ),
            [6.0, 0.5, -1.0, 1.0, -1.0],
        )
        self.assertEqual(
            self.sol.calcEquation(
                [["a", "b"], ["b", "c"], ["bc", "cd"]],
                [1.5, 2.5, 5.0],
                [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            ),
            [3.75000, 0.40000, 5.00000, 0.20000],
        )
        self.assertEqual(
            self.sol.calcEquation(
                [["a", "b"]],
                [0.5],
                [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
            ),
            [0.50000, 2.00000, -1.00000, -1.00000],
        )


if __name__ == "__main__":
    unittest.main()
