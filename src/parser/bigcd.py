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
        TestL = []
        bcnt = 0
        Blist = []
        Lofconst = []                                                                                              
        Dictoffns ={}
        fnvar = True
        DictofUOp = {}
        DictofBOp = {}
        for i in range(self.string_repr):
            if fnvar:
                if self.string_repr[i] == '(':
                    TestL.append('Dummy')
                    bcnt += 1
                    Blist.append(len(TestL)-1)
                    
                if self.string_repr[i] == ')':
                    posn = Blist.pop(-1)
                    TestL[posn] = Parentheses('(',posn,len(TestL),bcnt)
                    TestL.append(Parentheses(')',posn,len(TestL)),bcnt)
                    bcnt -= 1
                    

                if self.string_repr[i] == 'x':
                    TestL.append(Variable('x',i,len(i+1))                                             

                for j in DictofUOp:
                    if self.string_repr[i] = j and (self.string_repr[i] in ['('] and self.string_repr[i] in DictofBOp) :
                        TestL.append(UnaryOperator(j, i, i+1, DictofUOp[0], DictofUOp[1]))                         

                for j in DictofBOp:
                    if self.string_repr[i] = j:
                        TestL.append(BinaryOperator(j, i, i+1, DictofUOp[0], DictofUOp[1]))
                        

                for j in Dictoffns:
                    if self.string_repr[i:(i+len(j))] = j:
                        data1 = j                                                                                 
                        start1 = i

                #afterfn do const
                elif self.string_repr[i] in Lofconst:
                    TestL.append(Constant(self.string_repr[i],len(TestL),len(TestL)+1))
            if not fnvar:
                if i == ')':
                    stuff = self.string_repr[start1+len(data1)+1:i]
                    end1 = i
                    #end2 = len(data1)+len(stuff)+1 ignore
                    TestL.append(Function(data1, start1, end1, Dictoffns[data1], stuff))
                

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














































## Part 2



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
