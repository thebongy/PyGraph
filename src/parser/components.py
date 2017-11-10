'''
Classes required to construct an expression using post-fix
'''
from operators import BINARY_OPERATORS, UNARY_OPERATORS
from functions import FUNCTIONS
from constants import CONSTANTS
from decimal import Decimal # For floating point calcluations

class Unit(object):
    '''
    Represents an arbitrary, most basic distinctive component of an expression.
    '''
    def __init__(self, data, start, end):
        self.raw_data = data
        self.start = start
        self.end = end

class Constant(Unit):
    def __init__(self, data, start, end):
        Unit.__init__(self, data, start, end)
        self.value = Decimal(data)
    def evaluate(self, x):
        return self.value

class ObjectRepresentation(object):
    '''
    Converts a string expression into a list of python objects.
    '''
    def __init__(self, expr):
        self.string_repr = expr
        self.expression = []
        self.construct()

    def construct(self):
        #new
        self.expression = []
        bcnt = 0
        Blist = []
        Lofconst = []                                                                                              
        parsing_func = False
        n = ''
        for i in range(len(self.string_repr)):
            if not parsing_func:
                if self.string_repr[i] == '(':
                    self.expression.append('Dummy')
                    bcnt += 1
                    Blist.append(len(self.expression)-1)
                    
                elif self.string_repr[i] == ')':
                    posn = Blist.pop(-1)
                    self.expression[posn] = Parenthesis('(',posn,len(self.expression),bcnt)
                    self.expression.append(Parenthesis(')',posn,len(self.expression),bcnt))
                    bcnt -= 1
                    

                elif self.string_repr[i] == 'x':
                    self.expression.append(Variable('x',i,i+1))

                elif self.string_repr[i].isdigit() or self.string_repr[i] == '.':
                    n += self.string_repr[i]
                    if i == len(self.string_repr)-1 or not (self.string_repr[i+1].isdigit() or self.string_repr[i+1] == '.'):
                        self.expression.append(Constant(int(n),i,i+1))
                        n = ''

                elif self.string_repr[i] in UNARY_OPERATORS and (self.string_repr[i-1] == '(' or self.string_repr[i-1] in BINARY_OPERATORS) :
                    op = self.string_repr[i]
                    func = UNARY_OPERATORS[op]["func"]
                    priority = UNARY_OPERATORS[op]["priority"]
                    self.expression.append(UnaryOperator(op, i, i+1, func, priority))
                
                elif self.string_repr[i] in BINARY_OPERATORS:
                    op = self.string_repr[i]
                    func = BINARY_OPERATORS[op]["func"]
                    priority = BINARY_OPERATORS[op]["priority"]
                    self.expression.append(BinaryOperator(op, i, i+1, func, priority))
                
                elif self.string_repr[i] in CONSTANTS:
                    self.expression.append(Constant(CONSTANTS[self.string_repr[i]],len(self.expression),len(self.expression)+1))
                else:
                    for j in FUNCTIONS:
                        if self.string_repr[i:(i+len(j))] == j:
                            func_name = j                                                                                 
                            func_start = i
                            parsing_func = False
                            bcnt += 1
                            func_b = bcnt
            else:
                if self.string_repr[i] == '(':
                    bcnt += 1
                elif self.string_repr[i] == ')':
                    bcnt -= 1
                    if func_b-1 == bcnt:
                        func_end = i
                        func_arg = self.string_repr[func_start+len(func_name):func_end]
                        func_data = self.string_repr[func_start:func_end]
                        self.expression.append(Function(func_data, func_start, func_end, FUNCTIONS[func_name], func_arg))
                        parsing_func = True

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
            return None
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

        for obj in self.expr.expression:
            if isinstance(obj, Constant) or isinstance(obj, Variable) or isinstance(obj, Function):
                self.postfix.append(obj)
            elif isinstance(obj, Parenthesis):
                if obj.type == "OPENING":
                    self.opStack.push(obj)
                elif obj.type == "CLOSING":
                    # NOTE FOR LATER:
                    # if an epxression has invalid parenthesis, the error can be caught here.
                    while not isinstance(self.opStack.top(), Parenthesis):
                        self.postfix.append(self.opStack.pop())
                    self.opStack.pop()
            elif isinstance(obj, BinaryOperator):
                while not self.opStack.isEmpty():
                    current = self.opStack.top()
                    if isinstance(current, Operator):
                        if current.priority < obj.priority:
                            self.postfix.append(self.opStack.pop())
                        else:
                            break
                    else:
                        break
                self.opStack.push(obj)
            elif isinstance(obj, UnaryOperator):
                self.opStack.push(obj)
                continue

            if isinstance(self.opStack.top(), UnaryOperator):
                self.postfix.append(self.opStack.pop())
    def evaluate(self, x):
        '''
        Evaluate the postfix Expression for a given vakue of x.
        '''

        x = Decimal(x) # VERY IMP
        evaluation = Stack()
        expression = list(self.postfix)
        for current in expression:
            if isinstance(current, Variable) or isinstance(current, Constant)  or isinstance(current, Function):
                evaluation.push(current.evaluate(x))
            elif isinstance(current, BinaryOperator):
                right = evaluation.pop()
                left = evaluation.pop()
                evaluation.push(current.evaluate(left,right))
            elif isinstance(current, UnaryOperator):
                arg = evaluation.pop()
                evaluation.push(current.evaluate(arg))
        return evaluation.pop()

class Expression(object):
    '''
    Class to represent any arbitrary string math expression in postfix notation.
    It also identifies functions and operators in the expression and creates respective
    objects out of them. Has methods to return value of a function given args.
    '''
    def __init__(self, raw_expr):
        self.raw_expr = "(" + raw_expr + ")" # Standard postfix rules to add parenthesis.
        self.expr = ObjectRepresentation(self.raw_expr)
        self.postfix = PostfixExpression(self.expr)
    def evaluate(self, x):
        try:
            return self.postfix.evaluate(x)
        except UnderflowException as e:
            raise ValueError("""Something went wrong while parsing the expression.
            Either the expression is invalid, or it wasn't parsed correctly...""")

class Operator(Unit):
    def __init__(self, data, start, end, func, priority):
        Unit.__init__(self, data, start, end)
        self.func = func
        self.priority = priority
    def evaluate(self):
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


class Variable(Unit):
    def __init__(self, data, start, end): 
        Unit.__init__(self, data, start, end)
        self.var = data
    def evaluate(self, x):
        return x


class Function(Unit):
    def __init__(self, data, start, end, func, stuffinside):
        Unit.__init__(self, data, start, end)
        self.func = func
        self.expr = Expression(stuffinside)
    def evaluate(self, x):
        return self.func(self.expr.evaluate(x))


# Expressions with only variables work:
x = Expression("x^-(-2-x)+3")
print x.evaluate(3)
