from typing import Dict, List
import unittest


class Solution:

    def __init__(self):
        self.paren_map: Dict[str, str] = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

    def isValid(self, s: str) -> bool:
        paren_stack: List[str] = []
        for c in s:
            if c in '([{':
                paren_stack.append(c)
            elif c in ')]}' and len(paren_stack):
                popped = paren_stack.pop()
                if self.paren_map[popped] != c:
                    return False
            else:
                return False

        return not(len(paren_stack))


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_roman_to_int(self):
        self.assertTrue(self.sol.isValid('()[]{}'))
        self.assertTrue(self.sol.isValid('([{}])'))
        self.assertFalse(self.sol.isValid('(]'))
        self.assertFalse(self.sol.isValid('([)]'))
        self.assertFalse(self.sol.isValid('(()'))
        self.assertFalse(self.sol.isValid('())'))


if __name__ == '__main__':
    unittest.main()
