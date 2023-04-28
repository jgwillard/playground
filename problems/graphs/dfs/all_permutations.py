from typing import Dict, List
import unittest


class Solution:
    visited: Dict[str, bool] = {}

    def is_solution(self, solution_vector: List[str], data: List[str]) -> bool:
        return len(solution_vector) == len(data)

    def construct_candidates(
        self,
        data: List[str],
    ) -> List[str]:
        candidates: List[str] = []
        for item in data:
            if not self.visited.get(item):
                candidates.append(item)
        return candidates

    def make_move(
        self,
        candidate: str,
        solution_vector: List[str],
    ):
        solution_vector.append(candidate)
        self.visited[candidate] = True

    def unmake_move(
        self,
        candidate: str,
        solution_vector: List[str],
    ):
        solution_vector.pop()
        self.visited[candidate] = False

    def process_solution(self, solution_vector: List[str], data: List[str]):
        s = ""
        for v in solution_vector:
            s += f"{v}"
        print(",".join(s))

    def backtrack(
        self,
        solution_vector: List[str],
        data: List[str],
    ):
        if self.is_solution(solution_vector, data):
            self.process_solution(solution_vector, data)
        else:
            candidates = self.construct_candidates(data)
            for candidate in candidates:
                self.make_move(candidate, solution_vector)
                self.backtrack(solution_vector, data)
                self.unmake_move(candidate, solution_vector)

    def print_permutations(self, data: List[str]):
        self.backtrack([], data)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_print_subsets(self):
        self.sol.print_permutations(["1", "2", "3", "4"])


if __name__ == "__main__":
    unittest.main()
