from typing import Dict, List
import unittest


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # step 1: convert words list to adjacency list
        # words should be grouped successively by letters they start
        # with, for example the first group consists of all the words
        # and each first letter points to the next first letter in the
        # list, then for all words that start with the same letter, each
        # second letter points to the next second letter, and so forth
        # once we run out of such groupings, the DAG is complete
        adjacency_list: Dict[str, List[str]] = {
            letter: [] for letter in "wertf"
        }
        letter_idx = 0
        while letter_idx < 10:
            for word_idx, word in enumerate(words):
                print(word_idx, letter_idx)
                # letters in final word cannot point to anything so break
                if word_idx == len(words) - 1:
                    break
                # if current word or next word is smaller than current
                # letter index
                if letter_idx > len(words[word_idx]) - 1 or letter_idx > len(
                    words[word_idx + 1]
                ):
                    continue
                if (
                    letter_idx == 0
                    or words[word_idx][letter_idx - 1]
                    == words[word_idx + 1][letter_idx - 1]
                ) and words[word_idx][letter_idx] != words[word_idx + 1][
                    letter_idx
                ]:
                    adjacency_list[words[word_idx][letter_idx]].append(
                        words[word_idx + 1][letter_idx]
                    )
            letter_idx += 1

        print(adjacency_list)
        # step 2: run Kahn's algorithm on the DAG to get a topo sort


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testAlienOrder(self):
        self.assertEqual(
            self.sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]), "wertf"
        )
        self.assertEqual(self.sol.alienOrder(["z", "x"]), "zx")
        self.assertEqual(self.sol.alienOrder(["z", "x", "z"]), "")


if __name__ == "__main__":
    unittest.main()
