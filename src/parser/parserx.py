#dfjkd
import math


class Expression:
    def __init__(self,f):
        t=[]
        f = '('+f+')'
        for i in f:
            t.append(i)
        self.fn = t
        self.stack = []
        self.op = []
        self.Opstack = []
        self.Y = 0

    @staticmethod
    def bracsearch(T,i):
        t = 0
        while True:
            if T[i] == '(':
                t+=1
            if T[i] == ')':
                t-=1
            if t == 0:
                return i
            i+=1

    @staticmethod
    def Trigreplace(T,i,l):
        T = T[:i]+T[i+3:]
        end = Expression.bracsearch(T,i)
        T = T[:i+1]+[l,'*','(']+T[i+1:end]+[')']+T[end:]
        return T
            

    def Correct(self):
        T,i = list(self.fn),0
        if self.fn[0] == '-':
            self.fn = self.fn[:i]+['(','1','-','2',')','*']+self.fn[i+1:]
        while i < (len(self.fn)):
            p = self.fn[i]
            if p == '-' and self.fn[i-1] == '(' and i != 0:
                self.fn = self.fn[:i]+['(','1','-','2',')','*']+self.fn[i+1:]

            if self.fn[i].isalpha():
                if len(self.fn[i:i+3]) == 3:
                    if self.fn[i]+self.fn[i+1]+self.fn[i+2] == 'sin':
                        self.fn = Expression.Trigreplace(self.fn,i,'a')
                    if self.fn[i]+self.fn[i+1]+self.fn[i+2] == 'cos':
                        self.fn = Expression.Trigreplace(self.fn,i,'b')
                    if self.fn[i]+self.fn[i+1]+self.fn[i+2] == 'tan':
                        self.fn = Expression.Trigreplace(self.fn,i,'c')
                    if self.fn[i]+self.fn[i+1]+self.fn[i+2] == 'cosec':
                        self.fn = Expression.Trigreplace(self.fn,i,'d')
                    if self.fn[i]+self.fn[i+1]+self.fn[i+2] == 'sec':
                        self.fn = Expression.Trigreplace(self.fn,i,'e')
                    if self.fn[i]+self.fn[i+1]+self.fn[i+2] == 'cot':
                        self.fn = Expression.Trigreplace(self.fn,i,'f')
                        
                if len(self.fn[i:i+2]) == 2:
                    if self.fn[i]+self.fn[i+1] == 'pi':
                        self.fn = self.fn[:i]+[str(math.pi)]+self.fn[i+2:]
                        
                if self.fn[i] == 'e':
                    self.fn = self.fn[:i]+[str(math.e)]+self.fn[i+1:]

                if len(self.fn[i:i+5]) == 5:
                    if self.fn[i]+self.fn[i+1]+self.fn[i+2]+self.fn[i+3]+self.fn[i+4] == 'floor':
                        self.fn = self.fn[:i+3]+self.fn[i+5:]
                        self.fn = Expression.Trigreplace(self.fn,i,'g')

                if len(self.fn[i:i+4]) == 4:
                    if self.fn[i]+self.fn[i+1]+self.fn[i+2]+self.fn[i+3] == 'ceil':
                        self.fn = self.fn[:i+2]+self.fn[i+4:]
                        self.fn = Expression.Trigreplace(self.fn,i,'h')
                #add new fn here


            if self.fn[i] == '.':
                f,x=0,1
                while f==0:
                    if not self.fn[i-x].isdigit():
                        f=1
                        break
                    x+=1
                f,y=0,1
                while f==0:
                    if not self.fn[i+y].isdigit():
                        f=1
                        break
                    y+=1
                z=''
                for j in range(x,y+1):
                    z+=self.fn[j]
                self.op.append(z)

                    
                    
                




            i+=1

        



        
        print self.fn
                

    def Evaluate(self):
        D = {'+':1,'-':2,'*':3,'/':4,'^':5}
        t = '+'
        for i in self.fn:
            if i == '(':
                self.stack.append(i)
            elif i in ['+','-','*','/','^']:
                if D[t] <= D[i]:
                    self.stack.append(i)
                    t = self.stack[-1]
                elif D[t] > D[i]:
                    y = 1
                    while y !=0:
                        if self.stack[-1] == '(':
                            y = 0
                        else:
                            self.op.append(self.stack.pop(-1))
                    self.stack.append(i)
                    t = '+'
            elif i.isalnum() or '.' in i:
                self.op.append(i)

            elif i == ')':
                print ''
                y = 0
                while y ==0:
                    if self.stack[-1] == '(':
                        y = 1
                        self.stack.pop(-1)
                    else:
                        self.op.append(self.stack.pop(-1))
                if self.stack != []:
                    if self.stack[-1] != '(':
                        t = self.stack[-1]
                    else:
                        t = '+'
                
        print self.op

    def Output(self,x):

        for i in range(len(self.op)):
            if self.op[i] == 'x':
                self.op[i] = str(x)

        for i in range(len(self.op)):
            print self.Opstack
            if self.op[i].isalnum() or '.' in self.op[i]:
                self.Opstack.append(self.op[i])
            else:
                try:                    
                    b = float(self.Opstack[-1])
                except:
                    b =(self.Opstack.pop(-1))
                else:
                    b =float(self.Opstack.pop(-1))
                try:                    
                    a = float(self.Opstack[-1])
                except:
                    a =(self.Opstack.pop(-1))
                else:
                    a =float(self.Opstack.pop(-1))
                if self.op[i] == '+':
                    self.Opstack.append(a+b)
                if self.op[i] == '-':
                    self.Opstack.append(a-b)
                if self.op[i] == '/':
                    self.Opstack.append(a/b)
                if self.op[i] == '^':
                    self.Opstack.append(a**b)
                if self.op[i] == '*':
                    if type(a)==float and type(b)==float:
                        self.Opstack.append(a*b)
                    elif a == 'a':
                        self.Opstack.append(math.sin(b))
                    elif a == 'b':
                        self.Opstack.append(math.cos(b))
                    elif a == 'c':
                        self.Opstack.append(math.tan(b))
                    elif a == 'd':
                        self.Opstack.append((math.sin(b))**-1)
                    elif a == 'e':
                        self.Opstack.append((math.cos(b))**-1)
                    elif a == 'f':
                        self.Opstack.append((math.tan(b))**-1)
                    elif a == 'g':
                        self.Opstack.append(math.floor(b))
                    elif a == 'h':
                        self.Opstack.append(math.ceil(b))
        self.Y = self.Opstack[0]
        print self.Y
                        
                
        
                

p = raw_input('Enter')
o = Expression(p)
o.Correct()
o.Evaluate()
c = float(raw_input('enter x'))
o.Output(c)











##not self.fn[i-1].isdigit() or not self.fn[i+1].isdigit()




# correct
##                    self.fn = self.fn[:i]+self.fn[i+3:]
##                    end = Expression.bracsearch(self.fn,i)
##                    self.fn = self.fn[:i+1]+['a','*','(']+self.fn[i+1:end]+[')']+self.fn[end:]
