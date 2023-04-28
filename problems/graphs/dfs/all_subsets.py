from typing import List
import unittest


class Solution:
    def is_solution(self, solution_vector: List[bool], data: List[str]) -> bool:
        return len(solution_vector) == len(data)

    def construct_candidates(
        self,
    ) -> List[bool]:
        return [True, False]

    def make_move(
        self,
        candidate: bool,
        solution_vector: List[bool],
    ):
        solution_vector.append(candidate)

    def unmake_move(
        self,
        solution_vector: List[bool],
    ):
        solution_vector.pop()

    def process_solution(self, solution_vector: List[bool], data: List[str]):
        s = ""
        for k, v in enumerate(data):
            if solution_vector[k]:
                s += f"{v}"
        print("{", ",".join(s), "}")

    def backtrack(
        self,
        solution_vector: List[bool],
        data: List[str],
    ):
        if self.is_solution(solution_vector, data):
            self.process_solution(solution_vector, data)
        else:
            candidates = self.construct_candidates()
            for candidate in candidates:
                self.make_move(candidate, solution_vector)
                self.backtrack(solution_vector, data)
                self.unmake_move(solution_vector)

    def print_subsets(self, data: List[str]):
        self.backtrack([], data)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_print_subsets(self):
        self.sol.print_subsets(["1", "2", "3", "4"])


if __name__ == "__main__":
    unittest.main()
