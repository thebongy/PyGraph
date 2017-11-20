'''
Classes which handle the parsing and evaluation of a string expression
'''
from operators import BINARY_OPERATORS, UNARY_OPERATORS
from functions import FUNCTIONS
from constants import CONSTANTS
from decimal import Decimal # For floating point calcluations
from components import *
from stack import Stack


class ObjectRepresentation(object):
	'''
	Converts a string expression into a list of python objects.
	'''
	def __init__(self, expr):
		self.string_repr = expr.replace(" ","")
		if self.string_repr.count("(") != self.string_repr.count(")"):
			raise ValueError("Unmatched parenthesis in equation")
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
					try:
						posn = Blist.pop(-1)
					except:
						raise ValueError("Invalid Parenthesis order in Expression")
					self.expression[posn] = Parenthesis('(',posn,len(self.expression),bcnt)
					self.expression.append(Parenthesis(')',posn,len(self.expression),bcnt))
					bcnt -= 1
					

				elif self.string_repr[i] == 'x':
					self.expression.append(Variable('x',i,i+1))

				elif self.string_repr[i].isdigit() or self.string_repr[i] == '.':
					n += self.string_repr[i]
					if i == len(self.string_repr)-1 or not (self.string_repr[i+1].isdigit() or self.string_repr[i+1] == '.'):
						self.expression.append(Constant(Decimal(n),i,i+1))
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
					self.expression.append(Constant(Decimal(CONSTANTS[self.string_repr[i]]),len(self.expression),len(self.expression)+1))
				else:
					for j in FUNCTIONS:
						if self.string_repr[i:(i+len(j))] == j:
							func_name = j																				  
							func_start = i
							parsing_func = True
							bcnt += 1
							func_b = bcnt
							break
					else:
						raise ValueError("Invalid Character " + self.string_repr[i] + " in expression.")
			else:
				if self.string_repr[i] == '(':
					bcnt += 1
				elif self.string_repr[i] == ')':
					bcnt -= 1
					if func_b-1 == bcnt:
						func_end = i
						func_arg = self.string_repr[func_start+len(func_name):func_end]
						func_data = self.string_repr[func_start:func_end]
						self.expression.append(Function(func_data, func_start, func_end, FUNCTIONS[func_name], Expression(func_arg)))
						parsing_func = True

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
