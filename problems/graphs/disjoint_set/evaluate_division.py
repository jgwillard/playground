import copy
from typing import Dict, List
import unittest


class Solution:
    finished = False

    def backtrack_dfs(
        self,
        path: List[str],
        dest: str,
        graph: Dict[str, Dict[str, float]],
        solutions: List[List[str]],
        visited: Dict[str, bool],
    ):
        if dest not in graph:
            solutions.append([])
            return
        item = path[-1]
        if item == dest:
            solutions.append(copy.copy(path))
            self.finished = True
            return
        else:
            for candidate in graph[item]:
                if not visited[candidate]:
                    path.append(candidate)
                    visited[candidate] = True
                    self.backtrack_dfs(path, dest, graph, solutions, visited)
                    path.pop()
                    visited[candidate] = False
                    if self.finished:
                        return

    def process_solutions(
        self, graph: Dict[str, Dict[str, float]], solutions: List[List[str]]
    ):
        answers: List[float] = []
        for solution in solutions:
            answer: float = 1.0
            if len(solution) == 0:
                answer = -1.0
            for i, const in enumerate(solution):
                if const not in graph:
                    answer = -1.0
                    break
                # skip last item in list
                if i == len(solution) - 1:
                    break
                next_item = solution[i + 1]
                answer = answer * graph[const][next_item]
            answers.append(answer)
        return answers

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
        visited: Dict[str, bool] = {}
        for i, val in enumerate(values):
            x, y = equations[i]
            x_adj_list = graph.setdefault(x, {})
            y_adj_list = graph.setdefault(y, {})
            x_adj_list[y] = val
            y_adj_list[x] = 1 / val
            visited[x] = False
            visited[y] = False

        solutions: List[List[str]] = []
        for query in queries:
            source, dest = query
            path: List[str] = [source]
            visited[source] = True
            self.backtrack_dfs(path, dest, graph, solutions, visited)
            self.finished = False
            visited[source] = False

        return self.process_solutions(graph, solutions)


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
        self.sol.calcEquation(
            [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
            [3.0, 4.0, 5.0, 6.0],
            [
                ["x1", "x5"],
                ["x5", "x2"],
                ["x2", "x4"],
                ["x2", "x2"],
                ["x2", "x9"],
                ["x9", "x9"],
            ],
        )
        # TODO backtrack_dfs doesn't have a way of detecting no solution
        self.assertEqual(
            self.sol.calcEquation(
                [["a", "b"], ["c", "d"]],
                [1.0, 1.0],
                [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]],
            ),
            [-1.00000, -1.00000, 1.00000, 1.00000],
        )


if __name__ == "__main__":
    unittest.main()
