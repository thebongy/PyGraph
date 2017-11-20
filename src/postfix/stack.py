'''
Class to define a LIFO Stack
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