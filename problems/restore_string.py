from typing import List
import unittest


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        s_prime = [""] * n
        for k, v in enumerate(indices):
            s_prime[v] = s[k]
        return "".join(s_prime)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_restore_string(self):
        self.assertEqual(
            self.sol.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]),
            "leetcode",
        )


if __name__ == "__main__":
    unittest.main()
