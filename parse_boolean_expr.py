from typing import List


class Solution:
    # parse boolean expressions
    # !(f) -> true
    # |(f,t) -> true
    # &(t,f) -> false
    # |(&(t,f,t),!(t)) -> false
    def parseBoolExpr(self, expression: str) -> bool:
        operator_stack: List[str] = []
        operand_stack: List[str] = []

        for c in expression:
            if c in '&|!':
                operator_stack.append(c)
            if c in '(tf':
                operand_stack.append(c)
            if c == ')':
                # pop off operand stack until '('
                # pop one off operator stack
                # call operator with operands
                operands: List[str] = []
                while True:
                    op = operand_stack.pop()
                    if op == '(':
                        break
                    else:
                        operands.append(op)

                operator = operator_stack.pop()
                if operator == '&':
                    val = Solution.logical_and(operands)
                elif operator == '|':
                    val = Solution.logical_or(operands)
                elif operator == '!':
                    val = Solution.logical_not(operands)

                operand_stack.append(val)

        return True if val == 't' else False

    @staticmethod
    def logical_and(conditions: List[str]):
        for cond in conditions:
            if cond == 'f':
                return 'f'
        return 't'

    @staticmethod
    def logical_or(conditions: List[str]):
        for cond in conditions:
            if cond == 't':
                return 't'
        return 'f'

    @staticmethod
    def logical_not(condition: List[str]):
        return 't' if condition[0] == 'f' else 'f'
