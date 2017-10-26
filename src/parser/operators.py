'''
Defines multiple operators and their actions.
'''

from components import BinaryOperator,UnaryOperator

class Add(BinaryOperator):
    def evaluate(self,arg1,arg2):
        return arg1+arg2


class Subtract(BinaryOperator):
    pass