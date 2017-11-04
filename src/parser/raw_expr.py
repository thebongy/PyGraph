class ObjectRepresentation(object):
    '''
    Converts a string expression into a list of python objects.
    '''
    def __init__(self, expr):
        self.string_repr = expr


class Unit(Object):
    '''
    Represents an arbitrary, most basic distinctive component of an expression.
    '''
    def __init__(self, char, start, end):
        self.raw_data = char
        self.start = start
        self.end = end

class Parentheses(Unit):
    # Values of Pstate
    OPENING = 0
    CLOSING = 1

    '''
    Represents individual opening brackets '(' and closing brackets ')' components in the expression.
    '''
    def __init__(self, char, start, end, Pstate, Pdepth):
        Unit.__init__(self,char,start,end)
        self.state = Pstate # either OPENING OR CLOSING
        
        # PDepth: (Example):
        #
        # Expression:        ( x + ( x * ( x / 4 ) ) )
        #                    ^     ^     ^       ^ ^ ^
        # PDepth Value:      0     1     2       2 1 0

        self.depth = Pdepth

