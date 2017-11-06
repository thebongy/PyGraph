'''
Defines multiple operators and their actions.
'''

BINARY_OPERATORS = {
        "+":lambda x,y:x+y,
        "-":lambda x,y:x-y,
        "*":lambda x,y:x*y,
        "/":lambda x,y:x/y,
        "^":lambda x,y:x**y,
        }

UNARY_OPERATORS = {
        "-": lambda x:-x
        }

def add_binary_operator(char, func, binary = True):
    '''
    Add a custom operator
    '''
    if len(char) != 1:
        raise ValueError("Identifier for an operator must be just a character!")

    if binary:
        BINARY_OPERATORS[char] = func
    else:
        UNARY_OPERATORS[char] = func

