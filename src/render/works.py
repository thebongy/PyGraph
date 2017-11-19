from decimal import Decimal

M = [i+10 for i in range(5)]
for i, j in enumerate(M):
        print i,j


import os,math
W, H = 120,50
SCALEx = 0.1
SCALEy = 0.1

def cls():
        os.system("cls")

data = [[" " for i in range(W)] for j in range(H)]

X = [(SCALEx * i) for i in range(0,W)]
Y = [-2 + (SCALEy * i) for i in range(0,H)]

GOP = []
GOPI = []
Clist = []


def plot(x,y):
        x = X.index(x)
        valid_Y = []

        t1 = True
        if y < Y[0] or y > Y[-1]:
                try:
                        GOP.append(GOP[-1])
                        GOPI.append(GOP[-1])
                except:
                        pass
                Clist.append('D')
                return
        t = True
        for i,j in enumerate(Y):
                if j == y and t:
                        data[H-i-1][x] = "*"
                        GOP.append(j)
                        GOPI.append(i)
                        t = False
                elif y < j and t:
                        if i!= 0:
                                data[H-i][x] = "*"
                        data[H-i-1][x] = "*"
                        GOP.append(j)
                        GOPI.append(i)
                        t = False
                if len(GOP) > 1 and not t:
                        if (GOP[-1]-GOP[-2]) > SCALEy:
                                Clist.append('>')
                                for g in range(GOPI[-2], (GOPI[-2]+GOPI[-1])/2):
                                        data[H-1-g][x-1] = "@"
                                for g in range((GOPI[-2]+GOPI[-1])/2, GOPI[-1]):
                                        data[H-1-g][x] = "#"
                        elif (GOP[-2]-GOP[-1]) > SCALEy:
                                Clist.append('<')
                                for g in range((GOPI[-2]+GOPI[-1])/2-1,GOPI[-2]):
                                        data[H-1-g][x-1] = "@"
                                for g in range(GOPI[-1], (GOPI[-2]+GOPI[-1])/2):
                                        data[H-1-g][x] = "#"
                        else:
                                Clist.append('=')
                        return
                
                        
                        
                        
def display():
        for row in data:
                print ''.join(row)

##x = []
##delta = 0.1
##count,initial = 0,0
##current = 0
##for i in range(100):
##        x.append(current)
##        count+=1
##        current = initial + count*delta
##data[49][119] = '*'
for i in X:
        try:
##                plot(i,-((i-60)**2)/40.0+75)
                plot(i,math.sin(i))
        except:
                pass

for i in range(1,len(Clist)-1):
        if Clist[i] == 'D' and i != 0:
                if Clist[i-1] == '>':
                        for j in range(len(data)):
                                if data[j][i] == '*':
                                        break
                                #data[j][i] = '%'
                if Clist[i-1] == '<':
                        for j in range(len(data)):
                                if data[len(data)-1-j][i] == '*':
                                        break
                                #data[len(data)-1-j][i] = '%'

        if Clist[i] == 'D' and i != len(Clist)-1:
                if Clist[i+1] == '>':
                        for j in range(len(data)):
                                if data[j][i] == '*':
                                        break
                                #data[j][i] = '%'
                if Clist[i+1] == '<':
                        for j in range(1,len(data)-1):
                                if data[len(data)-j][i] == '*':
                                        break
                                #data[len(data)-j][i] = '%'
                                
        

        

display()
print len(Clist)   
