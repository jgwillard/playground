from typing import Dict, List
import unittest


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjacency_list: Dict[str, List[str]] = {}
        for ticket in tickets:
            if ticket[0] in adjacency_list:
                adjacency_list[ticket[0]].append(ticket[1])
            else:
                adjacency_list[ticket[0]] = [ticket[1]]

        # sort so last item is smallest
        for k, v in adjacency_list.items():
            adjacency_list[k] = sorted(v, reverse=True)

        # we are given that we always start at JFK
        stack: List[str] = ["JFK"]

        print(adjacency_list.keys())
        while stack:
            # get top item of stack and then take its last adjacent item
            item = stack[-1]
            # if the adjacency list is empty, check if we have a
            # finished itinerary: len(stack) == len(tickets) + 1
            # and if we do, return stack
            if item not in adjacency_list or len(adjacency_list[item]) == 0:
                if len(stack) == len(tickets) + 1:
                    return stack
                else:
                    # otherwise unwind the stack by popping the most
                    # recent item and checking its adjacency list
                    # if its adjacency list is empty, put the unwound
                    # item back into the adjacency list and keep going
                    # until we find a different choice to make
                    # when we find a different choice, pop it off the
                    # adjacency list and onto the stack and append the
                    # unwound item to its original adjacency list and
                    # leave inner loop
                    while True:
                        # print(stack)
                        unwound_item = stack.pop()
                        if not adjacency_list[stack[-1]]:
                            adjacency_list[stack[-1]].append(unwound_item)
                            continue
                        else:
                            stack.append(adjacency_list[stack[-1]].pop())
                            # print(stack[-1])
                            adjacency_list[stack[-2]].append(unwound_item)
                            break
            else:
                # otherwise, add the next item to the stack
                next_item = adjacency_list[item].pop()
                stack.append(next_item)

        # if an empty list is returned there was a problem with input
        return []


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
