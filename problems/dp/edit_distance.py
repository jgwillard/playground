import unittest


class Solution:
    def edit_distance(self, s: str, t: str) -> int:
        width = len(s) + 1
        height = len(t) + 1
        matrix = [[0 for _ in range(width)] for _ in range(height)]

        for col in range(width):
            matrix[0][col] = col

        for row in range(height):
            matrix[row][0] = row

        for col in range(1, width):
            for row in range(1, height):
                cost = min(
                    matrix[row][col - 1],
                    matrix[row - 1][col],
                    matrix[row - 1][col - 1],
                )
                if s[col - 1] != t[row - 1]:
                    cost += 1
                matrix[row][col] = cost

        return matrix[height - 1][width - 1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_edit_distance(self):
        self.assertEqual(self.sol.edit_distance("thou shalt", "you should"), 5)
        self.assertEqual(self.sol.edit_distance("art", "act"), 1)
        self.assertEqual(self.sol.edit_distance("at", "act"), 1)
        self.assertEqual(self.sol.edit_distance("", "act"), 3)


if __name__ == "__main__":
    unittest.main()
