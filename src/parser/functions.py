'''
Defines significant well-known mathematical functions
'''
import math


FUNCTIONS = {
        "sin":math.sin,
        "cos":math.cos,
        "tan":math.tan,
        "cosec":lambda x:(1/math.sin(x)),
        "sec": lambda x:(1/math.cos(x)),
        "cot": lambda x:(1/math.tan(x)),
        "abs": abs,
        "ceil":math.ceil,
        "gif":math.ceil,
        "floor":math.floor
        }

def add_func(name, func):
    '''
    Function to add a custom function to FUNCTIONS
    '''
    FUNCTIONS[name] = func


