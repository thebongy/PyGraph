class ObjectRepresentation(object):
    '''
    Converts a string expression into a list of python objects.
    '''
    def __init__(self, expr):
        self.string_repr = expr
        self.expression = []
        self.construct()

    def construct(self):
        raise NotImplementedError

class Unit(Object):
    '''
    Represents an arbitrary, most basic distinctive component of an expression.
    '''
    def __init__(self, data, start, end):
        self.raw_data = data
        self.start = start
        self.end = end

class Parentheses(Unit):
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

