from collections import defaultdict
from typing import Dict, List
import unittest


class Solution:
    def is_solution(
        self,
        solution_vector: List[str],
        data: Dict[str, int],
        n: int,
    ) -> bool:
        return len(solution_vector) == n

    def construct_candidates(
        self,
        data: Dict[str, int],
    ) -> List[str]:
        candidates: List[str] = []
        for k, v in data.items():
            if v > 0:
                candidates.append(k)
        return candidates

    def make_move(
        self,
        candidate: str,
        solution_vector: List[str],
        data: Dict[str, int],
    ):
        solution_vector.append(candidate)
        data[candidate] -= 1

    def unmake_move(
        self,
        candidate: str,
        solution_vector: List[str],
        data: Dict[str, int],
    ):
        el = solution_vector.pop()
        data[el] += 1

    def process_solution(
        self, solution_vector: List[str], data: Dict[str, int]
    ):
        s = ""
        for v in solution_vector:
            s += f"{v}"
        print(",".join(s))

    def backtrack(
        self, solution_vector: List[str], data: Dict[str, int], n: int
    ):
        if self.is_solution(solution_vector, data, n):
            self.process_solution(solution_vector, data)
        else:
            candidates = self.construct_candidates(data)
            for candidate in candidates:
                self.make_move(candidate, solution_vector, data)
                self.backtrack(solution_vector, data, n)
                self.unmake_move(candidate, solution_vector, data)

    def print_multisets(self, data: List[str]):
        frequency_table: Dict[str, int] = defaultdict(int)
        for el in data:
            frequency_table[el] += 1
        self.backtrack([], frequency_table, len(data))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_print_multisets(self):
        self.sol.print_multisets(["1", "2", "1", "2"])


if __name__ == "__main__":
    unittest.main()
