

'''
Classes required to construct an expression using post-fix
'''

from raw_expr import Unit, ObjectRepresentation

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
    def isEmpty(self):
        '''
        Returns True iff stack is empty.
        '''
        return len(self.stack) == 0
    def makeCopy(self):
        '''
        Returns a new object which is an exact copy of the current stack
        '''
        newObj = Stack()
        newObj.stack = list(self.stack)
        return newObj

class PostfixExpression(object):
    '''
    Computes Postfix representations, and also provides methods to evaluate
    these representations given args
    '''
    def __init__(self, expr):
        self.expr = expr
        self.postfix = []
        self.construct_postfix()
    def construct_postfix(self):
        '''
        Constructs a postfix expression out of self.expr in self.stack.
        '''

        self.opStack = Stack()

        for obj in expression:
            if isinstance(obj, Constant) or isinstance(obj, Variable) or isinstance(obj, Function):
                self.postfix.append(obj)
            elif isinstance(obj, Parenthesis):
                if Parenthesis.type == "OPENING":
                    self.opStack.push(obj)
                elif Parenthesis.type == "CLOSING":
                    # NOTE FOR LATER:
                    # if an epxression has invalid parenthesis, the error can be caught here.
                    while not isinstance(opStack.top(), Parenthesis):
                        self.postfix.append(opStack.pop())
                    opStack.pop()
            elif isinstance(obj, Operator):
                while not opStack.isEmpty():
                    current = opStack.top()
                    if isinstance(current, Operator):
                        if current.priority < obj.priority:
                            self.postfix.append(opStack.pop())
                        else:
                            break
                    else:
                        break
                self.opStack.push(obj)
    def evaluate(self, x):
        '''
        Evaluate the postfix Expression for a given vakue of x.
        '''
        evaluation = Stack()
        expression = list(self.postfix)
        for current in expression:
            if isinstance(current, Variable) or isinstance(current, Constant):
                evaluation.push(current)
            elif isinstance(current, BinaryOperator):
                right = evaluation.pop()
                left = evaluation.pop()
                evaluation.push(current.evaluate(left,right)
            elif isinstance(current, UnaryOperator) or isinstance(current, Function):
                arg = evaluation.pop()
                evaluation.push(current.evaluate(arg))
        return evaluation[0]

class Expression(object):
    '''
    Class to represent any arbitrary string math expression in postfix notation.
    It also identifies functions and operators in the expression and creates respective
    objects out of them. Has methods to return value of a function given args.
    '''
    def __init__(self, raw_expr):
        self.raw_expr = "(" + raw_expr + ")" # Standard postfix rules to add parenthesis.
        self.expr = ObjectRepresentation(raw_expr)
        self.postfix = PostfixExpression(self.expr)
    def evaluate(x):
        self.postfix.evaluate(x)

class Operator(Unit):
    def __init__(self, data, start, end):
        Unit.__init__(self, data, start, end, func, priority):
        self.func = func
        self.priority = priority
    def evaluate(*args):
        raise NotImplementedError


class UnaryOperator(Operator):
    def __init__(self, data, start, end, func, priority):
        Operator.__init__(self, data, start, end, func, priority)
    def evaluate(x):
        return self.func(x)


class BinaryOperator(Operator):
    def __init__(self, data, start, end, func, priority):
        Operator.__init__(self, data, start, end, func, priority):
    def evaluate(left, right):
        return self.func(left,right)


class Variable(Unit):
    def __init__(self, data, start, end): 
        Unit.__init__(self, data, start, end)
        self.var = data
    def evaluate(x):
        return x


class Constant(Unit):
    def __init__(self, data, start, end, func):
        Unit.__init__(self, data, start, end)
        self.value = float(data)
    def evaluate(x):
        return self.value

class Function(Unit):
    def __init__(self, data, start, end, func, stuffinside):
        Unit.__init__(self, data, start, end)
        self.func = func
        self.inside = stuffinside
    def evaluate(x):
        return self.func(self.expr.evaluate(x))
