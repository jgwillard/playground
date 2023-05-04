import unittest


class Solution:
    def binomial_coefficients(self, n: int, k: int) -> int:
        # (define (f k n)
        #   (cond ((= k 0) 1) ; left edge
        #         ((= k n) 1) ; right edge
        #         (else (+ (f k (dec n)) (f (dec k) (dec n))))))
        if n < k:
            return 0
        if k == 0:
            return 1
        if k == n:
            return 1
        return self.binomial_coefficients(
            n - 1, k
        ) + self.binomial_coefficients(n - 1, k - 1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_binomial_coefficients(self):
        # 7th row of Pascal's triangle
        self.assertEqual(self.sol.binomial_coefficients(7, 0), 1)
        self.assertEqual(self.sol.binomial_coefficients(7, 1), 7)
        self.assertEqual(self.sol.binomial_coefficients(7, 2), 21)
        self.assertEqual(self.sol.binomial_coefficients(7, 3), 35)
        self.assertEqual(self.sol.binomial_coefficients(7, 4), 35)
        self.assertEqual(self.sol.binomial_coefficients(7, 5), 21)
        self.assertEqual(self.sol.binomial_coefficients(7, 6), 7)
        self.assertEqual(self.sol.binomial_coefficients(7, 7), 1)

        # base cases
        self.assertEqual(
            self.sol.binomial_coefficients(3, 6),
            0,
            "0 ways to choose k elements from a set of n elements where n < k",
        )
        self.assertEqual(
            self.sol.binomial_coefficients(1234, 0),
            1,
            "n choose 0 = 1, exactly 1 way to choose 0 elements from a set of n elements",
        )
        self.assertEqual(
            self.sol.binomial_coefficients(1234, 1234),
            1,
            "n choose n = 1, exactly one way to choose n elements from a set of n elements",
        )


if __name__ == "__main__":
    unittest.main()
