from typing import Optional
import unittest


class Solution:
    def romanToInt(self, numeral: str) -> int:
        total: int = 0
        self.i = 0
        while self.i < len(numeral):
            current_char = numeral[self.i]
            next_char: Optional[str] = numeral[self.i +
                                               1] if self.i < len(numeral) - 1 else None
            if current_char == 'I':
                if next_char == 'V':
                    total += 4
                    self.skip_next_char()
                elif next_char == 'X':
                    total += 9
                    self.skip_next_char()
                else:
                    total += 1
            if current_char == 'X':
                if next_char == 'L':
                    total += 40
                    self.skip_next_char()
                elif next_char == 'C':
                    total += 90
                    self.skip_next_char()
                else:
                    total += 10
            if current_char == 'C':
                if next_char == 'D':
                    total += 400
                    self.skip_next_char()
                elif next_char == 'M':
                    total += 900
                    self.skip_next_char()
                else:
                    total += 100
            if current_char == 'V':
                total += 5
            if current_char == 'L':
                total += 50
            if current_char == 'D':
                total += 500
            if current_char == 'M':
                total += 1000

            self.i += 1

        return total

    def skip_next_char(self):
        self.i += 1


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_roman_to_int(self):
        self.assertEqual(self.sol.romanToInt('III'), 3)
        self.assertEqual(self.sol.romanToInt('IV'), 4)
        self.assertEqual(self.sol.romanToInt('IX'), 9)
        self.assertEqual(self.sol.romanToInt('LVIII'), 58)
        self.assertEqual(self.sol.romanToInt('MCMXCIV'), 1994)


if __name__ == '__main__':
    unittest.main()
