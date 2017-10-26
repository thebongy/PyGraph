'''
Classes required to construct an expression using post-fix
'''

class UnderflowException(Exception):
    '''
    Raised when any element access operation is attempted on
    an empty stack.
    '''
    pass


class Stack(object):
    '''
    Implements a Stack or a LIFO-style collection of elements.
    '''
    def __init__(self):
        self.stack = []
    def push(self, elem):
        '''
        Push an element to the top of the stack.
        '''
        self.stack.append(elem)
    def pop(self):
        '''
        Remove and returns the top element of the stack.
        '''
        if self.stack:
            return self.stack.pop()
        else:
            raise UnderflowException("Stack is empty!!")
    def top(self):
        '''
        Returns the next element of the stack.
        '''
        if self.stack:
            return self.stack[-1]
        else:
            raise UnderflowException("Stack is empty!!")

class PostfixExpression(object):
    '''
    Computes Postfix representations, and also provides methods to evaluate
    these representations given args
    '''
    def __init__(self, expr):
        self.expr = expr
        self.stack = Stack()
        self.construct_postfix()
    def construct_postfix(self):
        '''
        Constructs a postfix expression out of self.expr in self.stack.
        '''

        raise NotImplementedError

class Expression(object):
    '''
    Class to represent any arbitrary string math expression in postfix notation.
    It also identifies functions and operators in the expression and creates respective
    objects out of them. Has methods to return value of a function given args.
    '''
    def __init__(self, expr):
        self.expr = expr


class Operator(object):
    pass


class UnaryOperator(Operator):
    pass


class BinaryOperator(Operator):
    pass


class Variable(object):
    pass


class Constant(object):
    pass

class Function(object):
    pass
