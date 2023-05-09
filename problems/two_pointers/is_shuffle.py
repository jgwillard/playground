import unittest


class Solution:
    def is_shuffle(self, s: str, t: str, u: str) -> bool:
        n = len(u)
        i = 0
        j = 0
        for k in range(n):
            if i < len(s) and u[k] == s[i]:
                i += 1
            elif j < len(t) and u[k] == t[j]:
                j += 1
            else:
                return False

        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_is_shuffle(self):
        self.assertTrue(
            self.sol.is_shuffle("chocolate", "chips", "cchocohilaptes")
        )
        self.assertFalse(
            self.sol.is_shuffle("chocolate", "chips", "chocochilatspe")
        )
        self.assertTrue(self.sol.is_shuffle("cat", "dog", "catdog"))
        self.assertTrue(self.sol.is_shuffle("cat", "dog", "cadogt"))
        self.assertTrue(self.sol.is_shuffle("cat", "dog", "cadotg"))


if __name__ == "__main__":
    unittest.main()
