import unittest


class Solution:
    def intToRoman(self, num: int) -> str:
        out: str = ''
        thousands_place: int = 0
        hundreds_place: int = 0
        tens_place: int = 0
        ones_place: int = 0
        if num >= 1000:
            thousands_place = num // 1000
            num = num % 1000
        if num >= 100:
            hundreds_place = num // 100
            num = num % 100
        if num >= 10:
            tens_place = num // 10
            num = num % 10

        ones_place = num

        for i in range(thousands_place):
            out += 'M'

        if hundreds_place == 9:
            out += 'CM'
        elif hundreds_place == 4:
            out += 'CD'
        else:
            if hundreds_place > 4:
                out += 'D'
                hundreds_place = hundreds_place % 5
            for i in range(hundreds_place):
                out += 'C'

        if tens_place == 9:
            out += 'XC'
        elif tens_place == 4:
            out += 'XL'
        else:
            if tens_place > 4:
                out += 'L'
                tens_place = tens_place % 5
            for i in range(tens_place):
                out += 'X'

        if ones_place == 9:
            out += 'IX'
        elif ones_place == 4:
            out += 'IV'
        else:
            if ones_place > 4:
                out += 'V'
                ones_place = ones_place % 5
            for i in range(ones_place):
                out += 'I'

        return out


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_int_to_roman(self):
        self.assertEqual(self.sol.intToRoman(3), 'III')
        self.assertEqual(self.sol.intToRoman(4), 'IV')
        self.assertEqual(self.sol.intToRoman(5), 'V')
        self.assertEqual(self.sol.intToRoman(9), 'IX')
        self.assertEqual(self.sol.intToRoman(10), 'X')
        self.assertEqual(self.sol.intToRoman(40), 'XL')
        self.assertEqual(self.sol.intToRoman(50), 'L')
        self.assertEqual(self.sol.intToRoman(58), 'LVIII')
        self.assertEqual(self.sol.intToRoman(90), 'XC')
        self.assertEqual(self.sol.intToRoman(400), 'CD')
        self.assertEqual(self.sol.intToRoman(500), 'D')
        self.assertEqual(self.sol.intToRoman(900), 'CM')
        self.assertEqual(self.sol.intToRoman(1000), 'M')
        self.assertEqual(self.sol.intToRoman(1994), 'MCMXCIV')
        self.assertEqual(self.sol.intToRoman(2001), 'MMI')
        self.assertEqual(self.sol.intToRoman(2004), 'MMIV')


if __name__ == '__main__':
    unittest.main()
