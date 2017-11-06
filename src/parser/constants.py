'''
File to store special mathematical constants supported by the program
'''

import math

CONSTANTS = {
        "e":math.e,
        "pi":math.pi,
        "tau": math.tau
        }

def add_constant(name, value):
    CONSTANTS[name] = value
