from collections import deque
from functools import reduce
from typing import Deque, Dict, List
import unittest


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        alphabet = reduce(lambda s, acc: s + acc, words, "")
        unique_alphabet = set(alphabet)
        adjacency_list: Dict[str, List[str]] = {
            letter: [] for letter in unique_alphabet
        }
        indegree: Dict[str, int] = {letter: 0 for letter in unique_alphabet}
        indegree_zero_queue: Deque[str] = deque()
        sorted_list: List[str] = []
        # step 1: convert words list to adjacency list
        # words should be grouped successively by letters they start
        # with, for example the first group consists of all the words
        # and each first letter points to the next first letter in the
        # list, then for all words that start with the same letter, each
        # second letter points to the next second letter, and so forth
        # once we run out of such groupings, the DAG is complete
        letter_idx = 0
        while letter_idx < 10:
            for word_idx, _ in enumerate(words):
                # letters in final word cannot point to anything so break
                if word_idx == len(words) - 1:
                    break
                # if current word or next word is smaller than current
                # letter index
                if (letter_idx > len(words[word_idx]) - 1) or (
                    letter_idx > len(words[word_idx + 1]) - 1
                ):
                    continue

                if (
                    (
                        # first letter is always a single group
                        letter_idx == 0
                        or
                        # previous letter of current word == previous
                        # letter of next word
                        words[word_idx][letter_idx - 1]
                        == words[word_idx + 1][letter_idx - 1]
                    )
                    and
                    # current letters of each word do not equal each
                    # other (no self edges)
                    words[word_idx][letter_idx]
                    != words[word_idx + 1][letter_idx]
                ):
                    adjacency_list[words[word_idx][letter_idx]].append(
                        words[word_idx + 1][letter_idx]
                    )
            letter_idx += 1

        print(adjacency_list)
        # step 2: run Kahn's algorithm on the DAG to get a topo sort
        # compute indegree for each node
        for _, neighbors in adjacency_list.items():
            for neighbor in neighbors:
                indegree[neighbor] += 1
        print(indegree)
        # enqueue any nodes with indegree zero
        for node, _ in adjacency_list.items():
            if indegree[node] == 0:
                indegree_zero_queue.append(node)
        while indegree_zero_queue:
            node = indegree_zero_queue.popleft()
            sorted_list.append(node)
            for neighbor in adjacency_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    indegree_zero_queue.append(neighbor)

        return (
            "".join(sorted_list)
            if len(sorted_list) == len(adjacency_list)
            else ""
        )


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testAlienOrder(self):
        self.assertEqual(
            self.sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]), "wertf"
        )
        self.assertEqual(self.sol.alienOrder(["z", "x"]), "zx")
        self.assertEqual(self.sol.alienOrder(["z", "x", "z"]), "")
        self.assertEqual(self.sol.alienOrder(["abc", "ab"]), "")


if __name__ == "__main__":
    unittest.main()
