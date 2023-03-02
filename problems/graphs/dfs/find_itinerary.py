import copy
from typing import Dict, List, Tuple
import unittest


class Solution:
    def generate_adjacency_list_and_visited_list(
        self, tickets: List[List[str]]
    ) -> Tuple[Dict[str, List[str]], Dict[str, List[bool]]]:

        adjacency_list: Dict[str, List[str]] = {}
        visited_list: Dict[str, List[bool]] = {}

        for ticket in tickets:
            if ticket[0] in adjacency_list:
                adjacency_list[ticket[0]].append(ticket[1])
                visited_list[ticket[0]].append(False)
            else:
                adjacency_list[ticket[0]] = [ticket[1]]
                visited_list[ticket[0]] = [False]

        # sort so first item is lexically smallest
        for k, v in adjacency_list.items():
            adjacency_list[k] = sorted(v)

        return (adjacency_list, visited_list)

    def backtrack(
        self,
        stack: List[str],
        adjacency_list: Dict[str, List[str]],
        visited: Dict[str, List[bool]],
    ) -> None:
        if self.is_solution(stack):
            self.finished = True
            self.solution = copy.copy(stack)
        else:
            candidates = self.construct_candidates(stack, adjacency_list)
            item = stack[-1]
            for k, candidate in enumerate(candidates):
                if not visited[item][k]:
                    stack.append(candidate)
                    visited[item][k] = True
                    self.backtrack(stack, adjacency_list, visited)
                    stack.pop()
                    visited[item][k] = False
                    if self.finished:
                        return

    def is_solution(self, stack: List[str]) -> bool:
        return len(stack) == len(self.tickets) + 1

    def construct_candidates(
        self, stack: List[str], adjacency_list: Dict[str, List[str]]
    ) -> List[str]:
        """Return all the items adjacent to the current top of stack"""
        item = stack[-1]
        return adjacency_list[item] if item in adjacency_list.keys() else []

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # reset
        self.solution = []
        self.finished = False
        self.tickets = tickets
        adjacency_list, visited = self.generate_adjacency_list_and_visited_list(
            tickets
        )

        # we are given that we always start at JFK
        stack: List[str] = ["JFK"]

        self.backtrack(stack, adjacency_list, visited)
        return self.solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMethodName(self):
        self.assertEqual(
            self.sol.findItinerary(
                [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
            ),
            ["JFK", "MUC", "LHR", "SFO", "SJC"],
        )
        self.assertEqual(
            self.sol.findItinerary(
                [
                    ["JFK", "SFO"],
                    ["JFK", "ATL"],
                    ["SFO", "ATL"],
                    ["ATL", "JFK"],
                    ["ATL", "SFO"],
                ]
            ),
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
        )
        self.assertEqual(
            self.sol.findItinerary(
                [["JFK", "c"], ["c", "JFK"], ["JFK", "b"], ["b", "d"]]
            ),
            ["JFK", "c", "JFK", "b", "d"],
        )
        self.assertEqual(
            self.sol.findItinerary(
                [
                    ["JFK", "c"],
                    ["c", "JFK"],
                    ["JFK", "b"],
                    ["b", "JFK"],
                    ["JFK", "a"],
                    ["a", "b"],
                ]
            ),
            ["JFK", "a", "b", "JFK", "c", "JFK", "b"],
        )
        self.sol.findItinerary(
            [
                ["CBR", "JFK"],
                ["TIA", "EZE"],
                ["AUA", "TIA"],
                ["JFK", "EZE"],
                ["BNE", "CBR"],
                ["JFK", "CBR"],
                ["CBR", "AUA"],
                ["EZE", "HBA"],
                ["AXA", "ANU"],
                ["BNE", "EZE"],
                ["AXA", "EZE"],
                ["AUA", "ADL"],
                ["OOL", "JFK"],
                ["BNE", "AXA"],
                ["OOL", "EZE"],
                ["EZE", "ADL"],
                ["TIA", "BNE"],
                ["EZE", "TIA"],
                ["JFK", "AUA"],
                ["AUA", "EZE"],
                ["ANU", "ADL"],
                ["TIA", "BNE"],
                ["EZE", "OOL"],
                ["ANU", "BNE"],
                ["EZE", "ANU"],
                ["ANU", "AUA"],
                ["BNE", "ANU"],
                ["CNS", "JFK"],
                ["TIA", "ADL"],
                ["ADL", "AXA"],
                ["JFK", "OOL"],
                ["AUA", "ADL"],
                ["ADL", "TIA"],
                ["ADL", "ANU"],
                ["ADL", "JFK"],
                ["BNE", "EZE"],
                ["ANU", "BNE"],
                ["JFK", "BNE"],
                ["EZE", "AUA"],
                ["EZE", "AXA"],
                ["AUA", "TIA"],
                ["ADL", "CNS"],
                ["AXA", "AUA"],
            ]
        )


if __name__ == "__main__":
    unittest.main()
