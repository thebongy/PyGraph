'''
Classes to which represent individual components of a mathematical expression.
'''

from decimal import Decimal

class Unit(object):
    '''
    Represents an arbitrary, most basic distinctive component of an expression.
    '''
    def __init__(self, data, start, end):
        self.raw_data = data
        self.start = start
        self.end = end

class Operator(Unit):
    def __init__(self, data, start, end, func, priority):
        Unit.__init__(self, data, start, end)
        self.func = func
        self.priority = priority
    def evaluate(self, *args):
        raise NotImplementedError


class UnaryOperator(Operator):
    def __init__(self, data, start, end, func, priority):
        Operator.__init__(self, data, start, end, func, priority)
    def evaluate(self, x):
        return self.func(x)


class BinaryOperator(Operator):
    def __init__(self, data, start, end, func, priority):
        Operator.__init__(self, data, start, end, func, priority)
    def evaluate(self, left, right):
        return self.func(left,right)


class Constant(Unit):
    def __init__(self, data, start, end):
        Unit.__init__(self, data, start, end)
        self.value = Decimal(data)
    def evaluate(self, x):
        return self.value

class Variable(Unit):
    def __init__(self, data, start, end): 
        Unit.__init__(self, data, start, end)
        self.var = data
    def evaluate(self, x):
        return Decimal(x)

class Function(Unit):
    def __init__(self, data, start, end, func, expr):
        Unit.__init__(self, data, start, end)
        self.func = func
        self.expr = expr
    def evaluate(self, x):
        return Decimal(self.func(self.expr.evaluate(x)))

class Parenthesis(Unit):
    '''
    Represents individual opening brackets '(' and closing brackets ')' components in the expression.
    '''
    def __init__(self, char, start, end, Pdepth):
        Unit.__init__(self,char,start,end)
        
        # PDepth: (Example):
        #
        # Expression:        ( x + ( x * ( x / 4 ) ) )
        #                    ^     ^     ^       ^ ^ ^
        # PDepth Value:      0     1     2       2 1 0
        
        if char == "(":
            self.type = "OPENING"
        else:
            self.type = "CLOSING"
        self.depth = Pdepth

